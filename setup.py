from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT= '-e .'
def get_requirements(file_path: str) -> List[str]:
    '''Reads a requirements file and returns a list of requirements.'''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='ml_project',
    version='0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
# This setup script uses setuptools to package the project.
# It reads the requirements from a 'requirements.txt' file and includes them in the installation requirements