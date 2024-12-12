from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads the requirements file and returns a list of dependencies.
    """
    requirements = []
    try:
        with open(file_path, "r") as file_obj:
            requirements = file_obj.readlines()
            # Remove newline characters and strip extra spaces
            requirements = [req.strip() for req in requirements]
            # Remove "-e ." if present
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Mayur',
    author_email='mayur2209b01@aptechgdn.net',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),  # Correct filename
)
