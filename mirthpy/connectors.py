from typing import Type
from .filters import Filter
from .linkedHashMap import LinkedHashMap
from .transformers import Transformer
from .mirthElement import MirthElement

class Connector(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)
        
        self.metaDataId = self.getSafeText('metaDataId')
        self.name = self.getSafeText('name')

        if self.root.find('properties') is not None:
            prop = Mapping.connectorProperties(self.root.find('properties').attrib['class'])
        
            self.properties = prop(self.root.find('properties'))

        self.transformer = Transformer(self.root.find('transformer'))
        self.filter = Filter(self.root.find('filter'))

        self.transportName = self.getSafeText('transportName')
        self.mode = self.getSafeText('mode')
        self.enabled = self.getSafeText('enabled')
        self.waitForPrevious = self.getSafeText('waitForPrevious')

class ConnectorProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        # for e in self.root.findall('./pluginProperties'):
        #     self.pluginProperties.append(ConnectorPluginProperties(e))
        
        #self.protocol = self.getSafeText('protocol') #TODO: get rid of this, not every property has this
        #self.name = self.getSafeText('name')         #TODO: get rid of this, not every property has this
        self.pluginProperties = []

class ConnectorPluginProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)
    
        self.name = self.getSafeText('name')

class SourceConnectorProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.responseVariable = self.getSafeText("responseVariable")
        self.respondAfterProcessing = self.getSafeText("respondAfterProcessing")
        self.processBatch = self.getSafeText("processBatch")
        self.firstResponse = self.getSafeText("firstResponse")
        self.processingThreads = self.getSafeText("processingThreads")
        self.resourceIds = LinkedHashMap(self.root.find('resourceIds'))
        self.queueBufferSize = self.getSafeText("queueBufferSize")

class DestinationConnectorProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

class ListenerConnectorProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.host = self.getSafeText('host')
        self.port = self.getSafeText('port')

class PollConnectorProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.pollingType = self.getSafeText('pollingType')
        self.pollOnStart = self.getSafeText('pollOnStart')
        self.pollingFrequency = self.getSafeText('pollingFrequency')
        self.pollingHour = self.getSafeText('pollingHour')
        self.pollingMinute = self.getSafeText('pollingMinute')
        self.cronJobs = []  #TODO: implement
        self.pollConnectorPropertiesAdvanced = PollConnectorPropertiesAdvanced(self.root.find('pollConnectorPropertiesAdvanced'))

