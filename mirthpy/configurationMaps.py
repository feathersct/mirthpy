from .utilities import escape, getXMLString
from .mirthElement import MirthElement


class ConfigurationMaps(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)

        self.entry = []

        if uXml is not None:
            for c in self.root.findall('./entry'):
                self.entry.append(ConfigurationMap(c))

    def getXML(self, version="3.12.0"):
        xml = ""
        xml += "<map>"
        for entry in self.entry:
            xml += getXMLString(entry.getXML(version), 'entry')
        xml += "</map>"
        return xml

class ConfigurationMap(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.className = 'com.mirth.connect.util.ConfigurationProperty'

        self.string = ''
        self.configurationProperty = ConfigurationProperty()

        if uXml is not None:
            self.string = self.getSafeText('string')
            self.configurationProperty = ConfigurationProperty(self.root.find(self.className))
    
    def getXML(self, version="3.12.0"):
        xml = ""
        xml += getXMLString(self.string, 'string')
        xml += getXMLString(self.configurationProperty.getXML(version), self.className)
        return xml

class ConfigurationProperty(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.value = ''
        self.comment = ''

        if uXml is not None:
            self.value = self.getSafeText('value')
            self.comment = self.getSafeText('comment')
    
    def getXML(self, version="3.12.0"):
        xml = ""
        xml += getXMLString(escape(self.value), 'value')
        xml += getXMLString(escape(self.comment), 'comment')
        return xml
