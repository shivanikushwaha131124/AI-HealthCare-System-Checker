Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "Starting HealthAI Backend and Frontend..." -ForegroundColor Cyan
Write-Host "===================================================" -ForegroundColor Cyan

Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PSScriptRoot\backend'; & '.\.venv\Scripts\uvicorn.exe' app.main:app --host 127.0.0.1 --port 8000 --reload"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PSScriptRoot\frontend'; npm run dev"

Write-Host "`nBoth Backend and Frontend started in separate windows!" -ForegroundColor Green
Write-Host "Frontend:    http://localhost:3000" -ForegroundColor Yellow
Write-Host "Backend API: http://localhost:8000" -ForegroundColor Yellow
Write-Host "API Docs:    http://localhost:8000/docs" -ForegroundColor Yellow
