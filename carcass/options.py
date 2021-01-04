from pick import pick

class Options(object):

    __title = 'Please select all package options which you want carcass to generate'
    __options = ['Logger', 'Exceptions', 'Microsoft Graph OAuth2', 'Flask App']

    def pick(self):
        option = pick(self.__options, self.__title, multi_select=True)
        return option