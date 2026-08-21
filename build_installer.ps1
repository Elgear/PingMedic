param(
    [string]$Version = "0.1.0"
)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

Write-Host "=== PingerApp Windows installer build ===" -ForegroundColor Cyan
Write-Host "Version: $Version"

if (-not (Get-Command py -ErrorAction SilentlyContinue) -and -not (Get-Command python -ErrorAction SilentlyContinue)) {
    throw "Python was not found. Install Python 3.11 or 3.12 and try again."
}

$pythonCmd = if (Get-Command py -ErrorAction SilentlyContinue) { "py" } else { "python" }

if (-not (Test-Path ".venv-build")) {
    & $pythonCmd -m venv .venv-build
}

$venvPython = Join-Path $PSScriptRoot ".venv-build\Scripts\python.exe"
& $venvPython -m pip install --upgrade pip
& $venvPython -m pip install -r requirements.txt
& $venvPython -m pip install -r requirements-dev.txt

Remove-Item -Recurse -Force build, dist -ErrorAction SilentlyContinue
New-Item -ItemType Directory -Force release | Out-Null

Write-Host "Building standalone application..." -ForegroundColor Cyan
& $venvPython -m PyInstaller --noconfirm --clean PingerApp.spec

if (-not (Test-Path "dist\PingerApp\PingerApp.exe")) {
    throw "PyInstaller did not produce dist\PingerApp\PingerApp.exe"
}

$isccCandidates = @(
    "$env:ProgramFiles(x86)\Inno Setup 6\ISCC.exe",
    "$env:ProgramFiles\Inno Setup 6\ISCC.exe"
)
$iscc = $isccCandidates | Where-Object { Test-Path $_ } | Select-Object -First 1

if (-not $iscc) {
    Write-Host ""
    Write-Host "Standalone build succeeded." -ForegroundColor Green
    Write-Host "Inno Setup 6 is not installed, so the installer cannot be compiled yet." -ForegroundColor Yellow
    Write-Host "Install Inno Setup 6, then run this script again."
    Write-Host "Portable application: dist\PingerApp\PingerApp.exe"
    exit 2
}

Write-Host "Building installer..." -ForegroundColor Cyan
& $iscc "/DMyAppVersion=$Version" "installer\PingerApp.iss"

$setup = Get-ChildItem "release\PingerApp_Setup_*.exe" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
if (-not $setup) {
    throw "Inno Setup did not produce the installer."
}

Write-Host ""
Write-Host "Build complete." -ForegroundColor Green
Write-Host "Installer: $($setup.FullName)"
