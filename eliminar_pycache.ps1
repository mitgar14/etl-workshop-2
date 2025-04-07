Write-Host "Buscando y eliminando directorios __pycache__ (excepto los de venv)..."

Get-ChildItem -Path . -Recurse -Directory -Filter "__pycache__" | Where-Object {
    $_.FullName -notmatch "\\venv\\"
} | ForEach-Object {
    Write-Host "Eliminando:" $_.FullName
    Remove-Item $_.FullName -Recurse -Force
}

Write-Host "Eliminación completada."