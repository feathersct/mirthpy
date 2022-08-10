from .mirthElement import MirthElement


class LinkedHashMap(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)
        
        self.entry = []

        for e in self.root.findall('./entry'):
            self.entry.append(Entry(e))

class Entry(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)
        
        strings = self.root.findall('./string')
        self.string = []
        
        for e in strings:
            self.string.append(e.text)