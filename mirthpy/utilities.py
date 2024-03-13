from typing import Callable, List
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
import urllib


def getSafeText(self : Element, prop:str):
    return self.find(prop).text if self.find(prop) != None else None

def build_encoded_url_params(**kwargs):
    params = []

    for key, value in kwargs.items():
        if type(value) == list or type(value) == tuple:
            for x in value:
                params.append(key + "=" + urllib.parse.quote_plus(x))
        elif type(value) == bool:
            if value:
                params.append(key + "=true")
            else:
                params.append(key + "=false")
        elif type(value) == type(None):
            continue
        elif type(value) == int:
            params.append(key + "=" + str(value))
        else:
            params.append(key + "=" + urllib.parse.quote_plus(value))
    
    return '?' + '&'.join(params)

def escape(text):
   html_escape_table = {
        "&": "&amp;",
        '"': "&quot;",
        "'": "&apos;",
        ">": "&gt;",
        "<": "&lt;",
    }
   if text is None:
       return text
   
   return "".join(html_escape_table.get(c,c) for c in text)
 
def getXMLString(value, name, enclose=True, includeIfEmpty=True):
    xml = ""

    # replace None with empty string
    if value is None:
        value = ""
    
    xml = "<{}>{}</{}>".format(name, value, name)

    if not enclose and value == "":
        xml = "<{}/>".format(name)

    if not includeIfEmpty and value == "":
        xml = ""
    
    if type(value) == Element:
        xml = ElementTree.tostring(value).decode().replace('\n', '')

    return xml
