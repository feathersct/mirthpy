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
            respTransXML += '<responseTransformer version="{}">'.format(version)
            respTransXML += self.responseTransformer.getXML(version)
            respTransXML += '</responseTransformer>'

        xml = ''
        xml += getXMLString(self.metaDataId, "metaDataId")
        xml += getXMLString(self.name, "name")
        xml += '<properties class="{}" version="{}">'.format(self.properties.className, version)
        xml += self.properties.getXML(version)
        xml += '</properties>'
        xml += '<transformer version="{}">'.format(version)
        xml += self.transformer.getXML(version)
        xml += '</transformer>'
        xml += respTransXML
        xml += '<filter version="{}">'.format(version)
        xml += self.filter.getXML(version)
        xml += '</filter>'
        xml += getXMLString(self.transportName, "transportName")
        xml += getXMLString(self.mode, "mode")
        xml += getXMLString(self.enabled, "enabled")
        xml += getXMLString(self.waitForPrevious, "waitForPrevious")

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
        xml = ''
        xml += getXMLString(self.metaDataId, "metaDataId")
        xml += getXMLString(self.name, "name")
        xml += '<properties class="{}" version="{}">'.format(self.properties.className, version)
        xml += self.properties.getXML(version)
        xml += '</properties>'
        xml += '<transformer version="{}">'.format(version)
        xml += self.transformer.getXML(version)
        xml += '</transformer>'
        xml += '<filter version="{}">'.format(version)
        xml += self.filter.getXML(version)
        xml += '</filter>'
        xml += getXMLString(self.properties.transportName, "transportName")
        xml += getXMLString(self.mode, "mode")
        xml += getXMLString(self.enabled, "enabled")
        xml += getXMLString(self.waitForPrevious, "waitForPrevious")

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
        xml = ''
        xml += getXMLString(self.metaDataId, "metaDataId")
        xml += getXMLString(self.name, "name")
        xml += '<properties class="{}" version="{}">'.format(self.properties.className, version)
        xml += self.properties.getXML(version)
        xml += '</properties>'
        xml += '<transformer version="{}">'.format(version)
        xml += self.transformer.getXML(version)
        xml += '</transformer>'
        xml += '<responseTransformer version="{}">'.format(version)
        xml += self.responseTransformer.getXML(version)
        xml += '</responseTransformer>'
        xml += '<filter version="{}">'.format(version)
        xml += self.filter.getXML(version)
        xml += '</filter>'
        xml += getXMLString(self.properties.transportName, "transportName")
        xml += getXMLString(self.mode, "mode")
        xml += getXMLString(self.enabled, "enabled")
        xml += getXMLString(self.waitForPrevious, "waitForPrevious")

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
        xml = ''
        xml += getXMLString(self.responseVariable, "responseVariable")
        xml += getXMLString(self.respondAfterProcessing, "respondAfterProcessing")
        xml += getXMLString(self.processBatch, "processBatch")
        xml += getXMLString(self.firstResponse, "firstResponse")
        xml += getXMLString(self.processingThreads, "processingThreads")
        xml += '<resourceIds class="linked-hash-map">'
        xml += self.resourceIds.getXML(version)
        xml += '</resourceIds>'
        xml += getXMLString(self.queueBufferSize, "queueBufferSize")
                
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
        return '<host>{}</host><port>{}</port>'.format(self.host, self.port)

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
        self.cronJobs = []

        if uXml is not None:
            self.pollingType = self.getSafeText('pollingType')
            self.pollOnStart = self.getSafeText('pollOnStart')
            self.pollingFrequency = self.getSafeText('pollingFrequency')
            self.pollingHour = self.getSafeText('pollingHour')
            self.pollingMinute = self.getSafeText('pollingMinute')
            self.pollConnectorPropertiesAdvanced = PollConnectorPropertiesAdvanced(self.root.find('pollConnectorPropertiesAdvanced'))
            self.cronJobs = []

            for property in self.root.find('cronJobs').findall('./cronProperty'):
                self.cronJobs.append(CronProperty(property))

    def getXML(self, version = '3.12.0'):
        cronXML = "<cronJobs/>"

        if len(self.cronJobs) > 0:
            cronXML = "<cronJobs>"
            for job in self.cronJobs:
                cronXML += job.getXML(version)
            cronXML += "</cronJobs>"

        xml = ''
        xml += getXMLString(self.pollingType, "pollingType")
        xml += getXMLString(self.pollOnStart, "pollOnStart")
        xml += getXMLString(self.pollingFrequency, "pollingFrequency")
        xml += getXMLString(self.pollingHour, "pollingHour")
        xml += getXMLString(self.pollingMinute, "pollingMinute")
        xml += cronXML
        xml += getXMLString(self.pollConnectorPropertiesAdvanced.getXML(version), "pollConnectorPropertiesAdvanced")
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
        xml = getXMLString(self.weekly, "weekly")
        xml += '<inactiveDays>'

        for b in self.inactiveDays:
            xml += getXMLString(str(b).lower(), "boolean")

        xml += '</inactiveDays>'
        xml += getXMLString(self.dayOfMonth, "dayOfMonth")
        xml += getXMLString(self.allDay, "allDay")
        xml += getXMLString(self.startingHour, "startingHour")
        xml += getXMLString(self.startingMinute, "startingMinute")
        xml += getXMLString(self.endingHour, "endingHour")
        xml += getXMLString(self.endingMinute, "endingMinute")

        return xml

class CronProperty(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)

        self.description = ''
        self.expression = ''

        if uXml is not None:
            self.description = self.getSafeText('description')
            self.expression = self.getSafeText('expression')
            

    def getXML(self, version = "3.12.0"):
        xml = "<cronProperty>"
        xml += getXMLString(escape(self.description), "description")
        xml += getXMLString(escape(self.expression), "expression")
        xml += "</cronProperty>"

        return xml


