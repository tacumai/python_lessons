from dde_client import DDEClient

dde = DDEClient('RSS', 'N225.FUT01.OS')
print(dde.request(u'現在値'))
