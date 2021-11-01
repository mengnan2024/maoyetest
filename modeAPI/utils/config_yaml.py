'''读取yaml'''

class YamlHandler():
    def __init__(self, file):
        self.file = file


    def read_yaml(self, encoding='utf-8'):
        '''读取yaml数据'''
        with open(self.file, encoding=encoding) as f:
            return yaml.load