#region ReceiverProperties (SourceConnectorTypes)
class VmReceiverProperties(ConnectorProperties):
    def __init__(self, uXml = None):
        ConnectorProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.vm.VmReceiverProperties'
        self.transportName = 'Channel Reader'

        self.sourceConnectorProperties = SourceConnectorProperties()

        if uXml is not None:
            self.sourceConnectorProperties = SourceConnectorProperties(self.root.find('sourceConnectorProperties'))
            
    def getXML(self, version = '3.12.0'):
        xml = '<pluginProperties/><sourceConnectorProperties version="{}">{}</sourceConnectorProperties>'.format(version, self.sourceConnectorProperties.getXML(version))
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
        xml = '<pluginProperties/>'
        xml += '<listenerConnectorProperties version="{}">'.format(version)
        xml += self.listenerConnectorProperties.getXML(version)
        xml += '</listenerConnectorProperties>'
        xml += '<sourceConnectorProperties version="{}">'.format(version)
        xml += self.sourceConnectorProperties.getXML(version)
        xml += '</sourceConnectorProperties>'
        xml += getXMLString(self.applicationEntity, "applicationEntity")
        xml += getXMLString(self.localHost, "localHost")
        xml += getXMLString(self.localPort, "localPort")
        xml += getXMLString(self.localApplicationEntity, "localApplicationEntity")
        xml += getXMLString(self.soCloseDelay, "soCloseDelay")
        xml += getXMLString(self.releaseTo, "releaseTo")
        xml += getXMLString(self.requestTo, "requestTo")
        xml += getXMLString(self.idleTo, "idleTo")
        xml += getXMLString(self.reaper, "reaper")
        xml += getXMLString(self.rspDelay, "rspDelay")
        xml += getXMLString(self.pdv1, "pdv1")
        xml += getXMLString(self.sndpdulen, "sndpdulen")
        xml += getXMLString(self.rcvpdulen, "rcvpdulen")
        xml += getXMLString(self.asyncc, "async")
        xml += getXMLString(self.bigEndian, "bigEndian")
        xml += getXMLString(self.bufSize, "bufSize")
        xml += getXMLString(self.defts, "defts")
        xml += getXMLString(self.dest, "dest")
        xml += getXMLString(self.nativeData, "nativeData")
        xml += getXMLString(self.sorcvbuf, "sorcvbuf")
        xml += getXMLString(self.sosndbuf, "sosndbuf")
        xml += getXMLString(self.tcpDelay, "tcpDelay")
        xml += getXMLString(self.keyPW, "keyPW")
        xml += getXMLString(self.keyStore, "keyStore")
        xml += getXMLString(self.keyStorePW, "keyStorePW")
        xml += getXMLString(self.noClientAuth, "noClientAuth")
        xml += getXMLString(self.nossl2, "nossl2")
        xml += getXMLString(self.tls, "tls")
        xml += getXMLString(self.trustStore, "trustStore")
        xml += getXMLString(self.trustStorePW, "trustStorePW")
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
        xml = '<pluginProperties/>'
        xml += '<pollConnectorProperties version="{}">'.format(version)
        xml += self.pollConnectorProperties.getXML(version)
        xml += '</pollConnectorProperties>'
        xml += '<sourceConnectorProperties version="{}">'.format(version)
        xml += self.sourceConnectorProperties.getXML(version)
        xml += '</sourceConnectorProperties>'
        xml += getXMLString(self.driver, "driver")
        xml += getXMLString(self.url, "url")
        xml += getXMLString(self.username, "username")
        xml += getXMLString(self.password, "password")
        xml += getXMLString(escape(self.select), "select")
        xml += getXMLString(escape(self.update), "update")
        xml += getXMLString(self.useScript, "useScript")
        xml += getXMLString(self.aggregateResults, "aggregateResults")
        xml += getXMLString(self.cacheResults, "cacheResults")
        xml += getXMLString(self.keepConnectionOpen, "keepConnectionOpen")
        xml += getXMLString(self.updateMode, "updateMode")
        xml += getXMLString(self.retryCount, "retryCount")
        xml += getXMLString(self.retryInterval, "retryInterval")
        xml += getXMLString(self.fetchSize, "fetchSize")
        xml += getXMLString(self.encoding, "encoding")
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

        self.host = ''
        self.fileFilter = '*'
        self.regex = 'false'
        self.directoryRecursion = 'false'
        self.ignoreDot = 'true'
        self.anonymous = 'false'
        self.username = 'anonymous'
        self.password = 'anonymous'
        self.timeout = '10000'
        self.secure = 'true'
        self.passive = 'true'
        self.validateConnection = 'true'
        self.afterProcessingAction = 'NONE'
        self.moveToDirectory = ''
        self.moveToFileName = ''
        self.errprReadingAction = 'NONE'
        self.errorResponseAction = 'AFTER_PROCESSING'
        self.errorMoveToDirectory = ''
        self.errorMoveToFileName = ''
        self.checkFileAge = 'true'
        self.fileAge = '1000'
        self.fileSizeMinimum = '0'
        self.fileSizeMaximum = ''
        self.ignoreFileSizeMaximum = 'true'
        self.sortBy = 'date'
        self.binary = 'false'
        self.charsetEncoding = 'DEFAULT_ENCODING'

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
            schemPropXML = '<schemeProperties class="{}">'.format(self.schemeProperties.className)
            schemPropXML += self.schemeProperties.getXML(version)
            schemPropXML += '</schemeProperties>'

        xml = ''
        xml += '<pluginProperties/>'
        xml += '<pollConnectorProperties version="{}">{}</pollConnectorProperties>'.format(version, self.pollConnectorProperties.getXML(version))
        xml += '<sourceConnectorProperties version="{}">{}</sourceConnectorProperties>'.format(version, self.sourceConnectorProperties.getXML(version))
        xml += getXMLString(self.schemeProperties.scheme, "scheme")
        xml += schemPropXML
        xml += getXMLString(escape(self.host), "host")
        xml += getXMLString(self.fileFilter, "fileFilter")
        xml += getXMLString(self.regex, "regex")
        xml += getXMLString(self.directoryRecursion, "directoryRecursion")
        xml += getXMLString(self.ignoreDot, "ignoreDot")
        xml += getXMLString(self.anonymous, "anonymous")
        xml += getXMLString(self.username, "username")
        xml += getXMLString(self.password, "password")
        xml += getXMLString(self.timeout, "timeout")
        xml += getXMLString(self.secure, "secure")
        xml += getXMLString(self.passive, "passive")
        xml += getXMLString(self.validateConnection, "validateConnection")
        xml += getXMLString(self.afterProcessingAction, "afterProcessingAction")
        xml += getXMLString(self.moveToDirectory, "moveToDirectory")
        xml += getXMLString(self.moveToFileName, "moveToFileName")
        xml += getXMLString(self.errprReadingAction, "errorReadingAction")
        xml += getXMLString(self.errorResponseAction, "errorResponseAction")
        xml += getXMLString(self.errorMoveToDirectory, "errorMoveToDirectory")
        xml += getXMLString(self.errorMoveToFileName, "errorMoveToFileName")
        xml += getXMLString(self.checkFileAge, "checkFileAge")
        xml += getXMLString(self.fileAge, "fileAge")
        xml += getXMLString(self.fileSizeMinimum, "fileSizeMinimum")
        xml += getXMLString(self.fileSizeMaximum, "fileSizeMaximum")
        xml += getXMLString(self.ignoreFileSizeMaximum, "ignoreFileSizeMaximum")
        xml += getXMLString(self.sortBy, "sortBy")
        xml += getXMLString(self.binary, "binary")
        xml += getXMLString(self.charsetEncoding, "charsetEncoding")

        return xml
        
class HttpReceiverProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)

        self.className = 'com.mirth.connect.connectors.http.HttpReceiverProperties'
        self.transportName = 'HTTP Listener'

        self.pluginProperties = []
        self.listenerConnectorProperties = ListenerConnectorProperties()
        self.sourceConnectorProperties = SourceConnectorProperties()
        self.xmlBody = 'false'
        self.parseMultipart = 'true'
        self.includeMetadata = 'false'
        self.binaryMimeTypes = 'application/.*(?<!json|xml)$|image/.*|video/.*|audio/.*'
        self.binaryMimeTypesRegex = 'true'
        self.responseContentType = 'text/plain'
        self.responseDataTypeBinary = 'false'
        self.responseStatusCode = ''
        self.responseHeaders = LinkedHashMap()
        self.responseHeadersVariable = ''
        self.useResponseHeadersVariable = 'false'
        self.charset = 'UTF-8'
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
                pluginPropXML += '<{} version="{}">'''.format(p.className, version)
                pluginPropXML += p.getXML(version)
                pluginPropXML += '</{}>'.format(p.className)
            pluginPropXML += '''</pluginProperties>'''

        staticResXML = '''<staticResources/>'''
        if len(self.staticResources) > 0:
            staticResXML = '''<staticResources>'''
            for p in self.staticResources:
                staticResXML += '<{}>'.format(p.className)
                staticResXML += p.getXML(version)
                staticResXML += '</{}>'.format(p.className)
            staticResXML += '</staticResources>'


        xml = pluginPropXML
        xml += '<listenerConnectorProperties version="{}">{}</listenerConnectorProperties>'.format(version, self.listenerConnectorProperties.getXML(version))
        xml += '<sourceConnectorProperties version="{}">{}</sourceConnectorProperties>'.format(version, self.sourceConnectorProperties.getXML(version))
        xml += getXMLString(self.xmlBody, "xmlBody")
        xml += getXMLString(self.parseMultipart, "parseMultipart")
        xml += getXMLString(self.includeMetadata, "includeMetadata")
        xml += getXMLString(escape(self.binaryMimeTypes), "binaryMimeTypes")
        xml += getXMLString(self.binaryMimeTypesRegex, "binaryMimeTypesRegex")
        xml += getXMLString(self.responseContentType, "responseContentType")
        xml += getXMLString(self.responseDataTypeBinary, "responseDataTypeBinary")
        xml += getXMLString(self.responseStatusCode, "responseStatusCode")
        xml += '<responseHeaders class="linked-hash-map">{}</responseHeaders>'.format(self.responseHeaders.getXML(version))
        xml += getXMLString(self.responseHeadersVariable, "responseHeadersVariable")
        xml += getXMLString(self.useResponseHeadersVariable, "useResponseHeadersVariable")
        xml += getXMLString(self.charset, "charset")
        xml += getXMLString(self.contextPath, "contextPath")
        xml += getXMLString(self.timeout, "timeout")
        xml += staticResXML
        return xml

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
        xml = '<pluginProperties/>'
        xml += getXMLString(self.useJndi, "useJndi")
        xml += getXMLString(self.jndiProviderUrl, "jndiProviderUrl")
        xml += getXMLString(self.jndiInitialContextFactory, "jndiInitialContextFactory")
        xml += getXMLString(self.jndiConnectionFactoryName, "jndiConnectionFactoryName")
        xml += getXMLString(self.connectionFactoryClass, "connectionFactoryClass")
        xml += '<connectionProperties class="linked-hash-map">'
        xml += self.connectionProperties.getXML(version)
        xml += '</connectionProperties>'
        xml += getXMLString(self.username, "username")
        xml += getXMLString(self.password, "password")
        xml += getXMLString(self.destinationName, "destinationName")
        xml += getXMLString(self.topic, "topic")
        xml += getXMLString(self.clientId, "clientId")
        xml += '<sourceConnectorProperties version="{}">'.format(version)
        xml += self.sourceConnectorProperties.getXML(version)
        xml += '</sourceConnectorProperties>'
        xml += getXMLString(self.selector, "selector")
        xml += getXMLString(self.reconnectIntervalMillis, "reconnectIntervalMillis")
        xml += getXMLString(self.durableTopic, "durableTopic")
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
        xml = ''
        xml += '<pluginProperties/>'
        xml += '<pollConnectorProperties version="{}">'.format(version)
        xml += self.pollConnectorProperties.getXML(version)
        xml += '</pollConnectorProperties>'
        xml += '<sourceConnectorProperties version="{}">'.format(version)
        xml += self.sourceConnectorProperties.getXML(version)
        xml += '</sourceConnectorProperties>'
        xml += getXMLString(escape(self.script), "script")
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
        xml = ''
        xml += '<pluginProperties/>'
        xml += '<listenerConnectorProperties version="{}">'.format(version)
        xml += self.listenerConnectorProperties.getXML(version)
        xml += '</listenerConnectorProperties>'
        xml += '<sourceConnectorProperties version="{}">'.format(version)
        xml += self.sourceConnectorProperties.getXML(version)
        xml += '</sourceConnectorProperties>'
        xml += '<transmissionModeProperties class="{}">'.format(self.transmissionModeProperties.className)
        xml += self.transmissionModeProperties.getXML(version)
        xml += '</transmissionModeProperties>'
        xml += getXMLString(self.serverMode, "serverMode")
        xml += getXMLString(self.remoteAddress, "remoteAddress")
        xml += getXMLString(self.remotePort, "remotePort")
        xml += getXMLString(self.overrideLocalBinding, "overrideLocalBinding")
        xml += getXMLString(self.reconnectInterval, "reconnectInterval")
        xml += getXMLString(self.receiveTimeout, "receiveTimeout")
        xml += getXMLString(self.bufferSize, "bufferSize")
        xml += getXMLString(self.maxConnections, "maxConnections")
        xml += getXMLString(self.keepConnectionOpen, "keepConnectionOpen")
        xml += getXMLString(self.dataTypeBinary, "dataTypeBinary")
        xml += getXMLString(self.charsetEncoding, "charsetEncoding")
        xml += getXMLString(self.respondOnNewConnection, "respondOnNewConnection")
        xml += getXMLString(self.responseAddress, "responseAddress")
        xml += getXMLString(self.responsePort, "responsePort")

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
                if prop is not None:
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
                pluginXml += '<{} version="{}">'.format(plugin.className, version)
                pluginXml += plugin.getXML(version)
                pluginXml += '</{}>'.format(plugin.className)
            pluginXml += "</pluginProperties>"

        xml = ''
        xml += pluginXml
        xml += '<listenerConnectorProperties version="{}">'.format(version)
        xml += self.listenerConnectorProperties.getXML(version)
        xml += '</listenerConnectorProperties>'
        xml += '<sourceConnectorProperties version="{}">'.format(version)
        xml += self.sourceConnectorProperties.getXML(version)
        xml += '</sourceConnectorProperties>'
        xml += getXMLString(self.classNameT, "className")
        xml += getXMLString(self.serviceName, "serviceName")
        xml += getXMLString(escape(self.soapBinding), "soapBinding")

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
            mapVar += getXMLString(mv, 'string')

        xml = ''
        xml += '<pluginProperties/>'
        xml += '<destinationConnectorProperties version="{}">'.format(version)
        xml += self.destinationConnectorProperties.getXML(version)
        xml += '</destinationConnectorProperties>'
        xml += getXMLString(self.channelId, "channelId")
        xml += getXMLString(self.channelTemplate, "channelTemplate")
        xml += getXMLString(mapVar, "mapVariables", enclose=False)

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
        xml = ''
        xml += '<pluginProperties/>'
        xml += '<destinationConnectorProperties version="{}">'.format(version)
        xml += self.destinationConnectorProperties.getXML(version)
        xml += '</destinationConnectorProperties>'
        xml += getXMLString(escape(self.script), "script")
        
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
            schemePropXML = '<schemeProperties class="{}">'.format(self.schemeProperties.className)
            schemePropXML += self.schemeProperties.getXML(version)
            schemePropXML += '</schemeProperties>'

        xml = ''
        xml += '<pluginProperties/>'
        xml += '<destinationConnectorProperties version="{}">'.format(version)
        xml += self.destinationConnectorProperties.getXML(version)
        xml += '</destinationConnectorProperties>'
        xml += getXMLString(self.scheme, "scheme")                
        xml += schemePropXML
        xml += getXMLString(escape(self.host), "host")
        xml += getXMLString(escape(self.outputPattern), "outputPattern")
        xml += getXMLString(self.anonymous, "anonymous")
        xml += getXMLString(self.username, "username")
        xml += getXMLString(self.password, "password")
        xml += getXMLString(self.timeout, "timeout")
        xml += getXMLString(self.keepConnectionOpen, "keepConnectionOpen")
        xml += getXMLString(self.maxIdleTime, "maxIdleTime")
        xml += getXMLString(self.secure, "secure")
        xml += getXMLString(self.passive, "passive")
        xml += getXMLString(self.validateConnection, "validateConnection")
        xml += getXMLString(self.outputAppend, "outputAppend")
        xml += getXMLString(self.errorOnExists, "errorOnExists")
        xml += getXMLString(self.temporary, "temporary")
        xml += getXMLString(self.binary, "binary")
        xml += getXMLString(self.charsetEncoding, "charsetEncoding")
        xml += getXMLString(self.template, "template")
        
        return xml

