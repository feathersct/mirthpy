from .mirthElement import MirthElement


class CodeTemplate(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)
        self.id = self.root.find('id').text
        self.name = self.root.find('name').text
        self.revision = self.root.find('revision').text
        self.properties = self.root.find('properties')
        self.lastModified = self.root.find('./lastModified/time').text
        self.contextSet = self.root.find('contextSet')
        # self.root = uXml