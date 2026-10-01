@echo off
title HealthAI Launcher
echo ===================================================
echo Starting HealthAI Backend and Frontend...
echo ===================================================

start "HealthAI Backend (FastAPI)" cmd /k "cd /d %~dp0backend && .venv\Scripts\uvicorn.exe app.main:app --host 127.0.0.1 --port 8000 --reload"
start "HealthAI Frontend (Next.js)" cmd /k "cd /d %~dp0frontend && npm run dev"

echo.
echo Both Backend and Frontend started in separate windows!
echo - Frontend: http://localhost:3000
echo - Backend API: http://localhost:8000
echo - Swagger Docs: http://localhost:8000/docs
echo.
