import re
from xml.etree import ElementTree
import xml.etree.ElementTree as ET
from .utilities import escape


class MirthElement:
    def __init__(self, uXml):
        if not isinstance(uXml, ET.Element):
            if uXml is None:
                self.root = None
            else:
                self.root = ET.fromstring(re.sub('&.+[0-9]+;[^\x00-\x7F]+', '', re.sub('[^\x00-\x7F]+', '', uXml.decode('utf-8'))))
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

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if k != 'root'}

    def getSafeText(self, prop: str) -> str:
        return self.root.find(prop).text if self.root.find(prop) != None else None

    def getXML(self, version = "3.12.0") -> str:
        ret = ""
        parentTag = "<{}".format(self.root.tag)

        if 'className' in vars(self):
            parentTag += ' class="{}"'.format(self.className)
        if 'version' in vars(self):
            parentTag += ' version="{}"'.format(self.version)

        parentTag += ">"
        ret += parentTag

        variables = vars(self)
        keys = [key for key, value in variables.items() if key not in ['root', 'className', 'version']]

        
        for k in keys:
            if type(variables[k]) in [str]:
                ret += '<{}>{}</{}>'.format(k, escape(variables[k]), k)
            elif type(variables[k]) in [type(None)]:
                ret += '<{}></{}>'.format(k, k)
            elif type(variables[k]) == ElementTree.Element:
                ret += ElementTree.tostring(variables[k], method='xml').decode().replace('\n', '')
            elif issubclass(type(variables[k]), MirthElement):
                ret += variables[k].getXML()
            elif type(variables[k]) == tuple:
                for t in variables[k]:
                    ret += '<string>{}</string>'.format(escape(t))
            elif type(variables[k]) == list:
                if len(variables[k]) == 0:
                    ret += '<{}/>'.format(k)
                else:
                    if k not in ['entry', 'string']:
                        ret += '<{}>'.format(k)
                    for x in variables[k]:
                        if type(x) in [str]:
                            ret += '<string>{}</string>'.format(escape(x))
                        elif type(x) in [bool]:
                            ret += '<boolean>{}</boolean>'.format(str(x).lower())
                        elif type(x) in [type(None)]:
                            f = ''
                        elif type(variables[k]) == ElementTree.Element:
                            ret += ElementTree.tostring(x, method='xml').decode().replace('\n', '')
                        elif issubclass(type(x), MirthElement):
                            ret += x.getXML()
                    if k not in ['entry', 'string']:
                        ret += '</{}>'.format(k)
        ret += "</{}>".format(self.root.tag)

        return ret