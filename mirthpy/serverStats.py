from .mirthDate import MirthDate
from .mirthElement import MirthElement


class SystemStats(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.timestamp = MirthDate(self.root.find('timestamp'))
        self.cpuUsagePct = self.getSafeText('cpuUsagePct')
        self.allocatedMemoryBytes = int(self.getSafeText('allocatedMemoryBytes'))
        self.freeMemoryBytes = int(self.getSafeText('freeMemoryBytes'))
        self.maxMemoryBytes = int(self.getSafeText('maxMemoryBytes'))
        self.diskFreeBytes = int(self.getSafeText('diskFreeBytes'))
        self.diskTotalBytes = int(self.getSafeText('diskTotalBytes'))
