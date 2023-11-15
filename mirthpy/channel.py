from .channelProperties import ChannelProperties
from .utilities import escape, getXMLString
from .mirthDate import MirthDate
from .connectors import DestinationConnectorElement, SourceConnector
from .mirthElement import MirthElement


class Channel(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)

        self.id = ''
        self.nextMetaDataId = '2'
        self.name = ''
        self.description = ''
        self.revision = '1'

        self.sourceConnector = SourceConnector() 
        self.destinationConnectors = [DestinationConnectorElement()]     
        self.preprocessingScript = '// Modify the message variable below to pre process data\nreturn message;'
        self.postprocessingScript = '// This script executes once after a message has been processed\n// Responses returned from here will be stored as &quot;Postprocessor&quot; in the response map\nreturn;'
        self.deployScript = '// This script executes once when the channel is deployed\n// You only have access to the globalMap and globalChannelMap here to persist data\nreturn;'
        self.undeployScript = '// This script executes once when the channel is undeployed\n// You only have access to the globalMap and globalChannelMap here to persist data\nreturn;'
        self.properties = ChannelProperties()
        self.exportData = ExportData()
    
        if uXml is not None:
            self.id = self.getSafeText('id')
            self.nextMetaDataId = self.getSafeText('nextMetaDataId')
            self.name = self.getSafeText('name')
            self.description = self.getSafeText('description')
            self.revision = self.getSafeText('revision')

            self.sourceConnector = SourceConnector(self.root.find('sourceConnector'))
            self.destinationConnectors = []        
            self.preprocessingScript = self.getSafeText('preprocessingScript')
            self.postprocessingScript = self.getSafeText('postprocessingScript')
            self.deployScript = self.getSafeText('deployScript')
            self.undeployScript = self.getSafeText('undeployScript')
            self.properties = ChannelProperties(self.root.find('properties'))

            for c in self.root.findall('./destinationConnectors/connector'):
                self.destinationConnectors.append(DestinationConnectorElement(c))

            self.exportData = ExportData(self.root.find('exportData'))

    def getXML(self, version="3.12.0"):
        destinationXML = ""
        i = 0
        for destination in self.destinationConnectors:
            i = i + 1
            if destination.metaDataId == '':
                destination.metaDataId = str(i)
            destinationXML += '''<connector version="3.12.0">{}</connector>'''.format(destination.getXML(version))

        xml = getXMLString(self.id, "id")
        xml += getXMLString(self.nextMetaDataId, "nextMetaDataId")
        xml += getXMLString(self.name, "name")
        xml += getXMLString(escape(self.description), "description")
        xml += getXMLString(self.revision, "revision")
        xml += '<sourceConnector version="{}">'.format(version)
        xml += self.sourceConnector.getXML(version)
        xml += '</sourceConnector>'
        xml += getXMLString(destinationXML, "destinationConnectors")
        xml += getXMLString(escape(self.preprocessingScript), "preprocessingScript")
        xml += getXMLString(escape(self.postprocessingScript), "postprocessingScript")
        xml += getXMLString(escape(self.deployScript), "deployScript")
        xml += getXMLString(escape(self.undeployScript), "undeployScript")
        xml += '<properties version="{}">'.format(version)
        xml += self.properties.getXML()
        xml += '</properties>'
        xml += getXMLString(self.exportData.getXML(version), "exportData")
        return xml

class ExportData(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        
        self.metadata = MetaData()
        self.dependentIds = ''
        self.dependencyIds = ''
        self.channelTags = ''

        if uXml is not None:
            self.metadata = MetaData(self.root.find('metadata'))
            self.dependentIds = self.root.find('dependentIds')
            self.dependencyIds = self.root.find('dependencyIds')
            self.channelTags = self.root.find('channelTags')

    def getXML(self, version="3.12.0"):
        xml = getXMLString(self.metadata.getXML(version), "metadata")
        xml += getXMLString(self.dependentIds, "dependentIds", includeIfEmpty=False)
        xml += getXMLString(self.dependencyIds, "dependencyIds", includeIfEmpty=False)
        xml += getXMLString(self.channelTags, "channelTags", includeIfEmpty=False)

        return xml

class MetaData(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.enabled = 'false'
        self.lastModified = MirthDate()
        self.pruningSettings = PruneSettings()

        if uXml is not None:
            self.enabled = self.getSafeText('enabled')
            self.lastModified = MirthDate(self.root.find('lastModified'))
            self.pruningSettings = PruneSettings(self.root.find('pruningSettings'))

    def getXML(self, version="3.12.0"):
        xml = ''
        xml += getXMLString(self.enabled, "enabled")
        xml += getXMLString(self.lastModified.getXML(version), "lastModified")
        xml += getXMLString(self.pruningSettings.getXML(version), "pruningSettings")

        return xml

class PruneSettings(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.archiveEnabled = 'true'
        self.pruneErroredMessages = 'false'
        self.pruneMetaDataDays = ''
        self.pruneContentDays = ''

        if uXml is not None:
            self.archiveEnabled = self.getSafeText('archiveEnabled')
            self.pruneErroredMessages = self.getSafeText('pruneErroredMessages')
            self.pruneMetaDataDays = self.getSafeText('pruneMetaDataDays')
            self.pruneContentDays = self.getSafeText('pruneContentDays')

    def getXML(self, version="3.12.0"):
        xml = ''
        xml += getXMLString(self.pruneMetaDataDays, "pruneMetaDataDays", includeIfEmpty=False)
        xml += getXMLString(self.pruneContentDays, "pruneContentDays", includeIfEmpty=False)
        xml += getXMLString(self.archiveEnabled, "archiveEnabled")
        xml += getXMLString(self.pruneErroredMessages, "pruneErroredMessages")

        return xml
