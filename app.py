import shutil
from PIL import Image
from pathlib import Path

file_suffixes = ('.png', '.jpg', '.jpeg')

print("Enter working directory[0] or Choose current directory[1]: ")
user_input = input()
while user_input!=0 and user_input!=1:
    print("Enter valid input")
    user_input = input()

if (user_input == '0'):
    print('Enter directory: ')
    directory = input()
elif (user_input == '1'):
    directory = 'current'

print(directory)

working_directory = Path.cwd() / 'testdir'
categories = {'mobile':(0.2, 1.5), 'desktop':(1.5,1.8)}

def main():
    for category in categories:
        path_to_create = working_directory / category
        if not path_to_create.exists():
            path_to_create.mkdir(parents=True)

    file_list = working_directory.iterdir()
    for file in file_list: # 'file' is the full file path of a file
        if file.is_file():
            if file.suffix in file_suffixes:
                img = Image.open(file)
                ratio = img.size[0]/img.size[1]
                for category in categories:
                    values = categories[category]
                    if values[0]<= ratio < values[1]:
                        destination = working_directory / category / file.name
                        shutil.copy(file, destination)

