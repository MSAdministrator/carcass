import os

from template import Template

class Core(object):

    __package_path = None
    __package_name = None

    def __init__(self, package_name, package_path, force=False):
        self.requirements_list = []
        self.class_options = []
        self.force = force
        Core.__package_name = package_name
        Core.__package_path = self.__create_directory(package_path)
        self.__create_directory(Core.__package_path,name=package_name)


    def __create_directory(self, path, name=None):
        if name:
            abs_path = os.path.abspath(os.path.join(path,name))
            if not os.path.exists(abs_path):
                os.makedirs(abs_path)
            return abs_path
        else:
            abs_path = os.path.abspath(path)
            if not os.path.exists(abs_path):
                os.makedirs(abs_path)
            return abs_path
    
    def __create_markdown(self):
        for item in ['README', 'CONTRIBUTING', 'LICENSE']:
            template = Template(Core.__package_path, item)
            if self.force:
                template.clear('md')
            template.create('md',format={'name': Core.__package_name})

    def __create_root_files(self):
        template = Template(Core.__package_path, 'setup')
        if self.force:
            template.clear('py')
        template.create('py',format={'name': Core.__package_name})

        template = Template(Core.__package_path, '.gitignore')
        if self.force:
            template.clear('')
        template.create('',format={'name': Core.__package_name})


    def __create_requirements(self):
        template = Template(Core.__package_path, 'requirements')
        if self.force:
            template.clear('txt')
        template.create('txt',format={'requirements': '\n'.join(self.requirements_list) })
 

    def create(self, optional_template=None):
        self.__create_markdown()
        self.__create_root_files()

        template = Template('{package_path}/{package_name}'.format(package_path=Core.__package_path, package_name=Core.__package_name), '__init__')
        if self.force:
            template.clear('py')
        template.create('py',format={'imports': ''})

        template = Template('{package_path}/{package_name}'.format(package_path=Core.__package_path, package_name=Core.__package_name), 'class')
        if self.force:
            template.clear('py')
        template.create('py',format={'name': Core.__package_name})

        if optional_template:
            if isinstance(optional_template, list):
                for item in optional_template:
                    if item == 'Logger':
                        self.__create_logger()
                        template.append('py', '__LOGGER__ = logging.getLogger(__name__)', top=True)
                    if item == 'Exceptions':
                        self.__create_exceptions()
                        template.append('py', 'from {package_name}.utils.exceptions import IncorrectParameters'.format(package_name=Core.__package_name), top=True)
                    if item == 'Microsoft Graph OAuth2':
                        self.__create_graph_connector()
                        template.append('py', 'from {package_name}.graphconnector import GraphConnector'.format(package_name=Core.__package_name), top=True)
       
        self.__create_requirements()
       
        
    def __create_graph_connector(self):
        template = Template('{package_path}/{package_name}'.format(package_path=Core.__package_path, package_name=Core.__package_name), 'graphconnector')
        if self.force:
            template.clear('py')
        template.create('py')

        self.requirements_list.append('requests')
        self.requirements_list.append('oauthlib')
        self.requirements_list.append('pendulum')
        self.requirements_list.append('requests_oauthlib')

    def __create_exceptions(self):
        # create exceptions.py
        template = Template('{package_path}/{package_name}/utils'.format(package_path=Core.__package_path, package_name=Core.__package_name), 'exceptions')
        if self.force:
            template.clear('py')
        template.create('py')

    def __create_logger(self):
        self.requirements_list.append('pyyaml')
        # create logger.yml config
        template = Template(Core.__package_path, 'logger_yaml')
        if self.force:
            template.clear('yml')
        template.create('yml')


         # create logger.py
        template = Template('{package_path}/{package_name}/utils'.format(package_path=Core.__package_path, package_name=Core.__package_name), 'logger')
        if self.force:
            template.clear('py')
        template.create('py')

        # content
        content = '''
from {package_name}.utils.logger import setup_logging
setup_logging()
'''.format(package_name=Core.__package_name)

        template = Template('{package_path}/{package_name}'.format(
            package_path=Core.__package_path,
            package_name=Core.__package_name
        ),
        '__init__')
        
        if self.force:
            template.clear('py')
        template.append('py', content, top=True)