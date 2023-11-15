
class ChannelIdAndName():
    def __init__(self, linkedHashMap):
        self.idsAndNames = []

        for entry in linkedHashMap.entry:
            self.idsAndNames.append(IdAndName(entry.string[0], entry.string[1]))

class IdAndName():
    def __init__(self, id, name):
        self.id = id
        self.name = name