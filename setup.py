from setuptools import setup
from pkg_resources import require

require(
    'pip>=1.5.6',
    'setuptools>=5.4.1',
    'wheel>=0.24.0'
)

setup(
    name="pip-gun",
    packages=['pip_gun'],
    version='1.0.1',
    author="Thomas Grainger",
    author_email="pip-gun@graingert.co.uk",
    url="https://github.com/graingert/pip-gun"
)
