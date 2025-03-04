import logging
import time
from dataclasses import dataclass
from typing import Callable, ParamSpec, TypeVar

from lessons_reporter_bot.callback_data import (
    ReportBuilderShowItemListCallbackData,
    ShowItemsListCallbackData,
)
from lessons_reporter_bot.models import FormattedPaginationItem

FIRST_PAGE = 1


@dataclass
class PaginationResult:
    is_last_page: bool
    is_first_page: bool
    items: list[FormattedPaginationItem]


def paginate(
    items: list[FormattedPaginationItem],
    data: ShowItemsListCallbackData | ReportBuilderShowItemListCallbackData,
    page_size: int,
) -> PaginationResult:
    start = (data.page - 1) * page_size
    total_pages = (len(items) + page_size - 1) // page_size

    return PaginationResult(
        is_first_page=data.page == FIRST_PAGE,
        is_last_page=data.page == total_pages or len(items) == 0,
        items=items[start : start + page_size],
    )


P = ParamSpec('P')
T = TypeVar('T')


def measure_time(func: Callable[P, T]) -> Callable[P, T]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        before_time = time.time()
        result = func(*args, **kwargs)
        logging.error(
            f'call to {func} took {round((time.time() - before_time)*1000)} ms'
        )
        return result

    return wrapper
