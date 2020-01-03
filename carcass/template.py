import os

class Template(object):

    def __init__(self, path, template_name):
        self.path = path
        self.template = template_name

    
    def get_template_content(self, format=None):
        dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        template_file = '{template}.template'.format(template=self.template)
        full_path = os.path.join(dir_path, 'templates', template_file)
        f = open(os.path.abspath(full_path), "r")
        contents =f.read()
        if format:
            return contents.format(**format)
        return contents

    def create(self, extension, format=None):
        if self.template == '.gitignore':
            filename = '.gitignore'
        else:
            filename = '{template}.{extension}'.format(template=self.template, extension=extension)
        full_path = os.path.join(self.path, filename)
        print(full_path)
        content = self.get_template_content(format=format)
        if not os.path.exists(os.path.dirname(full_path)):
            try:
                os.makedirs(os.path.dirname(full_path))
            except:
                raise
            open(full_path, 'a').close()
            self.append(extension,content)
        else:
            open(full_path, 'a').close()
            self.clear(extension)
            self.append(extension,content)

    def append(self, extension, content, top=False):
        if self.template == '.gitignore':
            filename = '.gitignore'
            full_path = os.path.join(self.path, filename)
            print(full_path)
            with open(full_path, 'a+') as f:
                f.write(content)
                return 
        else:
            filename = '{template}.{extension}'.format(template=self.template, extension=extension)
        
            full_path = os.path.join(self.path, filename)
            if not os.path.exists(os.path.dirname(full_path)) or not os.path.exists(full_path):
                self.create(extension)
            if top:
                with open(full_path, 'r+') as f:
                    current_content = f.read()
                    f.seek(0, 0)
                    f.write(content.rstrip('\r\n') + '\n\n' + current_content)
            else:
                with open(full_path, 'a+') as f:
                    f.write(content)
    
    def clear(self, extension):
        if self.template == '.gitignore':
            filename = '.gitignore'
            full_path = os.path.join(self.path, filename)
            open(full_path, 'w').close()
            return
        else:
            filename = '{template}.{extension}'.format(template=self.template, extension=extension)
            full_path = os.path.join(self.path, filename)
            if not os.path.exists(os.path.dirname(full_path)):
                self.create(extension)
            open(full_path, 'w').close()

    