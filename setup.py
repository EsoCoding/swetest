from setuptools import setup, find_packages

setup(
    name='swetest',
    version='0.1.0',
    author='Gertjan Poortman',
    author_email='arjanpoortman@gmail.com',
    description='Python wrapper for swetest, a swissephemeris tool that calculates with high precision Astrological planetary positions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/esocoding/swetest',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=open('requirements.txt').readlines(),
    test_suite='tests',
)