class PollConnectorPropertiesAdvanced(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.weekly = self.getSafeText('weekly')
        self.inactiveDays = []
        self.dayOfMonth = self.getSafeText('dayOfMonth')
        self.allDay = self.getSafeText('allDay')
        self.startingHour = self.getSafeText('startingHour')
        self.startingMinute = self.getSafeText('startingMinute')
        self.endingHour = self.getSafeText('endingHour')
        self.endingMinute = self.getSafeText('endingMinute')

        # in active days
        for e in self.root.findall('./inactiveDays/boolean'):
            self.inactiveDays.append(e.text)


#region ReceiverProperties (SourceConnectorTypes)
class VmReceiverProperties(ConnectorProperties):
    def __init__(self, uXml):
        ConnectorProperties.__init__(self, uXml)

        self.sourceConnectorProperties = SourceConnectorProperties(self.root.find('sourceConnectorProperties'))

class DICOMReceiverProperties(ConnectorProperties):
    def __init__(self, uXml):
        ConnectorProperties.__init__(self, uXml)

        self.sourceConnectorProperties = SourceConnectorProperties(self.root.find('sourceConnectorProperties'))
        self.listenerConnectorProperties = ListenerConnectorProperties(self.root.find('listenerConnectorProperties'))
        self.soCloseDelay =  self.getSafeText("soCloseDelay")
        self.releaseTo =  self.getSafeText("releaseTo")
        self.requestTo = self.getSafeText("requestTo")
        self.idleTo =  self.getSafeText("idleTo") 
        self.reaper =  self.getSafeText("reaper")
        self.rspDelay =  self.getSafeText("rspDelay")
        self.pdv1 =  self.getSafeText("pdv1")
        self.sndpdulen =  self.getSafeText("sndpdulen")
        self.rcvpdulen =  self.getSafeText("rcvpdulen") 
        self.asyncc =  self.getSafeText("async")
        self.bigEndian = self.getSafeText("bigEndian")
        self.bufSize =  self.getSafeText("bufSize")
        self.defts =  self.getSafeText("defts")
        self.dest =  self.getSafeText("dest") 
        self.nativeData = self.getSafeText("nativeData")
        self.sorcvbuf =  self.getSafeText("sorcvbuf")
        self.sosndbuf =  self.getSafeText("sosndbuf")
        self.tcpDelay =  self.getSafeText("tcpDelay")
        self.keyPW =  self.getSafeText("keyPW")
        self.keyStore =  self.getSafeText("keyStore")
        self.keyStorePW =  self.getSafeText("keyStorePW")
        self.noClientAuth =  self.getSafeText("noClientAuth")
        self.nossl2 =  self.getSafeText("nossl2")
        self.tls =  self.getSafeText("tls")
        self.trustStore =  self.getSafeText("trustStore")
        self.trustStorePW =  self.getSafeText("trustStorePW")
        self.applicationEntity =  self.getSafeText("applicationEntity")
        self.localHost =  self.getSafeText("localHost")
        self.localPort =  self.getSafeText("localPort") 
        self.localApplicationEntity =  self.getSafeText("localApplicationEntity")

class DatabaseReceiverProperties(ConnectorProperties):
    def __init__(self, uXml):
        ConnectorProperties.__init__(self, uXml)

        self.sourceConnectorProperties = SourceConnectorProperties(self.root.find('sourceConnectorProperties'))
        self.pollConnectorProperties = PollConnectorProperties(self.root.find('pollConnectorProperties'))
        self.driver = self.getSafeText("driver")
        self.url = self.getSafeText("url")
        self.username = self.getSafeText("username")
        self.password = self.getSafeText("password")
        self.select = self.getSafeText("select")
        self.update = self.getSafeText("update")
        self.useScript = self.getSafeText("useScript")
        self.aggregateResults = self.getSafeText("aggregateResults")
        self.cacheResults = self.getSafeText("cacheResults")
        self.keepConnectionOpen = self.getSafeText("keepConnectionOpen")
        self.updateMode = self.getSafeText("updateMode")
        self.retryCount = self.getSafeText("retryCount")
        self.retryInterval = self.getSafeText("retryInterval")
        self.fetchSize = self.getSafeText("fetchSize")
        self.encoding = self.getSafeText("encoding")
        
class FileReceiverProperties(ConnectorProperties):
    def __init__(self, uXml):
        ConnectorProperties.__init__(self, uXml)

        self.sourceConnectorProperties = SourceConnectorProperties(self.root.find('sourceConnectorProperties'))
        self.pollConnectorProperties = PollConnectorProperties(self.root.find('pollConnectorProperties'))
        self.scheme = self.getSafeText("scheme")

        if self.root.find('schemeProperties') is not None:
            prop = Mapping.schemeProperties(self.root.find('schemeProperties').attrib['class'])
            
            self.properties = prop(self.root.find('schemeProperties'))

        self.host = self.getSafeText("host")
        self.fileFilter = self.getSafeText("fileFilter")
        self.regex = self.getSafeText("regex")
        self.directoryRecursion = self.getSafeText("directoryRecursion")
        self.ignoreDot = self.getSafeText("ignoreDot")
        self.anonymous = self.getSafeText("anonymous")
        self.username = self.getSafeText("username")
        self.password = self.getSafeText("password")
        self.timeout = self.getSafeText("timeout")
        self.secure = self.getSafeText("secure")
        self.passive = self.getSafeText("passive")
        self.validateConnection = self.getSafeText("validateConnection")
        self.afterProcessingAction = self.getSafeText("afterProcessingAction")
        self.moveToDirectory = self.getSafeText("moveToDirectory")
        self.moveToFileName = self.getSafeText("moveToFileName")
        self.errprReadingAction = self.getSafeText("errprReadingAction")
        self.errorResponseAction = self.getSafeText("errorResponseAction")
        self.errorMoveToDirectory = self.getSafeText("errorMoveToDirectory")
        self.errorMoveToFileName = self.getSafeText("errorMoveToFileName")
        self.checkFileAge = self.getSafeText("checkFileAge")
        self.fileAge = self.getSafeText("fileAge")
        self.fileSizeMinimum = self.getSafeText("fileSizeMinimum")
        self.fileSizeMaximum = self.getSafeText("fileSizeMaximum")
        self.ignoreFileSizeMaximum = self.getSafeText("ignoreFileSizeMaximum")
        self.sortBy = self.getSafeText("sortBy")
        self.binary = self.getSafeText("binary")
        self.charsetEncoding = self.getSafeText("charsetEncoding")
        
class HttpReceiverProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.pluginProperties = []

        if len(self.root.find('./pluginProperties').findall('./*')) > 0:
            for e in self.root.find('./pluginProperties').findall('./*'):
                prop = Mapping.httpAuthProperties(e.tag)
        
                self.pluginProperties.append(prop(e))

        self.listenerConnectorProperties = ListenerConnectorProperties(self.root.find('listenerConnectorProperties'))
        self.sourceConnectorProperties = SourceConnectorProperties(self.root.find('sourceConnectorProperties'))
        self.xmlBody = self.getSafeText('xmlBody')
        self.parseMultipart = self.getSafeText('parseMultipart')
        self.includeMetadata = self.getSafeText('includeMetadata')
        self.binaryMimeTypes = self.getSafeText('binaryMimeTypes')
        self.binaryMimeTypesRegex = self.getSafeText('binaryMimeTypesRegex')
        self.responseContentType = self.getSafeText('responseContentType')
        self.responseDataTypeBinary = self.getSafeText('responseDataTypeBinary')
        self.responseStatusCode = self.getSafeText('responseStatusCode')
        self.responseHeaders = '' #TODO: Implement
        self.responseHeadersVariable = self.getSafeText('responseHeadersVariable')
        self.useResponseHeadersVariable = self.getSafeText('useResponseHeadersVariable')
        self.charset = self.getSafeText('charset')
        self.contextPath = self.getSafeText('contextPath')
        self.staticResources = '' #TODO: Implement

class JmsReceiverProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.pluginProperties = []
        self.sourceConnectorProperties = SourceConnectorProperties(self.root.find('sourceConnectorProperties'))
        self.useJndi = self.getSafeText('useJndi')
        self.jndiProviderUrl = self.getSafeText('jndiProviderUrl')
        self.jndiInitialContextFactory = self.getSafeText('jndiInitialContextFactory')
        self.jndiConnectionFactoryName = self.getSafeText('jndiConnectionFactoryName')
        self.connectionFactoryClass = self.getSafeText('connectionFactoryClass')
        self.username = self.getSafeText('username')
        self.password = self.getSafeText('password')
        self.destinationName = self.getSafeText('destinationName')
        self.topic = self.getSafeText('topic')
        self.clientId = self.getSafeText('clientId')
        self.selector = self.getSafeText('selector')
        self.reconnectIntervalMillis = self.getSafeText('reconnectIntervalMillis')
        self.durableTopic = self.getSafeText('durableTopic')

        self.connectionProperties = []
        for e in self.root.findall('./connectionProperties/entry'):
            strings = e.findall('./string')
            self.connectionProperties.append((strings[0].text, strings[1].text))

class JavaScriptReceiverProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.pluginProperties = []
        self.sourceConnectorProperties = SourceConnectorProperties(self.root.find('sourceConnectorProperties'))
        self.pollConnectorProperties = PollConnectorProperties(self.root.find('pollConnectorProperties'))

        self.script = self.getSafeText('script')

class TcpReceiverProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.pluginProperties = []
        self.sourceConnectorProperties = SourceConnectorProperties(self.root.find('sourceConnectorProperties'))
        self.listenerConnectorProperties = ListenerConnectorProperties(self.root.find('listenerConnectorProperties'))
        
        if self.root.find('transmissionModeProperties') is not None:
            prop = Mapping.modeProperties(self.root.find('transmissionModeProperties').attrib['class'])
            self.transmissionModeProperties = prop(self.root.find('transmissionModeProperties'))

        self.serverMode = self.getSafeText('serverMode')
        self.remoteAddress = self.getSafeText('remoteAddress')
        self.remotePort = self.getSafeText('remotePort')
        self.overrideLocalBinding = self.getSafeText('overrideLocalBinding')
        self.reconnectInterval = self.getSafeText('reconnectInterval')
        self.receiveTimeout = self.getSafeText('receiveTimeout')
        self.bufferSize = self.getSafeText('bufferSize')
        self.maxConnections = self.getSafeText('maxConnections')
        self.keepConnectionOpen = self.getSafeText('keepConnectionOpen')
        self.dataTypeBinary = self.getSafeText('dataTypeBinary')
        self.charsetEncoding = self.getSafeText('charsetEncoding')
        self.respondOnNewConnection = self.getSafeText('respondOnNewConnection')
        self.responseAddress = self.getSafeText('responseAddress')
        self.responsePort = self.getSafeText('responsePort')

class WebServiceReceiverProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.pluginProperties = []

        if len(self.root.find('./pluginProperties').findall('./*')) > 0:
            for e in self.root.find('./pluginProperties').findall('./*'):
                prop = Mapping.httpAuthProperties(e.tag)
        
                self.pluginProperties.append(prop(e))

        self.sourceConnectorProperties = SourceConnectorProperties(self.root.find('sourceConnectorProperties'))
        self.listenerConnectorProperties = ListenerConnectorProperties(self.root.find('listenerConnectorProperties'))
        
        self.className = self.getSafeText('className')
        self.serviceName = self.getSafeText('serviceName')
        self.soapBinding = self.getSafeText('soapBinding')
        

#endregion

#region DispatcherProperties (DestinationConnectorTypes)
class DestinationConnector(ConnectorProperties):
    def __init__(self, uXml):
        ConnectorProperties.__init__(self, uXml)
        pluginProperties = []
        self.destinationConnectorProperties = DestinationConnectorProperties(self.root.find('destinationConnectorProperties'))

class JavaScriptDispatcherProperties(DestinationConnector):
    def __init__(self, uXml):
        DestinationConnector.__init__(self, uXml)
        self.script = self.getSafeText('script')

class DICOMDispatcherProperties(DestinationConnector):
    def __init__(self, uXml):
        DestinationConnector.__init__(self, uXml)
        self.host = self.getSafeText('host')
        self.port = self.getSafeText('port')
        self.applicationEntity = self.getSafeText('applicationEntity')
        self.localHost = self.getSafeText('localHost')
        self.localPort = self.getSafeText('localPort')
        self.localApplicationEntity = self.getSafeText('localApplicationEntity')
        self.template = self.getSafeText('template')
        self.acceptTo = self.getSafeText('acceptTo')
        self.asyncS = self.getSafeText('async') #TODO: this will mess with xml generation. figure a way to put async
        self.bufSize = self.getSafeText('bufSize')
        self.connectTo = self.getSafeText('connectTo')
        self.priority = self.getSafeText('priority')
        self.passcode = self.getSafeText('passcode')
        self.pdv1 = self.getSafeText('pdv1')
        self.rcvpdulen = self.getSafeText('rcvpdulen')
        self.reaper = self.getSafeText('reaper')
        self.releaseTo = self.getSafeText('releaseTo')
        self.rspTo = self.getSafeText('rspTo')
        self.shutdownDelay = self.getSafeText('shutdownDelay')
        self.sndpdulen = self.getSafeText('sndpdulen')
        self.soCloseDelay = self.getSafeText('soCloseDelay')
        self.sorcvbuf = self.getSafeText('sorcvbuf')
        self.sosndbuf = self.getSafeText('sosndbuf')
        self.stgcmt = self.getSafeText('stgcmt')
        self.tcpDelay = self.getSafeText('tcpDelay')
        self.ts1 = self.getSafeText('ts1')
        self.uidnegrsp = self.getSafeText('uidnegrsp')
        self.username = self.getSafeText('username')
        self.keyPW = self.getSafeText('keyPW')
        self.keyStore = self.getSafeText('keyStore')
        self.keyStorePW = self.getSafeText('keyStorePW')
        self.noClientAuth = self.getSafeText('noClientAuth')
        self.nossl2 = self.getSafeText('nossl2')
        self.tls = self.getSafeText('tls')
        self.trustStore = self.getSafeText('trustStore')
        self.trustStorePW = self.getSafeText('trustStorePW')

class WebServiceDispatcherProperties(ConnectorProperties):
    def __init__(self, uXml):
        ConnectorProperties.__init__(self, uXml)
        self.wsdlUrl = self.getSafeText('wsdlUrl')
        self.service = self.getSafeText('service')
        self.port = self.getSafeText('port')
        self.operation = self.getSafeText('operation')
        self.locationURI = self.getSafeText('locationURI')
        self.socketTimeout = self.getSafeText('socketTimeout')
        self.useAuthentication = self.getSafeText('useAuthentication')
        self.username = self.getSafeText('username')
        self.password = self.getSafeText('password')
        self.envelope = self.getSafeText('envelope')
        self.oneWay = self.getSafeText('oneWay')
        self.headers = ''#TODO: Implement
        self.headersVariable = self.getSafeText('headersVariable')
        self.isUseHeadersVariable = self.getSafeText('isUseHeadersVariable')
        self.useMtom = self.getSafeText('useMtom')
        self.attachmentNames = []
        self.attachmentContents = []
        self.attachmentTypes = []
        self.attachmentsVariable = self.getSafeText('attachmentsVariable')
        self.isUseAttachmentsVariable = self.getSafeText('isUseAttachmentsVariable')
        self.soapAction = self.getSafeText('soapAction')
        self.wsdlDefinitionMap = Map(self.root.find('wsdlDefinitionMap'))

class Map(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)
        self.map = LinkedHashMap(self.root.find('map'))

class VmDispatcherProperties(ConnectorProperties):
    def __init__(self, uXml):
        ConnectorProperties.__init__(self, uXml)
        self.channelId = self.getSafeText('channelId')
        self.channelTemplate = self.getSafeText('channelTemplate')
        self.mapVariables = []

        for e in self.root.findall('./mapVariables/string'):
            self.mapVariables.append(e.text)

class DestinationConnectorProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)
        
        self.queueEnabled = self.getSafeText('queueEnabled')
        self.sendFirst = self.getSafeText('sendFirst')
        self.retryIntervalMillis = self.getSafeText('retryIntervalMillis')
        self.regenerateTemplate = self.getSafeText('regenerateTemplate')
        self.retryCount = self.getSafeText('retryCount')
        self.rotate = self.getSafeText('rotate')
        self.includeFilterTransformer = self.getSafeText('includeFilterTransformer')
        self.threadCount = self.getSafeText('threadCount')
        self.threadAssignmentVariable = self.getSafeText('threadAssignmentVariable')
        self.validateResponse = self.getSafeText('validateResponse')
        self.resourceIds = LinkedHashMap(self.root.find('resourceIds'))
        self.queueBufferSize = self.getSafeText('queueBufferSize')
        self.reattachAttachments = self.getSafeText('reattachAttachments')


