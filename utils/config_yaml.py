'''读取yaml'''
import yaml

'''yaml 暂存数据'''


class YamlHandler:
    def __init__(self, file):
        self.file = file

    '''读取yaml数据'''

    def read_yaml(self, encoding='utf-8'):
        with open(self.file, encoding=encoding) as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)

    '''【字典】 写入yaml'''
    ''' mode='a' 修改写入方式，可实现追加，写入的时候采用字典的键值对形式'''

    def write_yaml(self, data, encoding='utf-8'):
        with open(self.file, encoding=encoding, mode='a') as f:
            return yaml.dump(data, stream=f)
