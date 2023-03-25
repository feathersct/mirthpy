from .mirthDate import MirthDate
from .mirthElement import MirthElement


class Snapshot(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.snapshotId = self.getSafeText('snapshotId')
        self.itemId = self.getSafeText('itemId')
        self.revision = self.getSafeText('revision')
        self.userId = self.getSafeText('userId')
        self.dateCreated = MirthDate(self.root.find('./dateCreated'))
        self.text = self.getSafeText('text')

class Snapshots(MirthElement):
    def __init__(self, listXML):
        MirthElement.__init__(self, listXML)

        self.snapshots = []

        for s in self.root.findall('./com.mirth.connect.plugins.history.model.Snapshot'):
            self.snapshots.append(Snapshot(s))