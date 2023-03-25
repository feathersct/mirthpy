from typing import Type

from .linkedHashMap import Entry, LinkedHashMap
from .utilities import escape, getXMLString
from .filters import Filter
from .transformers import Transformer
from .mirthElement import MirthElement

class Connector(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        
        self.metaDataId = ''
        self.name = ''
        self.transformer = Transformer()
        self.filter = Filter()
        self.enabled = 'true'
        self.waitForPrevious = 'true'
        
        if uXml is not None:
            self.metaDataId = self.getSafeText('metaDataId')
            self.name = self.getSafeText('name')
            self.transformer = Transformer(self.root.find('transformer'))
            self.filter = Filter(self.root.find('filter'))

            self.transportName = self.getSafeText('transportName')
            self.mode = self.getSafeText('mode')
            self.enabled = self.getSafeText('enabled')
            self.waitForPrevious = self.getSafeText('waitForPrevious')

    def getXML(self, version = '3.12.0'):
        respTransXML = ""
        if self.responseTransformer is not None:
            respTransXML += f'<responseTransformer version="{version}">'
            respTransXML += self.responseTransformer.getXML(version)
            respTransXML += '</responseTransformer>'

        xml = f'''
            {getXMLString(self.metaDataId, "metaDataId")}
            {getXMLString(self.name, "name")}
            <properties class="{self.properties.className}" version="{version}">
                {self.properties.getXML(version)}
            </properties>
            <transformer version="{version}">
                {self.transformer.getXML(version)}
            </transformer>
            {respTransXML}
            <filter version="{version}">
                {self.filter.getXML(version)}
            </filter>
            {getXMLString(self.transportName, "transportName")}
            {getXMLString(self.mode, "mode")}
            {getXMLString(self.enabled, "enabled")}
            {getXMLString(self.waitForPrevious, "waitForPrevious")}'''

        return xml

class SourceConnector(Connector):
    def __init__(self, uXml = None):
        Connector.__init__(self, uXml)

        self.metaDataId = '0'
        self.name = 'sourceConnector'
        self.properties = VmReceiverProperties()
        self.mode = 'SOURCE'

        if uXml is not None:
            if self.root.find('properties') is not None:
                prop = Mapping.connectorProperties(self.root.find('properties').attrib['class'])
            
                self.properties = prop(self.root.find('properties'))
    
    def getXML(self, version = '3.12.0'):
        xml = f'''
            {getXMLString(self.metaDataId, "metaDataId")}
            {getXMLString(self.name, "name")}
            <properties class="{self.properties.className}" version="{version}">
                {self.properties.getXML(version)}
            </properties>
            <transformer version="{version}">
                {self.transformer.getXML(version)}
            </transformer>
            <filter version="{version}">
                {self.filter.getXML(version)}
            </filter>
            {getXMLString(self.properties.transportName, "transportName")}
            {getXMLString(self.mode, "mode")}
            {getXMLString(self.enabled, "enabled")}
            {getXMLString(self.waitForPrevious, "waitForPrevious")}'''

        return xml

class DestinationConnectorElement(Connector):
    def __init__(self, uXml = None):
        Connector.__init__(self, uXml)

        self.name = 'Destination 1'
        self.properties = VmDispatcherProperties()
        self.responseTransformer = Transformer()
        self.mode = 'DESTINATION'

        if uXml is not None:
            self.name = self.getSafeText('name')
            self.responseTransformer = Transformer(self.root.find('responseTransformer'))

            if self.root.find('properties') is not None:
                prop = Mapping.connectorProperties(self.root.find('properties').attrib['class'])
            
                self.properties = prop(self.root.find('properties'))

    def getXML(self, version = '3.12.0'):
        xml = f'''
            {getXMLString(self.metaDataId, "metaDataId")}
            {getXMLString(self.name, "name")}
            <properties class="{self.properties.className}" version="{version}">
                {self.properties.getXML(version)}
            </properties>
            <transformer version="{version}">
                {self.transformer.getXML(version)}
            </transformer>
            <responseTransformer version="{version}">
                {self.responseTransformer.getXML(version)}
            </responseTransformer>
            <filter version="{version}">
                {self.filter.getXML(version)}
            </filter>
            {getXMLString(self.properties.transportName, "transportName")}
            {getXMLString(self.mode, "mode")}
            {getXMLString(self.enabled, "enabled")}
            {getXMLString(self.waitForPrevious, "waitForPrevious")}'''

        return xml

class ConnectorProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)

        self.pluginProperties = []

class ConnectorPluginProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
    
        self.name = self.getSafeText('name')

class SourceConnectorProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)

        self.responseVariable = 'None'
        self.respondAfterProcessing = 'true'
        self.processBatch = 'false'
        self.firstResponse = 'false'
        self.processingThreads = '1'
        self.queueBufferSize = '1000'
        self.resourceIds = LinkedHashMap()

        entry = Entry()
        entry.string.append('Default Resource')
        entry.string.append('[Default Resource]')

        self.resourceIds.entry.append(entry)

        if uXml is not None:
            self.responseVariable = self.getSafeText("responseVariable")
            self.respondAfterProcessing = self.getSafeText("respondAfterProcessing")
            self.processBatch = self.getSafeText("processBatch")
            self.firstResponse = self.getSafeText("firstResponse")
            self.processingThreads = self.getSafeText("processingThreads")
            self.resourceIds = LinkedHashMap(self.root.find('resourceIds'))
            self.queueBufferSize = self.getSafeText("queueBufferSize")

    def getXML(self, version = '3.12.0'):
        xml = f'''{getXMLString(self.responseVariable, "responseVariable")}
                {getXMLString(self.respondAfterProcessing, "respondAfterProcessing")}
                {getXMLString(self.processBatch, "processBatch")}
                {getXMLString(self.firstResponse, "firstResponse")}
                {getXMLString(self.processingThreads, "processingThreads")}
                <resourceIds class="linked-hash-map">
                    {self.resourceIds.getXML(version)}
                </resourceIds>
                {getXMLString(self.queueBufferSize, "queueBufferSize")}'''
        return xml

class ListenerConnectorProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.host = '0.0.0.0'
        self.port = '80'

        if uXml is not None:
            self.host = self.getSafeText('host')
            self.port = self.getSafeText('port')

    def getXML(self, version = '3.12.0'):
        return f'''
            <host>{self.host}</host>
            <port>{self.port}</port>'''

class PollConnectorProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        
        self.cronJobs = [] 
        self.pollingType = 'INTERVAL'
        self.pollOnStart = 'false'
        self.pollingFrequency = '23000'
        self.pollingHour = '0'
        self.pollingMinute = '0'
        self.pollConnectorPropertiesAdvanced = PollConnectorPropertiesAdvanced()

        if uXml is not None:
            self.pollingType = self.getSafeText('pollingType')
            self.pollOnStart = self.getSafeText('pollOnStart')
            self.pollingFrequency = self.getSafeText('pollingFrequency')
            self.pollingHour = self.getSafeText('pollingHour')
            self.pollingMinute = self.getSafeText('pollingMinute')
            self.pollConnectorPropertiesAdvanced = PollConnectorPropertiesAdvanced(self.root.find('pollConnectorPropertiesAdvanced'))

    def getXML(self, version = '3.12.0'):
        xml = f'''
        {getXMLString(self.pollingType, "pollingType")}
        {getXMLString(self.pollOnStart, "pollOnStart")}
        {getXMLString(self.pollingFrequency, "pollingFrequency")}
        {getXMLString(self.pollingHour, "pollingHour")}
        {getXMLString(self.pollingMinute, "pollingMinute")}
        <cronJobs/>
        {getXMLString(self.pollConnectorPropertiesAdvanced.getXML(version), "pollConnectorPropertiesAdvanced")}
        '''
        return xml

class PollConnectorPropertiesAdvanced(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)

        self.inactiveDays = [False, False, False, False, False, False, False, False]
        self.weekly = 'true'
        self.dayOfMonth = '1'
        self.allDay = 'true'
        self.startingHour = '8'
        self.startingMinute = '0'
        self.endingHour = '17'
        self.endingMinute = '0'

        if uXml is not None:
            self.weekly = self.getSafeText('weekly')
            self.dayOfMonth = self.getSafeText('dayOfMonth')
            self.allDay = self.getSafeText('allDay')
            self.startingHour = self.getSafeText('startingHour')
            self.startingMinute = self.getSafeText('startingMinute')
            self.endingHour = self.getSafeText('endingHour')
            self.endingMinute = self.getSafeText('endingMinute')

            # inactive days
            self.inactiveDays = []
            for e in self.root.findall('./inactiveDays/boolean'):
                self.inactiveDays.append(e.text=='true')

    def getXML(self, version = "3.12.0"):
        xml = f'''
            {getXMLString(self.weekly, "weekly")}
            <inactiveDays>
            '''

        for b in self.inactiveDays:
            xml += f'''{getXMLString(str(b).lower(), "boolean")}'''

        xml += f'''
            </inactiveDays>
            {getXMLString(self.dayOfMonth, "dayOfMonth")}
            {getXMLString(self.allDay, "allDay")}
            {getXMLString(self.startingHour, "startingHour")}
            {getXMLString(self.startingMinute, "startingMinute")}
            {getXMLString(self.endingHour, "endingHour")}
            {getXMLString(self.endingMinute, "endingMinute")}
        '''
        return xml


