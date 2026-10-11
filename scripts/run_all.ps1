# Rebuild + full validation pipeline for the EDH commander quiz.
# Usage:  Set-ExecutionPolicy -Scope Process Bypass -Force
#         & <repo>\scripts\run_all.ps1
#   or:   pwsh ./scripts/run_all.ps1        (macOS / Linux)
#
# NOTE: this file is intentionally ASCII-only. Windows PowerShell reads .ps1 files
# without a BOM as GBK, which corrupts non-ASCII text and breaks parsing.
# Chinese output comes from the Python/Node scripts, which handle UTF-8 themselves.
$ErrorActionPreference = "Continue"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root
$failed = @()

function Step($n, $name, [scriptblock]$body) {
    Write-Host ""
    Write-Host "=== $n. $name ===" -ForegroundColor Cyan
    try {
        $out = & $body
        $out | Select-Object -Last 4 | ForEach-Object { Write-Host $_ }
        if ($LASTEXITCODE -ne 0) { $script:failed += "$n. $name (exit $LASTEXITCODE)" }
    } catch {
        Write-Host "  EXCEPTION: $_" -ForegroundColor Red
        $script:failed += "$n. $name ($_)"
    }
}

Step 0  "engine constants"       { python scripts\check_engine_constants.py }
Step 1  "fix batch boundaries"   { python scripts\fix_boundaries.py }
Step 2  "merge question banks"   { python scripts\merge_banks.py }
Step 3  "validate questions"     { python scripts\validate_questions.py }
Step 4  "validate tag map"       { python scripts\validate_tagmap.py }
Step 5  "complexity / budget"    { python scripts\build_complexity.py }
Step 6  "build commander data"   { python scripts\build_commanders.py }
Step 7  "qc vectors"             { python scripts\qc_vectors.py }
Step 8  "validate descriptions"  { python scripts\validate_descriptions.py }
Step 9  "build HTML"             { python scripts\build_html.py }
Step 10 "build Markdown"         { python scripts\build_markdown.py }
Step 11 "run JS engine"          { node scripts\parity_js.mjs }
Step 12 "engine parity"          { python scripts\parity_compare.py }
Step 13 "axis match validation"  { python scripts\axis_validation.py }
Step 14 "UI smoke test"          { node scripts\ui_smoke.mjs }
Step 15 "publish safety"         { python scripts\check_publish_safety.py }

Write-Host ""
Write-Host ("=" * 64)
if ($failed.Count -gt 0) {
    Write-Host "FAILED: $($failed.Count) step(s)" -ForegroundColor Red
    $failed | ForEach-Object { Write-Host "  - $_" -ForegroundColor Red }
    exit 1
}
Write-Host "OK: all 15 steps passed" -ForegroundColor Green
Write-Host ""
Get-ChildItem commander_quiz.html, commander_quiz.md |
    Select-Object Name, @{n = 'KB'; e = { [math]::Round($_.Length / 1KB, 1) }}
