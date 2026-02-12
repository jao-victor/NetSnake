from napalm import get_network_driver
#import time
driver = get_network_driver('huawei_vrp')

switch = driver(
    hostname='192.168.200.227', username='napalm', password='q1w2e3R$', timeout=60,
    optional_args={'contextual_diff': True}
)

switch.open()

configuracao = """
vlan 10
desc testando
"""
switch.load_merge_candidate(config=configuracao)
print ('chegeui aq')
print(switch.compare_config())
switch.commit_config()

switch.close()
