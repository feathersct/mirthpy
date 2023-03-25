from .utilities import getXMLString
from .mirthDate import MirthDate
from .mirthElement import MirthElement


class LinkedHashMap(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        
        self.entry = []

        if uXml is not None:
            for e in self.root.findall('./entry'):
                self.entry.append(Entry(e))
    
    def getXML(self, version = "3.12.0"):
        xml = ""
        for e in self.entry:
            xml += f'{getXMLString(e.getXML(version), "entry")}'

        return xml

class Entry(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        
        self.string = []
        self.list = []
        
        if uXml is not None:
            strings = self.root.findall('./string')
            for e in strings:
                self.string.append(e.text)

            for l in self.root.findall('./list/string'):
                self.list.append(l.text)
    
    def getXML(self, version = "3.12.0"):
        xml = ""
        for s in self.string:
            xml += f'{getXMLString(s, "string")}'

        if len(self.list) > 0:
            xml += '<list>'
            for l in self.list:
                xml += f'{getXMLString(l, "string")}'

            xml += '</list>'

        return xml
        
class LinkedHashMapMessage(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)
        
        self.entry = []

        for e in self.root.findall('./entry'):
            self.entry.append(EntryMessage(e))
            
class EntryMessage(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)
        self.int = self.getSafeText('int')
        self.connectorMessage = ConnectorMessage(self.root.find('connectorMessage'))
        
 
class ConnectorMessage(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)       
      
        self.messageId = self.getSafeText('messageId')
        self.metaDataId = self.getSafeText('metaDataId')
        self.channelId = self.getSafeText('channelId')
        self.channelName = self.getSafeText('channelName')
        self.connectorName = self.getSafeText('connectorName')
        self.serverId = self.getSafeText('serverId')
        self.receivedDate = MirthDate(self.root.find('receivedDate'))
        self.status = self.getSafeText('status')
        self.raw = self.root.find('raw')

        # self.encoded = self.root.find('encoded')
        # self.sent = self.root.find('sent')
        # self.response = self.root.find('response')
        # self.sourceMapContent = self.root.find('sourceMapContent')
        # self.connectorMapContent = self.root.find('connectorMapContent')
        # self.channelMapContent = self.root.find('channelMapContent')
        # self.responseMapContent = self.root.find('responseMapContent')
        # self.metaDataMap = self.root.find('metaDataMap')
        # self.processingErrorContent = self.root.find('processingErrorContent')
        # self.postProcessorErrorContent = self.root.find('postProcessorErrorContent')
        # self.responseErrorContent = self.root.find('responseErrorContent')
        

        self.encrypted = self.getSafeText('encrypted')
        self.errorCode = self.getSafeText('errorCode')
        self.sendAttempts = self.getSafeText('sendAttempts')
        
        if self.root.find('sendDate') is not None:
            self.sendDate = MirthDate(self.root.find('sendDate'))
        
        if self.root.find('responseDate') is not None:
            self.responseDate = MirthDate(self.root.find('responseDate'))

        self.chainId = self.getSafeText('chainId')
        self.orderId = self.getSafeText('orderId')