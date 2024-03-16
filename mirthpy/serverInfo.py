from .channel import Channel
from .channelGroup import ChannelGroup
from .mirthElement import MirthElement
from .utilities import getXMLString

class SystemInfo(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.jvmVersion = self.getSafeText('jvmVersion')
        self.osName = self.getSafeText('osName')
        self.osVersion = self.getSafeText('osVersion')
        self.osArchitecture = self.getSafeText('osArchitecture')
        self.dbName = self.getSafeText('dbName')
        self.dbVersion = self.getSafeText('dbVersion')

class ServerAbout(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.date = ''
        self.channelCount = ''
        self.database = ''
        self.connectors = []
        self.plugins = []
        self.name = ''
        self.version = ''

        if uXml is not None:
            for entry in self.root.findall('entry'):
                name, value = entry
                name = name.text
                if name == 'date':
                    self.date = value.text
                elif name == 'channelCount':
                    self.channelCount = value.text
                elif name == 'database':
                    self.database = value.text
                elif name == 'connectors':
                    for e in value.findall('entry'):
                      self.connectors.append((e.findall('string')[0].text, e.findall('string')[1].text))
                elif name == 'plugins':
                    for e in value.findall('entry'):
                      self.plugins.append((e.findall('string')[0].text, e.findall('string')[1].text))
                elif name == 'name':
                    self.name = value.text
                elif name == 'version':
                    self.version = value.text


class ChannelDependencies(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.channelDependencies = []

        if uXml is not None:
            for entry in self.root.findall('channelDependency'):
                self.channelDependencies.append(ChannelDependency(entry))
    
    def getXML(self, version="3.12.0"):
        xml = '<set>'
        for channelDependency in self.channelDependencies:
            xml += getXMLString(channelDependency.getXML(version), 'channelDependency')
        xml += '</set>'
        return xml
                

class ChannelDependency(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.dependentId = ''
        self.dependencyId = ''

        if uXml is not None:
            self.dependentId = self.getSafeText('dependentId')
            self.dependencyId = self.getSafeText('dependencyId')

    def getXML(self, version="3.12.0"):
        xml = ''
        xml += getXMLString(self.dependentId, 'dependentId')
        xml += getXMLString(self.dependencyId, "dependencyId")
        return xml
    
class ServerConfiguration(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.channelGroups = []
        self.channels = []

        #TODO: Implement full server configuration
        if uXml is not None:
            for channelGroup in self.root.findall('./channelGroups/channelGroup'):
                self.channelGroups.append(ChannelGroup(channelGroup))
            
            for channel in self.root.findall('./channels/channel'):
                self.channels.append(Channel(channel))

        #TODO: implement getXML
    
class DriverInfoList(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.driverInfos = []

        if uXml is not None:
            for driverInfo in self.root.findall('driverInfo'):
                self.driverInfos.append(DriverInfo(driverInfo))

    def getXML(self, version="3.12.0"):
        xml = '<list>'
        for driverInfo in self.driverInfos:
            xml += driverInfo.getXML(version)
        xml += '</list>'
        return xml

class DriverInfo(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.className = ''
        self.name = ''
        self.template = ''
        self.selectLimit = ''
        self.alternativeClassNames = []

        if uXml is not None:
            self.className = self.getSafeText('className')
            self.name = self.getSafeText('name')
            self.template = self.getSafeText('template')
            self.selectLimit = self.getSafeText('selectLimit')
            
            for alt in self.root.findall('./alternativeClassNames/string'):
                self.alternativeClassNames.append(alt.text)

    def getXML(self, version="3.12.0"):
        xml = '<driverInfo>'
        xml += getXMLString(self.className, 'className')
        xml += getXMLString(self.name, 'name')
        xml += getXMLString(self.template, 'template')
        xml += getXMLString(self.selectLimit, 'selectLimit')
        
        xml += '<alternativeClassNames>'
        for alt in self.alternativeClassNames:
            xml += getXMLString(alt, 'string')
        xml += '</alternativeClassNames>'
        
        xml += '</driverInfo>'
        return xml
    
class EncryptionSettings(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.encryptExport = ''
        self.encryptProperties = ''
        self.encryptionAlgorithm = ''
        self.encryptionKeyLength = ''
        self.digestAlgorithm = ''
        self.securityProvider = ''
        self.secretKey = ''

        if uXml is not None:
            self.encryptExport = self.getSafeText('encryptExport')
            self.encryptProperties = self.getSafeText('encryptProperties')
            self.encryptionAlgorithm = self.getSafeText('encryptionAlgorithm')
            self.encryptionKeyLength = self.getSafeText('encryptionKeyLength')
            self.digestAlgorithm = self.getSafeText('digestAlgorithm')
            self.securityProvider = self.getSafeText('securityProvider')
            self.secretKey = self.getSafeText('secretKey')

    def getXML(self, version="3.12.0"):
        xml = '<com.mirth.connect.model.EncryptionSettings>'
        xml += getXMLString(self.encryptExport, 'encryptExport')
        xml += getXMLString(self.encryptProperties, 'encryptProperties')
        xml += getXMLString(self.encryptionAlgorithm, 'encryptionAlgorithm')
        xml += getXMLString(self.encryptionKeyLength, 'encryptionKeyLength')
        xml += getXMLString(self.digestAlgorithm, 'digestAlgorithm')
        xml += getXMLString(self.securityProvider, 'securityProvider')
        xml += getXMLString(self.secretKey, 'secretKey')
        xml += '</com.mirth.connect.model.EncryptionSettings>'

        return xml

class LicenseInfo(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.activated = ''
        self.online = ''
        self.expirationDate = ''
        self.gracePeriod = ''
        self.extensions = []

        if uXml is not None:
            self.activated = self.getSafeText('activated')
            self.online = self.getSafeText('online')
            self.expirationDate = self.getSafeText('expirationDate')
            self.gracePeriod = self.getSafeText('gracePeriod')
            
            for extension in self.root.findall('./extensions/string'):
                self.extensions.append(extension.text)

    def getXML(self, version="3.12.0"):
        xml = '<com.mirth.connect.model.LicenseInfo>'
        xml += getXMLString(self.activated, 'activated')
        xml += getXMLString(self.online, 'online')
        xml += getXMLString(self.expirationDate, 'expirationDate')
        xml += getXMLString(self.gracePeriod, 'gracePeriod')
        
        xml += '<extensions>'
        for extension in self.extensions:
            xml += getXMLString(extension, 'string')
        xml += '</extensions>'

        xml += '</com.mirth.connect.model.LicenseInfo>'

        return xml
