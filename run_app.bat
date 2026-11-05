@echo off
echo ========================================================
echo Starting Plant Disease Recognition System...
echo ========================================================
cd /d "%~dp0Plant_Disease_Prediction"
call .venv\Scripts\activate.bat
streamlit run main.py --server.port 8501
pause

