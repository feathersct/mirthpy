from .mirthElement import MirthElement
from datetime import datetime


class MirthDate(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

        self.time = ''
        self.timezone = ''

        if uXml is not None:
            self.time = self.getSafeText('time')
            self.timezone = self.getSafeText('timezone')

    def getXML(self, version):
        xml = '<time>'
        xml += self.time
        xml += '</time>'
        xml += '<timezone>'
        xml += self.timezone
        xml += '</timezone>'
        
        return xml

    def getDateTime(self):
        ts = int(self.time)

        # if you encounter a "year is out of range" error the timestamp
        # may be in milliseconds, try `ts /= 1000` in that case
        return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')