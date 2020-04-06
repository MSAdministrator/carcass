from setuptools import setup, find_packages


def parse_requirements(requirement_file):
    with open(requirement_file) as f:
        return f.readlines()


version = {}
with open("carcass/utils/version.py") as fp:
    exec(fp.read(), version)

setup(
    name='carcass',
    version=version['__version__'],
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A Python package to generate python package scaffolding based on best practices',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=parse_requirements('requirements.txt'),
    keywords=['scaffolding', 'scaffold', 'python'],
    url='https://github.com/msadministrator/carcass',
    author='MSAdministrator',
    author_email='rickardja@live.com',
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    entry_points={
          'console_scripts': [
              'carcass = carcass.__main__:main'
          ]
    },
    package_data={
        'carcass':  ['templates/*.template', 'templates/.gitignore.template']
    }
)
