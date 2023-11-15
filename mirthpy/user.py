from .mirthElement import MirthElement
from .mirthDate import MirthDate
from .utilities import getXMLString


class User(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)
        self.id = ""
        self.username = ""
        self.email = ""
        self.firstName = ""
        self.lastName = ""
        self.organization = ""
        self.description = ""
        self.phoneNumber = ""
        self.industry = ""
        self.lastLogin = None
        self.gracePeriodStart = None
        self.strikeCount = None
        self.lastStrikeTime = None

        if uXml is not None:
            self.id = self.getSafeText('id')
            self.username = self.getSafeText('username')
            self.email = self.getSafeText('email')
            self.firstName = self.getSafeText('firstName')
            self.lastName = self.getSafeText('lastName')
            self.organization = self.getSafeText('organization')
            self.description = self.getSafeText('description')
            self.phoneNumber = self.getSafeText('phoneNumber')
            self.industry = self.getSafeText('industry')
            self.strikeCount = self.getSafeText('strikeCount')
            
            if self.root.find('lastLogin'):
                self.lastLogin = MirthDate(self.root.find('lastLogin'))
            
            if self.root.find('gracePeriodStart'):
                self.gracePeriodStart = MirthDate(self.root.find('gracePeriodStart'))

            if self.root.find('lastStrikeTime'):
                self.lastStrikeTime = MirthDate(self.root.find('lastStrikeTime'))

    def getXML(self, version="3.12.0"):
        # grace period start xml
        try:
            gracePeriodStart = getXMLString(self.gracePeriodStart.getXML(version), "gracePeriodStart",includeIfEmpty=False)
        except:
            gracePeriodStart = ""

        # last login xml
        try:
            lastLogin = getXMLString(self.lastLogin.getXML(version), "lastLogin",includeIfEmpty=False)
        except:
            lastLogin = ""

        # last strike time xml
        try:
            lastStrikeTime = getXMLString(self.lastStrikeTime.getXML(version), "lastStrikeTime",includeIfEmpty=False)
        except:
            lastStrikeTime = ""

        xml = ""
        xml += getXMLString(self.id, "id", includeIfEmpty=False)
        xml += getXMLString(self.username, "username")
        xml += getXMLString(self.email, "email")
        xml += getXMLString(self.firstName, "firstName")
        xml += getXMLString(self.lastName, "lastName")
        xml += getXMLString(self.organization, "organization")
        xml += getXMLString(self.description, "description")
        xml += getXMLString(self.phoneNumber, "phoneNumber")
        xml += getXMLString(self.industry, "industry")
        xml += lastLogin
        xml += getXMLString(self.strikeCount, "strikeCount", includeIfEmpty=False)
        xml += gracePeriodStart
        xml += lastStrikeTime

        return xml