from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    """This function will return the list of libraries
    that we potentially need to install to develop our app"""
    req = []
    with open(file_path) as f:
        req = f.readlines()
        req = [r.replace("\n","") for r in req]

        if '-e .' in req:
            req.remove('-e .')
    return req

setup(
    name='machineLearningProject',
    version='0.0.1',
    author='Akash',
    author_email='akashpatel.21.ap@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)