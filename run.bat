@echo off
if not exist venv (
    echo Virtual environment not found. Please run setup first.
    pause
    exit /b
)
call venv\Scripts\activate
streamlit run src\app.py
pause
