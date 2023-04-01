import requests

from .serverStats import SystemStats
from .channelStatus import DashboardStatusList
from .channelStatistics import ChannelStatisticsList
from .mirthDate import MirthDate
from .channelTag import ChannelTags
from .message import Messages
from .snapshot import Snapshot, Snapshots
from .connectors import Map
from .linkedHashMap import LinkedHashMap
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

    def __init__(self, configuration = None, username = None, password = None, instance = None, port = None):
        
        if configuration != None:
            #configuration is a json object
            self.instance = configuration.get('instanceName')
            self.credentials = configuration.get('credentials')
        elif username != None and password != None and instance != None:
            self.instance = instance
            self.credentials = {"username": username, "password": password}
        else:
            raise Exception("Configuration was setup incorrectly. Please check your parameters and start over.")
        
        if port != None:
            self.port = port
        else:
            self.port = '8443'

        self.jsessionId = ''
        self.version = ''

        # intialize and login
        self.initialize(True)

    # Intialize any variables after constructor
    def initialize(self, login=False):
        self.apiUrl = f"https://{self.instance}:{self.port}/api"

    def open(self):
        self.login()
        self.version = self.getVersion()
    
    def close(self):
        if self.jsessionId != None:
            self.logout()

    def getVersion(self):
        version = requests.get(f"{self.apiUrl}/server/version", headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return version.text

    #region User Calls
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
    #endregion

    #region Event Calls
    def getEvents(self, params = {}) -> Events:

        parameters = []
        for key,value in params.items():
            parameters.append(f"{key}={value}")

        encParam = '?' + '&'.join(parameters)

        events = requests.get(f"{self.apiUrl}/events" + encParam, headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return Events(events.content)
    #endregion

    #region Server Calls
    def getGUID(self):
        guid = requests.post(f"{self.apiUrl}/server/_generateGUID", headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return guid.text
    
    def getTime(self):
        time = requests.get(f"{self.apiUrl}/server/time", headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return MirthDate(time.content)

    def getTags(self) -> ChannelTags:
        tags = requests.get(f"{self.apiUrl}/server/channelTags", headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return ChannelTags(tags.content)
    
    def getSystemStats(self) -> SystemStats:
        stats = requests.get(f"{self.apiUrl}/system/stats", headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return SystemStats(stats.content)
    #endregion

    #region Channel Calls
    def createChannel(self, channel):
        # set last modified time
        channel.exportData.metadata.lastModified = self.getTime()

        if type(channel) == Channel:
            channelString = f'<channel version="{self.version}">{channel.getXML(self.version)}</channel>'
        else:
            return (False, "channel not a channel object")
        
        response = requests.post(f"{self.apiUrl}/channels", data=channelString, headers={'X-Requested-With': 'XMLHttpRequest', 'Content-type': 'application/xml'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)
        
        if response.status_code in [204, 200]:
            return (True, None)
        else:
            return (False, response.text)

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
    
    def stopChannel(self, channelId):
        response = requests.post(f"{self.apiUrl}/channels/{channelId}/_stop?returnErrors=true", headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        if response.status_code in [204, 200]:
            return (True, None)
        else:
            return (False, response.text)
    
    def startChannel(self, channelId):
        response = requests.post(f"{self.apiUrl}/channels/{channelId}/_start?returnErrors=true", headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        if response.status_code in [204, 200]:
            return (True, None)
        else:
            return (False, response.text)
    #endregion

    #region Channel Status
    def getChannelStatus(self, channelIds = [], filter = "", includeUndeployed = False) -> Channels:
        
        encParam = build_encoded_url_params(channelId = channelIds, filter = filter, includeUndeployed = includeUndeployed)

        events = requests.get(f"{self.apiUrl}/channels/statuses" + encParam, headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return DashboardStatusList(events.content)
    #endregion

    #region Code Template Calls
    def getCodeTemplates(self, codeTemplates = []) -> CodeTemplates:
        
        encParam = build_encoded_url_params(codeTemplateId = codeTemplates)

        events = requests.get(f"{self.apiUrl}/codeTemplates" + encParam, headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return CodeTemplates(events.content)

    def getConfigurationMaps(self) -> ConfigurationMaps:

        configMaps = requests.get(f"{self.apiUrl}/server/configurationMap", headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return ConfigurationMaps(configMaps.content)
    #endregion

    #region Message Calls
    def getMessages(self, channelId, limit=20, includeContent = False, offset=0, startDate=None, endDate=None, status=None) -> ConfigurationMaps:
        encParam = build_encoded_url_params(includeContent=includeContent, limit=limit, offset=offset, startDate=startDate, endDate=endDate, status=status)
        messages = requests.get(f"{self.apiUrl}/channels/{channelId}/messages{encParam}", headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return Messages(messages.content)

    def getMessageCount(self, channelId, startDate=None, endDate=None, status=None) -> ConfigurationMaps:
        encParam = build_encoded_url_params(startDate=startDate, endDate=endDate, status=status)
        count = requests.get(f"{self.apiUrl}/channels/{channelId}/messages/count{encParam}", headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return int(count.text.replace('<long>','').replace('</long>', ''))
    #endregion

    #region Channel History
    def getChannelHistory(self, channelId) -> Snapshots:
        snapshots = requests.get(f"{self.apiUrl}/extensions/history/channels/{channelId}/snapshots", headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return Snapshots(snapshots.content)

    def getSnapshot(self, channelId, snapshotId):
        snapshot = requests.get(f"{self.apiUrl}/extensions/history/channels/{channelId}/snapshots/{snapshotId}", headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return Snapshot(snapshot.content)
    #endregion

    #region Channel Deployment
    def deployChannels(self, channelIds = [], returnErrors = False):
        # return number of channels deployed
        encParam = build_encoded_url_params(returnErrors=returnErrors)

        if len(channelIds) < 1:
            return 0
        
        setIds = f'<set><string>{"</string><string>".join(channelIds)}</string></set>'

        response = requests.post(f"{self.apiUrl}/channels/_deploy{encParam}", data=setIds, headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        if response.status_code in [204, 200]:
            return len(channelIds)
        else:
            return 0
    #endregion

    #region Server Configuration


    #endregion

    #region Channel Statistics
    def getChannelStatistics(self, channelIds = [], includeUndeployed = False, includeMetadataId = [], excludeMetaDataId = [], aggregateStats = False) -> ConfigurationMaps:
        encParam = build_encoded_url_params(channelIds=channelIds, includeUndeployed = includeUndeployed, includeMetadataId=includeMetadataId, excludeMetaDataId=excludeMetaDataId, aggregateStats=aggregateStats)
        stats = requests.get(f"{self.apiUrl}/channels/statistics", headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        return ChannelStatisticsList(stats.content)
    #endregion