class WebServiceDispatcherProperties(DestinationConnector):
    def __init__(self, uXml = None):
        DestinationConnector.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.ws.WebServiceDispatcherProperties'
        self.transportName = 'Web Service Sender'
        
        self.wsdlUrl = ''
        self.service = ''
        self.port = ''
        self.operation = 'Press Get Operations'
        self.locationURI = ''
        self.socketTimeout = '30000'
        self.useAuthentication = 'false'
        self.username = ''
        self.password = ''
        self.envelope = ''
        self.oneWay = 'false'
        self.headers = LinkedHashMap()
        self.headersVariable = ''
        self.isUseHeadersVariable = 'false'
        self.useMtom = 'false'
        self.attachmentNames = ''
        self.attachmentContents = ''
        self.attachmentTypes = ''
        self.attachmentsVariable = ''
        self.isUseAttachmentsVariable = 'false'
        self.soapAction = ''
        self.wsdlDefinitionMap = LinkedHashMap()


        if uXml is not None:
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
            mapXML += self.wsdlDefinitionMap.getXML(version)
            mapXML += '</map>'

        xml = ''
        xml += '<pluginProperties/>'
        xml += '<destinationConnectorProperties version="{}">'.format(version)
        xml += self.destinationConnectorProperties.getXML(version)
        xml += '</destinationConnectorProperties>'
        xml += getXMLString(self.wsdlUrl, "wsdlUrl")
        xml += getXMLString(self.service, "service")
        xml += getXMLString(self.port, "port")
        xml += getXMLString(self.operation, "operation")
        xml += getXMLString(self.locationURI, "locationURI")
        xml += getXMLString(self.socketTimeout, "socketTimeout")
        xml += getXMLString(self.useAuthentication, "useAuthentication")
        xml += getXMLString(self.username, "username")
        xml += getXMLString(self.password, "password")
        xml += getXMLString(escape(self.envelope), "envelope")
        xml += getXMLString(self.oneWay, "oneWay")
        xml += getXMLString(self.headers.getXML(version), "headers")
        xml += getXMLString(self.headersVariable, "headersVariable")
        xml += getXMLString(self.isUseHeadersVariable, "isUseHeadersVariable")
        xml += getXMLString(self.useMtom, "useMtom")
        xml += getXMLString(self.attachmentNames, "attachmentNames", enclose=False)
        xml += getXMLString(self.attachmentContents, "attachmentContents", enclose=False)
        xml += getXMLString(self.attachmentTypes, "attachmentTypes", enclose=False)
        xml += getXMLString(self.attachmentsVariable, "attachmentsVariable")
        xml += getXMLString(self.isUseAttachmentsVariable, "isUseAttachmentsVariable")
        xml += getXMLString(self.soapAction, "soapAction")
        xml += '<wsdlDefinitionMap>'
        xml += mapXML
        xml += '</wsdlDefinitionMap>'
        
        return xml

