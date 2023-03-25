from typing import Type
from .mirthDate import MirthDate
from .mirthElement import MirthElement


class CodeTemplate(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.id = self.getSafeText('id') 
        self.name = self.getSafeText('name')
        self.revision = self.getSafeText('revision')

        if self.root.find('properties') is not None:
            prop = CodeTemplate_Mapping.codeTemplates(self.root.find('properties').attrib['class'])
        
            self.properties = prop(self.root.find('properties'))

        self.lastModified = MirthDate(self.root.find('lastModified'))
        self.contextSet = self.root.find('contextSet')

class BasicCodeTemplateProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.type = self.getSafeText('type')
        self.code = self.getSafeText('code')

class ContextSet(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.delegate = Delegate(self.root.find('delegate'))

class Delegate(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.contextType = []
        
        for context in self.root.findall('contextType'):
            self.contextType.append(context.text)

class CodeTemplate_Mapping:
    def codeTemplates(c: str) -> Type:
        if c == "com.mirth.connect.model.codetemplates.BasicCodeTemplateProperties":
            return BasicCodeTemplateProperties