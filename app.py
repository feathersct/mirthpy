import json
from mirthpy.mirthService import MirthService

config = json.load(open('config.json'))

service = MirthService(config)
service.open()

c = service.getChannels({"channelId":"3bb08639-7725-4b1b-a2ac-13687101fe9b"}) 
c.channels[0].name

maps = service.getConfigurationMaps()

tokenConfigs = list(filter(lambda x: "token" in x.string, maps.entry))

print('')