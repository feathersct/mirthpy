import re
import unittest
from mirthapi.mirthService import MirthService

class TestChannel(unittest.TestCase):
    instance, username, password, port = "localhost", "test", "test", "8444"
    service = None

    def setUp(self):
        self.service = MirthService(instance=self.instance, username=self.username, password=self.password, port=self.port)
        self.service.open()

    def tearDown(self):
        self.service.close()
        
    def test_channel_sourceConnector(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('blank'))
        version = self.service.version

        xmlNode = re.sub(r'\>[\s]+\<', '><', sourceConnectorXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceChannel.sourceConnector.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

    def test_channel_pollConnProp(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('blank'))
        version = self.service.version

        xmlNode = re.sub(r'\>[\s]+\<', '><', pollConnectorPropXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceChannel.sourceConnector.properties.pollConnectorProperties.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)
    
    def test_channel_sourceConnProp(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('blank'))
        version = self.service.version

        xmlNode = re.sub(r'\>[\s]+\<', '><', sourceConnectorPropXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceChannel.sourceConnector.properties.sourceConnectorProperties.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

    def test_channel_destConnector(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('blank'))
        version = self.service.version

        xmlNode = re.sub(r'\>[\s]+\<', '><', destinationConnectorXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceChannel.destinationConnectors[0].getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

    def test_channel_destConnProp(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('blank'))
        version = self.service.version

        xmlNode = re.sub(r'\>[\s]+\<', '><', destinationConnPropXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceChannel.destinationConnectors[0].properties.destinationConnectorProperties.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

class TestDestination(unittest.TestCase):
    instance, username, password, port = "localhost", "test", "test", "8444"
    service = None

    def setUp(self):
        self.service = MirthService(instance=self.instance, username=self.username, password=self.password, port=self.port)
        self.service.open()

    def tearDown(self):
        self.service.close()

    def test_destination_channelWriter(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('XML_UnitTest'))
        version = self.service.version

        channelWriter = [destination for destination in sourceChannel.destinationConnectors if destination.name == 'Channel Writer']
        channelWriter = channelWriter[0]

        xmlNode = re.sub(r'\>[\s]+\<', '><', channelWriterXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', channelWriter.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

    def test_destination_dicomSender(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('XML_UnitTest'))
        version = self.service.version

        dicomWriter = [destination for destination in sourceChannel.destinationConnectors if destination.name == 'DICOM Sender']
        dicomWriter = dicomWriter[0]

        xmlNode = re.sub(r'\>[\s]+\<', '><', dicomSenderXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', dicomWriter.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

    def test_destination_databaseWriter(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('XML_UnitTest'))
        version = self.service.version

        databaseWriter = [destination for destination in sourceChannel.destinationConnectors if destination.name == 'Database Writer']
        databaseWriter = databaseWriter[0]

        xmlNode = re.sub(r'\>[\s]+\<', '><', databaseWriterXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', databaseWriter.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

    def test_destination_fileWriter(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('XML_UnitTest'))
        version = self.service.version

        fileWriter = [destination for destination in sourceChannel.destinationConnectors if destination.name == 'File Writer']
        fileWriter = fileWriter[0]

        xmlNode = re.sub(r'\>[\s]+\<', '><', fileWriterXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', fileWriter.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

class TestServer(unittest.TestCase):
    instance, username, password, port = "localhost", "test", "test", "8444"
    service = None

    def setUp(self):
        self.service = MirthService(instance=self.instance, username=self.username, password=self.password, port=self.port)
        self.service.open()

    def tearDown(self):
        self.service.close()
        
    def test_destination_tags(self):

        sourceChannel = self.service.getTags()
        version = self.service.version

        xmlNode = re.sub(r'\>[\s]+\<', '><', channelTagXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceChannel.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)


#region XML
blankXML = '''<channel version="4.1.1">
  <id>a33c919f-53c4-4042-b6c8-7ade0f06d8cb</id>
  <nextMetaDataId>2</nextMetaDataId>
  <name>blank</name>
  <description></description>
  <revision>6</revision>
  <sourceConnector version="4.1.1">
    <metaDataId>0</metaDataId>
    <name>sourceConnector</name>
    <properties class="com.mirth.connect.connectors.file.FileReceiverProperties" version="4.1.1">
      <pluginProperties/>
      <pollConnectorProperties version="4.1.1">
        <pollingType>INTERVAL</pollingType>
        <pollOnStart>false</pollOnStart>
        <pollingFrequency>5000</pollingFrequency>
        <pollingHour>0</pollingHour>
        <pollingMinute>0</pollingMinute>
        <cronJobs/>
        <pollConnectorPropertiesAdvanced>
          <weekly>true</weekly>
          <inactiveDays>
            <boolean>false</boolean>
            <boolean>false</boolean>
            <boolean>false</boolean>
            <boolean>false</boolean>
            <boolean>false</boolean>
            <boolean>false</boolean>
            <boolean>false</boolean>
            <boolean>false</boolean>
          </inactiveDays>
          <dayOfMonth>1</dayOfMonth>
          <allDay>true</allDay>
          <startingHour>8</startingHour>
          <startingMinute>0</startingMinute>
          <endingHour>17</endingHour>
          <endingMinute>0</endingMinute>
        </pollConnectorPropertiesAdvanced>
      </pollConnectorProperties>
      <sourceConnectorProperties version="4.1.1">
        <responseVariable>None</responseVariable>
        <respondAfterProcessing>true</respondAfterProcessing>
        <processBatch>false</processBatch>
        <firstResponse>false</firstResponse>
        <processingThreads>1</processingThreads>
        <resourceIds class="linked-hash-map">
          <entry>
            <string>Default Resource</string>
            <string>[Default Resource]</string>
          </entry>
        </resourceIds>
        <queueBufferSize>1000</queueBufferSize>
      </sourceConnectorProperties>
      <scheme>FILE</scheme>
      <host></host>
      <fileFilter>*</fileFilter>
      <regex>false</regex>
      <directoryRecursion>false</directoryRecursion>
      <ignoreDot>true</ignoreDot>
      <anonymous>true</anonymous>
      <username>anonymous</username>
      <password>anonymous</password>
      <timeout>10000</timeout>
      <secure>true</secure>
      <passive>true</passive>
      <validateConnection>true</validateConnection>
      <afterProcessingAction>NONE</afterProcessingAction>
      <moveToDirectory></moveToDirectory>
      <moveToFileName></moveToFileName>
      <errorReadingAction>NONE</errorReadingAction>
      <errorResponseAction>AFTER_PROCESSING</errorResponseAction>
      <errorMoveToDirectory></errorMoveToDirectory>
      <errorMoveToFileName></errorMoveToFileName>
      <checkFileAge>true</checkFileAge>
      <fileAge>1000</fileAge>
      <fileSizeMinimum>0</fileSizeMinimum>
      <fileSizeMaximum></fileSizeMaximum>
      <ignoreFileSizeMaximum>true</ignoreFileSizeMaximum>
      <sortBy>date</sortBy>
      <binary>false</binary>
      <charsetEncoding>DEFAULT_ENCODING</charsetEncoding>
    </properties>
    <transformer version="4.1.1">
      <elements/>
      <inboundDataType>HL7V2</inboundDataType>
      <outboundDataType>HL7V2</outboundDataType>
      <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
          <handleRepetitions>true</handleRepetitions>
          <handleSubcomponents>true</handleSubcomponents>
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <stripNamespaces>false</stripNamespaces>
          <segmentDelimiter>\r</segmentDelimiter>
          <convertLineBreaks>true</convertLineBreaks>
        </serializationProperties>
        <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <segmentDelimiter>\r</segmentDelimiter>
        </deserializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
          <splitType>MSH_Segment</splitType>
          <batchScript></batchScript>
        </batchProperties>
        <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
          <segmentDelimiter>\r</segmentDelimiter>
          <successfulACKCode>AA</successfulACKCode>
          <successfulACKMessage></successfulACKMessage>
          <errorACKCode>AE</errorACKCode>
          <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
          <rejectedACKCode>AR</rejectedACKCode>
          <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
          <msh15ACKAccept>false</msh15ACKAccept>
          <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
        </responseGenerationProperties>
        <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
          <successfulACKCode>AA,CA</successfulACKCode>
          <errorACKCode>AE,CE</errorACKCode>
          <rejectedACKCode>AR,CR</rejectedACKCode>
          <validateMessageControlId>true</validateMessageControlId>
          <originalMessageControlId>Destination_Encoded</originalMessageControlId>
          <originalIdMapVariable></originalIdMapVariable>
        </responseValidationProperties>
      </inboundProperties>
      <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
          <handleRepetitions>true</handleRepetitions>
          <handleSubcomponents>true</handleSubcomponents>
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <stripNamespaces>false</stripNamespaces>
          <segmentDelimiter>\r</segmentDelimiter>
          <convertLineBreaks>true</convertLineBreaks>
        </serializationProperties>
        <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <segmentDelimiter>\r</segmentDelimiter>
        </deserializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
          <splitType>MSH_Segment</splitType>
          <batchScript></batchScript>
        </batchProperties>
        <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
          <segmentDelimiter>\r</segmentDelimiter>
          <successfulACKCode>AA</successfulACKCode>
          <successfulACKMessage></successfulACKMessage>
          <errorACKCode>AE</errorACKCode>
          <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
          <rejectedACKCode>AR</rejectedACKCode>
          <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
          <msh15ACKAccept>false</msh15ACKAccept>
          <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
        </responseGenerationProperties>
        <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
          <successfulACKCode>AA,CA</successfulACKCode>
          <errorACKCode>AE,CE</errorACKCode>
          <rejectedACKCode>AR,CR</rejectedACKCode>
          <validateMessageControlId>true</validateMessageControlId>
          <originalMessageControlId>Destination_Encoded</originalMessageControlId>
          <originalIdMapVariable></originalIdMapVariable>
        </responseValidationProperties>
      </outboundProperties>
    </transformer>
    <filter version="4.1.1">
      <elements/>
    </filter>
    <transportName>File Reader</transportName>
    <mode>SOURCE</mode>
    <enabled>true</enabled>
    <waitForPrevious>true</waitForPrevious>
  </sourceConnector>
  <destinationConnectors>
    <connector version="4.1.1">
      <metaDataId>1</metaDataId>
      <name>Destination 1</name>
      <properties class="com.mirth.connect.connectors.vm.VmDispatcherProperties" version="4.1.1">
        <pluginProperties/>
        <destinationConnectorProperties version="4.1.1">
          <queueEnabled>false</queueEnabled>
          <sendFirst>false</sendFirst>
          <retryIntervalMillis>10000</retryIntervalMillis>
          <regenerateTemplate>false</regenerateTemplate>
          <retryCount>0</retryCount>
          <rotate>false</rotate>
          <includeFilterTransformer>false</includeFilterTransformer>
          <threadCount>1</threadCount>
          <threadAssignmentVariable></threadAssignmentVariable>
          <validateResponse>false</validateResponse>
          <resourceIds class="linked-hash-map">
            <entry>
              <string>Default Resource</string>
              <string>[Default Resource]</string>
            </entry>
          </resourceIds>
          <queueBufferSize>1000</queueBufferSize>
          <reattachAttachments>true</reattachAttachments>
        </destinationConnectorProperties>
        <channelId>none</channelId>
        <channelTemplate>${message.encodedData}</channelTemplate>
        <mapVariables/>
      </properties>
      <transformer version="4.1.1">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </transformer>
      <responseTransformer version="4.1.1">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </responseTransformer>
      <filter version="4.1.1">
        <elements/>
      </filter>
      <transportName>Channel Writer</transportName>
      <mode>DESTINATION</mode>
      <enabled>true</enabled>
      <waitForPrevious>true</waitForPrevious>
    </connector>
  </destinationConnectors>
  <preprocessingScript>// Modify the message variable below to pre process data
return message;</preprocessingScript>
  <postprocessingScript>// This script executes once after a message has been processed
// Responses returned from here will be stored as &quot;Postprocessor&quot; in the response map
return;</postprocessingScript>
  <deployScript>// This script executes once when the channel is deployed
// You only have access to the globalMap and globalChannelMap here to persist data
return;</deployScript>
  <undeployScript>// This script executes once when the channel is undeployed
// You only have access to the globalMap and globalChannelMap here to persist data
return;</undeployScript>
  <properties version="4.1.1">
    <clearGlobalChannelMap>true</clearGlobalChannelMap>
    <messageStorageMode>DEVELOPMENT</messageStorageMode>
    <encryptData>false</encryptData>
    <removeContentOnCompletion>false</removeContentOnCompletion>
    <removeOnlyFilteredOnCompletion>false</removeOnlyFilteredOnCompletion>
    <removeAttachmentsOnCompletion>false</removeAttachmentsOnCompletion>
    <initialState>STARTED</initialState>
    <storeAttachments>true</storeAttachments>
    <metaDataColumns>
      <metaDataColumn>
        <name>SOURCE</name>
        <type>STRING</type>
        <mappingName>mirth_source</mappingName>
      </metaDataColumn>
      <metaDataColumn>
        <name>TYPE</name>
        <type>STRING</type>
        <mappingName>mirth_type</mappingName>
      </metaDataColumn>
    </metaDataColumns>
    <attachmentProperties version="4.1.1">
      <type>None</type>
      <properties/>
    </attachmentProperties>
    <resourceIds class="linked-hash-map">
      <entry>
        <string>Default Resource</string>
        <string>[Default Resource]</string>
      </entry>
    </resourceIds>
  </properties>
  <exportData>
    <metadata>
      <enabled>false</enabled>
      <lastModified>
        <time>1678394948646</time>
        <timezone>America/New_York</timezone>
      </lastModified>
      <pruningSettings>
        <archiveEnabled>true</archiveEnabled>
        <pruneErroredMessages>false</pruneErroredMessages>
      </pruningSettings>
    </metadata>
  </exportData>
</channel>'''
destinationConnPropXML = '''<queueEnabled>false</queueEnabled>
          <sendFirst>false</sendFirst>
          <retryIntervalMillis>10000</retryIntervalMillis>
          <regenerateTemplate>false</regenerateTemplate>
          <retryCount>0</retryCount>
          <rotate>false</rotate>
          <includeFilterTransformer>false</includeFilterTransformer>
          <threadCount>1</threadCount>
          <threadAssignmentVariable></threadAssignmentVariable>
          <validateResponse>false</validateResponse>
          <resourceIds class="linked-hash-map">
            <entry>
              <string>Default Resource</string>
              <string>[Default Resource]</string>
            </entry>
          </resourceIds>
          <queueBufferSize>1000</queueBufferSize>
          <reattachAttachments>true</reattachAttachments>'''
destinationConnectorXML = '''<metaDataId>1</metaDataId>
      <name>Destination 1</name>
      <properties class="com.mirth.connect.connectors.vm.VmDispatcherProperties" version="4.1.1">
        <pluginProperties/>
        <destinationConnectorProperties version="4.1.1">
          <queueEnabled>false</queueEnabled>
          <sendFirst>false</sendFirst>
          <retryIntervalMillis>10000</retryIntervalMillis>
          <regenerateTemplate>false</regenerateTemplate>
          <retryCount>0</retryCount>
          <rotate>false</rotate>
          <includeFilterTransformer>false</includeFilterTransformer>
          <threadCount>1</threadCount>
          <threadAssignmentVariable></threadAssignmentVariable>
          <validateResponse>false</validateResponse>
          <resourceIds class="linked-hash-map">
            <entry>
              <string>Default Resource</string>
              <string>[Default Resource]</string>
            </entry>
          </resourceIds>
          <queueBufferSize>1000</queueBufferSize>
          <reattachAttachments>true</reattachAttachments>
        </destinationConnectorProperties>
        <channelId>none</channelId>
        <channelTemplate>${message.encodedData}</channelTemplate>
        <mapVariables/>
      </properties>
      <transformer version="4.1.1">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </transformer>
      <responseTransformer version="4.1.1">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </responseTransformer>
      <filter version="4.1.1">
        <elements/>
      </filter>
      <transportName>Channel Writer</transportName>
      <mode>DESTINATION</mode>
      <enabled>true</enabled>
      <waitForPrevious>true</waitForPrevious>'''
pollConnectorPropXML = '''<pollingType>INTERVAL</pollingType>
        <pollOnStart>false</pollOnStart>
        <pollingFrequency>5000</pollingFrequency>
        <pollingHour>0</pollingHour>
        <pollingMinute>0</pollingMinute>
        <cronJobs/>
        <pollConnectorPropertiesAdvanced>
          <weekly>true</weekly>
          <inactiveDays>
            <boolean>false</boolean>
            <boolean>false</boolean>
            <boolean>false</boolean>
            <boolean>false</boolean>
            <boolean>false</boolean>
            <boolean>false</boolean>
            <boolean>false</boolean>
            <boolean>false</boolean>
          </inactiveDays>
          <dayOfMonth>1</dayOfMonth>
          <allDay>true</allDay>
          <startingHour>8</startingHour>
          <startingMinute>0</startingMinute>
          <endingHour>17</endingHour>
          <endingMinute>0</endingMinute>
        </pollConnectorPropertiesAdvanced>'''
sourceConnectorPropXML = '''<responseVariable>None</responseVariable>
        <respondAfterProcessing>true</respondAfterProcessing>
        <processBatch>false</processBatch>
        <firstResponse>false</firstResponse>
        <processingThreads>1</processingThreads>
        <resourceIds class="linked-hash-map">
          <entry>
            <string>Default Resource</string>
            <string>[Default Resource]</string>
          </entry>
        </resourceIds>
        <queueBufferSize>1000</queueBufferSize>'''
sourceConnectorXML = '''<metaDataId>0</metaDataId>
    <name>sourceConnector</name>
    <properties class="com.mirth.connect.connectors.file.FileReceiverProperties" version="4.1.1">
      <pluginProperties/>
      <pollConnectorProperties version="4.1.1">
        <pollingType>INTERVAL</pollingType>
        <pollOnStart>false</pollOnStart>
        <pollingFrequency>5000</pollingFrequency>
        <pollingHour>0</pollingHour>
        <pollingMinute>0</pollingMinute>
        <cronJobs/>
        <pollConnectorPropertiesAdvanced>
          <weekly>true</weekly>
          <inactiveDays>
            <boolean>false</boolean>
            <boolean>false</boolean>
            <boolean>false</boolean>
            <boolean>false</boolean>
            <boolean>false</boolean>
            <boolean>false</boolean>
            <boolean>false</boolean>
            <boolean>false</boolean>
          </inactiveDays>
          <dayOfMonth>1</dayOfMonth>
          <allDay>true</allDay>
          <startingHour>8</startingHour>
          <startingMinute>0</startingMinute>
          <endingHour>17</endingHour>
          <endingMinute>0</endingMinute>
        </pollConnectorPropertiesAdvanced>
      </pollConnectorProperties>
      <sourceConnectorProperties version="4.1.1">
        <responseVariable>None</responseVariable>
        <respondAfterProcessing>true</respondAfterProcessing>
        <processBatch>false</processBatch>
        <firstResponse>false</firstResponse>
        <processingThreads>1</processingThreads>
        <resourceIds class="linked-hash-map">
          <entry>
            <string>Default Resource</string>
            <string>[Default Resource]</string>
          </entry>
        </resourceIds>
        <queueBufferSize>1000</queueBufferSize>
      </sourceConnectorProperties>
      <scheme>FILE</scheme>
      <host></host>
      <fileFilter>*</fileFilter>
      <regex>false</regex>
      <directoryRecursion>false</directoryRecursion>
      <ignoreDot>true</ignoreDot>
      <anonymous>true</anonymous>
      <username>anonymous</username>
      <password>anonymous</password>
      <timeout>10000</timeout>
      <secure>true</secure>
      <passive>true</passive>
      <validateConnection>true</validateConnection>
      <afterProcessingAction>NONE</afterProcessingAction>
      <moveToDirectory></moveToDirectory>
      <moveToFileName></moveToFileName>
      <errorReadingAction>NONE</errorReadingAction>
      <errorResponseAction>AFTER_PROCESSING</errorResponseAction>
      <errorMoveToDirectory></errorMoveToDirectory>
      <errorMoveToFileName></errorMoveToFileName>
      <checkFileAge>true</checkFileAge>
      <fileAge>1000</fileAge>
      <fileSizeMinimum>0</fileSizeMinimum>
      <fileSizeMaximum></fileSizeMaximum>
      <ignoreFileSizeMaximum>true</ignoreFileSizeMaximum>
      <sortBy>date</sortBy>
      <binary>false</binary>
      <charsetEncoding>DEFAULT_ENCODING</charsetEncoding>
    </properties>
    <transformer version="4.1.1">
      <elements/>
      <inboundDataType>HL7V2</inboundDataType>
      <outboundDataType>HL7V2</outboundDataType>
      <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
          <handleRepetitions>true</handleRepetitions>
          <handleSubcomponents>true</handleSubcomponents>
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <stripNamespaces>false</stripNamespaces>
          <segmentDelimiter>\\r</segmentDelimiter>
          <convertLineBreaks>true</convertLineBreaks>
        </serializationProperties>
        <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <segmentDelimiter>\\r</segmentDelimiter>
        </deserializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
          <splitType>MSH_Segment</splitType>
          <batchScript></batchScript>
        </batchProperties>
        <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
          <segmentDelimiter>\\r</segmentDelimiter>
          <successfulACKCode>AA</successfulACKCode>
          <successfulACKMessage></successfulACKMessage>
          <errorACKCode>AE</errorACKCode>
          <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
          <rejectedACKCode>AR</rejectedACKCode>
          <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
          <msh15ACKAccept>false</msh15ACKAccept>
          <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
        </responseGenerationProperties>
        <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
          <successfulACKCode>AA,CA</successfulACKCode>
          <errorACKCode>AE,CE</errorACKCode>
          <rejectedACKCode>AR,CR</rejectedACKCode>
          <validateMessageControlId>true</validateMessageControlId>
          <originalMessageControlId>Destination_Encoded</originalMessageControlId>
          <originalIdMapVariable></originalIdMapVariable>
        </responseValidationProperties>
      </inboundProperties>
      <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
          <handleRepetitions>true</handleRepetitions>
          <handleSubcomponents>true</handleSubcomponents>
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <stripNamespaces>false</stripNamespaces>
          <segmentDelimiter>\\r</segmentDelimiter>
          <convertLineBreaks>true</convertLineBreaks>
        </serializationProperties>
        <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <segmentDelimiter>\\r</segmentDelimiter>
        </deserializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
          <splitType>MSH_Segment</splitType>
          <batchScript></batchScript>
        </batchProperties>
        <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
          <segmentDelimiter>\\r</segmentDelimiter>
          <successfulACKCode>AA</successfulACKCode>
          <successfulACKMessage></successfulACKMessage>
          <errorACKCode>AE</errorACKCode>
          <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
          <rejectedACKCode>AR</rejectedACKCode>
          <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
          <msh15ACKAccept>false</msh15ACKAccept>
          <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
        </responseGenerationProperties>
        <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
          <successfulACKCode>AA,CA</successfulACKCode>
          <errorACKCode>AE,CE</errorACKCode>
          <rejectedACKCode>AR,CR</rejectedACKCode>
          <validateMessageControlId>true</validateMessageControlId>
          <originalMessageControlId>Destination_Encoded</originalMessageControlId>
          <originalIdMapVariable></originalIdMapVariable>
        </responseValidationProperties>
      </outboundProperties>
    </transformer>
    <filter version="4.1.1">
      <elements/>
    </filter>
    <transportName>File Reader</transportName>
    <mode>SOURCE</mode>
    <enabled>true</enabled>
    <waitForPrevious>true</waitForPrevious>''' 

# Source Connectors

# Destination Connectors
fileWriterXML = '''<metaDataId>5</metaDataId>
      <name>File Writer</name>
      <properties class="com.mirth.connect.connectors.file.FileDispatcherProperties" version="4.1.1">
        <pluginProperties/>
        <destinationConnectorProperties version="4.1.1">
          <queueEnabled>false</queueEnabled>
          <sendFirst>false</sendFirst>
          <retryIntervalMillis>10000</retryIntervalMillis>
          <regenerateTemplate>false</regenerateTemplate>
          <retryCount>0</retryCount>
          <rotate>false</rotate>
          <includeFilterTransformer>false</includeFilterTransformer>
          <threadCount>1</threadCount>
          <threadAssignmentVariable></threadAssignmentVariable>
          <validateResponse>false</validateResponse>
          <resourceIds class="linked-hash-map">
            <entry>
              <string>Default Resource</string>
              <string>[Default Resource]</string>
            </entry>
          </resourceIds>
          <queueBufferSize>1000</queueBufferSize>
          <reattachAttachments>true</reattachAttachments>
        </destinationConnectorProperties>
        <scheme>SFTP</scheme>
        <schemeProperties class="com.mirth.connect.connectors.file.SftpSchemeProperties">
          <passwordAuth>true</passwordAuth>
          <keyAuth>false</keyAuth>
          <keyFile></keyFile>
          <passPhrase></passPhrase>
          <hostKeyChecking>ask</hostKeyChecking>
          <knownHostsFile></knownHostsFile>
          <configurationSettings class="linked-hash-map"/>
        </schemeProperties>
        <host>www.google.com/sftpexample</host>
        <outputPattern>test.txt</outputPattern>
        <anonymous>false</anonymous>
        <username>anonymous</username>
        <password>anonymous</password>
        <timeout>10000</timeout>
        <keepConnectionOpen>true</keepConnectionOpen>
        <maxIdleTime>0</maxIdleTime>
        <secure>true</secure>
        <passive>true</passive>
        <validateConnection>true</validateConnection>
        <outputAppend>true</outputAppend>
        <errorOnExists>false</errorOnExists>
        <temporary>false</temporary>
        <binary>false</binary>
        <charsetEncoding>DEFAULT_ENCODING</charsetEncoding>
        <template>message</template>
      </properties>
      <transformer version="4.1.1">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </transformer>
      <responseTransformer version="4.1.1">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </responseTransformer>
      <filter version="4.1.1">
        <elements/>
      </filter>
      <transportName>File Writer</transportName>
      <mode>DESTINATION</mode>
      <enabled>true</enabled>
      <waitForPrevious>true</waitForPrevious>'''
documentWriterXML = '''<metaDataId>4</metaDataId>
      <name>Document Writer</name>
      <properties class="com.mirth.connect.connectors.doc.DocumentDispatcherProperties" version="4.1.1">
        <pluginProperties/>
        <destinationConnectorProperties version="4.1.1">
          <queueEnabled>false</queueEnabled>
          <sendFirst>false</sendFirst>
          <retryIntervalMillis>10000</retryIntervalMillis>
          <regenerateTemplate>false</regenerateTemplate>
          <retryCount>0</retryCount>
          <rotate>false</rotate>
          <includeFilterTransformer>false</includeFilterTransformer>
          <threadCount>1</threadCount>
          <threadAssignmentVariable></threadAssignmentVariable>
          <validateResponse>false</validateResponse>
          <resourceIds class="linked-hash-map">
            <entry>
              <string>Default Resource</string>
              <string>[Default Resource]</string>
            </entry>
          </resourceIds>
          <queueBufferSize>1000</queueBufferSize>
          <reattachAttachments>true</reattachAttachments>
        </destinationConnectorProperties>
        <host>C:/</host>
        <outputPattern>test.pdf</outputPattern>
        <documentType>pdf</documentType>
        <encrypt>false</encrypt>
        <output>FILE</output>
        <password></password>
        <pageWidth>8.5</pageWidth>
        <pageHeight>11</pageHeight>
        <pageUnit>INCHES</pageUnit>
        <template>pdf template</template>
      </properties>
      <transformer version="4.1.1">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </transformer>
      <responseTransformer version="4.1.1">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </responseTransformer>
      <filter version="4.1.1">
        <elements/>
      </filter>
      <transportName>Document Writer</transportName>
      <mode>DESTINATION</mode>
      <enabled>true</enabled>
      <waitForPrevious>true</waitForPrevious>'''
databaseWriterXML = '''<metaDataId>3</metaDataId>
      <name>Database Writer</name>
      <properties class="com.mirth.connect.connectors.jdbc.DatabaseDispatcherProperties" version="4.1.1">
        <pluginProperties/>
        <destinationConnectorProperties version="4.1.1">
          <queueEnabled>false</queueEnabled>
          <sendFirst>false</sendFirst>
          <retryIntervalMillis>10000</retryIntervalMillis>
          <regenerateTemplate>false</regenerateTemplate>
          <retryCount>0</retryCount>
          <rotate>false</rotate>
          <includeFilterTransformer>false</includeFilterTransformer>
          <threadCount>1</threadCount>
          <threadAssignmentVariable></threadAssignmentVariable>
          <validateResponse>false</validateResponse>
          <resourceIds class="linked-hash-map">
            <entry>
              <string>Default Resource</string>
              <string>[Default Resource]</string>
            </entry>
          </resourceIds>
          <queueBufferSize>1000</queueBufferSize>
          <reattachAttachments>true</reattachAttachments>
        </destinationConnectorProperties>
        <driver>org.postgresql.Driver</driver>
        <url>www.google.com</url>
        <username></username>
        <password></password>
        <query>select &quot;hello&quot;;</query>
        <useScript>false</useScript>
      </properties>
      <transformer version="4.1.1">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </transformer>
      <responseTransformer version="4.1.1">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </responseTransformer>
      <filter version="4.1.1">
        <elements/>
      </filter>
      <transportName>Database Writer</transportName>
      <mode>DESTINATION</mode>
      <enabled>true</enabled>
      <waitForPrevious>true</waitForPrevious>'''
dicomSenderXML = '''<metaDataId>2</metaDataId>
      <name>DICOM Sender</name>
      <properties class="com.mirth.connect.connectors.dimse.DICOMDispatcherProperties" version="4.1.1">
        <pluginProperties/>
        <destinationConnectorProperties version="4.1.1">
          <queueEnabled>false</queueEnabled>
          <sendFirst>false</sendFirst>
          <retryIntervalMillis>10000</retryIntervalMillis>
          <regenerateTemplate>false</regenerateTemplate>
          <retryCount>0</retryCount>
          <rotate>false</rotate>
          <includeFilterTransformer>false</includeFilterTransformer>
          <threadCount>1</threadCount>
          <threadAssignmentVariable></threadAssignmentVariable>
          <validateResponse>false</validateResponse>
          <resourceIds class="linked-hash-map">
            <entry>
              <string>Default Resource</string>
              <string>[Default Resource]</string>
            </entry>
          </resourceIds>
          <queueBufferSize>1000</queueBufferSize>
          <reattachAttachments>true</reattachAttachments>
        </destinationConnectorProperties>
        <host>127.0.0.1</host>
        <port>104</port>
        <applicationEntity></applicationEntity>
        <localHost></localHost>
        <localPort></localPort>
        <localApplicationEntity></localApplicationEntity>
        <template>${DICOMMESSAGE}</template>
        <acceptTo>5000</acceptTo>
        <async>0</async>
        <bufSize>1</bufSize>
        <connectTo>0</connectTo>
        <priority>med</priority>
        <passcode></passcode>
        <pdv1>false</pdv1>
        <rcvpdulen>16</rcvpdulen>
        <reaper>10</reaper>
        <releaseTo>5</releaseTo>
        <rspTo>60</rspTo>
        <shutdownDelay>1000</shutdownDelay>
        <sndpdulen>16</sndpdulen>
        <soCloseDelay>50</soCloseDelay>
        <sorcvbuf>0</sorcvbuf>
        <sosndbuf>0</sosndbuf>
        <stgcmt>false</stgcmt>
        <tcpDelay>true</tcpDelay>
        <ts1>false</ts1>
        <uidnegrsp>false</uidnegrsp>
        <username></username>
        <keyPW></keyPW>
        <keyStore></keyStore>
        <keyStorePW></keyStorePW>
        <noClientAuth>true</noClientAuth>
        <nossl2>true</nossl2>
        <tls>notls</tls>
        <trustStore></trustStore>
        <trustStorePW></trustStorePW>
      </properties>
      <transformer version="4.1.1">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </transformer>
      <responseTransformer version="4.1.1">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </responseTransformer>
      <filter version="4.1.1">
        <elements/>
      </filter>
      <transportName>DICOM Sender</transportName>
      <mode>DESTINATION</mode>
      <enabled>true</enabled>
      <waitForPrevious>true</waitForPrevious>'''
channelWriterXML = '''<metaDataId>1</metaDataId>
      <name>Channel Writer</name>
      <properties class="com.mirth.connect.connectors.vm.VmDispatcherProperties" version="4.1.1">
        <pluginProperties/>
        <destinationConnectorProperties version="4.1.1">
          <queueEnabled>false</queueEnabled>
          <sendFirst>false</sendFirst>
          <retryIntervalMillis>10000</retryIntervalMillis>
          <regenerateTemplate>false</regenerateTemplate>
          <retryCount>0</retryCount>
          <rotate>false</rotate>
          <includeFilterTransformer>false</includeFilterTransformer>
          <threadCount>1</threadCount>
          <threadAssignmentVariable></threadAssignmentVariable>
          <validateResponse>false</validateResponse>
          <resourceIds class="linked-hash-map">
            <entry>
              <string>Default Resource</string>
              <string>[Default Resource]</string>
            </entry>
          </resourceIds>
          <queueBufferSize>1000</queueBufferSize>
          <reattachAttachments>true</reattachAttachments>
        </destinationConnectorProperties>
        <channelId>71b5b97a-4e3d-4fd3-a065-93950aa217e5</channelId>
        <channelTemplate>${message.encodedData}</channelTemplate>
        <mapVariables>
          <string>Variable 1</string>
        </mapVariables>
      </properties>
      <transformer version="4.1.1">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </transformer>
      <responseTransformer version="4.1.1">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="4.1.1">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="4.1.1">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="4.1.1">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="4.1.1">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="4.1.1">
            <segmentDelimiter>\\r</segmentDelimiter>
            <successfulACKCode>AA</successfulACKCode>
            <successfulACKMessage></successfulACKMessage>
            <errorACKCode>AE</errorACKCode>
            <errorACKMessage>An Error Occurred Processing Message.</errorACKMessage>
            <rejectedACKCode>AR</rejectedACKCode>
            <rejectedACKMessage>Message Rejected.</rejectedACKMessage>
            <msh15ACKAccept>false</msh15ACKAccept>
            <dateFormat>yyyyMMddHHmmss.SSS</dateFormat>
          </responseGenerationProperties>
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="4.1.1">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </responseTransformer>
      <filter version="4.1.1">
        <elements/>
      </filter>
      <transportName>Channel Writer</transportName>
      <mode>DESTINATION</mode>
      <enabled>true</enabled>
      <waitForPrevious>true</waitForPrevious>'''

# Server
channelTagXML = '''<channelTag>
<id>429a2700-dfad-4520-abab-f6e03130cc9a</id>
<name>UnitTestTags</name>
<channelIds>
    <string>85584a88-be5f-479a-85f2-2c890e1daf4b</string>
</channelIds>
<backgroundColor>
    <red>255</red>
    <green>0</green>
    <blue>0</blue>
    <alpha>255</alpha>
</backgroundColor>
</channelTag>'''
#endregion