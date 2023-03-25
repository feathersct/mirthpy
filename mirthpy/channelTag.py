from .utilities import getXMLString
from .mirthElement import MirthElement


class ChannelTags(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)

        self.channelTags = []

        if uXml is not None:
            for tags in self.root.findall('./channelTag'):
                self.channelTags.append(ChannelTag(tags))

    def getXML(self, version="3.12.0"):
        xml = ""

        for tag in self.channelTags:
            xml += f'''{getXMLString(tag.getXML(version), 'channelTag')}'''

        return xml
    
class ChannelTag(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
    
        self.id = None
        self.name = None
        self.channelId = []
        self.backgroundColor = BackgroundColor()

        if uXml is not None:
            self.id = self.getSafeText('id')
            self.name = self.getSafeText('name')
            self.channelId = []

            for id in self.root.findall('./channelIds/string'):
                self.channelId.append(id.text)

            self.backgroundColor = BackgroundColor(self.root.find('backgroundColor'))
 
    def getXML(self, version="3.12.0"):
        channelIds = "<channelIds>"
        for string in self.channelId:
            channelIds += f"<string>{string}</string>"
        channelIds += "</channelIds>"

        return f'''{getXMLString(self.id, "id")}
                    {getXMLString(self.name, "name")}
                    {channelIds}
                    {getXMLString(self.backgroundColor.getXML(version), "backgroundColor")}'''
    
class BackgroundColor(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)

        self.red = '255'
        self.green = '0'
        self.blue = '0'
        self.alpha = '255'

        if uXml is not None:
            self.red = self.getSafeText('red')
            self.green = self.getSafeText('green')
            self.blue = self.getSafeText('blue')
            self.alpha = self.getSafeText('alpha')
    
    def getXML(self, version="3.12.0"):
        return f'''{getXMLString(self.red, "red")}
                    {getXMLString(self.green, "green")}
                    {getXMLString(self.blue, "blue")}
                    {getXMLString(self.alpha, "alpha")}'''