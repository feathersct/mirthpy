from typing import Callable, List
from xml.etree.ElementTree import Element


def getSafeText(self : Element, prop:str):
    return self.find(prop).text if self.find(prop) != None else None

def build_encoded_url_params(**kwargs):
    params = []

    for key, value in kwargs.items():
        if type(value) == list or type(value) == tuple:
            for x in value:
                params.append(f"{key}={x}")
        elif type(value) == bool:
            if value:
                params.append(f"{key}=true")
            else:
                params.append(f"{key}=false")
        elif type(value) == type(None):
            continue
        else:
            params.append(f"{key}={value}")
    
    return '?' + '&'.join(params)

def escape(text):
   html_escape_table = {
        "&": "&amp;",
        '"': "&quot;",
        "'": "&apos;",
        ">": "&gt;",
        "<": "&lt;",
    }
   
   return "".join(html_escape_table.get(c,c) for c in text)
 
def getXMLString(value, name, enclose=True, includeIfEmpty=True):
    xml = ""

    # replace None with empty string
    if value is None:
        value = ""
    
    xml = f"<{name}>{value}</{name}>"

    if not enclose and value == "":
        xml = f"<{name}/>"

    if not includeIfEmpty and value == "":
        xml = ""

    return xml
