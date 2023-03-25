import re
from xml.etree import ElementTree
import xml.etree.ElementTree as ET
from .utilities import escape
from .defaults import Defaults 


class MirthElement:
    def __init__(self, uXml):
        if not isinstance(uXml, ET.Element):
            if uXml is None:
                try:
                    self.root = ET.fromstring(self.getDefaultXML())
                except:
                    self.root = None
            else:
                self.root = ET.fromstring(re.sub('&.+[0-9]+;', '', uXml.decode('utf-8')))
        else:
            self.root = uXml

        try:
            self.version = self.root.attrib['version'] 
        except:
            i = 0

        try:
            self.className = self.root.attrib['class'] 
        except:
            i = 0

    def xmlString(self):
        return ElementTree.tostring(self.root, encoding='utf8', method='xml').decode()

    def getSafeText(self, prop: str) -> str:
        return self.root.find(prop).text if self.root.find(prop) != None else None
    
    def getDefaultXML(self):
        childClass = self.__class__.__name__
        
        return Defaults.getDefault(childClass)

    def getXML(self, version = "3.12.0") -> str:
        ret = ""
        parentTag = f"<{self.root.tag}"

        if 'className' in vars(self):
            parentTag += f' class="{self.className}"' 
        if 'version' in vars(self):
            parentTag += f' version="{self.version}"'

        parentTag += ">"
        ret += parentTag

        variables = vars(self)
        keys = [key for key, value in variables.items() if key not in ['root', 'className', 'version']]

        
        for k in keys:
            if type(variables[k]) in [str]:
                ret += f'<{k}>{escape(variables[k])}</{k}>'
            elif type(variables[k]) in [type(None)]:
                ret += f'<{k}></{k}>'
            elif type(variables[k]) == ElementTree.Element:
                ret += ElementTree.tostring(variables[k], method='xml').decode().replace('\n', '')
            elif issubclass(type(variables[k]), MirthElement):
                ret += variables[k].getXML()
            elif type(variables[k]) == tuple:
                for t in variables[k]:
                    ret += f'<string>{escape(t)}</string>'
            elif type(variables[k]) == list:
                if len(variables[k]) == 0:
                    ret += f'<{k}/>'
                else:
                    if k not in ['entry', 'string']:
                        ret += f'<{k}>'
                    for x in variables[k]:
                        if type(x) in [str]:
                            ret += f'<string>{escape(x)}</string>'
                        elif type(x) in [bool]:
                            ret += f'<boolean>{str(x).lower()}</boolean>'
                        elif type(x) in [type(None)]:
                            f = ''
                            #print(f'')
                        elif type(variables[k]) == ElementTree.Element:
                            ret += ElementTree.tostring(x, method='xml').decode().replace('\n', '')
                        elif issubclass(type(x), MirthElement):
                            ret += x.getXML()
                    if k not in ['entry', 'string']:
                        ret += f'</{k}>'
        ret += f"</{self.root.tag}>"

        return ret