import shutil
from PIL import Image
from pathlib import Path

file_suffixes = ('.png', '.jpg', '.jpeg')

def ui():
    print("(Only default options work)")
    print("Enter working directory[0] or Choose current directory[1]", end=":")
    user_input = verified_input('0', '1') # Throws error when letters are input
    
    if (user_input == 0):
        print('Enter directory: ') # Run regexp to check directory
        directory = input()
    elif (user_input == 1):
        directory = 'current'
    else:
        exit()
    
    print("Enter custom categories[0] or use default[1]: ")
    user_input = verified_input('0', '1')
    
    if (user_input == 0):
        default_categories = False
    elif (user_input == 1):
        default_categories = True
    else:
        exit()

    print("Proceed with these settings: Directory: " + directory + ", categories: " + str(default_categories) + "?") # Edit this later


categories = {'tall': (0.0,0.4),'mobile':(0.4, 0.76), 'square':(0.76,1.3), 'desktop':(1.3,2.0), 'wide': (2.0,50)}
resolutions = {'sd': (720,1080), 'hd': (1080,1440), 'fhd': (1440,2160), 'uhd': (2160,5000)}

def group_by_aspect_ratio(folders: dict, file_list: Path.glob, working_dir: Path):
    create_folders(working_dir, folders)

    for file in file_list: # 'file' is the full file path of a file
        if file.is_file():
            if file.suffix in file_suffixes:
                img = Image.open(file)
                ratio = img.size[0]/img.size[1]
                for category in categories:
                    values = categories[category]
                    if values[0]<= ratio < values[1]:
                        destination = working_dir / category / file.name
                        shutil.copy(file, destination)


def verified_input(*options):
    user_input = input()
    while user_input not in options:
        print("Enter valid input")
        user_input = input()
    return user_input

def group_by_resolution(folders: dict, file_list: Path.glob, working_dir: Path):
    create_folders(working_dir, folders)

    for file in file_list: # 'file' is the full file path of a file
        if file.is_file():
            if file.suffix in file_suffixes:
                img = Image.open(file)
                size = min(img.size[0], img.size[1])
                for resolution in resolutions:
                    values = resolutions[resolution]
                    if values[0] <= size < values[1]:
                        destination = working_dir / resolution / file.name
                        shutil.copy(file, destination)

def walk_directory(path: Path):
    file_list = path.glob('**/*')
    return file_list

def create_folders(path: Path, folder_list):
    for folder in folder_list:
        path_to_create = path / folder
        if not path_to_create.exists():
            path_to_create.mkdir(parents=True)


#ui()
#group_by_aspect_ratio()
group_by_resolution(resolutions, walk_directory(Path("./sort")), Path.cwd())
