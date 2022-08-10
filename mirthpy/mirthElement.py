from types import NoneType
from xml.etree import ElementTree
import xml.etree.ElementTree as ET


class MirthElement:
    def __init__(self, uXml):
        if not isinstance(uXml, ET.Element):
            self.root = ET.fromstring(uXml)
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

    def getXML(self) -> str:
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
                ret += f'<{k}>{variables[k]}</{k}>'
            elif type(variables[k]) in [NoneType]:
                ret += f'<{k}></{k}>'
            elif type(variables[k]) == ElementTree.Element:
                ret += ElementTree.tostring(variables[k], method='xml').decode().replace('\n', '')
            elif issubclass(type(variables[k]), MirthElement):
                ret += variables[k].getXML()
            elif type(variables[k]) == tuple:
                for t in variables[k]:
                    ret += f'<string>{t}</string>'
            elif type(variables[k]) == list:
                if len(variables[k]) == 0:
                    ret += f'<{k}/>'
                else:
                    #print(f'<{k}>')
                    for x in variables[k]:
                        if type(x) in [str]:
                            ret += f'<string>{x}</string>'
                        elif type(x) in [NoneType]:
                            print(f'')
                        elif type(variables[k]) == ElementTree.Element:
                            ret += ElementTree.tostring(x, method='xml').decode().replace('\n', '')
                        elif issubclass(type(x), MirthElement):
                            ret += x.getXML()
                    #print(f'</{k}>')
        ret += f"</{self.root.tag}>"

        return ret