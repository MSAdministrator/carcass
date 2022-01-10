import argparse
import os
import tempfile
import shutil
import atexit

from .options import Options
from carcass import Carcass


def carcass(package_path, force=False):
    configuration = {}
    package_name = str(input('Enter your package name: '))

    configuration['package_name'] = package_name.replace('-', '_').lower()
    first_last = str(input('Enter your first and last name: '))
    configuration['first_last'] = first_last 
    github_username = str(input('Enter your GitHub user name: '))
    configuration['github_username'] = github_username 
    email_address = str(input('Enter your email address: '))
    configuration['email_address'] = email_address
    configuration['package_path'] = os.path.abspath(os.path.join(package_path))
    configuration['class_imports'] = ''

    pick_list = Options().pick()
    options = [i[0] for i in pick_list]

    package = {}
    requirements_list = []
    package['README.md'] = 'README.template'
    package['CONTRIBUTING.md'] = 'CONTRIBUTING.template'
    package['LICENSE.md'] = 'LICENSE.template'
    package['.gitignore'] = '.gitignore.template'
    package['requirements.txt'] = 'requirements.template'
    package['setup.py'] = 'setup.template'
    package['mkdocs.yml'] = 'mkdocs.template'

    package['docs'] = {
        'README.md': 'README.template',
        '{}-ref.md'.format(configuration['package_name'].replace('-', '_').lower()): 'class-ref-doc.template',
        'CONTRIBUTING.md': 'CONTRIBUTING.template',
        'LICENSE.md': 'LICENSE.template'
    }

    package['.github'] = {
        'ISSUE_TEMPLATE': {
            'bug_report.md': 'bug_report.template',
            'feature_request.md': 'feature_request.template'
        },
        'workflows': {
            'macos.yml': 'macos.template',
            'windows.yml': 'windows.template',
            'ubuntu.yml': 'ubuntu.template',
            'publish.yml': 'publish_pypi.template',
            'docs.yml': 'doc_generation.template'
        }
    }

    package[configuration['package_name']] = {
        '__init__.py': '__init__.template',
        '{}.py'.format(configuration['package_name'].replace('-', '_').lower()): 'class.template',
        '__main__.py': 'main.template'
    }
    if options:
        package[configuration['package_name']]['utils'] = {}
        package[configuration['package_name']]['utils'].update({'__init__.py': 'utils_init.template'})
        package[configuration['package_name']]['utils'].update({'version.py': 'version.template'})
        if 'Flask App' in options:
            package['Dockerfile'] = 'flask/Dockerfile.template'
            package['docker-compose.yml'] = 'flask/docker-compose.template'
            package[configuration['package_name']]['app'] = {}
            package[configuration['package_name']]['app'].update({'__init__.py': 'flask/flask.template'})
            package[configuration['package_name']]['app'].update({'config.py': 'flask/flaskconfig.template'})
            package[configuration['package_name']]['app']['templates'] = {
                '404.html': 'flask/404.html',
                '500.html': 'flask/500.html',
                'base.html': 'flask/base.html',
                'index.html': 'flask/index.html'
            }
            requirements_list.append('Flask')
            requirements_list.append('Flask-API')
            requirements_list.append('flask-wtf')
            requirements_list.append('Flask-Session')
            requirements_list.append('flask-bootstrap')
            requirements_list.append('flask-nav')
            requirements_list.append('gunicorn')
            package[configuration['package_name']]['app']['api'] = {
                'api.py': 'flask/flaskblueprint.template'
            }
            package[configuration['package_name']]['app']['frontend'] = {
                'frontend.py': 'flask/flaskblueprint.template'
            }
        if 'Microsoft Graph OAuth2' in options:
            package[configuration['package_name']].update({'graphconnector.py': 'graphconnector.template'})
            requirements_list.append('requests')
            requirements_list.append('oauthlib')
            requirements_list.append('pendulum')
            requirements_list.append('requests_oauthlib')
            configuration['class_imports'] += 'from .graphconnector import GraphConnector\n'
        if 'Exceptions' in options:
            package[configuration['package_name']]['utils'].update({'exceptions.py': 'exceptions.template'})
            configuration['class_imports'] += 'from .utils.exceptions import IncorrectParameters\n'
        if 'Logger' in options:
            package[configuration['package_name']]['data'] = {}
            package[configuration['package_name']]['utils'].update({'logger.py': 'logger.template'})
            package[configuration['package_name']]['data']['logger.yml'] = 'logger_yaml.template'
            package[configuration['package_name']]['core.py'] = 'core.template'
            requirements_list.append('pyyaml')
            configuration['init_imports'] = '''
import logging

from .utils.logger import setup_logging
setup_logging()
'''.format(package_name=configuration['package_name'])
            configuration['class_imports'] += '''
import logging
__LOGGER__ = logging.getLogger(__name__)\n
            '''
    requirements_list.append('fire')
    configuration['requirements'] = '\n'.join(requirements_list)

    carcass = Carcass(configuration, force=force)
    carcass.create_package(configuration['package_path'], package)


def main(args=None):
    parser = argparse.ArgumentParser(description = 'carcass is a Python package to generate python package scaffolding based on best practices')
    parser.add_argument('-P', '--path', help='Path to generate template package')
    parser.add_argument('-F', '--force', help='Force the creation of a template package', action='store_true')

    args = parser.parse_args()
    carcass(args.path, force=args.force)


if __name__ == "__main__":
    main()