#region ReceiverProperties (SourceConnectorTypes)
class VmReceiverProperties(ConnectorProperties):
    def __init__(self, uXml = None):
        ConnectorProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.vm.VmReceiverProperties'
        self.transportName = 'Channel Reader'

        self.sourceConnectorProperties = SourceConnectorProperties(self.root.find('sourceConnectorProperties'))

    def getXML(self, version = '3.12.0'):
        xml = f'''<pluginProperties/>
        <sourceConnectorProperties version="{version}">
            {self.sourceConnectorProperties.getXML(version)}
        </sourceConnectorProperties>'''
        return xml

class DICOMReceiverProperties(ConnectorProperties):
    def __init__(self, uXml = None):
        ConnectorProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.dimse.DICOMReceiverProperties'
        self.transportName = 'DICOM Listener'

        self.sourceConnectorProperties = SourceConnectorProperties()
        self.listenerConnectorProperties = ListenerConnectorProperties()
        self.soCloseDelay =  '50'
        self.releaseTo =  '5'
        self.requestTo = '5'
        self.idleTo =  '60'
        self.reaper =  '10'
        self.rspDelay =  '0'
        self.pdv1 =  'false'
        self.sndpdulen =  '16'
        self.rcvpdulen =  '16' 
        self.asyncc =  '0'
        self.bigEndian = 'false'
        self.bufSize =  '1'
        self.defts =  'false'
        self.dest =  ''
        self.nativeData = 'false'
        self.sorcvbuf =  '0'
        self.sosndbuf =  '0'
        self.tcpDelay =  'true'
        self.keyPW = ''
        self.keyStore = ''
        self.keyStorePW = ''
        self.noClientAuth =  'true'
        self.nossl2 =  'true'
        self.tls = 'notls'
        self.trustStore =  ''
        self.trustStorePW = ''
        self.applicationEntity = ''
        self.localHost = ''
        self.localPort = ''
        self.localApplicationEntity = ''

        if uXml is not None:
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

    def getXML(self, version = '3.12.0'):
        xml = f'''<pluginProperties/>
         <listenerConnectorProperties version="{version}">
            {self.listenerConnectorProperties.getXML(version)}
        </listenerConnectorProperties>
        <sourceConnectorProperties version="{version}">
            {self.sourceConnectorProperties.getXML(version)}
        </sourceConnectorProperties>
        {getXMLString(self.applicationEntity, "applicationEntity")}
        {getXMLString(self.localHost, "localHost")}
        {getXMLString(self.localPort, "localPort")}
        {getXMLString(self.localApplicationEntity, "localApplicationEntity")}
        {getXMLString(self.soCloseDelay, "soCloseDelay")}
        {getXMLString(self.releaseTo, "releaseTo")}
        {getXMLString(self.requestTo, "requestTo")}
        {getXMLString(self.idleTo, "idleTo")}
        {getXMLString(self.reaper, "reaper")}
        {getXMLString(self.rspDelay, "rspDelay")}
        {getXMLString(self.pdv1, "pdv1")}
        {getXMLString(self.sndpdulen, "sndpdulen")}
        {getXMLString(self.rcvpdulen, "rcvpdulen")}
        {getXMLString(self.asyncc, "async")}
        {getXMLString(self.bigEndian, "bigEndian")}
        {getXMLString(self.bufSize, "bufSize")}
        {getXMLString(self.defts, "defts")}
        {getXMLString(self.dest, "dest")}
        {getXMLString(self.nativeData, "nativeData")}
        {getXMLString(self.sorcvbuf, "sorcvbuf")}
        {getXMLString(self.sosndbuf, "sosndbuf")}
        {getXMLString(self.tcpDelay, "tcpDelay")}
        {getXMLString(self.keyPW, "keyPW")}
        {getXMLString(self.keyStore, "keyStore")}
        {getXMLString(self.keyStorePW, "keyStorePW")}
        {getXMLString(self.noClientAuth, "noClientAuth")}
        {getXMLString(self.nossl2, "nossl2")}
        {getXMLString(self.tls, "tls")}
        {getXMLString(self.trustStore, "trustStore")}
        {getXMLString(self.trustStorePW, "trustStorePW")}'''
        return xml

class DatabaseReceiverProperties(ConnectorProperties):
    def __init__(self, uXml = None):
        ConnectorProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.jdbc.DatabaseReceiverProperties'
        self.transportName = 'Database Reader'

        self.sourceConnectorProperties = SourceConnectorProperties()
        self.pollConnectorProperties = PollConnectorProperties()
        self.driver = ''
        self.url = ''
        self.username = ''
        self.password = ''
        self.select = ''
        self.update = ''
        self.useScript = 'false'
        self.aggregateResults = 'false'
        self.cacheResults = 'true'
        self.keepConnectionOpen = 'true'
        self.updateMode = '1'
        self.retryCount = '3'
        self.retryInterval = '10000'
        self.fetchSize = '100'
        self.encoding = 'DEFAULT_ENCODING'

        if uXml is not None:
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

    def getXML(self, version = '3.12.0'):
        xml = f'''<pluginProperties/>
         <pollConnectorProperties version="{version}">
            {self.pollConnectorProperties.getXML(version)}
        </pollConnectorProperties>
        <sourceConnectorProperties version="{version}">
            {self.sourceConnectorProperties.getXML(version)}
        </sourceConnectorProperties>
        {getXMLString(self.driver, "driver")}
        {getXMLString(self.url, "url")}
        {getXMLString(self.username, "username")}
        {getXMLString(self.password, "password")}
        {getXMLString(escape(self.select), "select")}
        {getXMLString(escape(self.update), "update")}
        {getXMLString(self.useScript, "useScript")}
        {getXMLString(self.aggregateResults, "aggregateResults")}
        {getXMLString(self.cacheResults, "cacheResults")}
        {getXMLString(self.keepConnectionOpen, "keepConnectionOpen")}
        {getXMLString(self.updateMode, "updateMode")}
        {getXMLString(self.retryCount, "retryCount")}
        {getXMLString(self.retryInterval, "retryInterval")}
        {getXMLString(self.fetchSize, "fetchSize")}
        {getXMLString(self.encoding, "encoding")}'''
        return xml
      
class FileReceiverProperties(ConnectorProperties):
    def __init__(self, uXml = None):
        ConnectorProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.file.FileReceiverProperties'
        self.transportName = 'File Reader'

        self.sourceConnectorProperties = SourceConnectorProperties()
        self.pollConnectorProperties = PollConnectorProperties()
        self.scheme = 'FILE'
        self.schemeProperties = None

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
        self.errprReadingAction = self.getSafeText("errorReadingAction")
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

        if uXml is not None:
            self.sourceConnectorProperties = SourceConnectorProperties(self.root.find('sourceConnectorProperties'))
            self.pollConnectorProperties = PollConnectorProperties(self.root.find('pollConnectorProperties'))
            self.scheme = self.getSafeText("scheme")
            self.schemeProperties = None

            if self.root.find('schemeProperties') is not None:
                prop = Mapping.schemeProperties(self.root.find('schemeProperties').attrib['class'])
                
                self.schemeProperties = prop(self.root.find('schemeProperties'))

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
            self.errprReadingAction = self.getSafeText("errorReadingAction")
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

    def getXML(self, version = "3.12.0"):
        schemPropXML = ""

        if self.schemeProperties is not None:
            schemPropXML = f'<schemeProperties class="{self.schemeProperties.className}">'
            schemPropXML += self.schemeProperties.getXML(version)
            schemPropXML += '</schemeProperties>'

        xml = f'''
            <pluginProperties/>
            <pollConnectorProperties version="{version}">
                {self.pollConnectorProperties.getXML(version)}
            </pollConnectorProperties>
            <sourceConnectorProperties version="{version}">
                {self.sourceConnectorProperties.getXML(version)}
            </sourceConnectorProperties>
            {getXMLString(self.scheme, "scheme")}
            {schemPropXML}
            {getXMLString(self.host, "host")}
            {getXMLString(self.fileFilter, "fileFilter")}
            {getXMLString(self.regex, "regex")}
            {getXMLString(self.directoryRecursion, "directoryRecursion")}
            {getXMLString(self.ignoreDot, "ignoreDot")}
            {getXMLString(self.anonymous, "anonymous")}
            {getXMLString(self.username, "username")}
            {getXMLString(self.password, "password")}
            {getXMLString(self.timeout, "timeout")}
            {getXMLString(self.secure, "secure")}
            {getXMLString(self.passive, "passive")}
            {getXMLString(self.validateConnection, "validateConnection")}
            {getXMLString(self.afterProcessingAction, "afterProcessingAction")}
            {getXMLString(self.moveToDirectory, "moveToDirectory")}
            {getXMLString(self.moveToFileName, "moveToFileName")}
            {getXMLString(self.errprReadingAction, "errorReadingAction")}
            {getXMLString(self.errorResponseAction, "errorResponseAction")}
            {getXMLString(self.errorMoveToDirectory, "errorMoveToDirectory")}
            {getXMLString(self.errorMoveToFileName, "errorMoveToFileName")}
            {getXMLString(self.checkFileAge, "checkFileAge")}
            {getXMLString(self.fileAge, "fileAge")}
            {getXMLString(self.fileSizeMinimum, "fileSizeMinimum")}
            {getXMLString(self.fileSizeMaximum, "fileSizeMaximum")}
            {getXMLString(self.ignoreFileSizeMaximum, "ignoreFileSizeMaximum")}
            {getXMLString(self.sortBy, "sortBy")}
            {getXMLString(self.binary, "binary")}
            {getXMLString(self.charsetEncoding, "charsetEncoding")}
        '''
        return xml
        
class HttpReceiverProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)

        self.className = 'com.mirth.connect.connectors.http.HttpReceiverProperties'
        self.transportName = 'HTTP Listener'

        self.pluginProperties = []
        self.listenerConnectorProperties = ListenerConnectorProperties()
        self.sourceConnectorProperties = SourceConnectorProperties()
        self.xmlBody = ''
        self.parseMultipart = ''
        self.includeMetadata = ''
        self.binaryMimeTypes = ''
        self.binaryMimeTypesRegex = ''
        self.responseContentType = ''
        self.responseDataTypeBinary = ''
        self.responseStatusCode = ''
        self.responseHeaders = LinkedHashMap()
        self.responseHeadersVariable = ''
        self.useResponseHeadersVariable = ''
        self.charset = ''
        self.contextPath = ''
        self.timeout = '3000'
        self.staticResources = [] 

        if uXml is not None:
            if len(self.root.find('./pluginProperties').findall('./*')) > 0:
                for e in self.root.find('./pluginProperties').findall('./*'):
                    prop = Mapping.httpAuthProperties(e.tag)

                    if prop is not None:
                        self.pluginProperties.append(prop(e))
            
            if len(self.root.findall('./staticResources/com.mirth.connect.connectors.http.HttpStaticResource')):
                for e in self.root.findall('./staticResources/com.mirth.connect.connectors.http.HttpStaticResource'):
                    prop = Mapping.staticResources(e.tag)

                    if prop is not None:
                        self.staticResources.append(prop(e))

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
            self.responseHeaders = LinkedHashMap(self.root.find('responseHeaders'))
            self.responseHeadersVariable = self.getSafeText('responseHeadersVariable')
            self.useResponseHeadersVariable = self.getSafeText('useResponseHeadersVariable')
            self.charset = self.getSafeText('charset')
            self.contextPath = self.getSafeText('contextPath')
            self.timeout = self.getSafeText('timeout')
    
    def getXML(self, version="3.12.0"):
        pluginPropXML = '''<pluginProperties/>'''
        if len(self.pluginProperties) > 0:
            pluginPropXML = '''<pluginProperties>'''
            for p in self.pluginProperties:
                pluginPropXML += f'''<{p.className} version="{version}">'''
                pluginPropXML += f'''{p.getXML(version)}'''
                pluginPropXML += f'''</{p.className}>'''
            pluginPropXML += '''</pluginProperties>'''

        staticResXML = '''<staticResources/>'''
        if len(self.staticResources) > 0:
            staticResXML = '''<staticResources>'''
            for p in self.staticResources:
                staticResXML += f'''<{p.className}>'''
                staticResXML += f'''{p.getXML(version)}'''
                staticResXML += f'''</{p.className}>'''
            staticResXML += '''</staticResources>'''


        return f'''{pluginPropXML}
                <listenerConnectorProperties version="3.12.0">
                    {self.listenerConnectorProperties.getXML(version)}
                </listenerConnectorProperties>
                <sourceConnectorProperties version="3.12.0">
                    {self.sourceConnectorProperties.getXML(version)}
                </sourceConnectorProperties>
                {getXMLString(self.xmlBody, "xmlBody")}
                {getXMLString(self.parseMultipart, "parseMultipart")}
                {getXMLString(self.includeMetadata, "includeMetadata")}
                {getXMLString(escape(self.binaryMimeTypes), "binaryMimeTypes")}
                {getXMLString(self.binaryMimeTypesRegex, "binaryMimeTypesRegex")}
                {getXMLString(self.responseContentType, "responseContentType")}
                {getXMLString(self.responseDataTypeBinary, "responseDataTypeBinary")}
                {getXMLString(self.responseStatusCode, "responseStatusCode")}
                <responseHeaders class="linked-hash-map">
                    {self.responseHeaders.getXML(version)}
                </responseHeaders>
                {getXMLString(self.responseHeadersVariable, "responseHeadersVariable")}
                {getXMLString(self.useResponseHeadersVariable, "useResponseHeadersVariable")}
                {getXMLString(self.charset, "charset")}
                {getXMLString(self.contextPath, "contextPath")}
                {getXMLString(self.timeout, "timeout")}
                {staticResXML}'''

class JmsReceiverProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.jms.JmsReceiverProperties'
        self.transportName = 'JMS Listener'

        self.pluginProperties = []
        self.sourceConnectorProperties = SourceConnectorProperties()
        self.useJndi = 'false'
        self.jndiProviderUrl = ''
        self.jndiInitialContextFactory = ''
        self.jndiConnectionFactoryName = ''
        self.connectionFactoryClass = ''
        self.username = ''
        self.password = ''
        self.destinationName = ''
        self.topic = ''
        self.clientId = ''
        self.selector = ''
        self.reconnectIntervalMillis = ''
        self.durableTopic = ''

        self.connectionProperties = LinkedHashMap()

        if uXml is not None:
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

            self.connectionProperties = LinkedHashMap(self.root.find('connectionProperties'))
            # self.connectionProperties = []
            # for e in self.root.findall('./connectionProperties/entry'):
            #     strings = e.findall('./string')
            #     self.connectionProperties.append((strings[0].text, strings[1].text))
    
    def getXML(self, version = '3.12.0'):
        xml = f'''
            <pluginProperties/>
            {getXMLString(self.useJndi, "useJndi")}
            {getXMLString(self.jndiProviderUrl, "jndiProviderUrl")}
            {getXMLString(self.jndiInitialContextFactory, "jndiInitialContextFactory")}
            {getXMLString(self.jndiConnectionFactoryName, "jndiConnectionFactoryName")}
            {getXMLString(self.connectionFactoryClass, "connectionFactoryClass")}
            <connectionProperties class="linked-hash-map">
                {self.connectionProperties.getXML(version)}
            </connectionProperties>
            {getXMLString(self.username, "username")}
            {getXMLString(self.password, "password")}
            {getXMLString(self.destinationName, "destinationName")}
            {getXMLString(self.topic, "topic")}
            {getXMLString(self.clientId, "clientId")}
            <sourceConnectorProperties version="{version}">
                {self.sourceConnectorProperties.getXML(version)}
            </sourceConnectorProperties>
            {getXMLString(self.selector, "selector")}
            {getXMLString(self.reconnectIntervalMillis, "reconnectIntervalMillis")}
            {getXMLString(self.durableTopic, "durableTopic")}'''
        return xml
    
class JavaScriptReceiverProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.js.JavaScriptReceiverProperties'
        self.transportName = 'JavaScript Reader'

        self.pluginProperties = []
        self.sourceConnectorProperties = SourceConnectorProperties()
        self.pollConnectorProperties = PollConnectorProperties()
        self.script = ''
        
        if uXml is not None:
            self.sourceConnectorProperties = SourceConnectorProperties(self.root.find('sourceConnectorProperties'))
            self.pollConnectorProperties = PollConnectorProperties(self.root.find('pollConnectorProperties'))

            self.script = self.getSafeText('script')

    def getXML(self, version = '3.12.0'):
        xml = f'''
            <pluginProperties/>
            <pollConnectorProperties version="{version}">
                {self.pollConnectorProperties.getXML(version)}
            </pollConnectorProperties>
            <sourceConnectorProperties version="{version}">
                {self.sourceConnectorProperties.getXML(version)}
            </sourceConnectorProperties>
            {getXMLString(escape(self.script), "script")}
        '''
        return xml

class TcpReceiverProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.tcp.TcpReceiverProperties'
        self.transportName = 'TCP Listener'

        self.pluginProperties = []
        self.sourceConnectorProperties = SourceConnectorProperties() 
        self.listenerConnectorProperties = ListenerConnectorProperties()
        self.transmissionModeProperties = MLLPModeProperties()

        self.serverMode = 'true'
        self.remoteAddress = ''
        self.remotePort = ''
        self.overrideLocalBinding = 'false'
        self.reconnectInterval = '5000'
        self.receiveTimeout = '0'
        self.bufferSize = '65536'
        self.maxConnections = '10'
        self.keepConnectionOpen = 'true'
        self.dataTypeBinary = 'false'
        self.charsetEncoding = 'DEFAULT_ENCODING'
        self.respondOnNewConnection = '0'
        self.responseAddress = ''
        self.responsePort = ''

        if uXml is not None:
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

    def getXML(self, version = '3.12.0'):
        xml = f'''
            <pluginProperties/>
            <listenerConnectorProperties version="{version}">
                {self.listenerConnectorProperties.getXML(version)}
            </listenerConnectorProperties>
            <sourceConnectorProperties version="{version}">
                {self.sourceConnectorProperties.getXML(version)}
            </sourceConnectorProperties>
            <transmissionModeProperties class="{self.transmissionModeProperties.className}">
                {self.transmissionModeProperties.getXML(version)}
            </transmissionModeProperties>
            {getXMLString(self.serverMode, "serverMode")}
            {getXMLString(self.remoteAddress, "remoteAddress")}
            {getXMLString(self.remotePort, "remotePort")}
            {getXMLString(self.overrideLocalBinding, "overrideLocalBinding")}
            {getXMLString(self.reconnectInterval, "reconnectInterval")}
            {getXMLString(self.receiveTimeout, "receiveTimeout")}
            {getXMLString(self.bufferSize, "bufferSize")}
            {getXMLString(self.maxConnections, "maxConnections")}
            {getXMLString(self.keepConnectionOpen, "keepConnectionOpen")}
            {getXMLString(self.dataTypeBinary, "dataTypeBinary")}
            {getXMLString(self.charsetEncoding, "charsetEncoding")}
            {getXMLString(self.respondOnNewConnection, "respondOnNewConnection")}
            {getXMLString(self.responseAddress, "responseAddress")}
            {getXMLString(self.responsePort, "responsePort")}'''
        return xml

class WebServiceReceiverProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.ws.WebServiceReceiverProperties'
        self.transportName = 'Web Service Listener'

        self.pluginProperties = []

        if len(self.root.find('./pluginProperties').findall('./*')) > 0:
            for e in self.root.find('./pluginProperties').findall('./*'):
                prop = Mapping.httpAuthProperties(e.tag)
        
                self.pluginProperties.append(prop(e))

        self.sourceConnectorProperties = SourceConnectorProperties(self.root.find('sourceConnectorProperties'))
        self.listenerConnectorProperties = ListenerConnectorProperties(self.root.find('listenerConnectorProperties'))
        
        self.classNameT = self.getSafeText('className')
        self.serviceName = self.getSafeText('serviceName')
        self.soapBinding = self.getSafeText('soapBinding')

    def getXML(self, version = "3.12.0"):
        pluginXml = "<pluginProperties/>"

        if len(self.pluginProperties) > 0:
            pluginXml = "<pluginProperties>"
            for plugin in self.pluginProperties:
                pluginXml += f'<{plugin.className} version="{version}">'
                pluginXml += plugin.getXML(version)
                pluginXml += f'</{plugin.className}>'
            pluginXml += "</pluginProperties>"

        xml = f'''
            {pluginXml}
            <listenerConnectorProperties version="{version}">
                {self.listenerConnectorProperties.getXML(version)}
            </listenerConnectorProperties>
            <sourceConnectorProperties version="{version}">
                {self.sourceConnectorProperties.getXML(version)}
            </sourceConnectorProperties>
            {getXMLString(self.classNameT, "className")}
            {getXMLString(self.serviceName, "serviceName")}
            {getXMLString(escape(self.soapBinding), "soapBinding")}
        '''
        return xml
        
#endregion

#region DispatcherProperties (DestinationConnectorTypes)
class DestinationConnector(ConnectorProperties):
    def __init__(self, uXml = None):
        ConnectorProperties.__init__(self, uXml)
        pluginProperties = []
        #TODO: find a different name than this, it conflicts

        self.destinationConnectorProperties = DestinationConnectorProperties()

        if uXml is not None:
            self.destinationConnectorProperties = DestinationConnectorProperties(self.root.find('destinationConnectorProperties'))

class VmDispatcherProperties(ConnectorProperties):
    def __init__(self, uXml = None):
        DestinationConnector.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.vm.VmDispatcherProperties'
        self.transportName = 'Channel Writer'

        self.channelId = 'none'
        self.channelTemplate = '${message.encodedData}'
        self.mapVariables = []

        if uXml is not None:
            self.channelId = self.getSafeText('channelId')
            self.channelTemplate = self.getSafeText('channelTemplate')

            for e in self.root.findall('./mapVariables/string'):
                self.mapVariables.append(e.text)

    def getXML(self, version = "3.12.0"):
        mapVar = ""
        for mv in self.mapVariables:
            mapVar += f"{getXMLString(mv, 'string')}"


        xml = f'''
        	<pluginProperties/>
            <destinationConnectorProperties version="{version}">
                {self.destinationConnectorProperties.getXML(version)}
            </destinationConnectorProperties>
            {getXMLString(self.channelId, "channelId")}
            {getXMLString(self.channelTemplate, "channelTemplate")}
            {getXMLString(mapVar, "mapVariables", enclose=False)}
        '''
        return xml

class JavaScriptDispatcherProperties(DestinationConnector):
    def __init__(self, uXml = None):
        DestinationConnector.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.js.JavaScriptDispatcherProperties'
        self.transportName = 'JavaScript Writer'
        self.script = ''

        if uXml is not None:
            self.script = self.getSafeText('script')

    def getXML(self, version = "3.12.0"):
        xml = f'''
        	<pluginProperties/>
            <destinationConnectorProperties version="{version}">
                {self.destinationConnectorProperties.getXML(version)}
            </destinationConnectorProperties>
            {getXMLString(escape(self.script), "script")}'''
        
        return xml

class FileDispatcherProperties(DestinationConnector):
    def __init__(self, uXml = None):
        DestinationConnector.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.file.FileDispatcherProperties'
        self.transportName = 'File Writer'
        self.scheme = 'File'
        self.schemeProperties = None
        self.host = ''
        self.outputPattern = ''
        self.anonymous = 'false'
        self.username = ''
        self.password = ''
        self.timeout = '10000'
        self.keepConnectionOpen = 'true'
        self.maxIdleTime = '0'
        self.secure = 'true'
        self.passive = 'true'
        self.validateConnection = 'true'
        self.outputAppend = 'true'
        self.errorOnExists = 'false'
        self.temporary = 'false'
        self.binary = 'false'
        self.charsetEncoding = 'DEFAULT_ENCODING'
        self.template = ''

        if uXml is not None:
            self.scheme = self.getSafeText('scheme')
            if self.root.find('schemeProperties') is not None:
                prop = Mapping.schemeProperties(self.root.find('schemeProperties').attrib['class'])
                
                self.schemeProperties = prop(self.root.find('schemeProperties'))

            self.host = self.getSafeText('host')
            self.outputPattern = self.getSafeText('outputPattern')
            self.anonymous = self.getSafeText('anonymous')
            self.username = self.getSafeText('username')
            self.password = self.getSafeText('password')
            self.timeout = self.getSafeText('timeout')
            self.keepConnectionOpen = self.getSafeText('keepConnectionOpen')
            self.maxIdleTime = self.getSafeText('maxIdleTime')
            self.secure = self.getSafeText('secure')
            self.passive = self.getSafeText('passive')
            self.validateConnection = self.getSafeText('validateConnection')
            self.outputAppend = self.getSafeText('outputAppend')
            self.errorOnExists = self.getSafeText('errorOnExists')
            self.temporary = self.getSafeText('temporary')
            self.binary = self.getSafeText('binary')
            self.charsetEncoding = self.getSafeText('charsetEncoding')
            self.template = self.getSafeText('template')

    def getXML(self, version = "3.12.0"):
        schemePropXML = ""
        if self.schemeProperties is not None:
            schemePropXML = f'''<schemeProperties class="{self.schemeProperties.className}">
                                    {self.schemeProperties.getXML(version)}
                                </schemeProperties>'''
        xml = f'''
        	<pluginProperties/>
            <destinationConnectorProperties version="{version}">
                {self.destinationConnectorProperties.getXML(version)}
            </destinationConnectorProperties>
            {getXMLString(self.scheme, "scheme")}                
            {schemePropXML}
            {getXMLString(self.host, "host")}
            {getXMLString(self.outputPattern, "outputPattern")}
            {getXMLString(self.anonymous, "anonymous")}
            {getXMLString(self.username, "username")}
            {getXMLString(self.password, "password")}
            {getXMLString(self.timeout, "timeout")}
            {getXMLString(self.keepConnectionOpen, "keepConnectionOpen")}
            {getXMLString(self.maxIdleTime, "maxIdleTime")}
            {getXMLString(self.secure, "secure")}
            {getXMLString(self.passive, "passive")}
            {getXMLString(self.validateConnection, "validateConnection")}
            {getXMLString(self.outputAppend, "outputAppend")}
            {getXMLString(self.errorOnExists, "errorOnExists")}
            {getXMLString(self.temporary, "temporary")}
            {getXMLString(self.binary, "binary")}
            {getXMLString(self.charsetEncoding, "charsetEncoding")}
            {getXMLString(self.template, "template")}'''
        
        return xml

