from .connectors import Connector
from .mirthElement import MirthElement


class Channel(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.id = self.root.find('id').text
        self.nextMetaDataId = self.root.find('nextMetaDataId').text
        self.name = self.root.find('name').text
        self.description = self.root.find('description').text
        self.revision = self.root.find('revision').text

        self.sourceConnector = Connector(self.root.find('sourceConnector'))
        self.destinationConnectors = []        
        self.preprocessingScript = self.root.find('preprocessingScript')
        self.postprocessingScript = self.root.find('postprocessingScript')
        self.deployScript = self.root.find('deployScript')
        self.undeployScript = self.root.find('undeployScript')
        self.properties = self.root.find('properties')

        for c in self.root.findall('./destinationConnectors/connector'):
            self.destinationConnectors.append(Connector(c))

        self.exportData = ExportData(self.root.find('exportData'))

class ExportData(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.metadata = MetaData(self.root.find('metadata'))
        self.dependentIds = self.root.find('dependentIds')
        self.dependencyIds = self.root.find('dependencyIds')
        self.channelTags = self.root.find('channelTags')

class MetaData(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.enabled = self.getSafeText('enabled')
        self.lastModified = self.root.find('lastModified')
        self.pruningSettings = self.root.find('pruningSettings')
