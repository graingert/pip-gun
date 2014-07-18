from setuptools import setup
from pkg_resources import require

require(
    'pip>=1.5.6',
    'setuptools>=5.4.1',
    'wheel>=0.24.0'
)

setup(
    name="pip-gun",
    version='1.0.0',
)