class DatabaseDispatcherProperties(DestinationConnector):
    def __init__(self, uXml = None):
        DestinationConnector.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.jdbc.DatabaseDispatcherProperties'
        self.transportName = 'Database Writer'

        self.driver = ''
        self.url = ''
        self.username = ''
        self.password = ''
        self.query = ''
        self.useScript = 'false'

        if uXml is not None:
            self.driver = self.getSafeText('driver')
            self.url = self.getSafeText('url')
            self.username = self.getSafeText('username')
            self.password = self.getSafeText('password')
            self.query = self.getSafeText('query')
            self.useScript = self.getSafeText('useScript')
    
    def getXML(self, version = "3.12.0"):
        xml = ''
        xml += '<pluginProperties/>'
        xml += '<destinationConnectorProperties version="{}">'.format(version)
        xml += self.destinationConnectorProperties.getXML(version)
        xml += '</destinationConnectorProperties>'
        xml += getXMLString(self.driver, "driver")
        xml += getXMLString(self.url, "url")
        xml += getXMLString(self.username, "username")
        xml += getXMLString(self.password, "password")
        xml += getXMLString(escape(self.query), "query")
        xml += getXMLString(self.useScript, "useScript")

        return xml

class DICOMDispatcherProperties(DestinationConnector):
    def __init__(self, uXml = None):
        DestinationConnector.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.dimse.DICOMDispatcherProperties'
        self.transportName = 'DICOM Sender'

        self.host = ''
        self.port = ''
        self.applicationEntity = ''
        self.localHost = ''
        self.localPort = ''
        self.localApplicationEntity = ''
        self.template = '${DICOMMESSAGE}'
        self.acceptTo = '5000'
        self.asyncS = '0'
        self.bufSize = '1'
        self.connectTo = '0'
        self.priority = 'med'
        self.passcode = ''
        self.pdv1 = 'false'
        self.rcvpdulen = '16'
        self.reaper = '10'
        self.releaseTo = '5'
        self.rspTo = '60'
        self.shutdownDelay = '1000'
        self.sndpdulen = '16'
        self.soCloseDelay = '50'
        self.sorcvbuf = '0'
        self.sosndbuf = '0'
        self.stgcmt = 'false'
        self.tcpDelay = 'true'
        self.ts1 = 'false'
        self.uidnegrsp = 'false'
        self.username = ''
        self.keyPW = ''
        self.keyStore = ''
        self.keyStorePW = ''
        self.noClientAuth = 'true'
        self.nossl2 = 'true'
        self.tls = 'notls'
        self.trustStore = ''
        self.trustStorePW = ''

        if uXml is not None:
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
        xml = ''
        xml += '<pluginProperties/>'
        xml += '<destinationConnectorProperties version="{}">'.format(version)
        xml += self.destinationConnectorProperties.getXML(version)
        xml += '</destinationConnectorProperties>'
        xml += getXMLString(escape(self.host), "host")
        xml += getXMLString(self.port, "port")
        xml += getXMLString(self.applicationEntity, "applicationEntity")
        xml += getXMLString(self.localHost, "localHost")
        xml += getXMLString(self.localPort, "localPort")
        xml += getXMLString(self.localApplicationEntity, "localApplicationEntity")
        xml += getXMLString(self.template, "template")
        xml += getXMLString(self.acceptTo, "acceptTo")
        xml += getXMLString(self.asyncS, "async")
        xml += getXMLString(self.bufSize, "bufSize")
        xml += getXMLString(self.connectTo, "connectTo")
        xml += getXMLString(self.priority, "priority")
        xml += getXMLString(self.passcode, "passcode")
        xml += getXMLString(self.pdv1, "pdv1")
        xml += getXMLString(self.rcvpdulen, "rcvpdulen")
        xml += getXMLString(self.reaper, "reaper")
        xml += getXMLString(self.releaseTo, "releaseTo")
        xml += getXMLString(self.rspTo, "rspTo")
        xml += getXMLString(self.shutdownDelay, "shutdownDelay")
        xml += getXMLString(self.sndpdulen, "sndpdulen")
        xml += getXMLString(self.soCloseDelay, "soCloseDelay")
        xml += getXMLString(self.sorcvbuf, "sorcvbuf")
        xml += getXMLString(self.sosndbuf, "sosndbuf")
        xml += getXMLString(self.stgcmt, "stgcmt")
        xml += getXMLString(self.tcpDelay, "tcpDelay")
        xml += getXMLString(self.ts1, "ts1")
        xml += getXMLString(self.uidnegrsp, "uidnegrsp")
        xml += getXMLString(self.username, "username")
        xml += getXMLString(self.keyPW, "keyPW")
        xml += getXMLString(self.keyStore, "keyStore")
        xml += getXMLString(self.keyStorePW, "keyStorePW")
        xml += getXMLString(self.noClientAuth, "noClientAuth")
        xml += getXMLString(self.nossl2, "nossl2")
        xml += getXMLString(self.tls, "tls")
        xml += getXMLString(self.trustStore, "trustStore")
        xml += getXMLString(self.trustStorePW, "trustStorePW")
        
        return xml

