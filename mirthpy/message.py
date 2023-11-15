from .mirthDate import MirthDate
from .linkedHashMap import LinkedHashMap, LinkedHashMapMessage
from .mirthElement import MirthElement

class Messages(MirthElement):
    def __init__(self, listXML):
        MirthElement.__init__(self, listXML)

        messages = self.root
        self.messages = []

        for c in messages.findall('./message'):
            self.messages.append(Message(c))

class Message(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.serverId = self.getSafeText('serverId')
        self.channelId = self.getSafeText('channelId')
        self.receivedDate = MirthDate(self.root.find('receivedDate'))
        self.processed = self.getSafeText('processed')
        self.connectorMessages = LinkedHashMapMessage(self.root.find('connectorMessages'))
        self.messageId = self.getSafeText('messageId')
        # self.int = self.getSafeText('int')
        # self.status = self.getSafeText('status')
        # self.sourceMapContent = self.getSafeText('sourceMapContent')
        # 
        # self.connectorMapContent = self.getSafeText('connectorMapContent')
        # self.channelMapContent = self.getSafeText('channelMapContent')
        # self.responseMapContent = self.getSafeText('responseMapContent')
        # self.metaDataMap = self.getSafeText('metaDataMap')
        # self.processingErrorContent = self.getSafeText('processingErrorContent')
        # self.postProcessorErrorContent = self.getSafeText('postProcessorErrorContent')
        # self.responseErrorContent = self.getSafeText('responseErrorContent')
        # 