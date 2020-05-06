import argparse
import os
import tempfile
import shutil
import atexit

from .options import Options
from carcass import Carcass

class readable_dir(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        prospective_dir=values
        if not os.path.isdir(prospective_dir):
            raise argparse.ArgumentTypeError("readable_dir:{0} is not a valid path".format(prospective_dir))
        if os.access(prospective_dir, os.R_OK):
            setattr(namespace,self.dest,prospective_dir)
        else:
            raise argparse.ArgumentTypeError("readable_dir:{0} is not a readable dir".format(prospective_dir))

def carcass(package_path, force=False):
    configuration = {}
    package_name = str(input('Enter your package name: '))
    configuration['package_name'] = package_name 
    first_last = str(input('Enter your first and last name: '))
    configuration['first_last'] = first_last 
    github_username = str(input('Enter your GitHub user name: '))
    configuration['github_username'] = github_username 
    email_address = str(input('Enter your email address: '))
    configuration['email_address'] = email_address
    configuration['package_path'] = os.path.join(package_path, configuration['package_name'])
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
    
    package[configuration['package_name']] = {
        '__init__.py': '__init__.template',
        '{}.py'.format(configuration['package_name']): 'class.template'
    }
    if options:
        package[configuration['package_name']]['utils'] = {}
        package[configuration['package_name']]['utils'].update({'__init__.py': 'utils_init.template'})
        package[configuration['package_name']]['utils'].update({'version.py': 'version.template'})
        if 'Microsoft Graph OAuth2' in options:
            package[configuration['package_name']].update({'graphconnector.py': 'graphconnector.template'})
            requirements_list.append('requests')
            requirements_list.append('oauthlib')
            requirements_list.append('pendulum')
            requirements_list.append('requests_oauthlib')
            configuration['class_imports'] += 'from {package_name}.graphconnector import GraphConnector\n'.format(package_name=configuration['package_name'])
        if 'Exceptions' in options:
            package[configuration['package_name']]['utils'].update({'exceptions.py': 'exceptions.template'})
            configuration['class_imports'] += 'from {package_name}.utils.exceptions import IncorrectParameters\n'.format(package_name=configuration['package_name'])
        if 'Logger' in options:
            package[configuration['package_name']]['utils'].update({'logger.py': 'logger.template'})
            package['logger.yml'] = 'logger_yaml.template'
            requirements_list.append('pyyaml')
            configuration['init_imports'] = '''
import logging

from {package_name}.utils.logger import setup_logging
setup_logging()
'''.format(package_name=configuration['package_name'])
            configuration['class_imports'] += '__LOGGER__ = logging.getLogger(__name__)\n'

    configuration['requirements'] = '\n'.join(requirements_list)

    carcass = Carcass(configuration, force=force)
    carcass.create_package(configuration['package_path'], package)


def main(args=None):
    parser = argparse.ArgumentParser(description = 'carcass is a Python package to generate python package scaffolding based on best practices')
    parser.add_argument('-P', '--path', action=readable_dir, default=os.path.expanduser('~'), help='Path to generate template package')
   # parser.add_argument('-N', '--name', help='The package name to generate a template for')
    parser.add_argument('-F', '--force', help='Force the creation of a template package', action='store_true')

    args = parser.parse_args()
    #if not args.name:
    #    raise Exception('Exiting because you must provide a name of your template python package.')
    carcass(args.path, force=args.force)


if __name__ == "__main__":
    main()