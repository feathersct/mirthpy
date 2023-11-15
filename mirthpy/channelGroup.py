from .mirthDate import MirthDate
from .mirthElement import MirthElement
from .utilities import escape, getXMLString


class ChannelGroups(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

        self.channelGroups = []

        if uXml is not None:
            for c in self.root.findall('channelGroup'):
                self.channelGroups.append(ChannelGroup(c))

    def getXML(self, version="3.12.0"):
        xml = "<list>"
        for channelGroup in self.channelGroups:
            xml += channelGroup.getXML(version)
        xml += "</list>"
        return xml

class ChannelGroup(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

        self.id = ''
        self.name = ''
        self.revision = '1'
        self.lastModified = MirthDate()
        self.description = ''

        self.channels = []

        if uXml is not None:
            self.id = self.getSafeText('id')
            self.name = self.getSafeText('name')
            self.revision = self.getSafeText('revision')
            self.lastModified = MirthDate(self.root.get('lastModified'))
            self.description = self.getSafeText('description')

            self.channels = []
            for c in self.root.find('channels').findall('channel'):
                self.channels.append(ChannelGroupChannel(c))

    def getXML(self, version="3.12.0"):
        xml = "<channelGroup version={}>".format(version)

        xml += getXMLString('id', self.id)
        xml += getXMLString('name', self.name)
        xml += getXMLString('revision', self.revision)
        xml += self.lastModified.getXML(version)
        xml += getXMLString('description', self.description)

        xml += "<channels>"
        for channel in self.channels:
            xml += channel.getXML(version)
        xml += "</channels>"

        xml += "</channelGroup>"
        return xml

class ChannelGroupChannel(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

        self.id = ''
        self.revision = '1'

        if uXml is not None:
            self.id = self.getSafeText('id')
            self.revision = self.getSafeText('revision')
    
    def getXML(self, version="3.12.0"):
        xml = "<channel version={}>".format(version)
        xml += getXMLString('id', self.id)
        xml += getXMLString('revision', self.revision)
        xml += "</channel>"
        return xml