#endregion

#region HttpAuthProperties
class BasicHttpAuthProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.authType = self.getSafeText('authType')
        self.realm = self.getSafeText('realm')
        self.credentials = []
        for e in self.root.findall('./credentials/entry'):
            strings = e.findall('./string')
            self.credentials.append((strings[0].text, strings[1].text))

        self.isUseCredentialsVariable = self.getSafeText('isUseCredentialsVariable')
        self.credentialsVariable = self.getSafeText('credentialsVariable')

class DigestHttpAuthProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.authType = self.getSafeText('authType')
        self.realm = self.getSafeText('realm')
        self.credentials = []
        for e in self.root.findall('./credentials/entry'):
            strings = e.findall('./string')
            self.credentials.append((strings[0].text, strings[1].text))

        self.isUseCredentialsVariable = self.getSafeText('isUseCredentialsVariable')
        self.credentialsVariable = self.getSafeText('credentialsVariable')
        self.qopModes = self.root.find('qopModes')
        self.opaque = self.getSafeText('opaque')
        self.algorithm = self.root.find('algorithms')

class JavaScriptHttpAuthProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.authType = self.getSafeText('authType')
        self.script = self.getSafeText('script')

class CustomHttpAuthProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.authType = self.getSafeText('authType')
        self.authenticatorClass = self.getSafeText('authenticatorClass')

        self.properties = []
        for e in self.root.findall('./properties/entry'):
            strings = e.findall('./string')
            self.properties.append((strings[0].text, strings[1].text))

