from .mirthElement import MirthElement


class ConfigurationMaps(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.entry = []

        for c in self.root.findall('./entry'):
            self.entry.append(ConfigurationMap(c))

class ConfigurationMap(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.string = self.getSafeText('string')
        self.configurationProperty = ConfigurationProperty(self.root.find('com.mirth.connect.util.ConfigurationProperty'))

class ConfigurationProperty(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.value = self.getSafeText('value')
        self.comment = self.getSafeText('comment')
