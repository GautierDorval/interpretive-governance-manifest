param(
  [switch]$Check
)

$ErrorActionPreference = "Stop"

Write-Host "== interpretive-governance-manifest :: build artifacts ==" -ForegroundColor Cyan

if (-not (Test-Path "./scripts/requirements.txt")) {
  throw "Run this script from the repository root." 
}

# Ensure Python deps for generation are present.
python -m pip install --upgrade pip | Out-Null
python -m pip install -r "./scripts/requirements.txt" | Out-Null

if ($Check) {
  Write-Host "[CHECK] entity-graph artifacts" -ForegroundColor Yellow
  python "./scripts/generate_entity_graph.py" --check

  Write-Host "[CHECK] integrity hashes" -ForegroundColor Yellow
  python "./scripts/recompute_integrity_hashes.py" --check

  Write-Host "✅ Check OK." -ForegroundColor Green
  exit 0
}

Write-Host "[BUILD] entity-graph artifacts" -ForegroundColor Yellow
python "./scripts/generate_entity_graph.py"

Write-Host "[BUILD] integrity hashes" -ForegroundColor Yellow
python "./scripts/recompute_integrity_hashes.py"

Write-Host "✅ Build complete. Review changes, then commit." -ForegroundColor Green
