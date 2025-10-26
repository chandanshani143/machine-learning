from setuptools import setup, find_packages
from typing import List

#this file basically makes your application into a package that can be installed using pip

HYPEN_E_DOT = "-e ."   #present in requirements.txt which runs the setup.py file
def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    mentioned in the requirements.txt file
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:      #removing -e . from the list of requirements
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="machine-learning-project",
    version="0.1.0",
    author="Chandan Kumar Shani",
    author_email="chandankumarshani98@gmail.com",
    packages=find_packages(),                #this will automatically find all packages in the project
    install_requires=get_requirements("requirements.txt")
)