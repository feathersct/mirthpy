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
    

# Connector Models
class Connectors(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

        self.connectors = []

        if uXml is not None:
            for entry in self.root.findall('entry'):
              self.connectors.append(ConnectorEntry(entry))
              

    def getXML(self, version):
        xml = '<map>'
        for connector in self.connectors:
          xml += getXMLString(connector.getXML(version), 'entry')
        xml += '</map>'
        
        return xml

class ConnectorEntry(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)
        
        self.name = ''
        self.connector = ConnectorMetaData()

        if uXml is not None:
            self.name = self.getSafeText('string')
            self.connector = ConnectorMetaData(self.root.find('connectorMetaData'))
              
    def getXML(self, version):
        xml = getXMLString(self.name, "string")
        xml += self.connector.getXML(version)
        
        return xml
    
class ConnectorMetaData(MirthElement):
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
        
        self.templateClassName = ''
        self.serverClassName = ''
        self.sharedClassName = ''
        self.clientClassName = ''
        self.transformers = ''
        self.protocol = ''
        self.type = ''

        if uXml is not None:
            self.path = self.root.attrib.get('path')  # grabbed from the attribute 'path'
            self.name = self.getSafeText('name')
            self.author = self.getSafeText('author')
            self.mirthVersion = self.getSafeText('mirthVersion')
            self.pluginVersion = self.getSafeText('pluginVersion')
            self.url = self.getSafeText('url')
            self.description = self.getSafeText('description')
            self.type = self.getSafeText('type')
            self.templateClassName = self.getSafeText('templateClassName')
            self.serverClassName = self.getSafeText('serverClassName')
            self.sharedClassName = self.getSafeText('sharedClassName')
            self.clientClassName = self.getSafeText('clientClassName')
            self.transformers = self.getSafeText('transformers')
            self.protocol = self.getSafeText('protocol')

            for apiProvider in self.root.findall('apiProvider'):
              self.apiProviders.append(ApiProvider(apiProvider.attrib.get('type'), apiProvider.attrib.get('name')))

            for libary in self.root.findall('library'):
              self.libraries.append(Library(libary.attrib.get('path'), libary.attrib.get('type')))

class Properties(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

        self.properties = []

        if uXml is not None:
            for property in self.root.findall('property'):
                self.properties.append(Property(property))

class Property(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

        self.name = ''
        self.value = ''

        if uXml is not None:
            self.name = self.root.attrib.get('name')
            self.value = self.root.text