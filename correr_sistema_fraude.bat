@echo off
title Consola de Auditoria de Fraude - IA
echo Iniciando el servidor de Streamlit...

:: 1. Activa el entorno virtual de forma silenciosa
call src\.venv\Scripts\activate.bat

:: 2. Corre tu aplicación de Streamlit
streamlit run src/app.py
pause