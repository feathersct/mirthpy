from .mirthElement import MirthElement


class User(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.id = self.root.find('id').text
        self.username = self.root.find('username').text
        self.email = self.root.find('email').text
        self.firstName = self.root.find('firstName').text
        self.lastName = self.root.find('lastName').text
        self.organization = self.root.find('organization').text
        self.description = self.root.find('description').text
        self.phoneNumber = self.root.find('phoneNumber').text
        self.strikeCount = self.root.find('strikeCount').text