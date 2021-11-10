'./data/temp_data.yaml'
from modeUI.base.baseMethod import BaseMethod
from utils.config_yaml import YamlHandler

file_path = '../data/temp_data.yaml'
# data = 'SG21111009503048000'
# YamlHandler(file_path).write_yaml(data)

data = YamlHandler('../data/temp_data.yaml').read_yaml()
print(data)

# f = open(file_path, 'r+')
# f.truncate()
dataA = {'2': '3'}
dataB = {'1': '2'}
dataC = ['12':'1
data = YamlHandler('../data/temp_data.yaml').write_yaml(dataC)
