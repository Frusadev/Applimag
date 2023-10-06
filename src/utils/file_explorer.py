import os
from rich.console import Console
from rich.tree import Tree
import shutil
import zipfile
import string_utils

def show_directory_structure(directory_path:str) -> Tree:
    console = Console()
    
    if not os.path.isdir(directory_path):
        raise Exception(f"{directory_path} is not a directory")
    
    tree = Tree(directory_path)

    for root, dirs, files in os.walk(directory_path):
        
        subtree = tree.add(root)
        for dir in dirs:
            subtree.add(dir)

        for file in files:
            subtree.add(file)

    console.print(tree)
    return tree

def remove_files(files:set):
    for file in files:
        if os.path.exists(os.path.abspath(file)):
            os.remove(file) if not os.path.isdir(file) else shutil.rmtree(file)

def extract_zip(src:str, dest:str, error_message_prefix="Unable to extract file due to ") -> str:
    if not os.path.exists():
        raise FileNotFoundError(f"{src}")
    if os.path.isdir(src):
        raise IsADirectoryError
    with zipfile.ZipFile(src, 'r') as file:
        try:
            file.extractall(dest)
            return dest
        except PermissionError:
            print(string_utils.color(f'{error_message_prefix} + | Permission error', 'red'))
            return None
        except zipfile.BadZipFile:
            print(string_utils.color(f'{error_message_prefix} + | Baz zip file', 'red'))
            return None
        except:
            print(string_utils.color(f'{error_message_prefix} + | Unknown error', 'red'))