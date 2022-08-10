from .mirthElement import MirthElement


class Event(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.id = self.getSafeText('id')
        self.dateTime = self.getSafeText('dateTime')
        self.eventTime = self.getSafeText('./eventTime/time')
        self.level = self.getSafeText('level')
        self.name = self.getSafeText('name')
        self.outcome = self.getSafeText('outcome')
        self.userId = self.getSafeText('userId')
        self.ipAddress = self.getSafeText('ipAddress') #self.root.find('ipAddress').text if self.root.find('ipAddress') != None else None
        self.serverId = self.getSafeText('serverId')
        # self.root = uXml

        self.attributes = []
        for a in self.root.findall('./attributes/entry'):
            self.attributes.append((a.findall('string')[0].text, a.findall('string')[1].text))