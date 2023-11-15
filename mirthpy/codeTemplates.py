from .utilities import escape, getXMLString
from .linkedHashMap import Entry
from .mirthDate import MirthDate
from .codeTemplate import CodeTemplate
from .mirthElement import MirthElement

class CodeTemplates(MirthElement):
    def __init__(self, listXML=None):
        MirthElement.__init__(self, listXML)
        codeTemplates = self.root
        self.codeTemplates = []

        if listXML is not None:
            for ct in codeTemplates.findall('./codeTemplate'):
                self.codeTemplates.append(CodeTemplate(ct))
    
    def getXML(self, version="3.12.0"):
        xml = "<codeTemplates>"
        for ct in self.codeTemplates:
            xml += ct.getXML(version)
        xml += "</codeTemplates>"
        return xml

class CodeTemplateLibrary(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

        self.id = ''
        self.name = ''
        self.revision = 1
        self.lastModified = MirthDate()
        self.description = ''
        self.includeNewChannels = 'false'
        self.enabledChannelIds = Entry()
        self.disabledChannelIds = Entry()
        self.codeTemplates = CodeTemplates()

        if uXml is not None:
            self.id = self.getSafeText('id')
            self.name = self.getSafeText('name')
            self.revision = self.getSafeText('revision')
            self.lastModified = MirthDate(self.root.find('lastModified'))
            self.description = self.getSafeText('description')
            self.includeNewChannels = self.getSafeText('includeNewChannels')
            self.enabledChannelIds = Entry(self.root.find('enabledChannelIds'))
            self.disabledChannelIds = Entry(self.root.find('disabledChannelIds'))
            self.codeTemplates = CodeTemplates(self.root.find('codeTemplates'))

    def getXML(self, version="3.12.0"):
        xml = '<codeTemplateLibrary version="{}">'.format(version)
        xml += getXMLString(self.id, 'id')
        xml += getXMLString(self.name, 'name')
        xml += getXMLString(self.revision, 'revision')
        xml += getXMLString(self.lastModified.getXML(version), 'lastModified')
        xml += getXMLString(escape(self.description), 'description')
        xml += getXMLString(self.includeNewChannels, 'includeNewChannels')
        xml += getXMLString(self.enabledChannelIds.getXML(version), 'enabledChannelIds')
        xml += getXMLString(self.disabledChannelIds.getXML(version), 'disabledChannelIds')
        xml += self.codeTemplates.getXML(version)
        xml += '</codeTemplateLibrary>'
        return xml
    
class CodeTemplateLibraryList(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.codeTemplateLibaries = []

        if uXml is not None:
            self.codeTemplateLibaries = []
            for ct in self.root.findall('./codeTemplateLibrary'):
                self.codeTemplateLibaries.append(CodeTemplateLibrary(ct))

    def getXML(self, version="3.12.0"):
        xml = '<list>'
        for ctl in self.codeTemplateLibaries:
            xml += ctl.getXML(version)
        xml += '</list>'
        return xml