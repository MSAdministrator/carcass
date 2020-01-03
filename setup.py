from setuptools import setup, find_packages

def parse_requirements(requirement_file):
    with open(requirement_file) as f:
        return f.readlines()

setup(
    name='carcass',
    version='0.0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A Python package to generate python package scaffolding based on best practices',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=parse_requirements('./requirements.txt'),
    keywords=['scaffolding', 'scaffold', 'python'],
    url='https://github.com/msadministrator/carcass',
    author='MSAdministrator',
    author_email='rickardja@live.com',
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    entry_points = {
        'console_scripts': ['carcass=carcass.command_line:main'],
    },
    package_data={
        'templates':['*.template']
    }
)