class WebServiceDispatcherProperties(DestinationConnector):
    def __init__(self, uXml = None):
        DestinationConnector.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.ws.WebServiceDispatcherProperties'
        self.transportName = 'Web Service Sender'

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
        self.headers = LinkedHashMap(self.root.find('headers'))
        self.headersVariable = self.getSafeText('headersVariable')
        self.isUseHeadersVariable = self.getSafeText('isUseHeadersVariable')
        self.useMtom = self.getSafeText('useMtom')
        self.attachmentNames = self.getSafeText('attachmentNames')
        self.attachmentContents = self.getSafeText('attachmentContents')
        self.attachmentTypes = self.getSafeText('attachmentTypes')
        self.attachmentsVariable = self.getSafeText('attachmentsVariable')
        self.isUseAttachmentsVariable = self.getSafeText('isUseAttachmentsVariable')
        self.soapAction = self.getSafeText('soapAction')
        self.wsdlDefinitionMap = LinkedHashMap(self.root.find('wsdlDefinitionMap'))

    def getXML(self, version="3.12.0") -> str:
        mapXML = '<map class="linked-hash-map"/>'
        
        if len(self.wsdlDefinitionMap.entry) > 0:
            mapXML = '<map class="linked-hash-map">'
            mapXML += f'{self.wsdlDefinitionMap.getXML(version)}'
            mapXML += '</map>'

        return f'''
            <pluginProperties/>
            <destinationConnectorProperties version="{version}">
                {self.destinationConnectorProperties.getXML(version)}
            </destinationConnectorProperties>
            {getXMLString(self.wsdlUrl, "wsdlUrl")}
            {getXMLString(self.service, "service")}
            {getXMLString(self.port, "port")}
            {getXMLString(self.operation, "operation")}
            {getXMLString(self.locationURI, "locationURI")}
            {getXMLString(self.socketTimeout, "socketTimeout")}
            {getXMLString(self.useAuthentication, "useAuthentication")}
            {getXMLString(self.username, "username")}
            {getXMLString(self.password, "password")}
            {getXMLString(escape(self.envelope), "envelope")}
            {getXMLString(self.oneWay, "oneWay")}
            {getXMLString(self.headers.getXML(version), "headers")}
            {getXMLString(self.headersVariable, "headersVariable")}
            {getXMLString(self.isUseHeadersVariable, "isUseHeadersVariable")}
            {getXMLString(self.useMtom, "useMtom")}
            {getXMLString(self.attachmentNames, "attachmentNames", enclose=False)}
            {getXMLString(self.attachmentContents, "attachmentContents", enclose=False)}
            {getXMLString(self.attachmentTypes, "attachmentTypes", enclose=False)}
            {getXMLString(self.attachmentsVariable, "attachmentsVariable")}
            {getXMLString(self.isUseAttachmentsVariable, "isUseAttachmentsVariable")}
            {getXMLString(self.soapAction, "soapAction")}
            <wsdlDefinitionMap>
                {mapXML}
            </wsdlDefinitionMap>
            '''

class DatabaseDispatcherProperties(DestinationConnector):
    def __init__(self, uXml = None):
        DestinationConnector.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.jdbc.DatabaseDispatcherProperties'
        self.transportName = 'Database Writer'

        self.driver = self.getSafeText('driver')
        self.url = self.getSafeText('url')
        self.username = self.getSafeText('username')
        self.password = self.getSafeText('password')
        self.query = self.getSafeText('query')
        self.useScript = self.getSafeText('useScript')
    
    def getXML(self, version = "3.12.0"):
        xml = f'''
        	<pluginProperties/>
            <destinationConnectorProperties version="{version}">
                {self.destinationConnectorProperties.getXML(version)}
            </destinationConnectorProperties>
            {getXMLString(self.driver, "driver")}
            {getXMLString(self.url, "url")}
            {getXMLString(self.username, "username")}
            {getXMLString(self.password, "password")}
            {getXMLString(escape(self.query), "query")}
            {getXMLString(self.useScript, "useScript")}
        '''
        return xml

class DICOMDispatcherProperties(DestinationConnector):
    def __init__(self, uXml = None):
        DestinationConnector.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.dimse.DICOMDispatcherProperties'
        self.transportName = 'DICOM Sender'

        self.host = self.getSafeText('host')
        self.port = self.getSafeText('port')
        self.applicationEntity = self.getSafeText('applicationEntity')
        self.localHost = self.getSafeText('localHost')
        self.localPort = self.getSafeText('localPort')
        self.localApplicationEntity = self.getSafeText('localApplicationEntity')
        self.template = self.getSafeText('template')
        self.acceptTo = self.getSafeText('acceptTo')
        self.asyncS = self.getSafeText('async')
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

    def getXML(self, version = "3.12.0"):
        xml = f'''
        	<pluginProperties/>
            <destinationConnectorProperties version="{version}">
                {self.destinationConnectorProperties.getXML(version)}
            </destinationConnectorProperties>
            {getXMLString(self.host, "host")}
            {getXMLString(self.port, "port")}
            {getXMLString(self.applicationEntity, "applicationEntity")}
            {getXMLString(self.localHost, "localHost")}
            {getXMLString(self.localPort, "localPort")}
            {getXMLString(self.localApplicationEntity, "localApplicationEntity")}
            {getXMLString(self.template, "template")}
            {getXMLString(self.acceptTo, "acceptTo")}
            {getXMLString(self.asyncS, "async")}
            {getXMLString(self.bufSize, "bufSize")}
            {getXMLString(self.connectTo, "connectTo")}
            {getXMLString(self.priority, "priority")}
            {getXMLString(self.passcode, "passcode")}
            {getXMLString(self.pdv1, "pdv1")}
            {getXMLString(self.rcvpdulen, "rcvpdulen")}
            {getXMLString(self.reaper, "reaper")}
            {getXMLString(self.releaseTo, "releaseTo")}
            {getXMLString(self.rspTo, "rspTo")}
            {getXMLString(self.shutdownDelay, "shutdownDelay")}
            {getXMLString(self.sndpdulen, "sndpdulen")}
            {getXMLString(self.soCloseDelay, "soCloseDelay")}
            {getXMLString(self.sorcvbuf, "sorcvbuf")}
            {getXMLString(self.sosndbuf, "sosndbuf")}
            {getXMLString(self.stgcmt, "stgcmt")}
            {getXMLString(self.tcpDelay, "tcpDelay")}
            {getXMLString(self.ts1, "ts1")}
            {getXMLString(self.uidnegrsp, "uidnegrsp")}
            {getXMLString(self.username, "username")}
            {getXMLString(self.keyPW, "keyPW")}
            {getXMLString(self.keyStore, "keyStore")}
            {getXMLString(self.keyStorePW, "keyStorePW")}
            {getXMLString(self.noClientAuth, "noClientAuth")}
            {getXMLString(self.nossl2, "nossl2")}
            {getXMLString(self.tls, "tls")}
            {getXMLString(self.trustStore, "trustStore")}
            {getXMLString(self.trustStorePW, "trustStorePW")}'''
        
        return xml

class TcpDispatcherProperties(DestinationConnector):
    def __init__(self, uXml = None):
        DestinationConnector.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.tcp.TcpDispatcherProperties'
        self.transportName = 'TCP Sender'

        if self.root.find('transmissionModeProperties') is not None:
            prop = Mapping.modeProperties(self.root.find('transmissionModeProperties').attrib['class'])
            self.transmissionModeProperties = prop(self.root.find('transmissionModeProperties'))
    
        self.serverMode = self.getSafeText('serverMode')
        self.remoteAddress = self.getSafeText('remoteAddress')
        self.remotePort = self.getSafeText('remotePort')
        self.overrideLocalBinding = self.getSafeText('overrideLocalBinding')
        self.localAddress = self.getSafeText('localAddress')
        self.localPort = self.getSafeText('localPort')
        self.sendTimeout = self.getSafeText('sendTimeout')
        self.bufferSize = self.getSafeText('bufferSize')
        self.maxConnections = self.getSafeText('maxConnections')
        self.keepConnectionOpen = self.getSafeText('keepConnectionOpen')
        self.checkRemoteHost = self.getSafeText('checkRemoteHost')
        self.responseTimeout = self.getSafeText('responseTimeout')
        self.ignoreResponse = self.getSafeText('ignoreResponse')
        self.queueOnResponseTimeout = self.getSafeText('queueOnResponseTimeout')
        self.dataTypeBinary = self.getSafeText('dataTypeBinary')
        self.charsetEncoding = self.getSafeText('charsetEncoding')
        self.template = self.getSafeText('template')
    
    def getXML(self, version = "3.12.0"):
        xml = f'''
        	<pluginProperties/>
            <destinationConnectorProperties version="{version}">
                {self.destinationConnectorProperties.getXML(version)}
            </destinationConnectorProperties>
            <transmissionModeProperties class="{self.transmissionModeProperties.className}">
                {self.transmissionModeProperties.getXML(version)}
            </transmissionModeProperties>
            {getXMLString(self.serverMode, "serverMode")}
            {getXMLString(self.remoteAddress, "remoteAddress")}
            {getXMLString(self.remotePort, "remotePort")}
            {getXMLString(self.overrideLocalBinding, "overrideLocalBinding")}
            {getXMLString(self.localAddress, "localAddress")}
            {getXMLString(self.localPort, "localPort")}
            {getXMLString(self.sendTimeout, "sendTimeout")}
            {getXMLString(self.bufferSize, "bufferSize")}
            {getXMLString(self.maxConnections, "maxConnections")}
            {getXMLString(self.keepConnectionOpen, "keepConnectionOpen")}
            {getXMLString(self.checkRemoteHost, "checkRemoteHost")}
            {getXMLString(self.responseTimeout, "responseTimeout")}
            {getXMLString(self.ignoreResponse, "ignoreResponse")}
            {getXMLString(self.queueOnResponseTimeout, "queueOnResponseTimeout")}
            {getXMLString(self.dataTypeBinary, "dataTypeBinary")}
            {getXMLString(self.charsetEncoding, "charsetEncoding")}
            {getXMLString(self.template, "template")}'''
        
        return xml

