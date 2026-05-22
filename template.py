import os
from pathlib import Path
import logging

#logging String
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = 'Kidney_Disease_Classification'

list_of_file = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templets/index.html"
]
 

for file_path in list_of_file:
    filepath = Path(file_path) # windows sometime uses \ instead of / so Path fix that
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True) # exist_ok=True will not create if folder exists
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating Empty File: {filepath}")
    else:
        logging.info(f"{filename} already exists")
 