class TcpDispatcherProperties(DestinationConnector):
    def __init__(self, uXml = None):
        DestinationConnector.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.tcp.TcpDispatcherProperties'
        self.transportName = 'TCP Sender'
        
        self.transmissionModeProperties = MLLPModeProperties()
        self.serverMode = 'false'
        self.remoteAddress = '127.0.0.1'
        self.remotePort = '6660'
        self.overrideLocalBinding = 'false'
        self.localAddress = '0.0.0.0'
        self.localPort = '0'
        self.sendTimeout = '5000'
        self.bufferSize = '65536'
        self.maxConnections = '10'
        self.keepConnectionOpen = 'false'
        self.checkRemoteHost = 'false'
        self.responseTimeout = '5000'
        self.ignoreResponse = 'false'
        self.queueOnResponseTimeout = 'true'
        self.dataTypeBinary = 'false'
        self.charsetEncoding = 'DEFAULT_ENCODING'
        self.template = '${message.encodedData}'

        if uXml is not None:
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
        xml = ''
        xml += '<pluginProperties/>'
        xml += '<destinationConnectorProperties version="{}">'.format(version)
        xml += self.destinationConnectorProperties.getXML(version)
        xml += '</destinationConnectorProperties>'
        xml += '<transmissionModeProperties class="{}">'.format(self.transmissionModeProperties.className)
        xml += self.transmissionModeProperties.getXML(version)
        xml += '</transmissionModeProperties>'
        xml += getXMLString(self.serverMode, "serverMode")
        xml += getXMLString(self.remoteAddress, "remoteAddress")
        xml += getXMLString(self.remotePort, "remotePort")
        xml += getXMLString(self.overrideLocalBinding, "overrideLocalBinding")
        xml += getXMLString(self.localAddress, "localAddress")
        xml += getXMLString(self.localPort, "localPort")
        xml += getXMLString(self.sendTimeout, "sendTimeout")
        xml += getXMLString(self.bufferSize, "bufferSize")
        xml += getXMLString(self.maxConnections, "maxConnections")
        xml += getXMLString(self.keepConnectionOpen, "keepConnectionOpen")
        xml += getXMLString(self.checkRemoteHost, "checkRemoteHost")
        xml += getXMLString(self.responseTimeout, "responseTimeout")
        xml += getXMLString(self.ignoreResponse, "ignoreResponse")
        xml += getXMLString(self.queueOnResponseTimeout, "queueOnResponseTimeout")
        xml += getXMLString(self.dataTypeBinary, "dataTypeBinary")
        xml += getXMLString(self.charsetEncoding, "charsetEncoding")
        xml += getXMLString(self.template, "template")
        
        return xml

class HttpDispatcherProperties(DestinationConnector):
    def __init__(self, uXml = None):
        DestinationConnector.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.http.HttpDispatcherProperties'
        self.transportName = 'HTTP Sender'
        
        self.host = ''
        self.useProxyServer = 'false'
        self.proxyAddress = ''
        self.proxyPort = ''
        self.method = 'post' #TODO: create enum for this
        self.headers = LinkedHashMap()
        self.parameters = LinkedHashMap()
        self.useHeadersVariable = 'false'
        self.headersVariable = ''
        self.useParametersVariable = 'false'
        self.parametersVariable = ''
        self.responseXmlBody = 'false'
        self.responseParseMultipart = 'true'
        self.responseIncludeMetadata = 'false'
        self.responseBinaryMimeTypes = 'application/.*(?<!json|xml)$|image/.*|video/.*|audio/.*'
        self.responseBinaryMimeTypesRegex = 'true'
        self.multipart = 'false'
        self.useAuthentication = 'false'
        self.authenticationType = 'Basic' #TODO: create enum for this
        self.usePreemptiveAuthentication = 'false'
        self.username = ''
        self.password = ''
        self.content = ''
        self.contentType = 'text/plain'
        self.dataTypeBinary = 'false'
        self.charset = 'UTF-8'
        self.socketTimeout = '30000'

        if uXml is not None:
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
        xml = ''
        xml += '<pluginProperties/>'
        xml += '<destinationConnectorProperties version="{}">'.format(version)
        xml += self.destinationConnectorProperties.getXML(version)
        xml += '</destinationConnectorProperties>'
        xml += getXMLString(escape(self.host), "host")
        xml += getXMLString(self.useProxyServer, "useProxyServer")
        xml += getXMLString(self.proxyAddress, "proxyAddress")
        xml += getXMLString(self.proxyPort, "proxyPort")
        xml += getXMLString(self.method, "method")
        xml += '<headers class="linked-hash-map">'
        xml += self.headers.getXML(version)
        xml += '</headers>'
        xml += '<parameters class="linked-hash-map">'
        xml += self.parameters.getXML(version)
        xml += '</parameters>'
        xml += getXMLString(self.useHeadersVariable, "useHeadersVariable")
        xml += getXMLString(self.headersVariable, "headersVariable")
        xml += getXMLString(self.useParametersVariable, "useParametersVariable")
        xml += getXMLString(self.parametersVariable, "parametersVariable")
        xml += getXMLString(self.responseXmlBody, "responseXmlBody")
        xml += getXMLString(self.responseParseMultipart, "responseParseMultipart")
        xml += getXMLString(self.responseIncludeMetadata, "responseIncludeMetadata")
        xml += getXMLString(escape(self.responseBinaryMimeTypes), "responseBinaryMimeTypes")
        xml += getXMLString(self.responseBinaryMimeTypesRegex, "responseBinaryMimeTypesRegex")
        xml += getXMLString(self.multipart, "multipart")
        xml += getXMLString(self.useAuthentication, "useAuthentication")
        xml += getXMLString(self.authenticationType, "authenticationType")
        xml += getXMLString(self.usePreemptiveAuthentication, "usePreemptiveAuthentication")
        xml += getXMLString(self.username, "username")
        xml += getXMLString(self.password, "password")
        xml += getXMLString(self.content, "content")
        xml += getXMLString(self.contentType, "contentType")
        xml += getXMLString(self.dataTypeBinary, "dataTypeBinary")
        xml += getXMLString(self.charset, "charset")
        xml += getXMLString(self.socketTimeout, "socketTimeout")

        return xml

