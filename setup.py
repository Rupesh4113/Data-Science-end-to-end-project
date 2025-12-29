from setuptools import find_packages, setup

from typing import List

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file:
        requirements = file.readlines()
    return [req.strip() for req in requirements if req.strip() and not req.startswith("#")]

    requirements=[]
    with open(file_path) as file:
        requirements = file.readlines()
        requirements=[req.replace("\n","") for req in requirements if req.strip() and not req.startswith("#")]
        return requirements

setup(
name= "Data Science Project",
version= "1.0",
author= "Rupesh Pandey",
author_email= "amerupesh08@gmail.com",
packages= find_packages(),
install_requires=get_requirements("requirements.txt"),
description= "A sample data science project setup",
long_description= open("README.md").read(),


)