import os

path_file = f"E:\Stoqn\Programirane\Python\ExamplesProject\Test_File.txt"
path_folder = f"E:\Stoqn\Programirane\Python\ExamplesProject\Test_Folder"

def Is_Folder():
    if os.path.exists(path_folder):
        print("Указаното място съществува!")
        if os.path.isdir(path_folder):
            print("Това е папка!")
    else:
        print("Указаното място НЕ съществува!")

def Is_File():
    if os.path.exists(path_file):
        print("Указаното място съществува!")
        if os.path.isfile(path_file):
            print("Това е файл!")
    else:
        print("Указаното място НЕ съществува!")

Is_Folder()
print()
Is_File()
