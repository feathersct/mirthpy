from .utilities import getXMLString
from .mirthElement import MirthElement

class Plugins(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

        self.plugins = []

        if uXml is not None:
            for entry in self.root.findall('entry'):
              self.plugins.append(PluginEntry(entry))
              

    def getXML(self, version):
        xml = '<map>'
        for plugin in self.plugins:
          xml += getXMLString(plugin.getXML(version), 'entry')
        xml += '</map>'
        
        return xml

class PluginEntry(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)
        
        self.name = ''
        self.plugin = PluginMetaData()

        if uXml is not None:
            self.name = self.getSafeText('string')
            self.plugin = PluginMetaData(self.root.find('pluginMetaData'))
              
    def getXML(self, version):
        xml = getXMLString(self.name, "string")
        xml += self.plugin.getXML(version)
        
        return xml

class PluginMetaData(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

        self.path = ''  # grabbed from the attribute 'path'
        self.name = ''
        self.author = ''
        self.mirthVersion = ''
        self.pluginVersion = ''
        self.url = ''
        self.description = ''
        self.apiProviders = []
        self.libraries = []
        self.serverClasses = []
        self.clientClasses = []

        if uXml is not None:
            self.path = self.root.attrib.get('path')  # grabbed from the attribute 'path'
            self.name = self.getSafeText('name')
            self.author = self.getSafeText('author')
            self.mirthVersion = self.getSafeText('mirthVersion')
            self.pluginVersion = self.getSafeText('pluginVersion')
            self.url = self.getSafeText('url')
            self.description = self.getSafeText('description')

            for apiProvider in self.root.findall('apiProvider'):
              self.apiProviders.append(ApiProvider(apiProvider.attrib.get('type'), apiProvider.attrib.get('name')))

            for libary in self.root.findall('library'):
              self.libraries.append(Library(libary.attrib.get('path'), libary.attrib.get('type')))

            if self.root.find('serverClasses'):
                for pluginClass in self.root.find('serverClasses').findall('pluginClass'):
                    self.serverClasses.append(PluginClass(pluginClass))
            
            if self.root.find('clientClasses'):
                for pluginClass in self.root.find('clientClasses').findall('pluginClass'):
                    self.clientClasses.append(PluginClass(pluginClass))

    def getXML(self, version):
        xml = '<pluginMetaData path="{}">'.format(self.path)
        xml += getXMLString(self.name, 'name')
        xml += getXMLString(self.name, 'author')
        xml += getXMLString(self.name, 'mirthVersion')
        xml += getXMLString(self.name, 'pluginVersion')
        xml += getXMLString(self.name, 'url')
        xml += getXMLString(self.name, 'description')

        for apiProvider in self.apiProviders:
            xml += '<apiProvider type="{}" name="{}"/>'.format(apiProvider.type, apiProvider.name)
        
        for library in self.libraries:
            xml += '<library path="{}" type="{}"/>'.format(library.path, library.type)

        if len(self.serverClasses) > 0:
            xml += '<serverClasses>'
            for pluginClass in self.serverClasses:
                xml += pluginClass.getXML(version)
            xml += '</serverClasses>'

        if len(self.clientClasses) > 0:
            xml += '<clientClasses>'
            for pluginClass in self.clientClasses:
                xml += pluginClass.getXML(version)
            xml += '</clientClasses>'

        xml += '</pluginMetaData>'
        
        return xml

class Library:
  def __init__(self, path, type):
    self.path = path
    self.type = type

class ApiProvider:
  def __init__(self, type, name):
    self.type = type
    self.name = name

class PluginClass(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

        self.name = ''
        self.weight = ''

        if uXml is not None:
            self.name = self.getSafeText('name')
            self.weight = self.getSafeText('weight')
              
    def getXML(self, version):
        xml = '<pluginClass>'
        xml += getXMLString(self.name, 'name')
        xml += getXMLString(self.weight, 'weight')
        xml += '</pluginClass>'
        
        return xml