class HttpDispatcherProperties(DestinationConnector):
    def __init__(self, uXml = None):
        DestinationConnector.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.http.HttpDispatcherProperties'
        self.transportName = 'HTTP Sender'

        self.host = self.getSafeText('host')
        self.useProxyServer = self.getSafeText('useProxyServer')
        self.proxyAddress = self.getSafeText('proxyAddress')
        self.proxyPort = self.getSafeText('proxyPort')
        self.method = self.getSafeText('method')
        self.headers = LinkedHashMap(self.root.find('headers'))
        self.parameters = LinkedHashMap(self.root.find('parameters'))
        self.useHeadersVariable = self.getSafeText('useHeadersVariable')
        self.headersVariable = self.getSafeText('headersVariable')
        self.useParametersVariable = self.getSafeText('useParametersVariable')
        self.parametersVariable = self.getSafeText('parametersVariable')
        self.responseXmlBody = self.getSafeText('responseXmlBody')
        self.responseParseMultipart = self.getSafeText('responseParseMultipart')
        self.responseIncludeMetadata = self.getSafeText('responseIncludeMetadata')
        self.responseBinaryMimeTypes = self.getSafeText('responseBinaryMimeTypes')
        self.responseBinaryMimeTypesRegex = self.getSafeText('responseBinaryMimeTypesRegex')
        self.multipart = self.getSafeText('multipart')
        self.useAuthentication = self.getSafeText('useAuthentication')
        self.authenticationType = self.getSafeText('authenticationType')
        self.usePreemptiveAuthentication = self.getSafeText('usePreemptiveAuthentication')
        self.username = self.getSafeText('username')
        self.password = self.getSafeText('password')
        self.content = self.getSafeText('content')
        self.contentType = self.getSafeText('contentType')
        self.dataTypeBinary = self.getSafeText('dataTypeBinary')
        self.charset = self.getSafeText('charset')
        self.socketTimeout = self.getSafeText('socketTimeout')
    
    def getXML(self, version = "3.12.0"):
        xml = f'''
        	<pluginProperties/>
            <destinationConnectorProperties version="{version}">
                {self.destinationConnectorProperties.getXML(version)}
            </destinationConnectorProperties>
            {getXMLString(self.host, "host")}
            {getXMLString(self.useProxyServer, "useProxyServer")}
            {getXMLString(self.proxyAddress, "proxyAddress")}
            {getXMLString(self.proxyPort, "proxyPort")}
            {getXMLString(self.method, "method")}
            <headers class="linked-hash-map">
                {self.headers.getXML(version)}
            </headers>
            <parameters class="linked-hash-map">
                {self.parameters.getXML(version)}
            </parameters>
            {getXMLString(self.useHeadersVariable, "useHeadersVariable")}
            {getXMLString(self.headersVariable, "headersVariable")}
            {getXMLString(self.useParametersVariable, "useParametersVariable")}
            {getXMLString(self.parametersVariable, "parametersVariable")}
            {getXMLString(self.responseXmlBody, "responseXmlBody")}
            {getXMLString(self.responseParseMultipart, "responseParseMultipart")}
            {getXMLString(self.responseIncludeMetadata, "responseIncludeMetadata")}
            {getXMLString(escape(self.responseBinaryMimeTypes), "responseBinaryMimeTypes")}
            {getXMLString(self.responseBinaryMimeTypesRegex, "responseBinaryMimeTypesRegex")}
            {getXMLString(self.multipart, "multipart")}
            {getXMLString(self.useAuthentication, "useAuthentication")}
            {getXMLString(self.authenticationType, "authenticationType")}
            {getXMLString(self.usePreemptiveAuthentication, "usePreemptiveAuthentication")}
            {getXMLString(self.username, "username")}
            {getXMLString(self.password, "password")}
            {getXMLString(self.content, "content")}
            {getXMLString(self.contentType, "contentType")}
            {getXMLString(self.dataTypeBinary, "dataTypeBinary")}
            {getXMLString(self.charset, "charset")}
            {getXMLString(self.socketTimeout, "socketTimeout")}
        '''
        return xml

class SmtpDispatcherProperties(DestinationConnector):
    def __init__(self, uXml = None):
        DestinationConnector.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.smtp.SmtpDispatcherProperties'
        self.transportName = 'SMTP Sender'

        self.smtpHost = self.getSafeText('smtpHost')
        self.smtpPort = self.getSafeText('smtpPort')
        self.overrideLocalBinding = self.getSafeText('overrideLocalBinding')
        self.localAddress = self.getSafeText('localAddress')
        self.localPort = self.getSafeText('localPort')
        self.timeout = self.getSafeText('timeout')
        self.encryption = self.getSafeText('encryption')
        self.authentication = self.getSafeText('authentication')
        self.username = self.getSafeText('username')
        self.password = self.getSafeText('password')
        self.to = self.getSafeText('to')
        self.fromT = self.getSafeText('from')
        self.cc = self.getSafeText('cc')
        self.bcc = self.getSafeText('bcc')
        self.replyTo = self.getSafeText('replyTo')
        self.headers = LinkedHashMap(self.root.find('headers'))
        self.headersVariable = self.getSafeText('headersVariable')
        self.isUseHeadersVariable = self.getSafeText('isUseHeadersVariable')
        self.subject = self.getSafeText('subject')
        self.charsetEncoding = self.getSafeText('charsetEncoding')
        self.html = self.getSafeText('html')
        self.body = self.getSafeText('body')
        self.attachments = self.getSafeText('attachments')
        self.attachmentsVariable = self.getSafeText('attachmentsVariable')
        self.isUseAttachmentsVariable = self.getSafeText('isUseAttachmentsVariable')
        self.attachments = []

        for a in self.root.findall('./attachments/com.mirth.connect.connectors.smtp.Attachment'):
            self.attachments.append(Attachment(a))

    def getXML(self, version = "3.12.0"):
        attachXML = "<attachments/>"

        if len(self.attachments) > 0:
            attachXML = "<attachments>"
            for a in self.attachments:
                attachXML += f"<{a.className}>"
                attachXML += f"{a.getXML(version)}"
                attachXML += f"</{a.className}>"
            attachXML += "</attachments>"    

        xml = f'''
        	<pluginProperties/>
            <destinationConnectorProperties version="{version}">
                {self.destinationConnectorProperties.getXML(version)}
            </destinationConnectorProperties>
            {getXMLString(self.smtpHost, "smtpHost")}
            {getXMLString(self.smtpPort, "smtpPort")}
            {getXMLString(self.overrideLocalBinding, "overrideLocalBinding")}
            {getXMLString(self.localAddress, "localAddress")}
            {getXMLString(self.localPort, "localPort")}
            {getXMLString(self.timeout, "timeout")}
            {getXMLString(self.encryption, "encryption")}
            {getXMLString(self.authentication, "authentication")}
            {getXMLString(self.username, "username")}
            {getXMLString(self.password, "password")}
            {getXMLString(self.to, "to")}
            {getXMLString(self.fromT, "from")}
            {getXMLString(self.cc, "cc")}
            {getXMLString(self.bcc, "bcc")}
            {getXMLString(self.replyTo, "replyTo")}
            <headers class="linked-hash-map">
                {self.headers.getXML(version)}
            </headers>
            {getXMLString(self.headersVariable, "headersVariable")}
            {getXMLString(self.isUseHeadersVariable, "isUseHeadersVariable")}
            {getXMLString(self.subject, "subject")}
            {getXMLString(self.charsetEncoding, "charsetEncoding")}
            {getXMLString(self.html, "html")}
            {getXMLString(self.body, "body")}
            {attachXML}
            {getXMLString(self.attachmentsVariable, "attachmentsVariable")}
            {getXMLString(self.isUseAttachmentsVariable, "isUseAttachmentsVariable")}'''
            
        return xml

class DocumentDispatcherProperties(DestinationConnector):
    def __init__(self, uXml = None):
        DestinationConnector.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.doc.DocumentDispatcherProperties'
        self.transportName = 'Document Writer'

        self.host = self.getSafeText('host')
        self.outputPattern = self.getSafeText('outputPattern')
        self.documentType = self.getSafeText('documentType')
        self.encrypt = self.getSafeText('encrypt')
        self.output = self.getSafeText('output')
        self.password = self.getSafeText('password')
        self.pageWidth = self.getSafeText('pageWidth')
        self.pageHeight = self.getSafeText('pageHeight')
        self.pageUnit = self.getSafeText('pageUnit')
        self.template = self.getSafeText('template')
    
    def getXML(self, version = "3.12.0"):
        xml = f'''
        	<pluginProperties/>
            <destinationConnectorProperties version="{version}">
                {self.destinationConnectorProperties.getXML(version)}
            </destinationConnectorProperties>
            {getXMLString(self.host, "host")}
            {getXMLString(self.outputPattern, "outputPattern")}
            {getXMLString(self.documentType, "documentType")}
            {getXMLString(self.encrypt, "encrypt")}
            {getXMLString(self.output, "output")}
            {getXMLString(self.password, "password")}
            {getXMLString(self.pageWidth, "pageWidth")}
            {getXMLString(self.pageHeight, "pageHeight")}
            {getXMLString(self.pageUnit, "pageUnit")}
            {getXMLString(self.template, "template")}
        '''
        return xml

