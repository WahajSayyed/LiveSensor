from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    requirements_list: List[str] = []
    return requirements_list

setup (
    name='APS',
    author='Wahaj Sayyed',
    version='0.0.1',
    packages= find_packages(),
    install_requriements = get_requirements(),
)