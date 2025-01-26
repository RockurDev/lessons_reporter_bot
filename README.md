# Lessons Reporter Bot

Effortlessly manage and report student lesson details with this feature-rich Telegram bot for tutors.

## Project Description
The **Lessons Reporter Bot** is a Telegram bot designed to streamline reporting for tutors. It simplifies communication between tutors and parents, providing clear and organized information about students' attendance, lesson details, and homework status. Built with Python and leveraging technologies like Pydantic, Telebot, SQLModel, and Dataclasses, the bot ensures smooth interaction and data management.

The code is organized into logical modules for better maintainability and clarity:
- **topic_storage**: Manages topic-related data.
- **student_storage**: Handles student records and information.
- **report_storage**: Stores and retrieves lesson reports.
- **report_builder**: Builds lesson reports step by step.
- **models**: Defines database models and schemas.
- **main**: Entry point for the bot.
- **bot_service**: Core bot logic and user interaction.
- **authorization_service**: Manages user authorization and permissions.

## Features
- **Student and Topic Pagination**: Easily navigate through lists of students and lesson topics using inline buttons.
  - *Example*: Quickly find a specific student or topic by scrolling through organized pages instead of viewing an overwhelming list.
- **Lesson Report Creation**: Answer simple questions or click buttons to generate detailed lesson reports.
- **Error and Exception Handling**: Robust error handling ensures a smooth user experience.
- **Intuitive Interface**: Buttons and messages are designed for easy use and quick navigation.

## How to Launch
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/RockurDev/Lessons_Reporter_Bot/
   cd lessons_reporter_bot
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the project root and define the following variables:
   ```env
   BOT_TOKEN=<your-telegram-bot-token>
   SUPERUSERS=[123456789, 234567891]  # List of Telegram user IDs with admin access
   DATABASE_URL=sqlite:///local_database.db  # SQLite database used by default
   ```

4. **Start the Bot**:
   ```bash
   python lesson_reporter_bot/main.py
   ```

5. **Deploy to a Server**:
   For stable operation, deploy the bot to a server. Recommended setup:
   - Python runtime environment
   - `.env` file containing the bot's settings
   - Use process managers like `systemd` or `supervisord` to ensure the bot runs continuously.

## Author
This bot was developed by RockurDev. For questions or collaborations, please contact the author via [GitHub](https://github.com/RockurDev).