class OAuth2HttpAuthProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.authType = self.getSafeText('authType')
        self.tokenLocation = self.getSafeText('tokenLocation')
        self.locationKey = self.getSafeText('locationKey')
        self.verificationURL = self.getSafeText('verificationURL')

class NoneHttpAuthProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.authType = self.getSafeText('authType')
#endregion

#region SchemeProperties
class SchemeProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

class SftpSchemeProperties(SchemeProperties):
    def __init__(self, uXml):
        SchemeProperties.__init__(self, uXml)

        self.passwordAuth = self.getSafeText('passwordAuth')
        self.keyAuth = self.getSafeText('keyAuth')
        self.keyFile = self.getSafeText('keyFile')
        self.passPhrase = self.getSafeText('passPhrase')
        self.hostKeyChecking = self.getSafeText('hostKeyChecking')
        self.knownHostsFile = self.getSafeText('knownHostsFile')
        self.configurationSettings = []

        for e in self.root.findall('./configurationSettings/entry'):
            strings = e.findall('./string')
            self.configurationSettings.append((strings[0].text, strings[1].text))
        
class FTPSchemeProperties(SchemeProperties):
    def __init__(self, uXml):
        SchemeProperties.__init__(self, uXml)

        self.initalCommands = []

        for e in self.root.findall('./initialCommands/string'):
            self.initalCommands.append(e.text)
        
