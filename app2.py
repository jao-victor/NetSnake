from napalm import get_network_driver
import os
from dotenv import load_dotenv

load_dotenv()
user = os.getenv('USER')
passwd = os.getenv('PASS')


driver = get_network_driver('huawei_vrp')

switchs = ['192.168.200.227', '192.168.200.225']

print(user)
print(passwd)

for s in switchs:
    with driver(hostname=s, username=user, password=passwd, timeout=60,optional_args={'contextual_diff': True}) as switch:

        print(f'Alterando configurações do host {s}')
        configuracao = """
        vlan 50
        desc testando
        """
        switch.load_merge_candidate(config=configuracao)
        print ('chegeui aq')
        print(switch.compare_config())
        switch.commit_config()
        print(f'configuração finalizada')
            
