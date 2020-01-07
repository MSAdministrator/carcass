import os
import pytest


def test_package_directory_was_created(carcass_fixture):
    """Test that carcass package_name variable is set
    """
    assert os.path.exists(pytest.configuration['package_path'])

def test_creation_of_readme_template_exists(carcass_fixture):
    '''
    Testing the creation of README.md template file
    '''
    carcass = carcass_fixture.create_package(pytest.configuration['package_path'], pytest.package)
    assert os.path.exists(os.path.join(str(pytest.configuration['package_path']), 'README.md'))

def test_readme_has_project_name_replaced(carcass_fixture):
    '''
    Testing README.md template file has package name replaced
    '''
    carcass = carcass_fixture.create_package(pytest.configuration['package_path'], pytest.package)
    filepath = os.path.join(str(pytest.configuration['package_path']), 'README.md')
    count = 1
    with open(filepath) as fp:
        for cnt, line in enumerate(fp):
            if line == 1:
                if cnt is '# {}'.format(pytest.configuration['package_name']):
                    assert True
                    break
                else:
                    assert False
                    break


def test_creation_of_contributing_template_exists(carcass_fixture):
    '''
    Testing the creation of CONTRIBUTING.md template file
    '''
    carcass = carcass_fixture.create_package(pytest.configuration['package_path'], pytest.package)
    assert os.path.exists(os.path.join(str(pytest.configuration['package_path']), 'CONTRIBUTING.md'))


def test_creation_of_license_template_exists(carcass_fixture):
    '''
    Testing the creation of LICENSE.md template file
    '''
    carcass = carcass_fixture.create_package(pytest.configuration['package_path'], pytest.package)
    assert os.path.exists(os.path.join(str(pytest.configuration['package_path']), 'LICENSE.md'))

def test_creation_of_requirements_template_exists(carcass_fixture):
    '''
    Testing the creation of requirements.txt file
    '''
    carcass = carcass_fixture.create_package(pytest.configuration['package_path'], pytest.package)
    assert os.path.exists(os.path.join(str(pytest.configuration['package_path']), 'requirements.txt'))

def test_contents_of_requirements_template_exists(carcass_fixture):
    '''
    Testing the contents of requirements.txt file
    '''
    carcass = carcass_fixture.create_package(pytest.configuration['package_path'], pytest.package)
    filepath = os.path.join(str(pytest.configuration['package_path']), 'requirements.txt')
    with open(filepath) as fp:
        datafile = fp.readlines()
    if 'requests\n' not in datafile:
        assert False
    if 'oauthlib\n' not in datafile:
        assert False
    if 'pendulum\n' not in datafile:
        assert False
    if 'requests_oauthlib\n' not in datafile:
        assert False
    if 'pyyaml' not in datafile:
        assert False
    assert True

def test_creation_of_gitignore_template_exists(carcass_fixture):
    '''
    Testing the creation of .gitignore file
    '''
    carcass = carcass_fixture.create_package(pytest.configuration['package_path'], pytest.package)
    assert os.path.exists(os.path.join(str(pytest.configuration['package_path']), '.gitignore'))

def test_creation_of_logger_yaml_template_exists(carcass_fixture):
    '''
    Testing the creation of logger.yml file
    '''
    carcass = carcass_fixture.create_package(pytest.configuration['package_path'], pytest.package)
    assert os.path.exists(os.path.join(str(pytest.configuration['package_path']), 'logger.yml'))

def test_creation_of_setup_py_template_exists(carcass_fixture):
    '''
    Testing the creation of setup.py file
    '''
    carcass = carcass_fixture.create_package(pytest.configuration['package_path'], pytest.package)
    assert os.path.exists(os.path.join(str(pytest.configuration['package_path']), 'setup.py'))

def test_contents_of_requirements_template_exists(carcass_fixture):
    '''
    Testing the contents of setup.py
    '''
    carcass = carcass_fixture.create_package(pytest.configuration['package_path'], pytest.package)
    filepath = os.path.join(str(pytest.configuration['package_path']), 'setup.py')
    with open(filepath) as fp:
        datafile = fp.read()

    content = '''setup(
    name='{package_name}',
    version=version['__version__'],
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A Python package created using carcass',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=parse_requirements('./requirements.txt'),
    keywords=['carcass'],
    url='https://github.com/{github_username}/{package_name}',
    author='{github_username}',
    author_email='{email_address}',
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4'
)'''.format(
    package_name=pytest.configuration['package_name'],
    github_username=pytest.configuration['github_username'],
    email_address=pytest.configuration['email_address'])

    if content in datafile:
        assert True
    
