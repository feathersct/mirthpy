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
        self.destinationConnectors = []        #TODO: convert to class
        self.preprocessingScript = self.root.find('preprocessingScript')
        self.postprocessingScript = self.root.find('postprocessingScript')
        self.deployScript = self.root.find('deployScript')
        self.undeployScript = self.root.find('undeployScript')
        self.properties = self.root.find('properties')

        for c in self.root.findall('./destinationConnectors/connector'):
            self.destinationConnectors.append(Connector(c))