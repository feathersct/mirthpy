from typing import Callable
from xml.etree.ElementTree import Element


def getSafeText(self : Element, prop:str):
    return self.find(prop).text if self.find(prop) != None else None
 