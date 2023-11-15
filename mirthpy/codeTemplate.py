from typing import Type

from .utilities import escape, getXMLString
from .mirthDate import MirthDate
from .mirthElement import MirthElement


class CodeTemplate(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)

        self.id = ''
        self.name = ''
        self.revision = 0
        self.lastModified = MirthDate()
        self.contextSet = ContextSet()
        self.properties = BasicCodeTemplateProperties()        

        if uXml is not None:
            self.id = self.getSafeText('id') 
            self.name = self.getSafeText('name')
            self.revision = self.getSafeText('revision')

            if self.root.find('properties') is not None:
                prop = CodeTemplate_Mapping.codeTemplates(self.root.find('properties').attrib['class'])
            
                self.properties = prop(self.root.find('properties'))

            self.lastModified = MirthDate(self.root.find('lastModified'))
            self.contextSet = ContextSet(self.root.find('contextSet'))
    
    def getXML(self, version="3.12.0"):
        xml = '<codeTemplate version="{}">'.format(version)
        xml += getXMLString(self.id, 'id')
        xml += getXMLString(self.name, 'name')
        xml += getXMLString(self.revision, 'revision')
        xml += getXMLString(self.lastModified.getXML(version), 'lastModified')
        xml += self.contextSet.getXML(version)
        xml += self.properties.getXML(version)
        xml += "</codeTemplate>"
        return xml

class BasicCodeTemplateProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.className = 'com.mirth.connect.model.codetemplates.BasicCodeTemplateProperties'

        self.type = 'FUNCTION'
        self.code = ''

        if uXml is not None:
            self.type = self.getSafeText('type')
            self.code = self.getSafeText('code')
    
    def getXML(self, version="3.12.0"):
        xml = '<properties class="{}">'.format(self.className)
        xml += getXMLString(self.type, 'type')
        xml += getXMLString(escape(self.code), 'code')
        xml += '</properties>'
        return xml

class ContextSet(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)

        self.delegate = Delegate()

        if uXml is not None:
            self.delegate = Delegate(self.root.find('delegate'))
    
    def getXML(self, version="3.12.0"):
        xml = "<contextSet>"
        xml += self.delegate.getXML(version)
        xml += "</contextSet>"
        return xml

class Delegate(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.contextType = []
        
        if uXml is not None:
            for context in self.root.findall('contextType'):
                self.contextType.append(context.text)
    
    def getXML(self, version="3.12.0"):
        xml = "<delegate>"
        for ct in self.contextType:
            xml += getXMLString(ct, "contextType")
        xml += "</delegate>"
        return xml

class CodeTemplate_Mapping:
    def codeTemplates(c):
        if c == "com.mirth.connect.model.codetemplates.BasicCodeTemplateProperties":
            return BasicCodeTemplateProperties