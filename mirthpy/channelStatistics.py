from .utilities import getXMLString
from .mirthElement import MirthElement


class ChannelStatistics(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.serverId = ''
        self.channelId = ''
        self.received = '0'
        self.sent = '0'
        self.error = '0'
        self.filtered = '0'
        self.queued = '0'

        if uXml is not None:
            self.serverId = self.getSafeText('serverId')
            self.channelId = self.getSafeText('channelId')
            self.received = self.getSafeText('received')
            self.sent = self.getSafeText('sent')
            self.error = self.getSafeText('error')
            self.filtered = self.getSafeText('filtered')
            self.queued = self.getSafeText('queued')

    def getXML(self, version="3.12.0"):
        xml = f'''
            {getXMLString(self.serverId, "serverId")}
            {getXMLString(self.channelId, "channelId")}
            {getXMLString(self.received, "received")}
            {getXMLString(self.sent, "sent")}
            {getXMLString(self.error, "error")}            
            {getXMLString(self.filtered, "filtered")}
            {getXMLString(self.queued, "queued")}
        '''
        return xml
    
class ChannelStatisticsList(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)

        self.channelStatistics = []

        if uXml is not None:
            for cs in self.root.findall('channelStatistics'):
                self.channelStatistics.append(ChannelStatistics(cs))

    def getXML(self, version="3.12.0"):
        csXML = ''
        for cs in self.channelStatistics:
            csXML += getXMLString(cs.getXML(version), "channelStatistics")

        xml = f'''<list>{csXML}</list>'''
        return xml