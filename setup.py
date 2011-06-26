from setuptools import setup, find_packages
from os import path
BASE_DIR = path.abspath(path.dirname(__file__))


setup(
    name='titere',
    version='0.0.1',
    description='Configuration Management Tool',
    author='Jorge Eduardo Cardona',
    author_email='jorgeecardona@gmail.com',
    license="BSD",
    url="http://pypi.python.org/pypi/titere/",
    long_description=open(path.join(BASE_DIR, 'README.rst')).read(),
    packages=find_packages(),
    test_suite='titere.tests',
    entry_points={
        'console_scripts': [
            'titere = titere.main:main',
            ],
        },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        ],
    )
