from setuptools import find_packages, setup
from typing import List #type: ignore

def get_requirements(file_path):
    with open(file_path, 'r') as file_obj:
        modules = file_obj.readlines()
    
    modules = [module.replace("\n","") for module in modules]

    if "-e ." in modules:
        modules.remove("-e .")


setup(
    name = "Flight Price Prediction System",
    version = "0.0.1",
    author = "Shubhankar Chaturvedi",
    author_email = "shubhankar5848@gmail.com",
    packages = find_packages(),
    install_here = get_requirements('requirements.txt')
)