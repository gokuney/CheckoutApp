from setuptools import setup
from distutils.cmd import Command

setup(
    name='CheckoutApp',
    version='1.0',
    description='A simple cart checkout application',
    author='Priyanshu Sharma',
    author_email='gokney@gmail.com',
    tests_require=['pytest'],
    install_requires=['pytest', 'tabulate'],
)
