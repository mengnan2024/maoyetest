__author__ = 'mengnan'

from utils.config_yaml import YamlHandler

'''连接sql用，以下为ssh连接'''

import pymysql


class ConnectToMysql:

    @classmethod
    def huMysql_(self, statements):
        '''读取ymal数据'''
        read_date = YamlHandler('../config/mySQL.yaml').read_yaml()
        '''获取第一个key的值'''
        first_key = next(iter(read_date))
        r = read_date.get(first_key)

        # 设置数据库
        client = pymysql.connect(
            host='127.0.0.1',  # 此处固定
            port=server.local_bind_port,
            user=r.get('sql_username'),
            passwd=r.get('sql_password'),
            db=r.get('sql_db')
        )
        cursor = client.cursor()
        cursor.execute(statements)  # 查询
        data = cursor.fetchall()
        result = ''.join('%s' % a for a in data)
        client.commit()
        return result
        # print('删除成功！')
        client.commit()
        server.close()

    # @classmethod
    # def huimingMysql_ssh(self, statements):
    #     '''读取ymal数据'''
    #     read_date = YamlHandler('../config/mySQL.yaml').read_yaml()
    #     '''获取第一个key的值'''
    #     first_key = next(iter(read_date))
    #     r = read_date.get(first_key)
    #
    #     # 设置ssh
    #     server = SSHTunnelForwarder(
    #         (r.get('ssh_adress'), r.get('ssh_port')),  # ssh的配置
    #         ssh_password=r.get('ssh_password'),
    #         ssh_username=r.get('ssh_username'),
    #         remote_bind_address=(r.get('sql_adress'), r.get('sql_port'))
    #     )
    #
    #     server.start()
    #
    #     # 设置数据库
    #     client = pymysql.connect(
    #         host='127.0.0.1',  # 此处固定
    #         port=server.local_bind_port,
    #         user=r.get('sql_username'),
    #         passwd=r.get('sql_password'),
    #         db=r.get('sql_db')
    #     )
    #     cursor = client.cursor()
    #     cursor.execute(statements)  # 查询
    #     data = cursor.fetchall()
    #     result = ''.join('%s' % a for a in data)
    #     client.commit()
    #     return result
    #     # print('删除成功！')
    #     client.commit()
    #     server.close()
