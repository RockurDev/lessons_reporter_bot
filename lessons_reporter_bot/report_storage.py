import logging
import time
from typing import Callable, Optional, ParamSpec, Sequence, TypeVar

from sqlmodel import Session, desc, func, select
import sqlalchemy

from lessons_reporter_bot.models import Report

P = ParamSpec('P')
T = TypeVar('T')


def measure_time(func: Callable[P, T]) -> Callable[P, T]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        before_time = time.time()
        result = func(*args, **kwargs)
        logging.error(f'call to {func} took {round(time.time() - before_time)*1000} ms')
        return result

    return wrapper


class ReportStorage:
    def __init__(self, engine: sqlalchemy.Engine) -> None:
        self.engine = engine

    def count_reports(self) -> int:
        with Session(self.engine) as session:
            statement = select(Report)
            result = session.exec(statement)
            return len(result.all())

    def add_report(self, report: Report) -> int:
        with Session(self.engine) as session:
            session.add(report)
            session.commit()
            session.refresh(report)
            return report.report_id

    @measure_time
    def list_reports(self, order_by: str | None = None, descending: bool = False) -> Sequence[Report]:
        with Session(self.engine) as session:
            statement = select(Report)
            if order_by:
                column = getattr(Report, order_by)
                statement = statement.order_by(desc(column)) if descending else statement.order_by(column)
            return session.exec(statement).all()

    def list_reports_by_student_id(
        self, student_id: int, order_by: str | None = None, descending: bool = False
    ) -> Sequence[Report]:
        with Session(self.engine) as session:
            statement = select(Report).where(Report.student_id == student_id)
            if order_by:
                column = getattr(Report, order_by)
                statement = statement.order_by(desc(column)) if descending else statement.order_by(column)
            return session.exec(statement).all()

    def get_report_by_id(self, report_id: int) -> Optional[Report]:
        with Session(self.engine) as session:
            statement = select(Report).where(Report.report_id == report_id)
            return session.exec(statement).first()

    def lessons_count_by_student_id(self, student_id: int) -> int:
        with Session(self.engine) as session:
            statement = select(func.count(Report.report_id)).where(  # type: ignore
                Report.student_id == student_id
            )
            return session.exec(statement).first()

    def get_saved_reports(self) -> Sequence[Report]:
        with Session(self.engine) as session:
            statement = select(Report).where(Report.is_sent == False)
            return session.exec(statement).all()

    def set_is_sent(self, report_id: int) -> None:
        with Session(self.engine) as session:
            report = session.get(Report, report_id)
            assert report
            report.is_sent = True
            session.commit()
