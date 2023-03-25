import json
from mirthpy.mirthService import MirthService

#config = json.load(open('config.json'))

#service = MirthService(config)

service = MirthService(username="admin", password="admin", instance="localhost")
service.open()


c = service.getChannels(['1f636389-a1cb-4355-910c-29c7eeb9fd15']) 
c.channels[0].name

maps = service.getConfigurationMaps()
maps.getXML()

tokenConfigs = list(filter(lambda x: "token" in x.string, maps.entry))

print('')