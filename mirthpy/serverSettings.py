from .channelProperties import MetaDataColumn
from .channelTag import BackgroundColor
from .mirthElement import MirthElement

class ServerSettings(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)


        self.environmentName = ''
        self.serverName = ''
        self.clearGlobalMap = 'true'
        self.queueBufferSize = '1000'
        self.defaultMetaDataColumns = []
        self.defaultAdministratorBackgroundColor = BackgroundColor(self.root.find('defaultAdministratorBackgroundColor'))
        self.smtpHost = ''
        self.smtpPort = ''
        self.smtpTimeout = '5000'
        self.smtpFrom = ''
        self.smtpSecure = 'none'
        self.smtpAuth = 'false'
        self.smtpUsername = ''
        self.smtpPassword = ''

        if uXml is not None:
            self.environmentName = self.getSafeText('environmentName')
            self.serverName = self.getSafeText('serverName')
            self.clearGlobalMap = self.getSafeText('clearGlobalMap')
            self.queueBufferSize = self.getSafeText('queueBufferSize')
            self.defaultAdministratorBackgroundColor = BackgroundColor(self.root.find('defaultAdministratorBackgroundColor'))
            self.smtpHost = self.getSafeText('smtpHost')
            self.smtpPort = self.getSafeText('smtpPort')
            self.smtpTimeout = self.getSafeText('smtpTimeout')
            self.smtpFrom = self.getSafeText('smtpFrom')
            self.smtpSecure = self.getSafeText('smtpSecure')
            self.smtpAuth = self.getSafeText('smtpAuth')
            self.smtpUsername = self.getSafeText('smtpUsername')
            self.smtpPassword = self.getSafeText('smtpPassword')

            for m in self.root.findall('./defaultMetaDataColumns/metaDataColumn'):
                self.defaultMetaDataColumns.append(MetaDataColumn(m))