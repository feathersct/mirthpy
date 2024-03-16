from .utilities import escape, getXMLString
from .mirthDate import MirthDate
from .mirthElement import MirthElement


class GlobalScripts(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        
        self.scripts = []

        if uXml is not None:
            for e in self.root.findall('./entry'):
                self.scripts.append(GlobalScript(e))
    
    def getXML(self, version = "3.12.0"):
        xml = ""
        for e in self.scripts:
            xml += getXMLString(e.getXML(version), "entry")

        return xml
    
class GlobalScript(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        
        self.type = ''
        self.script = ''

        if uXml is not None:
            strings = self.root.findall('string')
            self.type = strings[0].text
            self.script = strings[1].text
                
    
    def getXML(self, version = "3.12.0"):
        xml = ""
        xml += getXMLString(self.type, 'string')
        xml += getXMLString(escape(self.script), 'string')

        return xml