from .mirthDate import MirthDate
from .utilities import getXMLString
from .mirthElement import MirthElement


class DashboardStatus(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.channelId = ''
        self.name = ''
        self.state = 'STARTED'
        self.deployedRevisionDelta = '0'
        self.deployedDate = MirthDate()
        self.lifetimeStatistics = ''
        self.childStatuses = ''
        self.metaDataId = ''
        self.queueEnabled = 'false'
        self.queued = '0'
        self.waitForPrevious = 'false'
        self.statusType = 'SOURCE_CONNECTOR'

        if uXml is not None:
            self.channelId = self.getSafeText('channelId')
            self.name = self.getSafeText('name')
            self.state = self.getSafeText('state')
            self.deployedRevisionDelta = self.getSafeText('deployedRevisionDelta')
            self.deployedDate = MirthDate(self.root.find('deployedDate'))
            self.lifetimeStatistics = self.getSafeText('lifetimeStatistics')
            self.childStatuses = self.getSafeText('childStatuses')
            self.metaDataId = self.getSafeText('metaDataId')
            self.queueEnabled = self.getSafeText('queueEnabled')
            self.queued = self.getSafeText('queued')
            self.waitForPrevious = self.getSafeText('waitForPrevious')
            self.statusType = self.getSafeText('statusType')


    def getXML(self, version="3.12.0"):
        #TODO: Implement
        xml = f'''
            {getXMLString(self.channelId, "channelId")}
        '''
        return xml
    

class DashboardStatusList(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)

        self.dashboardStatuses = []

        for ds in self.root.findall('dashboardStatus'):
            self.dashboardStatuses.append(DashboardStatus(ds))