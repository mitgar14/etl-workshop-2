Write-Host "Buscando y eliminando todos los directorios __pycache__..."

Get-ChildItem -Path . -Recurse -Directory -Filter "__pycache__" | ForEach-Object {
    Write-Host "Eliminando:" $_.FullName
    Remove-Item $_.FullName -Recurse -Force
}

Write-Host "Eliminación completada."