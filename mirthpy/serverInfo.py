from .mirthElement import MirthElement

class SystemInfo(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.jvmVersion = self.getSafeText('jvmVersion')
        self.osName = self.getSafeText('osName')
        self.osVersion = self.getSafeText('osVersion')
        self.osArchitecture = self.getSafeText('osArchitecture')
        self.dbName = self.getSafeText('dbName')
        self.dbVersion = self.getSafeText('dbVersion')