class SmtpDispatcherProperties(DestinationConnector):
    def __init__(self, uXml = None):
        DestinationConnector.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.smtp.SmtpDispatcherProperties'
        self.transportName = 'SMTP Sender'

        self.attachments = []
        self.smtpHost = ''
        self.smtpPort = '25'
        self.overrideLocalBinding = 'false'
        self.localAddress = '0.0.0.0'
        self.localPort = '0'
        self.timeout = '5000'
        self.encryption = 'none'
        self.authentication = 'false'
        self.username = ''
        self.password = ''
        self.to = ''
        self.fromT = ''
        self.cc = ''
        self.bcc = ''
        self.replyTo = ''
        self.headers = LinkedHashMap()
        self.headersVariable = ''
        self.isUseHeadersVariable = 'false'
        self.subject = ''
        self.charsetEncoding = 'DEFAULT_ENCODING'
        self.html = 'false'
        self.body = ''
        self.attachmentsVariable = ''
        self.isUseAttachmentsVariable = 'false'


        if uXml is not None:
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
            self.attachmentsVariable = self.getSafeText('attachmentsVariable')
            self.isUseAttachmentsVariable = self.getSafeText('isUseAttachmentsVariable')

            for a in self.root.findall('./attachments/com.mirth.connect.connectors.smtp.Attachment'):
                self.attachments.append(Attachment(a))

    def getXML(self, version = "3.12.0"):
        attachXML = "<attachments/>"

        if len(self.attachments) > 0:
            attachXML = "<attachments>"
            for a in self.attachments:
                attachXML += "<{}>".format(a.className)
                attachXML += a.getXML(version)
                attachXML += "</{}>".format(a.className)
            attachXML += "</attachments>"    

        xml = ''
        xml += '<pluginProperties/>'
        xml += '<destinationConnectorProperties version="{}">'.format(version)
        xml += self.destinationConnectorProperties.getXML(version)
        xml += '</destinationConnectorProperties>'
        xml += getXMLString(self.smtpHost, "smtpHost")
        xml += getXMLString(self.smtpPort, "smtpPort")
        xml += getXMLString(self.overrideLocalBinding, "overrideLocalBinding")
        xml += getXMLString(self.localAddress, "localAddress")
        xml += getXMLString(self.localPort, "localPort")
        xml += getXMLString(self.timeout, "timeout")
        xml += getXMLString(self.encryption, "encryption")
        xml += getXMLString(self.authentication, "authentication")
        xml += getXMLString(self.username, "username")
        xml += getXMLString(self.password, "password")
        xml += getXMLString(self.to, "to")
        xml += getXMLString(self.fromT, "from")
        xml += getXMLString(self.cc, "cc")
        xml += getXMLString(self.bcc, "bcc")
        xml += getXMLString(self.replyTo, "replyTo")
        xml += '<headers class="linked-hash-map">'
        xml += self.headers.getXML(version)
        xml += '</headers>'
        xml += getXMLString(self.headersVariable, "headersVariable")
        xml += getXMLString(self.isUseHeadersVariable, "isUseHeadersVariable")
        xml += getXMLString(self.subject, "subject")
        xml += getXMLString(self.charsetEncoding, "charsetEncoding")
        xml += getXMLString(self.html, "html")
        xml += getXMLString(self.body, "body")
        xml += attachXML
        xml += getXMLString(self.attachmentsVariable, "attachmentsVariable")
        xml += getXMLString(self.isUseAttachmentsVariable, "isUseAttachmentsVariable")
            
        return xml

class DocumentDispatcherProperties(DestinationConnector):
    def __init__(self, uXml = None):
        DestinationConnector.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.doc.DocumentDispatcherProperties'
        self.transportName = 'Document Writer'

        self.host = ''
        self.outputPattern = ''
        self.documentType = 'pdf' #TODO: create enum
        self.encrypt = 'false'
        self.output = 'FILE' #TODO: create enum
        self.password = ''
        self.pageWidth = '8.5'
        self.pageHeight = '11'
        self.pageUnit = 'INCHES' #TODO: create enum
        self.template = ''

        if uXml is not None:
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
        xml = ''
        xml += '<pluginProperties/>'
        xml += '<destinationConnectorProperties version="{}">'.format(version)
        xml += self.destinationConnectorProperties.getXML(version)
        xml += '</destinationConnectorProperties>'
        xml += getXMLString(escape(self.host), "host")
        xml += getXMLString(escape(self.outputPattern), "outputPattern")
        xml += getXMLString(self.documentType, "documentType")
        xml += getXMLString(self.encrypt, "encrypt")
        xml += getXMLString(self.output, "output")
        xml += getXMLString(self.password, "password")
        xml += getXMLString(self.pageWidth, "pageWidth")
        xml += getXMLString(self.pageHeight, "pageHeight")
        xml += getXMLString(self.pageUnit, "pageUnit")
        xml += getXMLString(self.template, "template")

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
                
                connectionPropXML += '<entry><string>{}</string>'.format(cp[0])
                connectionPropXML += '<string>{}</string></entry>'.format(cp[1])
            connectionPropXML += '</connectionProperties>'

        xml = ''
        xml += '<pluginProperties/>'
        xml += getXMLString(self.useJndi, "useJndi")
        xml += getXMLString(self.jndiProviderUrl, "jndiProviderUrl")
        xml += getXMLString(self.jndiInitialContextFactory, "jndiInitialContextFactory")
        xml += getXMLString(self.jndiConnectionFactoryName, "jndiConnectionFactoryName")
        xml += getXMLString(self.connectionFactoryClass, "connectionFactoryClass")
        xml += connectionPropXML
        xml += getXMLString(self.username, "username")
        xml += getXMLString(self.password, "password")
        xml += getXMLString(self.destinationName, "destinationName")
        xml += getXMLString(self.topic, "topic")
        xml += getXMLString(self.clientId, "clientId")
        xml += getXMLString(self.template, "template")
        xml += '<destinationConnectorProperties version="{}">'.format(version)
        xml += self.destinationConnectorProperties.getXML(version)
        xml += '</destinationConnectorProperties>'

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
        xml = ''
        xml += getXMLString(self.name, "name")
        xml += getXMLString(self.content, "content")
        xml += getXMLString(self.mimeType, "mimeType")
        return xml
        
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
        xml = getXMLString(self.queueEnabled, "queueEnabled")
        xml += getXMLString(self.sendFirst, "sendFirst")
        xml += getXMLString(self.retryIntervalMillis, "retryIntervalMillis")
        xml += getXMLString(self.regenerateTemplate, "regenerateTemplate")
        xml += getXMLString(self.retryCount, "retryCount")
        xml += getXMLString(self.rotate, "rotate")
        xml += getXMLString(self.includeFilterTransformer, "includeFilterTransformer")
        xml += getXMLString(self.threadCount, "threadCount")
        xml += getXMLString(self.threadAssignmentVariable, "threadAssignmentVariable")
        xml += getXMLString(self.validateResponse, "validateResponse")
        xml += '<resourceIds class="linked-hash-map">'
        xml += self.resourceIds.getXML(version)
        xml += '</resourceIds>'
        xml += getXMLString(self.queueBufferSize, "queueBufferSize")
        xml += getXMLString(self.reattachAttachments, "reattachAttachments")
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
            propXML += getXMLString(prop[0], 'string')
            propXML += getXMLString(prop[1], 'string')
            propXML += "</entry>"
        propXML += "</credentials>"

        xml = getXMLString(self.authType, "authType")
        xml += getXMLString(self.realm, "realm")
        xml += propXML
        xml += getXMLString(self.isUseCredentialsVariable, "isUseCredentialsVariable")
        xml += getXMLString(self.credentialsVariable, "credentialsVariable")

        return xml

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
            propXML += getXMLString(prop[0], 'string')
            propXML += getXMLString(prop[1], 'string')
            propXML += "</entry>"
        propXML += "</credentials>"

        xml = getXMLString(self.authType, "authType")
        xml += getXMLString(self.realm, "realm")
        xml += propXML
        xml += getXMLString(self.isUseCredentialsVariable, "isUseCredentialsVariable")
        xml += getXMLString(self.credentialsVariable, "credentialsVariable")
        xml += getXMLString(self.qopModes, "qopModes")
        xml += getXMLString(self.opaque, "opaque")
        xml += getXMLString(self.algorithm, "authenticatorClass")

        return xml

class JavaScriptHttpAuthProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.httpauth.javascript.JavaScriptHttpAuthProperties'

        self.authType = 'JAVASCRIPT'
        self.script = ''

        if uXml is not None:
            self.authType = self.getSafeText('authType')
            self.script = self.getSafeText('script')

    def getXML(self, version="3.12.0"):
        xml = ""
        xml += getXMLString(self.authType, "authType")
        xml += getXMLString(escape(self.script), "script")
        return xml

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
            propXML += getXMLString(prop[0], 'string')
            propXML += getXMLString(prop[1], 'string')
            propXML += "</entry>"
        propXML += "</properties>"

        xml = ""
        xml += getXMLString(self.authType, "authType")
        xml += getXMLString(self.authenticatorClass, "authenticatorClass")
        xml += propXML

        return xml

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
        xml = ""
        xml += getXMLString(self.authType, "authType")
        xml += getXMLString(self.tokenLocation, "tokenLocation")
        xml += getXMLString(self.locationKey, "locationKey")
        xml += getXMLString(self.verificationURL, "verificationURL")

        return xml

class NoneHttpAuthProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.httpauth.NoneHttpAuthProperties'
        
        self.authType = 'NONE'

        if uXml is not None:
            self.authType = self.getSafeText('authType')
    
    def getXML(self, version="3.12.0"):
        return getXMLString(self.authType, 'authType')
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
        xml = getXMLString(self.contextPath, 'contextPath')
        xml += getXMLString(self.resourceType, 'resourceType')
        xml += getXMLString(self.value, 'value')
        xml += getXMLString(self.contentType, 'contentType')
        return xml

#endregion

#region SchemeProperties
class SchemeProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.scheme = 'FILE'

class SftpSchemeProperties(SchemeProperties):
    def __init__(self, uXml = None):
        SchemeProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.file.SftpSchemeProperties'
        self.scheme = 'SFTP'

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
                configSet += '<string>{}</string>'.format(e[0])
                configSet += '<string>{}</string>'.format(e[1])
                configSet += '</entry>'
            configSet += '</configurationSettings>'

        xml = ''
        xml += getXMLString(self.passwordAuth, "passwordAuth")
        xml += getXMLString(self.keyAuth, "keyAuth")
        xml += getXMLString(self.keyFile, "keyFile")
        xml += getXMLString(self.passPhrase, "passPhrase")
        xml += getXMLString(self.hostKeyChecking, "hostKeyChecking")
        xml += getXMLString(self.knownHostsFile, "knownHostsFile")
        xml += configSet
        
        return xml
        
class FTPSchemeProperties(SchemeProperties):
    def __init__(self, uXml = None):
        SchemeProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.file.FTPSchemeProperties'
        self.scheme = 'FTP'
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
        self.scheme = 'S3'
        
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

        xml = ''
        xml += getXMLString(self.useDefaultCredentialProviderChain, 'useDefaultCredentialProviderChain')
        xml += getXMLString(self.useTemporaryCredentials, 'useTemporaryCredentials')
        xml += getXMLString(self.duration, 'duration')
        xml += getXMLString(self.region, 'region')
        xml += customHeadersXML
            
        return xml

class SmbSchemeProperties(SchemeProperties):
    def __init__(self, uXml = None):
        SchemeProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.connectors.file.SmbSchemeProperties'
        self.scheme = 'SMB'

        self.smbMinVersion = 'SMB202'
        self.smbMaxVersion = 'SMB311'

        if uXml is not None:
            self.smbMinVersion = self.getSafeText('smbMinVersion')
            self.smbMaxVersion = self.getSafeText('smbMaxVersion')
    
    def getXML(self, version = "3.12.0"):
        xml = ''
        xml += getXMLString(self.smbMinVersion, "smbMinVersion")
        xml += getXMLString(self.smbMaxVersion, "smbMaxVersion")
        
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
        xml = ''
        xml += getXMLString(self.pluginPointName, "pluginPointName")
        xml += getXMLString(self.startOfMessageBytes, "startOfMessageBytes")
        xml += getXMLString(self.endOfMessageBytes, "endOfMessageBytes")
        xml += getXMLString(self.useMLLPv2, "useMLLPv2")
        xml += getXMLString(self.ackBytes, "ackBytes")
        xml += getXMLString(self.nackBytes, "nackBytes")
        xml += getXMLString(self.maxRetries, "maxRetries")
        return xml

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
        xml = ''
        xml += getXMLString(self.pluginPointName, "pluginPointName")
        xml += getXMLString(self.startOfMessageBytes, "startOfMessageBytes")
        xml += getXMLString(self.endOfMessageBytes, "endOfMessageBytes")
        return xml
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