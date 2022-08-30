import json
from mirthpy.connectors import JavaScriptReceiverProperties
from mirthpy.mirthService import MirthService

# Get config file
config = json.load(open('config.json'))

# Open the Mirth Service
service = MirthService(config)
service.open()

channelIds = ["44dacc20-718a-490c-bfcf-82355ed9209d", "3bb08639-7725-4b1b-a2ac-13687101fe9b"]
pollingOnly = True
i = 0
s = "hi"

# Get channel names
# namesAndIds = service.getChannelIdsAndNames()
# for ni in namesAndIds.entry:
#     print(f"{ni.string[1]} - {ni.string[0]}") # channelName - channelId


id = service.getChannelIdByName('us_matrixcare_soap_outbound_claytontest')
channel = service.getChannel(id)
channel.name
channel.description
channel.sourceConnector.transformer

if type(channel.sourceConnector.properties) == JavaScriptReceiverProperties:
    # do stuff we'd know only a javascript reader would have
    channel.sourceConnector.properties.script


# Get one channel
c = service.getChannels(channelIds, True)#{"channelId":"3bb08639-7725-4b1b-a2ac-13687101fe9b"}) 

for channel in c.channels: print(channel.name)

# Get all polling channels
c = service.getChannels(pollingOnly=True)

for channel in c.channels:
    print(f"{channel.name} - {channel.description}")

# Get all channels
channels = service.getChannels()

# Look at each channel
for channel in channels.channels:
    print(f"{channel.name} - {channel.description}")

# get all enabled channels
enabledChannels = [channel for channel in channels.channels if channel.exportData.metadata.enabled == 'true']

# get only javascript readers
jReaders = [channel for channel in enabledChannels if type(channel.sourceConnector.properties) == JavaScriptReceiverProperties]

# get certain code templates
codeTemplates = service.getCodeTemplates(['0d42f17b-54a4-40c1-8e7b-b43c3eb1b433', '37139e86-88db-41fa-bf80-8c08456caa10'])

for ct in codeTemplates.codeTemplates:
    print(f"{ct.name} - {ct.id}")

# get all code templates
codeTemplates = service.getCodeTemplates()

for ct in codeTemplates.codeTemplates:
    print(f"{ct.name} - {ct.id}")
    code = ct.properties.find('code').text

print('')