import requests

from mirthpy.connectors import Map
from mirthpy.linkedHashMap import LinkedHashMap

from .utilities import build_encoded_url_params
from .configurationMaps import ConfigurationMaps
from .channels import Channels, Channel
from .codeTemplates import CodeTemplates
from .events import Events
from .user import User
from .users import Users


class MirthService:
    apiUrl = ""
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest'
    }

    def __init__(self, configuration = None, username = None, password = None, instance = None):
        
        if configuration != None:
            #configuration is a json object
            self.instance = configuration.get('instanceName')
            self.credentials = configuration.get('credentials')
        elif username != None and password != None and instance != None:
            self.instance = instance
            self.credentials = {"username": username, "password": password}
        else:
            raise Exception("Configuration was setup incorrectly. Please check your parameters and start over.")
        
        self.jsessionId = ''

        # intialize and login
        self.initialize(True)

    # Intialize any variables after constructor
    def initialize(self, login=False):
        self.apiUrl = f"https://{self.instance}:8443/api"

    def open(self):
        self.login()
    
    def close(self):
        if self.jsessionId != None:
            self.logout()

    # User Calls
    def login(self):
        x = requests.post(f"{self.apiUrl}/users/_login?username={self.credentials.get('username')}&password={self.credentials.get('password')}", verify=False, headers=self.headers)

        self.jsessionId = x.cookies.get('JSESSIONID')
    
    def logout(self):
        x = requests.post(f"{self.apiUrl}/users/_logout", headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        self.jsessionId = None

    def getUsers(self) -> Users:
        users = requests.get(f"{self.apiUrl}/users", headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return Users(users.content)

    def getUser(self, userIdOrName) -> User:
        users = requests.get(f"{self.apiUrl}/users/{userIdOrName}", headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return User(users.content)

    # Event Calls
    def getEvents(self, params = {}) -> Events:

        parameters = []
        for key,value in params.items():
            parameters.append(f"{key}={value}")

        encParam = '?' + '&'.join(parameters)

        events = requests.get(f"{self.apiUrl}/events" + encParam, headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return Events(events.content)

    # Channel Calls
    def getChannels(self, channelIds = [], pollingOnly = False, includeCodeTemplates = False) -> Channels:
        
        encParam = build_encoded_url_params(channelId = channelIds, pollingOnly = pollingOnly, includeCodeTemplateLibraries = includeCodeTemplates)

        events = requests.get(f"{self.apiUrl}/channels" + encParam, headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return Channels(events.content)

    def getChannel(self, channelId, includeCodeTemplates = False) -> Channel:
        
        encParam = build_encoded_url_params(includeCodeTemplateLibraries = includeCodeTemplates)

        events = requests.get(f"{self.apiUrl}/channels/{channelId}" + encParam, headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return Channel(events.content)

    def getChannelIdsAndNames(self) -> LinkedHashMap:
        
        events = requests.get(f"{self.apiUrl}/channels/idsAndNames", headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return LinkedHashMap(events.content)

    def getChannelIdByName(self, name) -> str:
        
        events = requests.get(f"{self.apiUrl}/channels/idsAndNames", headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        map = LinkedHashMap(events.content)
        for e in map.entry: 
            if e.string[1] == name: 
                return e.string[0]

        return LinkedHashMap(events.content)

    # Code Template Calls
    def getCodeTemplates(self, codeTemplates = []) -> CodeTemplates:
        
        encParam = build_encoded_url_params(codeTemplateId = codeTemplates)

        events = requests.get(f"{self.apiUrl}/codeTemplates" + encParam, headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return CodeTemplates(events.content)

    def getConfigurationMaps(self) -> ConfigurationMaps:

        configMaps = requests.get(f"{self.apiUrl}/server/configurationMap", headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return ConfigurationMaps(configMaps.content)