class JmsDispatcherProperties(MirthElement):
    def __init__(self, uXml = None):
        DestinationConnector.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.jms.JmsDispatcherProperties'
        self.transportName = 'JMS Sender'

        self.useJndi = 'false'
        self.jndiProviderUrl = ''
        self.jndiInitialContextFactory = ''
        self.jndiConnectionFactoryName = ''
        self.connectionFactoryClass = ''
        self.username = ''
        self.password = ''
        self.destinationName = ''
        self.topic = ''
        self.clientId = ''
        self.template = ''

        self.connectionProperties = []

        if uXml is not None:
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
            self.template = self.getSafeText('template')

            self.connectionProperties = []
            for e in self.root.findall('./connectionProperties/entry'):
                strings = e.findall('./string')
                self.connectionProperties.append((strings[0].text, strings[1].text))
    
    def getXML(self, version = "3.12.0"):
        connectionPropXML = '<connectionProperties class="linked-hash-map"/>'
        if len(self.connectionProperties) > 0:
            connectionPropXML = '<connectionProperties class="linked-hash-map">'
            for cp in self.connectionProperties:
                
                connectionPropXML += f'<entry><string>{cp[0]}</string>'
                connectionPropXML += f'<string>{cp[1]}</string></entry>'
            connectionPropXML += '</connectionProperties>'

        xml = f'''
        	<pluginProperties/>
            {getXMLString(self.useJndi, "useJndi")}
            {getXMLString(self.jndiProviderUrl, "jndiProviderUrl")}
            {getXMLString(self.jndiInitialContextFactory, "jndiInitialContextFactory")}
            {getXMLString(self.jndiConnectionFactoryName, "jndiConnectionFactoryName")}
            {getXMLString(self.connectionFactoryClass, "connectionFactoryClass")}
            {connectionPropXML}
            {getXMLString(self.username, "username")}
            {getXMLString(self.password, "password")}
            {getXMLString(self.destinationName, "destinationName")}
            {getXMLString(self.topic, "topic")}
            {getXMLString(self.clientId, "clientId")}
            {getXMLString(self.template, "template")}
            <destinationConnectorProperties version="{version}">
                {self.destinationConnectorProperties.getXML(version)}
            </destinationConnectorProperties>
        '''
        return xml

