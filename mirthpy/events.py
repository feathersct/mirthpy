import xml.etree.ElementTree as ET
from .event import Event
from .mirthElement import MirthElement

class Events(MirthElement):
    def __init__(self, listXML):
        MirthElement.__init__(self, listXML)

        events = self.root
        self.events = []

        for e in events.findall('./event'):
            self.events.append(Event(e))