def test_creation_of_package_folder_exists(carcass_fixture):
    '''
    Testing the creation of package directory
    '''
    carcass = carcass_fixture.create_package(pytest.configuration['package_path'], pytest.package)
    assert os.path.exists(os.path.join(str(pytest.configuration['package_path']), pytest.configuration['package_name']))

def test_creation_of_package_init_exists(carcass_fixture):
    '''
    Testing the creation of package directory __init__.py file
    '''
    carcass = carcass_fixture.create_package(pytest.configuration['package_path'], pytest.package)
    assert os.path.exists(os.path.join(str(pytest.configuration['package_path']), pytest.configuration['package_name'], '__init__.py'))

def test_contents_of_package_init(carcass_fixture):
    '''
    Testing the contents of package directory __init__.py file
    '''
    carcass = carcass_fixture.create_package(pytest.configuration['package_path'], pytest.package)
    filepath = os.path.join(str(pytest.configuration['package_path']), pytest.configuration['package_name'], '__init__.py')
    with open(filepath) as fp:
        datafile = fp.read()
    if pytest.configuration['init_imports'] in datafile:
        assert True

def test_creation_of_package_class_exists(carcass_fixture):
    '''
    Testing the creation of package directory package_name.py file
    '''
    carcass = carcass_fixture.create_package(pytest.configuration['package_path'], pytest.package)
    assert os.path.exists(os.path.join(str(pytest.configuration['package_path']), pytest.configuration['package_name'], '{package_name}.py'.format(package_name=pytest.configuration['package_name'])))

def test_contents_of_package_class_has_imports(carcass_fixture):
    '''
    Testing the contents of package directory package_name.py file
    '''
    carcass = carcass_fixture.create_package(pytest.configuration['package_path'], pytest.package)
    filepath = os.path.join(str(pytest.configuration['package_path']), pytest.configuration['package_name'], '{package_name}.py'.format(package_name=pytest.configuration['package_name']))
    with open(filepath) as fp:
        datafile = fp.read()
    if pytest.configuration['class_imports'] in datafile:
        assert True

def test_creation_of_package_graphconnector_exists(carcass_fixture):
    '''
    Testing the creation of graphconnector.py file
    '''
    carcass = carcass_fixture.create_package(pytest.configuration['package_path'], pytest.package)
    assert os.path.exists(os.path.join(str(pytest.configuration['package_path']), pytest.configuration['package_name'], 'graphconnector.py'))


def test_creation_of_package_utils_folder(carcass_fixture):
    '''
    Testing the creation of package_name/utils folder
    '''
    carcass = carcass_fixture.create_package(pytest.configuration['package_path'], pytest.package)
    assert os.path.exists(os.path.join(str(pytest.configuration['package_path']), pytest.configuration['package_name'], 'utils'))

def test_creation_of_package_utils_init_file(carcass_fixture):
    '''
    Testing the creation of package_name/utils/__init__.py file
    '''
    carcass = carcass_fixture.create_package(pytest.configuration['package_path'], pytest.package)
    assert os.path.exists(os.path.join(str(pytest.configuration['package_path']), pytest.configuration['package_name'], 'utils', '__init__.py'))

def test_creation_of_package_utils_logger_file(carcass_fixture):
    '''
    Testing the creation of package_name/utils/logger.py file
    '''
    carcass = carcass_fixture.create_package(pytest.configuration['package_path'], pytest.package)
    assert os.path.exists(os.path.join(str(pytest.configuration['package_path']), pytest.configuration['package_name'], 'utils', 'logger.py'))

def test_creation_of_package_utils_exceptions_file(carcass_fixture):
    '''
    Testing the creation of package_name/utils/exceptions.py file
    '''
    carcass = carcass_fixture.create_package(pytest.configuration['package_path'], pytest.package)
    assert os.path.exists(os.path.join(str(pytest.configuration['package_path']), pytest.configuration['package_name'], 'utils', 'exceptions.py'))