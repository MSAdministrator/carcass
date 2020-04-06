import os
from string import Formatter


class Carcass(object):

    def __init__(self, configuration, force=False):
        self.requirements_list = []
        self.class_options = []
        self.force = force
        self.configuration = configuration
        self.package_name = configuration['package_name']
        self.package_path = self.__create_directory(configuration['package_path'],name=configuration['package_name'])

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
    
    def __get_variable_names(self, content):
        return [fn for _, fn, _, _ in Formatter().parse(content) if fn is not None]

    def __get_formatted_content(self, content):
        properties = {}
        for item in self.__get_variable_names(content):
           # print(item)
            for key, value in self.configuration.items():
                if key == item:
                    properties[key] = value
        return content.format(**properties)

    def get_template_content(self, template):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        full_path = os.path.join(dir_path, 'templates', template)
        f = open(os.path.abspath(full_path), "r")
        contents =f.read()
        if self.configuration:
            if template == 'graphconnector.template':
                return contents
            return self.__get_formatted_content(contents)
        return contents

    def __write_data(self, root_directory, key, val):
        abs_path = os.path.abspath(root_directory)
        if not os.path.exists(abs_path):
            os.makedirs(abs_path)
        content = self.get_template_content(val)
        filename = os.path.join(abs_path, key)
        if self.force:
            open(filename, 'w').close()
        with open(filename, 'a+') as f:
            f.write(content)

    def create_package(self, root_directory, package_structure):
        for k, v in package_structure.items():
            if not isinstance(v, dict):
                # write the file
                self.__write_data(root_directory, k, v)
            else: # it's another dict, so recurse
                # add the key to the path
                new_root = os.path.join(root_directory, k) # you'll need to import os
                self.create_package(new_root, v)