class S3SchemeProperties(SchemeProperties):
    def __init__(self, uXml):
        SchemeProperties.__init__(self, uXml)

        self.useDefaultCredentialProviderChain = self.getSafeText('useDefaultCredentialProviderChain')
        self.useTemporaryCredentials = self.getSafeText('useTemporaryCredentials')
        self.duration = self.getSafeText('useTemporaryCredentials')
        self.region = self.getSafeText('useTemporaryCredentials')
        self.customerHeaders = []   # TODO: implement

class SmbSchemeProperties(SchemeProperties):
    def __init__(self, uXml):
        SchemeProperties.__init__(self, uXml)

        self.smbMinVersion = self.getSafeText('smbMinVersion')
        self.smbMaxVersion = self.getSafeText('smbMaxVersion')
#endregion

#region ModeProperties
class MLLPModeProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.pluginPointName = self.getSafeText('pluginPointName')
        self.startOfMessageBytes = self.getSafeText('startOfMessageBytes')
        self.endOfMessageBytes = self.getSafeText('endOfMessageBytes')
        self.useMLLPv2 = self.getSafeText('useMLLPv2')
        self.ackBytes = self.getSafeText('ackBytes')
        self.nackBytes = self.getSafeText('nackBytes')
        self.maxRetries = self.getSafeText('maxRetries')

class FrameModeProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.pluginPointName = self.getSafeText('pluginPointName')
        self.startOfMessageBytes = self.getSafeText('startOfMessageBytes')
        self.endOfMessageBytes = self.getSafeText('endOfMessageBytes')
#endregion

#region Mapping
class Mapping():   
    def connectorProperties(c: str) -> Type:
        if c == "com.mirth.connect.connectors.vm.VmReceiverProperties":
            return VmReceiverProperties
        elif c == "com.mirth.connect.connectors.dimse.DICOMReceiverProperties":
            return DICOMReceiverProperties
        elif c == "com.mirth.connect.connectors.jdbc.DatabaseReceiverProperties":
            return DatabaseReceiverProperties
        elif c == "com.mirth.connect.connectors.file.FileReceiverProperties":
            return FileReceiverProperties
        elif c == "com.mirth.connect.connectors.http.HttpReceiverProperties":
            return HttpReceiverProperties
        elif c == "com.mirth.connect.connectors.jms.JmsReceiverProperties":
            return JmsReceiverProperties
        elif c == "com.mirth.connect.connectors.js.JavaScriptReceiverProperties":
            return JavaScriptReceiverProperties
        elif c == "com.mirth.connect.connectors.tcp.TcpReceiverProperties":
            return TcpReceiverProperties
        elif c == "com.mirth.connect.connectors.ws.WebServiceReceiverProperties":
            return WebServiceReceiverProperties
        elif c == "com.mirth.connect.connectors.js.JavaScriptDispatcherProperties":
            return JavaScriptDispatcherProperties
        elif c == "com.mirth.connect.connectors.vm.VmDispatcherProperties":
            return VmDispatcherProperties
        elif c == "com.mirth.connect.connectors.dimse.DICOMDispatcherProperties":
            return DICOMDispatcherProperties
        else:
            return ConnectorProperties
    
    def schemeProperties(c: str) -> Type:
        if c == "com.mirth.connect.connectors.file.SftpSchemeProperties":
            return SftpSchemeProperties
        elif c == "com.mirth.connect.connectors.file.FTPSchemeProperties":
            return FTPSchemeProperties
        elif c == "com.mirth.connect.connectors.file.S3SchemeProperties":
            return S3SchemeProperties    
        elif c == "com.mirth.connect.connectors.file.SmbSchemeProperties":
            return SmbSchemeProperties
    
    def httpAuthProperties(c: str) -> Type:
        if c == "com.mirth.connect.plugins.httpauth.basic.BasicHttpAuthProperties":
            return BasicHttpAuthProperties
        elif c == "com.mirth.connect.plugins.httpauth.digest.DigestHttpAuthProperties":
            return DigestHttpAuthProperties
        elif c == "com.mirth.connect.plugins.httpauth.javascript.JavaScriptHttpAuthProperties":
            return JavaScriptHttpAuthProperties
        elif c == "com.mirth.connect.plugins.httpauth.custom.CustomHttpAuthProperties":
            return CustomHttpAuthProperties
        elif c == "com.mirth.connect.plugins.httpauth.oauth2.OAuth2HttpAuthProperties":
            return OAuth2HttpAuthProperties
        elif c == "com.mirth.connect.plugins.httpauth.NoneHttpAuthProperties":
            return NoneHttpAuthProperties
    
    def modeProperties(c: str) -> Type:
        if c == "com.mirth.connect.plugins.mllpmode.MLLPModeProperties":
            return MLLPModeProperties
        elif c == "com.mirth.connect.model.transmission.framemode.FrameModeProperties":
            return FrameModeProperties

#endregion