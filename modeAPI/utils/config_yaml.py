'''读取yaml'''
import yaml

'''yaml  具体配置excel数据匹配'''

class YamlHandler():
    def __init__(self, file):
        self.file = file


    def read_yaml(self, encoding='utf-8'):
        '''读取yaml数据'''
        with open(self.file, encoding=encoding) as f:
            return yaml.load(f.read(),Loader=yaml.FullLoader)

    def write_yaml(self, data, encoding='utf-8'):
        with open(self.file, encoding=encoding, mode='w') as f:
            return yaml.dump(data, stream=f)