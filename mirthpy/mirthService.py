import requests
import xml.etree.ElementTree as ET

from .extensions import Plugins
from .serverSettings import ServerSettings
from .channelIdAndName import ChannelIdAndName
from .channelGroup import ChannelGroups
from .exceptions import UnauthorizedError
from .serverStats import SystemStats
from .serverInfo import SystemInfo
from .channelStatus import DashboardStatusList, DashboardStatus
from .channelStatistics import ChannelStatisticsList, ChannelStatistics
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
        'X-Requested-With': 'XMLHttpRequest'
    }
    cookies = {}

    def __init__(self, configuration = None, username = None, password = None, instance = None, port = '8443'):
        
        if configuration is not None:
            # configuration is a dictionary
            self.instance = configuration.get('instanceName')
            self.credentials = configuration.get('credentials')
        elif username is not None and password is not None and instance is not None:
            self.instance = instance
            self.credentials = {"username": username, "password": password}
        else:
            raise ValueError("Configuration was setup incorrectly. Please check your parameters and start over.")
        
        self.port = port
        self.jsessionId = ''
        self.version = ''

        # intialize and login
        self.initialize(True)

    def __enter__(self):
        self.open()
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    # Intialize any variables after constructor
    def initialize(self, login=False):
        self.apiUrl = "https://" + self.instance + ":" + str(self.port) + "/api"

    def open(self):
        self.version = self.getVersion()
        self.login()
    
    def close(self):
        if self.jsessionId != None:
            self.logout()
    
    def _get(self, url):
        results = requests.get(self.apiUrl + "/" + url, headers=self.headers, cookies=self.cookies, verify=False)
        return results
    
    def _post(self, url):
        results = requests.post(self.apiUrl + "/" + url, headers=self.headers, cookies=self.cookies, verify=False)
        return results

    def _put(self, url, data, headers):
        if not headers:
            headers = self.headers

        results = requests.put(self.apiUrl + "/" + url, data=data, headers=headers, cookies=self.cookies, verify=False)
        return results

    def getVersion(self) -> str:
        r"""Returns the version of Mirth the server is running.
            :return: the version of mirth
            :rtype: str
            """
        version = self._get("server/version")

        return version.text
    
    #region User Calls
    def login(self):
        r"""Logs in to the Mirth Connect server using the specified name and password passed in the constructor.
            """
        
        self.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        x = self._post("users/_login?username={}&password={}".format(self.credentials.get('username'), self.credentials.get('password')))

        # unauthorized
        if x.status_code == 401:
            raise UnauthorizedError('{}: Unauthorized. Check permissons and user/password.'.format(x.status_code))

        self.jsessionId = x.cookies.get('JSESSIONID')
        self.cookies['JSESSIONID'] = self.jsessionId
        if 'Content-Type' in self.headers:
            self.headers.pop('Content-Type')
    
    def logout(self):
        r"""Logs out of the Mirth Connect server.
            """
        x = self._post("users/_logout")

        self.jsessionId = None
        if self.cookies.get('JSESSIONID'):
            self.cookies.pop("JSESSIONID")

    def getUsers(self) -> Users:
        r"""Returns a list of all users
            :return: :class:`Users <Users>` object
            :rtype: Users
            """
        users = self._get("users")

        return Users(users.content)

    def getUser(self, userIdOrName) -> User:
        r"""Returns a single user based on the user id or username
            :return: :class:`User <User>` object
            :rtype: User
            """
        response = self._get("users/{}".format(userIdOrName))
        
        if response.status_code in [204, 200]:
            return User(response.content)
        elif response.status_code in [500]:
            raise Exception("Internal Mirth server error.")
        else:
            return None

    
    def isUserLoggedIn(self, userid) -> bool:
        r"""Returns a true if the specified user is logged in to the server.
            :return: True if logged in, False if not logged in
            :rtype: bool
            """
        
        loggedIn = self._get("users/{}/loggedIn".format(userid))
        strToEvaluate = loggedIn.text.replace('<boolean>','').replace('</boolean>', '')
        return strToEvaluate == "true"
    
    def addUser(self, user:User):
        r"""Creates a new user.
            :return: True if user is created, False if user is not created, with an error message
            :rtype: bool
            """
        
        if type(user) == User:
            userString = '<user>{}</user>'.format(user.getXML(self.version))
        else:
            return (False, "user is not a User object")
        
        #TODO: convert to use self.post instead
        response = requests.post(self.apiUrl + "/users", data=userString, headers={'X-Requested-With': 'XMLHttpRequest', 'Content-type': 'application/xml'}, cookies=self.cookies, verify=False)
        
        if response.status_code in [204, 200]:
            return (True, None)
        elif response.status_code in [500]:
            return (False, ET.fromstring(response.text).findtext('detailMessage'))
        else:
            return (False, "{} Error: User could not be created.".format(response.status_code))
    
    def deleteUser(self, userId):
        r"""Delete's a user in mirth based on the user's id.

            :param userId: Mirth user id
            :return: True if successful, False if not success, with error message.
            :rtype: tuple[bool, str]
            """
        
        response = requests.delete(self.apiUrl + "/users/{}".format(userId), headers=self.headers, cookies=self.cookies, verify=False)
        
        if response.status_code in [204, 200]:
            return (True, None)
        elif response.status_code in [500]:
            return (False, ET.fromstring(response.text).findtext('detailMessage'))
        else:
            return (False, "{} Error: Could not delete user {}.".format(response.status_code, userId))
    
    def updateUserPassword(self, userId, password):
        r"""Updates a user's password in mirth based on the user's id.

            :param userId: Mirth user id
            :return: True if successful, False if not success, with error message.
            :rtype: tuple[bool, str]
            """
        
        response = requests.put(self.apiUrl + "/users/{}/password".format(userId), data=password, headers={'X-Requested-With': 'XMLHttpRequest', 'Content-type': 'text/plain'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)
        
        if response.status_code in [204, 200]:
            return (True, None)
        elif response.status_code in [500]:
            return (False, ET.fromstring(response.text).findtext('detailMessage'))
        else:
            return (False, response.status_code + " Error: Could not update user {}'s password.".format(userId))
    #endregion

    #region Event Calls
    def getEvents(self, params = {}) -> Events:
        r"""Get mirth events based on parameters used.

        :param params: json with key and value
        :return: :class:`Events <Events>` object
            :rtype: Events
        """
        parameters = []
        for key,value in params.items():
            parameters.append(key + "=" + value)

        encParam = '?' + '&'.join(parameters)

        events = self._get("events" + encParam)

        return Events(events.content)
    #endregion

    #region Server Calls
    def getGUID(self) -> str:
        r"""Returns a globally unique id.

        :return: guid 
        :rtype: str
        """
        guid = self._post("server/_generateGUID")

        return guid.text
    
    def getTime(self) -> MirthDate:
        r"""Returns the time of the mirth server.

        :return: :class:`MirthDate <MirthDate>` object
        :rtype: MirthDate with current time
        """
        time = self._get("server/time")

        return MirthDate(time.content)

    def getTags(self) -> ChannelTags:
        r"""Returns a set containing all channel tags for this Mirth Server. 
        
        :return: :class:`ChannelTags <ChannelTags>` object
        :rtype: ChannelTags for the mirth server.
        """
        tags = self._get("server/channelTags")

        return ChannelTags(tags.content)
    
    def getSystemStats(self) -> SystemStats:
        r"""Returns statistics for underlying system. This can include timestamp, cpu usage, allocated memory,
        free memory, max memory, free disk space, total disk space. 
        
        :return: :class:`SystemStats <SystemStats>` object
        :rtype: System Stats for the mirth server.
        """
        stats = self._get("system/stats")

        return SystemStats(stats.content)
    
    def getSystemInfo(self) -> SystemInfo:
        r"""Returns statistics for underlying system. This can include jvmVersion, os name, os version, os architecture, db name, db version.
        
        :return: :class:`SystemInfo <SystemInfo>` object
        :rtype: System Info for the mirth server.
        """
        stats = self._get("system/info")

        return SystemInfo(stats.content)
    
    def getServerSettings(self) -> ServerSettings:
        r"""Returns all server settings. This can include environment name, server name, default meta data columns, smtp settings, etc.
        
        :return: :class:`ServerSettings <ServerSettings>` object
        :rtype: Server Settings for the mirth server.
        """
        settings = self._get("server/settings")

        return ServerSettings(settings.content)

    #endregion

    #region Channel Calls
    def createChannel(self, channel, set_time = True):
        r"""Creates a new channel based off of mirthpy channel object.

        :param channel: Channel object 
        :return: True if successful, False if not success, with error message.
        :rtype: tuple[bool, str]
        """
        # set last modified time
        if set_time:
            channel.exportData.metadata.lastModified = self.getTime()

        if type(channel) == Channel:
            channelString = '<channel version="{}">'.format(self.version)
            channelString += channel.getXML(self.version)
            channelString += '</channel>'
        else:
            return (False, "channel not a channel object")
        
        #TODO: convert to use self.post instead
        response = requests.post(self.apiUrl + "/channels", data=channelString.encode('utf-8'), headers={'X-Requested-With': 'XMLHttpRequest', 'Content-type': 'application/xml'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)
        
        if response.status_code in [204, 200]:
            return (True, self.getChannelIdByName(channel.name))
        elif response.status_code in [500]:
            return (False, ET.fromstring(response.text).findtext('detailMessage'))
        else:
            return (False, response.status_code + " Error: Could not create channel.")

    def updateChannel(self, channel, override = False, set_time = True):
        r"""Updates a channel based off of mirthpy channel object.

        :param channel: Channel object 
        :return: True if successful, False if not success, with error message.
        :rtype: tuple[bool, str]
        """
        # set last modified time
        if set_time:
            channel.exportData.metadata.lastModified = self.getTime()

        if type(channel) == Channel:
            channelString = '<channel version="{}">'.format(self.version)
            channelString += channel.getXML(self.version)
            channelString += '</channel>'
        else:
            return (False, "channel not a channel object")
        
        encParam = build_encoded_url_params(override=override)
        
        response = requests.put(self.apiUrl+ "/channels/{}{}".format(channel.id, encParam), data=channelString.encode('utf-8'), headers={'X-Requested-With': 'XMLHttpRequest', 'Content-type': 'application/xml'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)
        
        if response.status_code in [204, 200]:
            return (True, None)
        elif response.status_code in [500]:
            return (False, ET.fromstring(response.text).findtext('detailMessage'))
        else:
            return (False, response.status_code + " Error: Could not update channel.")

    def deleteChannel(self, channelId, override = False):
        r"""Deletes a channel based off of channel id.

        :param channel: Channel object 
        :return: True if successful, False if not success, with error message.
        :rtype: tuple[bool, str]
        """

        response = requests.delete(self.apiUrl + "/channels/{}".format(channelId), headers={'X-Requested-With': 'XMLHttpRequest', 'Content-type': 'application/xml'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)
        
        if response.status_code in [204, 200]:
            return (True, None)
        elif response.status_code in [500]:
            return (False, ET.fromstring(response.text).findtext('detailMessage'))
        else:
            return (False, response.status_code + " Error: Could not delete channel.")

    def getChannels(self, channelIds = [], pollingOnly = False, includeCodeTemplates = False) -> Channels:
        r"""Returns specified channel objects. 
            If channelIds is empty then all channels will be retrieved.
        :param channelIds: array of channel ids 
        :param pollingOnly: bool indicating if polling channels should be the only received
        :param includeCodeTemplates: bool, include code templates in object
        :return: :class:`Channels <Channels>` object
        :rtype: Channels
        """

        encParam = build_encoded_url_params(channelId = channelIds, pollingOnly = pollingOnly, includeCodeTemplateLibraries = includeCodeTemplates)

        events = self._get("channels{}".format(encParam))

        return Channels(events.content)

    def getChannel(self, channelId, includeCodeTemplates = False) -> Channel:
        r"""Returns 1 channel object.

        :param channelId: channel id to be retrieved 
        :param includeCodeTemplates: bool, include code templates in object
        :return: :class:`Channel <Channel>` object
        :rtype: Channel
        """

        encParam = build_encoded_url_params(includeCodeTemplateLibraries = includeCodeTemplates)

        events = self._get("channels/{}{}".format(channelId, encParam))

        return Channel(events.content)

    def getChannelIdsAndNames(self):
        r"""Get all channel ids and names

        :return: :class:`ChannelIdAndName <ChannelIdAndName>` object with names and ids
        :rtype: LinkedHashMap
        """
        if self.version == '3.6.1':
            map = ET.Element('map')
            channels = self.getChannels()
            for channel in channels.channels:
                entry = ET.SubElement(map, 'entry')
                string1 = ET.SubElement(entry, 'string')
                string2 = ET.SubElement(entry, 'string')

                string1.text = channel.id
                string2.text = channel.name
                
            return ChannelIdAndName(LinkedHashMap(map))

        events = self._get("channels/idsAndNames")
        
        return ChannelIdAndName(LinkedHashMap(events.content))

    def getChannelIdByName(self, name) -> str:
        r"""Get channel id by a name, uses getChannelIdsAndNames and filters them.
        If name not found then empty string is returned

        :param name: channel name to be retrieved 
        :rtype: str
        """
        events = self._get("channels/idsAndNames")

        map = LinkedHashMap(events.content)
        for e in map.entry: 
            if e.string[1] == name: 
                return e.string[0]

        return ""
    #endregion

    #region Channel Status Operations
    def haltChannels(self, channelIds = [], returnErrors = False) -> int:
        r"""Halt a set of channels. If channelIds is empty, all channels will be halted.
            
            :param channelIds: channel ids to attempt to halt
            :param returnErrors: to return any errors with halting

            :return: number of how many channels were halted
            :rtype: int
            """
        # return number of channels haulted
        encParam = build_encoded_url_params(returnErrors=returnErrors)

        if len(channelIds) < 1:
            return 0
        
        data = 'channelId=' + '&channelId='.join(channelIds)
        
        response = requests.post(self.apiUrl + "/channels/_halt{}".format(encParam), data=data, headers={'X-Requested-With': 'XMLHttpRequest', 'Content-Type': 'application/x-www-form-urlencoded'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        if response.status_code in [204, 200]:
            return len(channelIds)
        else:
            return 0
        
    def pauseChannels(self, channelIds = [], returnErrors = False) -> int:
        r"""Pause a set of channels. If channelIds is empty, all channels will be Paused.
            
            :param channelIds: channel ids to attempt to Pause
            :param returnErrors: to return any errors

            :return: number of how many channels were Paused
            :rtype: int
            """
        # return number of channels haulted
        encParam = build_encoded_url_params(returnErrors=returnErrors)

        if len(channelIds) < 1:
            return 0
        
        data = 'channelId=' + '&channelId='.join(channelIds)
        
        response = requests.post(self.apiUrl + "/channels/_pause{}".format(encParam), data=data, headers={'X-Requested-With': 'XMLHttpRequest', 'Content-Type': 'application/x-www-form-urlencoded'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        if response.status_code in [204, 200]:
            return len(channelIds)
        else:
            return 0
        
    def resumeChannels(self, channelIds = [], returnErrors = False) -> int:
        r"""Resume a set of channels. If channelIds is empty, all channels will be resumed.
            
            :param channelIds: channel ids to attempt to resume
            :param returnErrors: to return any errors

            :return: number of how many channels were resumed
            :rtype: int
            """
        # return number of channels haulted
        encParam = build_encoded_url_params(returnErrors=returnErrors)

        if len(channelIds) < 1:
            return 0
        
        data = 'channelId=' + '&channelId='.join(channelIds)
        
        response = requests.post(self.apiUrl + "/channels/_resume{}".format(encParam), data=data, headers={'X-Requested-With': 'XMLHttpRequest', 'Content-Type': 'application/x-www-form-urlencoded'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        if response.status_code in [204, 200]:
            return len(channelIds)
        else:
            return 0
        
    def startChannels(self, channelIds = [], returnErrors = False) -> int:
        r"""Start a set of channels. If channelIds is empty, all channels will be started.
            
            :param channelIds: channel ids to attempt to start
            :param returnErrors: to return any errors

            :return: number of how many channels were started
            :rtype: int
            """
        # return number of channels haulted
        encParam = build_encoded_url_params(returnErrors=returnErrors)

        if len(channelIds) < 1:
            return 0
        
        data = 'channelId=' + '&channelId='.join(channelIds)
        
        response = requests.post(self.apiUrl + "/channels/_start{}".format(encParam), data=data, headers={'X-Requested-With': 'XMLHttpRequest', 'Content-Type': 'application/x-www-form-urlencoded'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        if response.status_code in [204, 200]:
            return len(channelIds)
        else:
            return 0
        
    def stopChannels(self, channelIds = [], returnErrors = False) -> int:
        r"""Stop a set of channels. If channelIds is empty, all channels will be stopped.
            
            :param channelIds: channel ids to attempt to stop
            :param returnErrors: to return any errors

            :return: number of how many channels were stopped
            :rtype: int
            """
        # return number of channels haulted
        encParam = build_encoded_url_params(returnErrors=returnErrors)

        if len(channelIds) < 1:
            return 0
        
        data = 'channelId=' + '&channelId='.join(channelIds)
        
        response = requests.post(self.apiUrl + "/channels/_stop{}".format(encParam), data=data, headers={'X-Requested-With': 'XMLHttpRequest', 'Content-Type': 'application/x-www-form-urlencoded'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        if response.status_code in [204, 200]:
            return len(channelIds)
        else:
            return 0
        
    def haltChannel(self, channelId, returnErrors = False):
        r"""Attempts to halt channel based on channel id.

            :param channelId: The channel id of channel to halt
            :return: True if successful, False if not success, with error message.
            :rtype: tuple[bool, str]
            """
        encParam = build_encoded_url_params(returnErrors=returnErrors)

        response = self._post("channels/{}/_halt{}".format(channelId,encParam))

        if response.status_code in [204, 200]:
            return (True, None)
        elif response.status_code in [500]:
            return (False, ET.fromstring(response.text).findtext('detailMessage'))
        else:
            return (False, str(response.status_code) + " Error: Could not halt channel {}.".format(channelId))
        
    def pauseChannel(self, channelId, returnErrors = False):
        r"""Attempts to pause channel based on channel id.

            :param channelId: The channel id of channel to pause
            :return: True if successful, False if not success, with error message.
            :rtype: tuple[bool, str]
            """
        encParam = build_encoded_url_params(returnErrors=returnErrors)

        response = self._post("channels/{}/_pause{}".format(channelId,encParam))

        if response.status_code in [204, 200]:
            return (True, None)
        elif response.status_code in [500]:
            return (False, ET.fromstring(response.text).findtext('detailMessage'))
        else:
            return (False, str(response.status_code) + " Error: Could not pause channel {}.".format(channelId))

    def resumeChannel(self, channelId, returnErrors = False):
        r"""Attempts to resume channel based on channel id.

            :param channelId: The channel id of channel to resume
            :return: True if successful, False if not success, with error message.
            :rtype: tuple[bool, str]
            """
        encParam = build_encoded_url_params(returnErrors=returnErrors)

        response = self._post("channels/{}/_resume{}".format(channelId,encParam))

        if response.status_code in [204, 200]:
            return (True, None)
        elif response.status_code in [500]:
            return (False, ET.fromstring(response.text).findtext('detailMessage'))
        else:
            return (False, str(response.status_code) + " Error: Could not pause channel {}.".format(channelId))

    def stopChannel(self, channelId):
        r"""Attempts to stop channel based on channel id.

            :param channelId: The channel id of channel to stop
            :return: True if successful, False if not success, with error message.
            :rtype: tuple[bool, str]
            """
        
        response = self._post("channels/{}/_stop?returnErrors=true".format(channelId))

        if response.status_code in [204, 200]:
            return (True, None)
        elif response.status_code in [500]:
            return (False, ET.fromstring(response.text).findtext('detailMessage'))
        else:
            return (False, str(response.status_code) + " Error: Could not stop channel {}.".format(channelId))
    
    def startChannel(self, channelId):
        r"""Attempts to start channel based on channel id.

            :param channelId: The channel id of channel to start
            :return: True if successful, False if not success, with error message.
            :rtype: tuple[bool, str]
            """
        response = self._post("channels/{}/_start?returnErrors=true".format(channelId))

        if response.status_code in [204, 200]:
            return (True, None)
        elif response.status_code in [500]:
            return (False, ET.fromstring(response.text).findtext('detailMessage'))
        else:
            return (False, str(response.status_code) + " Error: Could not start channel {}.".format(channelId))
    
    def startConnectors(self, channelId, metadataIds = [], returnErrors = False):
        r"""Attempts to start connectors based on channel id and metadata id.

            :param channelId: The channel id of channel to start
            :param metadataId: The metadata id of connector to start
            :return: True if successful, False if not success, with error message.
            :rtype: tuple[bool, str]
            """
        # query parameters
        encParam = build_encoded_url_params(returnErrors=returnErrors)

        # request body
        data = "<map>"
        data += "<entry>"
        data += "<string>{}</string>".format(channelId)
        data += "<list>"
        for metadataId in metadataIds:
            data += "<int>{}</int>".format(metadataId)
        data += "</list>"
        data += "</entry>"
        data += "</map>"

        response = requests.post(self.apiUrl + "/channels/_startConnectors{}".format(encParam), data=data, headers={'X-Requested-With': 'XMLHttpRequest', 'Content-Type': 'application/xml'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        if response.status_code in [204, 200]:
            return (True, None)
        else:
            return (False, str(response.status_code) + " Error: Could not start connector {}.".format(metadataId))
    
    def stopConnectors(self, channelId, metadataIds = [], returnErrors = False):
        r"""Attempts to stop connectors based on channel id and metadata id.

            :param channelId: The channel id of channel to stop
            :param metadataId: The metadata id of connector to stop
            :return: True if successful, False if not success, with error message.
            :rtype: tuple[bool, str]
            """
        # query parameters
        encParam = build_encoded_url_params(returnErrors=returnErrors)

        # request body
        data = "<map>"
        data += "<entry>"
        data += "<string>{}</string>".format(channelId)
        data += "<list>"
        for metadataId in metadataIds:
            data += "<int>{}</int>".format(metadataId)
        data += "</list>"
        data += "</entry>"
        data += "</map>"

        response = requests.post(self.apiUrl + "/channels/_stopConnectors{}".format(encParam), data=data, headers={'X-Requested-With': 'XMLHttpRequest', 'Content-Type': 'application/xml'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        if response.status_code in [204, 200]:
            return (True, None)
        else:
            return (False, str(response.status_code) + " Error: Could not stop connector {}.".format(metadataId))

    def getChannelStatus(self, channelId):
        r"""Get the status of a channel.

            :param channelId: channel id corresponding to the status
            :return: :class:`DashboardStatusList <DashboardStatusList>` object
            :rtype: DashboardStatusList
            """
        events = self._get("channels/{}/status".format(channelId))

        return DashboardStatus(events.content)
    
    def getChannelStatuses(self, channelIds = [], filter = "", includeUndeployed = False) -> DashboardStatusList:
        r"""Get the status of specified channels or all if channelIds is empty.

            :param channelIds: list of channel ids
            :param filter: str of channel to be filtered
            :param includeUndeployed: only get deployed channels
            :return: :class:`DashboardStatusList <DashboardStatusList>` object
            :rtype: DashboardStatusList
            """
        encParam = build_encoded_url_params(channelId = channelIds, filter = filter, includeUndeployed = includeUndeployed)

        events = self._get("channels/statuses{}".format(encParam))

        return DashboardStatusList(events.content)

    #endregion

    #region Code Template Calls
    def getCodeTemplates(self, codeTemplates = []) -> CodeTemplates:
        r"""Get specified code templates, if codeTemplates is empty get all code templates.
            
            :param codeTemplates: array of code template ids
            :return: :class:`CodeTemplates <CodeTemplates>` object
            :rtype: CodeTemplates
            """
        
        encParam = build_encoded_url_params(codeTemplateId = codeTemplates)

        events = self._get("codeTemplates{}".format(encParam))

        return CodeTemplates(events.content)

    def putCodeTemplates(self, codeTemplates, override=False):
        encParam = build_encoded_url_params(override=override)

        response = self._put("codeTemplateLibraries{}".format(encParam), data=codeTemplates, headers={'X-Requested-With': 'XMLHttpRequest', 'Content-type': 'application/xml'})

        if response.status_code in [204, 200]:
            return (True, None)
        elif response.status_code in [500]:
            return (False, ET.fromstring(response.text).findtext('detailMessage'))
        else:
            return (False, response.status_code + " Error: Could not update code templates.")
    
    def putCodeTemplate(self, codeTemplateId, codeTemplates, override=False):
        encParam = build_encoded_url_params(override=override)

        response = self._put("codeTemplates/{}{}".format(codeTemplateId,encParam), data=codeTemplates, headers={'X-Requested-With': 'XMLHttpRequest', 'Content-type': 'application/xml'})

        if response.status_code in [204, 200]:
            return (True, None)
        elif response.status_code in [500]:
            return (False, ET.fromstring(response.text).findtext('detailMessage'))
        else:
            return (False, response.status_code + " Error: Could not update code templates.")
    #endregion

    #region Message Calls
    def getMessages(self, channelId, limit=20, includeContent = False, offset=0, startDate=None, endDate=None, status=None) -> Messages:
        r"""Get messages for a specific channel and filter by date and status.
            
            :param channelId: channel id corresponding to the message to receive
            :param limit: number of message to limit by
            :param includeContent: include the actual message payload
            :param offset: the page to offset the message to receive
            :param startDate: the date to start looking for messages
            :param endDate: the date to end looking for messages
            :param status: the status of the messages to receive. ie RECEIVED, FILTERED, TRANSFORMED, SENT, QUEUED, ERROR, PENDING
            
            :return: :class:`Messages <Messages>` object
            :rtype: Messages
            """
        
        encParam = build_encoded_url_params(includeContent=includeContent, limit=limit, offset=offset, startDate=startDate, endDate=endDate, status=status)
        
        messages = self._get("channels/{}/messages{}".format(channelId, encParam))

        return Messages(messages.content)

    def getMessageCount(self, channelId, startDate=None, endDate=None, status=None) -> int:
        r"""Get messages count for a specific channel and filter by date and status.
            
            :param channelId: channel id corresponding to the message to receive
            :param startDate: the date to start looking for messages
            :param endDate: the date to end looking for messages
            :param status: the status of the messages to receive. ie RECEIVED, FILTERED, TRANSFORMED, SENT, QUEUED, ERROR, PENDING
            
            :return: the count of message based on filters
            :rtype: int
            """
        encParam = build_encoded_url_params(startDate=startDate, endDate=endDate, status=status)
        count = self._get("channels/{}/messages/count{}".format(channelId, encParam))

        return int(count.text.replace('<long>','').replace('</long>', ''))
    #endregion

    #region Channel History
    def getChannelHistory(self, channelId) -> Snapshots:
        r"""Get the history of a channel with snapshots. This is a paid exetension.
            
            :param channelId: channel id corresponding to the history

            :return: :class:`Snapshots <Snapshots>` object
            :rtype: Snapshots
            """
        snapshots = self._get("extensions/history/channels/{}/snapshots".format(channelId))

        return Snapshots(snapshots.content)

    def getSnapshot(self, channelId, snapshotId) -> Snapshot:
        r"""Get a specific snapshot of a channels history. This is a paid exetension.
        
            :param channelId: channel id corresponding to the history
            :param snapshotId: snapshot id corresponding to the history

            :return: :class:`Snapshot <Snapshot>` object
            :rtype: Snapshot
            """
        snapshot = self._get("extensions/history/channels/{}/snapshots/{}".format(channelId, snapshotId))

        return Snapshot(snapshot.content)
    #endregion

    #region Channel Deployment
    def deployChannels(self, channelIds = [], returnErrors = False) -> int:
        r"""Deploy a set of channels. If channelIds is empty, all channels will be deployed.
            
            :param channelIds: channel ids to attempt to deploy
            :param returnErrors: to return any errors with deploying

            :return: number of how many channels were deployed
            :rtype: int
            """
        # return number of channels deployed
        encParam = build_encoded_url_params(returnErrors=returnErrors)

        if len(channelIds) < 1:
            return 0
        
        setIds = '<set><string>' + "</string><string>".join(channelIds)+ '</string></set>'

        #TODO: Convert to use self.post
        response = requests.post(self.apiUrl + "/channels/_deploy{}".format(encParam), data=setIds, headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        if response.status_code in [204, 200]:
            return len(channelIds)
        else:
            return 0
        
    def deployChannel(self, channelId, returnErrors = False):
        r"""Deploy a single channel.
            
            :param channelIds: channel id to attempt to deploy
            :param returnErrors: to return any errors with deploying

            :return: number of how many channels were deployed
            :rtype: int
            """
        encParam = build_encoded_url_params(returnErrors=returnErrors)

        #TODO: Convert to use self.post
        response = requests.post(self.apiUrl + "/channels/" + channelId + "/_deploy{}".format(encParam), headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        if response.status_code in [204, 200]:
            return True
        else:
            return False
        
    def undeployChannels(self, channelIds = [], returnErrors = False) -> int:
        r"""Undeploy a set of channels. If channelIds is empty, all channels will be undeployed.
            
            :param channelIds: channel ids to attempt to undeploy
            :param returnErrors: to return any errors with undeploying

            :return: number of how many channels were undeployed
            :rtype: int
            """
        # return number of channels undeployed
        encParam = build_encoded_url_params(returnErrors=returnErrors)

        if len(channelIds) < 1:
            return 0
        
        setIds = '<set><string>' + "</string><string>".join(channelIds)+ '</string></set>'

        #TODO: Convert to use self.post
        response = requests.post(self.apiUrl + "/channels/_undeploy{}".format(encParam), data=setIds, headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        if response.status_code in [204, 200]:
            return len(channelIds)
        else:
            return 0

    def undeployChannel(self, channelId, returnErrors = False):
        r"""Undeploy a single channel.
            
            :param channelIds: channel id to attempt to undeploy
            :param returnErrors: to return any errors with undeploying

            :return: number of how many channels were undeployed
            :rtype: int
            """
        encParam = build_encoded_url_params(returnErrors=returnErrors)

        #TODO: Convert to use self.post
        response = requests.post(self.apiUrl + "/channels/" + channelId + "/_undeploy{}".format(encParam), headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        if response.status_code in [204, 200]:
            return True
        else:
            return False    
    
    def redeployAllChannels(self, returnErrors = False):
        r"""Re-deploy all channels. 
            
            :param returnErrors: to return any errors with deploying

            """
        # return number of channels undeployed
        encParam = build_encoded_url_params(returnErrors=returnErrors)
        
        #TODO: Convert to use self.post
        response = requests.post(self.apiUrl + "/channels/_redeployAll{}".format(encParam), headers={'X-Requested-With': 'XMLHttpRequest'}, cookies={'JSESSIONID': self.jsessionId}, verify=False)

        if response.status_code in [204, 200]:
            return True
        else:
            return False
    #endregion

    #region Channel Groups
    def getChannelGroups(self, channelGroupIds = []):
        r"""Retrieve a list of all channel groups, or multiple channel groups by ID.
            
            :rtype: ChannelGroups
            """
        map = self._get("channelgroups")

        return ChannelGroups(map.content)
    
    def getChannelGroupByName(self, name):
        r"""Retrieve a channel group by name. This uses getChannelGroups and filters by name.
            
            :rtype: ChannelGroups
            """
        map = self._get("channelgroups")
        groups = ChannelGroups(map.content)

        for group in groups.channelGroups:
            if group.name == name:
                return group

        return None
    #endregion

    #region Server Configuration
    def getServerId(self):
        server_id = self._get("server/id")

        return server_id.content
    
    def getConfigurationMaps(self) -> ConfigurationMaps:
        r"""Get all configuration mappings.
            
            :return: :class:`ConfigurationMaps <ConfigurationMaps>` object
            :rtype: ConfigurationMaps
            """
        configMaps = self._get("server/configurationMap")

        return ConfigurationMaps(configMaps.content)
    
    def putConfigurationMaps(self, configurationMaps):
        r"""Updates all entries in the configuration map.
            
            :return: :class:`ConfigurationMaps <ConfigurationMaps>` object
            :rtype: ConfigurationMaps
            """
        
        if type(configurationMaps) != ConfigurationMaps:
            return (False, "configurationMaps must be a ConfigurationMaps Object")
        
        response = self._put("server/configurationMap", data=configurationMaps.getXML(), headers={'X-Requested-With': 'XMLHttpRequest', 'Content-type': 'application/xml'})

        if response.status_code in [204, 200]:
            return (True, None)
        elif response.status_code in [500]:
            return (False, ET.fromstring(response.text).findtext('detailMessage'))
        else:
            return (False, response.status_code + " Error: Could not update config maps.")

    #endregion

    #region Extensions
    def getPlugins(self) -> Plugins:
        r"""Returns all active plugin metadata.
            
            :return: :class:`Plugins <Plugins>` object
            :rtype: Plugins
            """
        plugins = self._get("extensions/plugins")

        return Plugins(plugins.content)
    #endregion

    #region Channel Statistics
    def getChannelStatistics(self, channelIds = [], includeUndeployed = False, includeMetadataId = [], excludeMetaDataId = [], aggregateStats = False) -> ChannelStatisticsList:
        r"""Get channel statistics for specified channel. If channelIds is empty then get all channel statistics.
            
            :param channelIds: ids of the channels to retrieve. If blank, all channels will be retrieved.
            :param includeUndeployed: bool. If True, statistics for undeployed channels will also be included.
            :param includeMetadataId: The ids of connectors to include. Cannot include and exclude connectors
            :param excludeMetaDataId: The ids of connectors to exclude. Cannot include and exclude connectors
            :param aggregateStats: bool, If True, statistics will be aggregated into one result.
            :return: :class:`ChannelStatisticsList <ChannelStatisticsList>` object
            :rtype: ChannelStatisticsList
            """
        encParam = build_encoded_url_params(channelId=channelIds, includeUndeployed = includeUndeployed, includeMetadataId=includeMetadataId, excludeMetaDataId=excludeMetaDataId, aggregateStats=aggregateStats)
        
        stats = self._get("channels/statistics{}".format(encParam))

        return ChannelStatisticsList(stats.content)
    
    def getChannelStatistic(self, channelId):
        r"""Get channel statistics for specified channel.
            
            :param channelIds: ids of the channels to retrieve. If blank, all channels will be retrieved.
            :return: :class:`ChannelStatistics <ChannelStatistics>` object
            :rtype: ChannelStatistics
            """
        stats = self._get("channels/{}/statistics".format(channelId))

        return ChannelStatistics(stats.content)
    #endregion