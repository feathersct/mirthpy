from .mirthElement import MirthElement
from .user import User

class Users(MirthElement):
    def __init__(self, userListXml):
        MirthElement.__init__(self, userListXml)
        users = self.root
        self.users = []

        for u in users.findall('./user'):
            self.users.append(User(u))