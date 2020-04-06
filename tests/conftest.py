import os
import pytest
import tempfile
import shutil


def pytest_configure():
    pytest.configuration = {}
    pytest.configuration['package_name'] = 'testpackage'
    pytest.configuration['first_last'] = 'Josh Rickard'
    pytest.configuration['github_username'] = 'MSAdministrator'
    pytest.configuration['email_address'] = 'rickardja@live.com'
    pytest.configuration['class_imports'] = ''

    requirements_list = []

    pytest.package = {}
    pytest.package['README.md'] = 'README.template'
    pytest.package['CONTRIBUTING.md'] = 'CONTRIBUTING.template'
    pytest.package['LICENSE.md'] = 'LICENSE.template'
    pytest.package['.gitignore'] = '.gitignore.template'
    pytest.package['requirements.txt'] = 'requirements.template'
    pytest.package['setup.py'] = 'setup.template'
    
    pytest.package[pytest.configuration['package_name']] = {
        '__init__.py': '__init__.template',
        '{}.py'.format(pytest.configuration['package_name']): 'class.template'
    }
    
    pytest.package[pytest.configuration['package_name']]['utils'] = {}
    pytest.package[pytest.configuration['package_name']]['utils'].update({'__init__.py': 'utils_init.template'})
    
    pytest.package[pytest.configuration['package_name']].update({'graphconnector.py': 'graphconnector.template'})
    requirements_list.append('requests')
    requirements_list.append('oauthlib')
    requirements_list.append('pendulum')
    requirements_list.append('requests_oauthlib')
    pytest.configuration['class_imports'] += 'from {package_name}.graphconnector import GraphConnector\n'.format(package_name=pytest.configuration['package_name'])
    pytest.package[pytest.configuration['package_name']]['utils'].update({'exceptions.py': 'exceptions.template'})
    pytest.configuration['class_imports'] += 'from {package_name}.utils.exceptions import IncorrectParameters\n'.format(package_name=pytest.configuration['package_name'])
    pytest.package[pytest.configuration['package_name']]['utils'].update({'logger.py': 'logger.template'})
    pytest.package['logger.yml'] = 'logger_yaml.template'
    requirements_list.append('pyyaml')
    pytest.configuration['init_imports'] = '''
from {package_name}.utils.logger import setup_logging
setup_logging()
'''.format(package_name=pytest.configuration['package_name'])
    pytest.configuration['class_imports'] += '__LOGGER__ = logging.getLogger(__name__)\n'
    pytest.configuration['requirements'] = '\n'.join(requirements_list)



@pytest.fixture(scope='session')
def carcass_fixture():
    dirpath = tempfile.mkdtemp()
    from carcass import Carcass
    pytest.configuration['package_path'] = os.path.join(dirpath, pytest.configuration['package_name'])
    carcass = Carcass(pytest.configuration, force=True)
    return carcass
