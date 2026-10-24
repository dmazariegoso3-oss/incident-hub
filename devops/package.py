"""Empaquetar únicamente archivos versionables; nunca bases de datos o secretos."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
version = (root / 'VERSION').read_text().strip()
out = root / 'dist'
out.mkdir(exist_ok=True)
allowed = {'.py', '.js', '.css', '.html', '.sql', '.md', '.yml', '.txt', '.csv', '.ps1'}
with ZipFile(out / f'incident-hub-{version}.zip', 'w', ZIP_DEFLATED) as archive:
    for path in root.rglob('*'):
        relative = path.relative_to(root)
        if any(part in {'.git', '__pycache__', 'dist', '.venv'} for part in relative.parts):
            continue
        if path.is_file() and (path.suffix in allowed or path.name in {'VERSION', '.gitignore'}):
            archive.write(path, relative)
print(out / f'incident-hub-{version}.zip')