class Map(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.map = LinkedHashMap(self.root.find('map'))

class Attachment(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.smtp.Attachment'
        self.name = "Attachment"
        self.content = ""
        self.mimeType = ""

        if uXml is not None:
            self.name = self.getSafeText('name')
            self.content = self.getSafeText('content')
            self.mimeType = self.getSafeText('mimeType')

    def getXML(self, version="3.12.0") -> str:
        return f'''
            {getXMLString(self.name, "name")}
            {getXMLString(self.content, "content")}
            {getXMLString(self.mimeType, "mimeType")}'''
        
class DestinationConnectorProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        
        self.queueEnabled = 'false'
        self.sendFirst = 'false'
        self.retryIntervalMillis = '10000'
        self.regenerateTemplate = 'false'
        self.retryCount = '0'
        self.rotate = 'false'
        self.includeFilterTransformer = 'false'
        self.threadCount = '1'
        self.threadAssignmentVariable = ''
        self.validateResponse = 'false'
        self.queueBufferSize = '1000'
        self.reattachAttachments = 'true'
        self.resourceIds = LinkedHashMap()
        entry = Entry()
        entry.string.append('Default Resource')
        entry.string.append('[Default Resource]')

        self.resourceIds.entry.append(entry)

        if uXml is not None:
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
    
    def getXML(self, version = "3.12.0"):

        xml = f'''{getXMLString(self.queueEnabled, "queueEnabled")}
                {getXMLString(self.sendFirst, "sendFirst")}
                {getXMLString(self.retryIntervalMillis, "retryIntervalMillis")}
                {getXMLString(self.regenerateTemplate, "regenerateTemplate")}
                {getXMLString(self.retryCount, "retryCount")}
                {getXMLString(self.rotate, "rotate")}
                {getXMLString(self.includeFilterTransformer, "includeFilterTransformer")}
                {getXMLString(self.threadCount, "threadCount")}
                {getXMLString(self.threadAssignmentVariable, "threadAssignmentVariable")}
                {getXMLString(self.validateResponse, "validateResponse")}
                <resourceIds class="linked-hash-map">
                    {self.resourceIds.getXML(version)}
                </resourceIds>
                {getXMLString(self.queueBufferSize, "queueBufferSize")}
                {getXMLString(self.reattachAttachments, "reattachAttachments")}'''
        return xml
#endregion

#region HttpAuthProperties
class BasicHttpAuthProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.httpauth.basic.BasicHttpAuthProperties'

        self.credentials = []
        self.authType = ''
        self.realm = ''
        self.isUseCredentialsVariable = ''
        self.credentialsVariable = ''

        if uXml is not None:
            self.authType = self.getSafeText('authType')
            self.realm = self.getSafeText('realm')
            for e in self.root.findall('./credentials/entry'):
                strings = e.findall('./string')
                self.credentials.append((strings[0].text, strings[1].text))

            self.isUseCredentialsVariable = self.getSafeText('isUseCredentialsVariable')
            self.credentialsVariable = self.getSafeText('credentialsVariable')

    def getXML(self, version="3.12.0"):
        propXML = "<credentials>"
        for prop in self.credentials:
            propXML += "<entry>"
            propXML += f"{getXMLString(prop[0], 'string')}{getXMLString(prop[1], 'string')}"
            propXML += "</entry>"
        propXML += "</credentials>"

        return f'''{getXMLString(self.authType, "authType")}
                {getXMLString(self.realm, "realm")}
                {propXML}
                {getXMLString(self.isUseCredentialsVariable, "isUseCredentialsVariable")}
                {getXMLString(self.credentialsVariable, "credentialsVariable")}'''

class DigestHttpAuthProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.httpauth.digest.DigestHttpAuthProperties'
        
        self.credentials = []
        self.authType = ''
        self.realm = ''
        self.isUseCredentialsVariable = ''
        self.credentialsVariable = ''
        self.qopModes = ''
        self.opaque = ''
        self.algorithm = ''

        if uXml is not None:
            self.authType = self.getSafeText('authType')
            self.realm = self.getSafeText('realm')
            for e in self.root.findall('./credentials/entry'):
                strings = e.findall('./string')
                self.credentials.append((strings[0].text, strings[1].text))

            self.isUseCredentialsVariable = self.getSafeText('isUseCredentialsVariable')
            self.credentialsVariable = self.getSafeText('credentialsVariable')
            self.qopModes = self.root.find('qopModes')
            self.opaque = self.getSafeText('opaque')
            self.algorithm = self.root.find('algorithms')

    def getXML(self, version="3.12.0"):
        propXML = "<credentials>"
        for prop in self.credentials:
            propXML += "<entry>"
            propXML += f"{getXMLString(prop[0], 'string')}{getXMLString(prop[1], 'string')}"
            propXML += "</entry>"
        propXML += "</credentials>"

        return f'''{getXMLString(self.authType, "authType")}
                {getXMLString(self.realm, "realm")}
                {propXML}
                {getXMLString(self.isUseCredentialsVariable, "isUseCredentialsVariable")}
                {getXMLString(self.credentialsVariable, "credentialsVariable")}
                {getXMLString(self.qopModes, "qopModes")}
                {getXMLString(self.opaque, "opaque")}
                {getXMLString(self.algorithm, "authenticatorClass")}'''

class JavaScriptHttpAuthProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.httpauth.javascript.JavaScriptHttpAuthProperties'

        self.authType = ''
        self.script = ''

        if uXml is not None:
            self.authType = self.getSafeText('authType')
            self.script = self.getSafeText('script')

    def getXML(self, version="3.12.0"):
        return f'''{getXMLString(self.authType, "authType")}
                    {getXMLString(escape(self.script), "script")}'''

class CustomHttpAuthProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.httpauth.custom.CustomHttpAuthProperties'

        self.properties = []
        self.authType = ''
        self.authenticatorClass = ''

        if uXml is not None:
            self.authType = self.getSafeText('authType')
            self.authenticatorClass = self.getSafeText('authenticatorClass')

            for e in self.root.findall('./properties/entry'):
                strings = e.findall('./string')
                self.properties.append((strings[0].text, strings[1].text))

    def getXML(self, version="3.12.0"):
        propXML = "<properties>"
        for prop in self.properties:
            propXML += "<entry>"
            propXML += f"{getXMLString(prop[0], 'string')}{getXMLString(prop[1], 'string')}"
            propXML += "</entry>"
        propXML += "</properties>"

        return f'''{getXMLString(self.authType, "authType")}
            {getXMLString(self.authenticatorClass, "authenticatorClass")}
            {propXML}'''

class OAuth2HttpAuthProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.httpauth.oauth2.OAuth2HttpAuthProperties'

        self.authType = ''
        self.tokenLocation = ''
        self.locationKey = ''
        self.verificationURL = ''

        if uXml is not None:
            self.authType = self.getSafeText('authType')
            self.tokenLocation = self.getSafeText('tokenLocation')
            self.locationKey = self.getSafeText('locationKey')
            self.verificationURL = self.getSafeText('verificationURL')

    def getXML(self, version="3.12.0"):
        return f'''{getXMLString(self.authType, "authType")}
            {getXMLString(self.tokenLocation, "tokenLocation")}
            {getXMLString(self.locationKey, "locationKey")}
            {getXMLString(self.verificationURL, "verificationURL")}'''

class NoneHttpAuthProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.httpauth.NoneHttpAuthProperties'
        
        self.authType = 'NONE'

        if uXml is not None:
            self.authType = self.getSafeText('authType')
    
    def getXML(self, version="3.12.0"):
        return f'''{getXMLString(self.authType, 'authType')}'''
#endregion

#region Static Resources
class HttpStaticResource(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.http.HttpStaticResource'
        
        self.contextPath = ''
        self.resourceType = ''
        self.value = ''
        self.contentType = ''

        if uXml is not None:
            self.contextPath = self.getSafeText('contextPath')
            self.resourceType = self.getSafeText('resourceType')
            self.value = self.getSafeText('value')
            self.contentType = self.getSafeText('contentType')
    
    def getXML(self, version="3.12.0"):
        return f'''{getXMLString(self.contextPath, 'contextPath')}
                    {getXMLString(self.resourceType, 'resourceType')}
                    {getXMLString(self.value, 'value')}
                    {getXMLString(self.contentType, 'contentType')}'''

#endregion

#region SchemeProperties
class SchemeProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)

class SftpSchemeProperties(SchemeProperties):
    def __init__(self, uXml = None):
        SchemeProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.file.SftpSchemeProperties'

        self.passwordAuth = 'true'
        self.keyAuth = 'false'
        self.keyFile = ''
        self.passPhrase = ''
        self.hostKeyChecking = 'ask'
        self.knownHostsFile = ''
        self.configurationSettings = []
        
        if uXml is not None:
            self.passwordAuth = self.getSafeText('passwordAuth')
            self.keyAuth = self.getSafeText('keyAuth')
            self.keyFile = self.getSafeText('keyFile')
            self.passPhrase = self.getSafeText('passPhrase')
            self.hostKeyChecking = self.getSafeText('hostKeyChecking')
            self.knownHostsFile = self.getSafeText('knownHostsFile')

            for e in self.root.findall('./configurationSettings/entry'):
                strings = e.findall('./string')
                self.configurationSettings.append((strings[0].text, strings[1].text))

    def getXML(self, version = "3.12.0"):
        if len(self.configurationSettings) == 0:
            configSet = '<configurationSettings class="linked-hash-map"/>'
        else:
            configSet = '<configurationSettings class="linked-hash-map">'
            for e in self.configurationSettings:
                configSet += '<entry>'
                configSet += f'<string>{e[0]}</string>'
                configSet += f'<string>{e[1]}</string>'
                configSet += '</entry>'
            configSet += '</configurationSettings>'

        xml = f'''
            {getXMLString(self.passwordAuth, "passwordAuth")}
            {getXMLString(self.keyAuth, "keyAuth")}
            {getXMLString(self.keyFile, "keyFile")}
            {getXMLString(self.passPhrase, "passPhrase")}
            {getXMLString(self.hostKeyChecking, "hostKeyChecking")}
            {getXMLString(self.knownHostsFile, "knownHostsFile")}
            {configSet}
            '''
        
        return xml
        
class FTPSchemeProperties(SchemeProperties):
    def __init__(self, uXml = None):
        SchemeProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.file.FTPSchemeProperties'

        self.initalCommands = []

        if uXml is not None:
            for e in self.root.findall('./initialCommands/string'):
                self.initalCommands.append(e.text)

    def getXML(self, version="3.12.0"):
        xml = '<initialCommands/>'
        if len(self.initalCommands) > 0:
            xml = '<initialCommands>'
            for ic in self.initalCommands:
                xml += getXMLString(ic, 'string')
            xml += '</initialCommands>'
        return xml
        
class S3SchemeProperties(SchemeProperties):
    def __init__(self, uXml = None):
        SchemeProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.file.S3SchemeProperties'

        self.useDefaultCredentialProviderChain = 'true'
        self.useTemporaryCredentials = 'false'
        self.duration = '7200'
        self.region = 'us-east-1'
        self.customHeaders = LinkedHashMap()

        if uXml is not None:
            self.useDefaultCredentialProviderChain = self.getSafeText('useDefaultCredentialProviderChain')
            self.useTemporaryCredentials = self.getSafeText('useTemporaryCredentials')
            self.duration = self.getSafeText('duration')
            self.region = self.getSafeText('region')
            self.customHeaders = LinkedHashMap(self.root.find('customHeaders'))

    def getXML(self, version="3.12.0"):
        customHeadersXML = '<customHeaders class="linked-hash-map"/>'
        if len(self.customHeaders.entry) > 0:
            customHeadersXML = '<customHeaders class="linked-hash-map">'
            customHeadersXML += self.customHeaders.getXML(version)
            customHeadersXML += '</customHeaders>'

        xml = f'''
            {getXMLString(self.useDefaultCredentialProviderChain, 'useDefaultCredentialProviderChain')}
            {getXMLString(self.useTemporaryCredentials, 'useTemporaryCredentials')}
            {getXMLString(self.duration, 'duration')}
            {getXMLString(self.region, 'region')}
            {customHeadersXML}
            
        '''
        return xml

class SmbSchemeProperties(SchemeProperties):
    def __init__(self, uXml = None):
        SchemeProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.file.SmbSchemeProperties'

        self.smbMinVersion = 'SMB202'
        self.smbMaxVersion = 'SMB311'

        if uXml is not None:
            self.smbMinVersion = self.getSafeText('smbMinVersion')
            self.smbMaxVersion = self.getSafeText('smbMaxVersion')
    
    def getXML(self, version = "3.12.0"):
        xml = f'''
            {getXMLString(self.smbMinVersion, "smbMinVersion")}
            {getXMLString(self.smbMaxVersion, "smbMaxVersion")}
            '''
        
        return xml
#endregion

#region ModeProperties
class MLLPModeProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.mllpmode.MLLPModeProperties'

        self.pluginPointName = 'MLLP'
        self.startOfMessageBytes = '0B'
        self.endOfMessageBytes = '1C0D'
        self.useMLLPv2 = 'false'
        self.ackBytes = '06'
        self.nackBytes = '15'
        self.maxRetries = '2'

        if uXml is not None:
            self.pluginPointName = self.getSafeText('pluginPointName')
            self.startOfMessageBytes = self.getSafeText('startOfMessageBytes')
            self.endOfMessageBytes = self.getSafeText('endOfMessageBytes')
            self.useMLLPv2 = self.getSafeText('useMLLPv2')
            self.ackBytes = self.getSafeText('ackBytes')
            self.nackBytes = self.getSafeText('nackBytes')
            self.maxRetries = self.getSafeText('maxRetries')

    def getXML(self, version="3.12.0") -> str:
        return f'''
            {getXMLString(self.pluginPointName, "pluginPointName")}
            {getXMLString(self.startOfMessageBytes, "startOfMessageBytes")}
            {getXMLString(self.endOfMessageBytes, "endOfMessageBytes")}
            {getXMLString(self.useMLLPv2, "useMLLPv2")}
            {getXMLString(self.ackBytes, "ackBytes")}
            {getXMLString(self.nackBytes, "nackBytes")}
            {getXMLString(self.maxRetries, "maxRetries")}'''

class FrameModeProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.className = 'com.mirth.connect.model.transmission.framemode.FrameModeProperties'

        self.pluginPointName = ''
        self.startOfMessageBytes = ''
        self.endOfMessageBytes = ''
        
        if uXml is not None:
            self.pluginPointName = self.getSafeText('pluginPointName')
            self.startOfMessageBytes = self.getSafeText('startOfMessageBytes')
            self.endOfMessageBytes = self.getSafeText('endOfMessageBytes')

    def getXML(self, version="3.12.0") -> str:
        return f'''
            {getXMLString(self.pluginPointName, "pluginPointName")}
            {getXMLString(self.startOfMessageBytes, "startOfMessageBytes")}
            {getXMLString(self.endOfMessageBytes, "endOfMessageBytes")}'''
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
        elif c == "com.mirth.connect.connectors.file.FileDispatcherProperties":
            return FileDispatcherProperties
        elif c == "com.mirth.connect.connectors.tcp.TcpDispatcherProperties":
            return TcpDispatcherProperties
        elif c == "com.mirth.connect.connectors.http.HttpDispatcherProperties":
            return HttpDispatcherProperties
        elif c == "com.mirth.connect.connectors.smtp.SmtpDispatcherProperties":
            return SmtpDispatcherProperties
        elif c == "com.mirth.connect.connectors.jdbc.DatabaseDispatcherProperties":
            return DatabaseDispatcherProperties
        elif c == "com.mirth.connect.connectors.ws.WebServiceDispatcherProperties":
            return WebServiceDispatcherProperties
        elif c == "com.mirth.connect.connectors.doc.DocumentDispatcherProperties":
            return DocumentDispatcherProperties
        elif c == "com.mirth.connect.connectors.jms.JmsDispatcherProperties":
            return JmsDispatcherProperties
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
        return None
    
    def modeProperties(c: str) -> Type:
        if c == "com.mirth.connect.plugins.mllpmode.MLLPModeProperties":
            return MLLPModeProperties
        elif c == "com.mirth.connect.model.transmission.framemode.FrameModeProperties":
            return FrameModeProperties
        
    def staticResources(c: str) -> Type:
        if c == "com.mirth.connect.connectors.http.HttpStaticResource":
            return HttpStaticResource
        else:
            return None
#endregion