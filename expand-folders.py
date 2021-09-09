import shutil
from pathlib import Path

def create_folders(path: Path, folder_list: dict):
    for folder in folder_list:
        path_to_create = path / folder
        if not path_to_create.exists():
            path_to_create.mkdir(parents=True)

def walk_directory(path: Path):
    file_list = path.glob('**/*')
    return file_list


cwd = Path.cwd()
create_folders(cwd, {'expanded': 0})
expanded = cwd / 'expanded'

file_list = walk_directory(cwd)

for file in file_list:
    if file.is_file() and file.name != 'expand-folders.py':
        if not Path.exists(expanded / file.name):
            if not file.samefile(expanded / file.name):
                shutil.move(file, expanded / file.name)

# Rethink your life choices