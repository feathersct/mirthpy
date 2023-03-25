import re
import unittest

from mirthapi.mirthService import MirthService
from mirthapi.connectors import FTPSchemeProperties, S3SchemeProperties
from mirthapi.channelStatistics import ChannelStatisticsList

class TestSource(unittest.TestCase):
    instance, username, password, port = "localhost", "test", "test", "8443"
    service = None

    def setUp(self):
        self.service = MirthService(instance=self.instance, username=self.username, password=self.password, port=self.port)
        self.service.open()

    def tearDown(self):
        self.service.close()

    def test_source_channelReader(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('ChannelReader_UnitTest'))
        version = self.service.version

        xmlNode = re.sub(r'\>[\s]+\<', '><', channelReaderXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceChannel.sourceConnector.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)
    
    def test_source_httpListener(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('HTTPListener_UnitTest'))
        version = self.service.version

        xmlNode = re.sub(r'\>[\s]+\<', '><', httpListenerXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceChannel.sourceConnector.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

    def test_source_javascriptReader(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('JavaScriptReader_UnitTest'))
        version = self.service.version

        xmlNode = re.sub(r'\>[\s]+\<', '><', javascriptReaderXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceChannel.sourceConnector.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

    def test_source_jmsListener(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('JMSListener_UnitTest'))
        version = self.service.version

        xmlNode = re.sub(r'\>[\s]+\<', '><', jmsListenerXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceChannel.sourceConnector.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)
    
    def test_source_tcpListener(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('TCPListener_UnitTest'))
        version = self.service.version

        xmlNode = re.sub(r'\>[\s]+\<', '><', tcpListenerXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceChannel.sourceConnector.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)   

    def test_source_databaseReader(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('DatabaseReader_UnitTest'))
        version = self.service.version

        xmlNode = re.sub(r'\>[\s]+\<', '><', databaseReaderXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceChannel.sourceConnector.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)   

    def test_source_dicomListener(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('DICOMListener_UnitTest'))
        version = self.service.version

        xmlNode = re.sub(r'\>[\s]+\<', '><', dicomListenerXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceChannel.sourceConnector.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)   

    def test_source_fileReader(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('FileReader_UnitTest'))
        version = self.service.version

        xmlNode = re.sub(r'\>[\s]+\<', '><', fileReaderXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceChannel.sourceConnector.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)
        
    def test_source_webserviceListener(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('WebServiceListener_UnitTest'))
        version = self.service.version

        xmlNode = re.sub(r'\>[\s]+\<', '><', webserviceListenerXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceChannel.sourceConnector.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)   

class TestDestination(unittest.TestCase):
    instance, username, password, port = "localhost", "test", "test", "8443"
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

    def test_destination_httpSender(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('XML_UnitTest'))
        version = self.service.version

        httpSender = [destination for destination in sourceChannel.destinationConnectors if destination.name == 'HTTP Sender']
        httpSender = httpSender[0]

        xmlNode = re.sub(r'\>[\s]+\<', '><', httpSenderXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', httpSender.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)
      
    def test_destination_jmsSender(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('XML_UnitTest'))
        version = self.service.version

        jmsSender = [destination for destination in sourceChannel.destinationConnectors if destination.name == 'JMS Sender']
        jmsSender = jmsSender[0]

        xmlNode = re.sub(r'\>[\s]+\<', '><', jmsSenderXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', jmsSender.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

    def test_destination_javaScriptWriter(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('XML_UnitTest'))
        version = self.service.version

        javaScriptWriter = [destination for destination in sourceChannel.destinationConnectors if destination.name == 'JavaScript Writer']
        javaScriptWriter = javaScriptWriter[0]

        xmlNode = re.sub(r'\>[\s]+\<', '><', javaScriptWriterXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', javaScriptWriter.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

    def test_destination_smtpSender(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('XML_UnitTest'))
        version = self.service.version

        smtpSender = [destination for destination in sourceChannel.destinationConnectors if destination.name == 'SMTP Sender']
        smtpSender = smtpSender[0]

        xmlNode = re.sub(r'\>[\s]+\<', '><', smtpSenderXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', smtpSender.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

    def test_destination_tcpSender(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('XML_UnitTest'))
        version = self.service.version

        tcpSender = [destination for destination in sourceChannel.destinationConnectors if destination.name == 'TCP Sender']
        tcpSender = tcpSender[0]

        xmlNode = re.sub(r'\>[\s]+\<', '><', tcpSenderXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', tcpSender.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

    def test_destination_webServiceSender(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('XML_UnitTest'))
        version = self.service.version

        webServiceSender = [destination for destination in sourceChannel.destinationConnectors if destination.name == 'Web Service Sender']
        webServiceSender = webServiceSender[0]

        xmlNode = re.sub(r'\>[\s]+\<', '><', webServiceSenderXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', webServiceSender.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

class TestFilterRules(unittest.TestCase):
    instance, username, password, port = "localhost", "test", "test", "8443"
    service = None

    def setUp(self):
        self.service = MirthService(instance=self.instance, username=self.username, password=self.password, port=self.port)
        self.service.open()

    def tearDown(self):
        self.service.close()

    #region RuleBuilder
    def test_filterRules_ruleBuilder_exists(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('FilterRule_UnitTest'))
        version = self.service.version

        baseXML = ruleBuilder_Exists
        sourceXML = [destination for destination in sourceChannel.destinationConnectors if destination.name == 'Filters'][0].filter.elements[0]

        xmlNode = re.sub(r'\>[\s]+\<', '><', baseXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceXML.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

    def test_filterRules_ruleBuilder_notexists(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('FilterRule_UnitTest'))
        version = self.service.version

        baseXML = ruleBuilder_NotExists
        sourceXML = [destination for destination in sourceChannel.destinationConnectors if destination.name == 'Filters'][0].filter.elements[1]

        xmlNode = re.sub(r'\>[\s]+\<', '><', baseXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceXML.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

    def test_filterRules_ruleBuilder_equals(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('FilterRule_UnitTest'))
        version = self.service.version

        baseXML = ruleBuilder_Equals
        sourceXML = [destination for destination in sourceChannel.destinationConnectors if destination.name == 'Filters'][0].filter.elements[2]

        xmlNode = re.sub(r'\>[\s]+\<', '><', baseXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceXML.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

    def test_filterRules_ruleBuilder_notequals(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('FilterRule_UnitTest'))
        version = self.service.version

        baseXML = ruleBuilder_NotEquals
        sourceXML = [destination for destination in sourceChannel.destinationConnectors if destination.name == 'Filters'][0].filter.elements[3]

        xmlNode = re.sub(r'\>[\s]+\<', '><', baseXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceXML.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

    def test_filterRules_ruleBuilder_contains(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('FilterRule_UnitTest'))
        version = self.service.version

        baseXML = ruleBuilder_Contains
        sourceXML = [destination for destination in sourceChannel.destinationConnectors if destination.name == 'Filters'][0].filter.elements[4]

        xmlNode = re.sub(r'\>[\s]+\<', '><', baseXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceXML.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

    def test_filterRules_ruleBuilder_notcontains(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('FilterRule_UnitTest'))
        version = self.service.version

        baseXML = ruleBuilder_NotContains
        sourceXML = [destination for destination in sourceChannel.destinationConnectors if destination.name == 'Filters'][0].filter.elements[5]

        xmlNode = re.sub(r'\>[\s]+\<', '><', baseXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceXML.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

    #endregion
    def test_filterRules_mirthPull(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('FilterRule_UnitTest'))
        version = self.service.version

        baseXML = mirthPullXML
        sourceXML = [destination for destination in sourceChannel.destinationConnectors if destination.name == 'Filters'][0].filter

        xmlNode = re.sub(r'\>[\s]+\<', '><', baseXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceXML.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

class TestSchemeProperties(unittest.TestCase):
    instance, username, password, port = "localhost", "test", "test", "8443"
    service = None

    def setUp(self):
        self.service = MirthService(instance=self.instance, username=self.username, password=self.password, port=self.port)
        self.service.open()

    def tearDown(self):
        self.service.close()

    #region FTPSchemeProperties
    def test_schemeProperties_FTP_default(self):
        version = self.service.version

        baseXML = '<initialCommands/>'
        ftpProp = FTPSchemeProperties()

        xmlNode = re.sub(r'\>[\s]+\<', '><', baseXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', ftpProp.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

    def test_schemeProperties_FTP_2initialcommands(self):
        version = self.service.version

        baseXML = '<initialCommands><string>NAMEFMT</string><string>NAMEFMT</string></initialCommands>'
        ftpProp = FTPSchemeProperties()
        ftpProp.initalCommands.append('NAMEFMT')
        ftpProp.initalCommands.append('NAMEFMT')

        xmlNode = re.sub(r'\>[\s]+\<', '><', baseXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', ftpProp.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

    def test_schemeProperties_FTP_mirthPull(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('SchemeProperties_UnitTest'))
        version = self.service.version

        baseXML = ftpSchemePropXML
        sourceXML = [destination for destination in sourceChannel.destinationConnectors if destination.name == 'FTP'][0].properties.schemeProperties

        xmlNode = re.sub(r'\>[\s]+\<', '><', baseXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceXML.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)
    #endregion

    #region S3SchemeProperties
    def test_schemeProperties_S3_default(self):
        version = self.service.version

        baseXML = '''<useDefaultCredentialProviderChain>true</useDefaultCredentialProviderChain>
                    <useTemporaryCredentials>false</useTemporaryCredentials>
                    <duration>7200</duration>
                    <region>us-east-1</region>
                    <customHeaders class="linked-hash-map"/>'''
        prop = S3SchemeProperties()

        xmlNode = re.sub(r'\>[\s]+\<', '><', baseXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', prop.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

    def test_schemeProperties_S3_mirthPull(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('SchemeProperties_UnitTest'))
        version = self.service.version

        baseXML = s3SchemePropXML
        sourceXML = [destination for destination in sourceChannel.destinationConnectors if destination.name == 'S3'][0].properties.schemeProperties

        xmlNode = re.sub(r'\>[\s]+\<', '><', baseXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceXML.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)
    #endregion

    #region SFTPSchemeProperties
    def test_schemeProperties_SFTP_mirthPull(self):
        sourceChannel = self.service.getChannel(self.service.getChannelIdByName('SchemeProperties_UnitTest'))
        version = self.service.version

        baseXML = sftpSchemePropXML
        sourceXML = [destination for destination in sourceChannel.destinationConnectors if destination.name == 'SFTP'][0].properties.schemeProperties

        xmlNode = re.sub(r'\>[\s]+\<', '><', baseXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', sourceXML.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)
    #endregion

class TestChannelStatistics(unittest.TestCase):
    instance, username, password, port = "localhost", "test", "test", "8443"
    service = None

    def setUp(self):
        self.service = MirthService(instance=self.instance, username=self.username, password=self.password, port=self.port)
        self.service.open()

    def tearDown(self):
        self.service.close()

    def test_channelStatistics(self):
        version = self.service.version

        baseXML = '''<list><channelStatistics><serverId>034af130-aba3-4154-9d61-ced8dc78e8b2</serverId><channelId>9aa20638-7881-4abf-b9c6-fe807e667ad0</channelId><received>0</received><sent>0</sent><error>0</error><filtered>0</filtered><queued>0</queued></channelStatistics><channelStatistics><serverId>034af130-aba3-4154-9d61-ced8dc78e8b2</serverId><channelId>76ec077d-1145-4439-a3f8-280aa6f4a2af</channelId><received>0</received><sent>0</sent><error>0</error><filtered>0</filtered><queued>0</queued></channelStatistics><channelStatistics><serverId>034af130-aba3-4154-9d61-ced8dc78e8b2</serverId><channelId>72ef2c87-f71b-44e0-b03b-4eb776bed6fb</channelId><received>1</received><sent>1</sent><error>0</error><filtered>0</filtered><queued>0</queued></channelStatistics></list>'''
        prop = ChannelStatisticsList(bytes(baseXML, 'utf-8'))

        xmlNode = re.sub(r'\>[\s]+\<', '><', baseXML.strip())
        sourceNode = re.sub(r'\>[\s]+\<', '><', prop.getXML(version).strip())
        self.assertEqual(xmlNode, sourceNode)

#region XML
# Filters
mirthPullXML = '''<elements>
          <com.mirth.connect.plugins.rulebuilder.RuleBuilderRule version="3.12.0">
            <name>Accept message if &quot;msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()&quot; exists</name>
            <sequenceNumber>0</sequenceNumber>
            <enabled>true</enabled>
            <field>msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()</field>
            <condition>EXISTS</condition>
            <values/>
          </com.mirth.connect.plugins.rulebuilder.RuleBuilderRule>
          <com.mirth.connect.plugins.rulebuilder.RuleBuilderRule version="3.12.0">
            <name>Accept message if &quot;msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()&quot; does not exist</name>
            <sequenceNumber>1</sequenceNumber>
            <enabled>true</enabled>
            <operator>AND</operator>
            <field>msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()</field>
            <condition>NOT_EXIST</condition>
            <values/>
          </com.mirth.connect.plugins.rulebuilder.RuleBuilderRule>
          <com.mirth.connect.plugins.rulebuilder.RuleBuilderRule version="3.12.0">
            <name>Accept message if &quot;msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()&quot; equals &quot;test&quot; or &quot;test123&quot;</name>
            <sequenceNumber>2</sequenceNumber>
            <enabled>true</enabled>
            <operator>AND</operator>
            <field>msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()</field>
            <condition>EQUALS</condition>
            <values>
              <string>&quot;test&quot;</string>
              <string>&quot;test123&quot;</string>
            </values>
          </com.mirth.connect.plugins.rulebuilder.RuleBuilderRule>
          <com.mirth.connect.plugins.rulebuilder.RuleBuilderRule version="3.12.0">
            <name>Accept message if &quot;msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()&quot; does not equal &quot;test&quot;</name>
            <sequenceNumber>3</sequenceNumber>
            <enabled>true</enabled>
            <operator>AND</operator>
            <field>msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()</field>
            <condition>NOT_EQUAL</condition>
            <values>
              <string>&quot;test&quot;</string>
            </values>
          </com.mirth.connect.plugins.rulebuilder.RuleBuilderRule>
          <com.mirth.connect.plugins.rulebuilder.RuleBuilderRule version="3.12.0">
            <name>Accept message if &quot;msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()&quot; contains &quot;test&quot;</name>
            <sequenceNumber>4</sequenceNumber>
            <enabled>true</enabled>
            <operator>AND</operator>
            <field>msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()</field>
            <condition>CONTAINS</condition>
            <values>
              <string>&quot;test&quot;</string>
            </values>
          </com.mirth.connect.plugins.rulebuilder.RuleBuilderRule>
          <com.mirth.connect.plugins.rulebuilder.RuleBuilderRule version="3.12.0">
            <name>Accept message if &quot;msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()&quot; does not contain &quot;test&quot;</name>
            <sequenceNumber>5</sequenceNumber>
            <enabled>true</enabled>
            <operator>AND</operator>
            <field>msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()</field>
            <condition>NOT_CONTAIN</condition>
            <values>
              <string>&quot;test&quot;</string>
            </values>
          </com.mirth.connect.plugins.rulebuilder.RuleBuilderRule>
          <com.mirth.connect.plugins.javascriptrule.JavaScriptRule version="3.12.0">
            <name>JavaScript</name>
            <sequenceNumber>6</sequenceNumber>
            <enabled>true</enabled>
            <operator>AND</operator>
            <script></script>
          </com.mirth.connect.plugins.javascriptrule.JavaScriptRule>
          <com.mirth.connect.plugins.scriptfilerule.ExternalScriptRule version="3.12.0">
            <sequenceNumber>7</sequenceNumber>
            <enabled>true</enabled>
            <operator>AND</operator>
            <scriptPath>script/path/etc</scriptPath>
          </com.mirth.connect.plugins.scriptfilerule.ExternalScriptRule>
        </elements>'''
ruleBuilder_NotContains = '''<name>Accept message if &quot;msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()&quot; does not contain &quot;test&quot;</name>
            <sequenceNumber>5</sequenceNumber>
            <enabled>true</enabled>
            <operator>AND</operator>
            <field>msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()</field>
            <condition>NOT_CONTAIN</condition>
            <values>
              <string>&quot;test&quot;</string>
            </values>'''
ruleBuilder_Contains = '''<name>Accept message if &quot;msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()&quot; contains &quot;test&quot;</name>
            <sequenceNumber>4</sequenceNumber>
            <enabled>true</enabled>
            <operator>AND</operator>
            <field>msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()</field>
            <condition>CONTAINS</condition>
            <values>
              <string>&quot;test&quot;</string>
            </values>'''
ruleBuilder_Exists = '''<name>Accept message if &quot;msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()&quot; exists</name>
            <sequenceNumber>0</sequenceNumber>
            <enabled>true</enabled>
            <field>msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()</field>
            <condition>EXISTS</condition>
            <values/>'''
ruleBuilder_NotExists = '''<name>Accept message if &quot;msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()&quot; does not exist</name>
            <sequenceNumber>1</sequenceNumber>
            <enabled>true</enabled>
            <operator>AND</operator>
            <field>msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()</field>
            <condition>NOT_EXIST</condition>
            <values/>'''
ruleBuilder_Equals = '''<name>Accept message if &quot;msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()&quot; equals &quot;test&quot; or &quot;test123&quot;</name>
            <sequenceNumber>2</sequenceNumber>
            <enabled>true</enabled>
            <operator>AND</operator>
            <field>msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()</field>
            <condition>EQUALS</condition>
            <values>
              <string>&quot;test&quot;</string>
              <string>&quot;test123&quot;</string>
            </values>'''
ruleBuilder_NotEquals = '''<name>Accept message if &quot;msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()&quot; does not equal &quot;test&quot;</name>
            <sequenceNumber>3</sequenceNumber>
            <enabled>true</enabled>
            <operator>AND</operator>
            <field>msg[&apos;PV1&apos;][&apos;PV1.10&apos;][&apos;PV1.10.1&apos;].toString()</field>
            <condition>NOT_EQUAL</condition>
            <values>
              <string>&quot;test&quot;</string>
            </values>'''

# Destination Connectors
webServiceSenderXML = '''<metaDataId>11</metaDataId>
      <name>Web Service Sender</name>
      <properties class="com.mirth.connect.connectors.ws.WebServiceDispatcherProperties" version="3.12.0">
        <pluginProperties/>
        <destinationConnectorProperties version="3.12.0">
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
        <wsdlUrl>www.google.com</wsdlUrl>
        <service>someService</service>
        <port>9039</port>
        <operation>Press Get Operations</operation>
        <locationURI></locationURI>
        <socketTimeout>30000</socketTimeout>
        <useAuthentication>false</useAuthentication>
        <username></username>
        <password></password>
        <envelope>&lt;soap&gt;&lt;/soap&gt;</envelope>
        <oneWay>false</oneWay>
        <headers>
          <entry>
            <string>Property 1</string>
            <list>
              <string></string>
            </list>
          </entry>
        </headers>
        <headersVariable></headersVariable>
        <isUseHeadersVariable>false</isUseHeadersVariable>
        <useMtom>false</useMtom>
        <attachmentNames/>
        <attachmentContents/>
        <attachmentTypes/>
        <attachmentsVariable></attachmentsVariable>
        <isUseAttachmentsVariable>false</isUseAttachmentsVariable>
        <soapAction></soapAction>
        <wsdlDefinitionMap>
          <map class="linked-hash-map"/>
        </wsdlDefinitionMap>
      </properties>
      <transformer version="3.12.0">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </transformer>
      <responseTransformer version="3.12.0">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </responseTransformer>
      <filter version="3.12.0">
        <elements/>
      </filter>
      <transportName>Web Service Sender</transportName>
      <mode>DESTINATION</mode>
      <enabled>true</enabled>
      <waitForPrevious>true</waitForPrevious>'''
tcpSenderXML = '''<metaDataId>10</metaDataId>
      <name>TCP Sender</name>
      <properties class="com.mirth.connect.connectors.tcp.TcpDispatcherProperties" version="3.12.0">
        <pluginProperties/>
        <destinationConnectorProperties version="3.12.0">
          <queueEnabled>false</queueEnabled>
          <sendFirst>false</sendFirst>
          <retryIntervalMillis>10000</retryIntervalMillis>
          <regenerateTemplate>false</regenerateTemplate>
          <retryCount>0</retryCount>
          <rotate>false</rotate>
          <includeFilterTransformer>false</includeFilterTransformer>
          <threadCount>1</threadCount>
          <threadAssignmentVariable></threadAssignmentVariable>
          <validateResponse>true</validateResponse>
          <resourceIds class="linked-hash-map">
            <entry>
              <string>Default Resource</string>
              <string>[Default Resource]</string>
            </entry>
          </resourceIds>
          <queueBufferSize>1000</queueBufferSize>
          <reattachAttachments>true</reattachAttachments>
        </destinationConnectorProperties>
        <transmissionModeProperties class="com.mirth.connect.plugins.mllpmode.MLLPModeProperties">
          <pluginPointName>MLLP</pluginPointName>
          <startOfMessageBytes>0B</startOfMessageBytes>
          <endOfMessageBytes>1C0D</endOfMessageBytes>
          <useMLLPv2>false</useMLLPv2>
          <ackBytes>06</ackBytes>
          <nackBytes>15</nackBytes>
          <maxRetries>2</maxRetries>
        </transmissionModeProperties>
        <serverMode>false</serverMode>
        <remoteAddress>127.0.0.1</remoteAddress>
        <remotePort>6660</remotePort>
        <overrideLocalBinding>false</overrideLocalBinding>
        <localAddress>0.0.0.0</localAddress>
        <localPort>0</localPort>
        <sendTimeout>5000</sendTimeout>
        <bufferSize>65536</bufferSize>
        <maxConnections>10</maxConnections>
        <keepConnectionOpen>false</keepConnectionOpen>
        <checkRemoteHost>false</checkRemoteHost>
        <responseTimeout>5000</responseTimeout>
        <ignoreResponse>false</ignoreResponse>
        <queueOnResponseTimeout>true</queueOnResponseTimeout>
        <dataTypeBinary>false</dataTypeBinary>
        <charsetEncoding>DEFAULT_ENCODING</charsetEncoding>
        <template>${message.encodedData}</template>
      </properties>
      <transformer version="3.12.0">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </transformer>
      <responseTransformer version="3.12.0">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </responseTransformer>
      <filter version="3.12.0">
        <elements/>
      </filter>
      <transportName>TCP Sender</transportName>
      <mode>DESTINATION</mode>
      <enabled>true</enabled>
      <waitForPrevious>true</waitForPrevious>'''
smtpSenderXML = '''<metaDataId>9</metaDataId>
      <name>SMTP Sender</name>
      <properties class="com.mirth.connect.connectors.smtp.SmtpDispatcherProperties" version="3.12.0">
        <pluginProperties/>
        <destinationConnectorProperties version="3.12.0">
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
        <smtpHost>www.google.com</smtpHost>
        <smtpPort>25</smtpPort>
        <overrideLocalBinding>false</overrideLocalBinding>
        <localAddress>0.0.0.0</localAddress>
        <localPort>0</localPort>
        <timeout>5000</timeout>
        <encryption>none</encryption>
        <authentication>false</authentication>
        <username></username>
        <password></password>
        <to>example@mirth.com</to>
        <from>examplefrom@mirth.com</from>
        <cc></cc>
        <bcc></bcc>
        <replyTo></replyTo>
        <headers class="linked-hash-map">
          <entry>
            <string>Header 1</string>
            <string>agad</string>
          </entry>
          <entry>
            <string>Header 2</string>
            <string>bvaafd</string>
          </entry>
        </headers>
        <headersVariable></headersVariable>
        <isUseHeadersVariable>false</isUseHeadersVariable>
        <subject>Example</subject>
        <charsetEncoding>DEFAULT_ENCODING</charsetEncoding>
        <html>false</html>
        <body>Example Body</body>
        <attachments>
          <com.mirth.connect.connectors.smtp.Attachment>
            <name>Attachment 1</name>
            <content>afdasd</content>
            <mimeType>txt</mimeType>
          </com.mirth.connect.connectors.smtp.Attachment>
          <com.mirth.connect.connectors.smtp.Attachment>
            <name>Attachment 2</name>
            <content>bagafe</content>
            <mimeType>txt</mimeType>
          </com.mirth.connect.connectors.smtp.Attachment>
        </attachments>
        <attachmentsVariable></attachmentsVariable>
        <isUseAttachmentsVariable>false</isUseAttachmentsVariable>
      </properties>
      <transformer version="3.12.0">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </transformer>
      <responseTransformer version="3.12.0">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </responseTransformer>
      <filter version="3.12.0">
        <elements/>
      </filter>
      <transportName>SMTP Sender</transportName>
      <mode>DESTINATION</mode>
      <enabled>true</enabled>
      <waitForPrevious>true</waitForPrevious>'''
javaScriptWriterXML = '''<metaDataId>8</metaDataId>
      <name>JavaScript Writer</name>
      <properties class="com.mirth.connect.connectors.js.JavaScriptDispatcherProperties" version="3.12.0">
        <pluginProperties/>
        <destinationConnectorProperties version="3.12.0">
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
        <script>logger.debug(&quot;this is an example&quot;)
logger.debug(&apos;this is also an example&apos;)


// basic arithmatic
var i = 0;
i++
i += 10

i = i * 10</script>
      </properties>
      <transformer version="3.12.0">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </transformer>
      <responseTransformer version="3.12.0">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </responseTransformer>
      <filter version="3.12.0">
        <elements/>
      </filter>
      <transportName>JavaScript Writer</transportName>
      <mode>DESTINATION</mode>
      <enabled>true</enabled>
      <waitForPrevious>true</waitForPrevious>'''
jmsSenderXML = '''<metaDataId>7</metaDataId>
      <name>JMS Sender</name>
      <properties class="com.mirth.connect.connectors.jms.JmsDispatcherProperties" version="3.12.0">
        <pluginProperties/>
        <useJndi>false</useJndi>
        <jndiProviderUrl></jndiProviderUrl>
        <jndiInitialContextFactory></jndiInitialContextFactory>
        <jndiConnectionFactoryName></jndiConnectionFactoryName>
        <connectionFactoryClass>com.example.jms.Connection</connectionFactoryClass>
        <connectionProperties class="linked-hash-map">
          <entry>
            <string>Property 1</string>
            <string>dafa</string>
          </entry>
        </connectionProperties>
        <username></username>
        <password></password>
        <destinationName>ExampleDestination</destinationName>
        <topic>false</topic>
        <clientId></clientId>
        <template>${message.encodedData}</template>
        <destinationConnectorProperties version="3.12.0">
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
      </properties>
      <transformer version="3.12.0">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </transformer>
      <responseTransformer version="3.12.0">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </responseTransformer>
      <filter version="3.12.0">
        <elements/>
      </filter>
      <transportName>JMS Sender</transportName>
      <mode>DESTINATION</mode>
      <enabled>true</enabled>
      <waitForPrevious>true</waitForPrevious>'''
httpSenderXML = '''<metaDataId>6</metaDataId>
  <name>HTTP Sender</name>
  <properties class="com.mirth.connect.connectors.http.HttpDispatcherProperties" version="3.12.0">
    <pluginProperties/>
    <destinationConnectorProperties version="3.12.0">
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
    <host>www.google.com</host>
    <useProxyServer>false</useProxyServer>
    <proxyAddress></proxyAddress>
    <proxyPort></proxyPort>
    <method>post</method>
    <headers class="linked-hash-map">
      <entry>
        <string>Property 1</string>
        <list>
          <string>vagafe</string>
        </list>
      </entry>
    </headers>
    <parameters class="linked-hash-map">
      <entry>
        <string>Property 1</string>
        <list>
          <string>dfa</string>
          <string>dfa2</string>
        </list>
      </entry>
    </parameters>
    <useHeadersVariable>false</useHeadersVariable>
    <headersVariable></headersVariable>
    <useParametersVariable>false</useParametersVariable>
    <parametersVariable></parametersVariable>
    <responseXmlBody>false</responseXmlBody>
    <responseParseMultipart>true</responseParseMultipart>
    <responseIncludeMetadata>false</responseIncludeMetadata>
    <responseBinaryMimeTypes>application/.*(?&lt;!json|xml)$|image/.*|video/.*|audio/.*</responseBinaryMimeTypes>
    <responseBinaryMimeTypesRegex>true</responseBinaryMimeTypesRegex>
    <multipart>false</multipart>
    <useAuthentication>false</useAuthentication>
    <authenticationType>Basic</authenticationType>
    <usePreemptiveAuthentication>false</usePreemptiveAuthentication>
    <username></username>
    <password></password>
    <content></content>
    <contentType>text/plain</contentType>
    <dataTypeBinary>false</dataTypeBinary>
    <charset>UTF-8</charset>
    <socketTimeout>30000</socketTimeout>
  </properties>
  <transformer version="3.12.0">
    <elements/>
    <inboundDataType>HL7V2</inboundDataType>
    <outboundDataType>HL7V2</outboundDataType>
    <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
      <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
        <handleRepetitions>true</handleRepetitions>
        <handleSubcomponents>true</handleSubcomponents>
        <useStrictParser>false</useStrictParser>
        <useStrictValidation>false</useStrictValidation>
        <stripNamespaces>false</stripNamespaces>
        <segmentDelimiter>\\r</segmentDelimiter>
        <convertLineBreaks>true</convertLineBreaks>
      </serializationProperties>
      <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
        <useStrictParser>false</useStrictParser>
        <useStrictValidation>false</useStrictValidation>
        <segmentDelimiter>\\r</segmentDelimiter>
      </deserializationProperties>
      <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
        <splitType>MSH_Segment</splitType>
        <batchScript></batchScript>
      </batchProperties>
      <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
      <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
        <successfulACKCode>AA,CA</successfulACKCode>
        <errorACKCode>AE,CE</errorACKCode>
        <rejectedACKCode>AR,CR</rejectedACKCode>
        <validateMessageControlId>true</validateMessageControlId>
        <originalMessageControlId>Destination_Encoded</originalMessageControlId>
        <originalIdMapVariable></originalIdMapVariable>
      </responseValidationProperties>
    </inboundProperties>
    <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
      <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
        <handleRepetitions>true</handleRepetitions>
        <handleSubcomponents>true</handleSubcomponents>
        <useStrictParser>false</useStrictParser>
        <useStrictValidation>false</useStrictValidation>
        <stripNamespaces>false</stripNamespaces>
        <segmentDelimiter>\\r</segmentDelimiter>
        <convertLineBreaks>true</convertLineBreaks>
      </serializationProperties>
      <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
        <useStrictParser>false</useStrictParser>
        <useStrictValidation>false</useStrictValidation>
        <segmentDelimiter>\\r</segmentDelimiter>
      </deserializationProperties>
      <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
        <splitType>MSH_Segment</splitType>
        <batchScript></batchScript>
      </batchProperties>
      <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
      <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
        <successfulACKCode>AA,CA</successfulACKCode>
        <errorACKCode>AE,CE</errorACKCode>
        <rejectedACKCode>AR,CR</rejectedACKCode>
        <validateMessageControlId>true</validateMessageControlId>
        <originalMessageControlId>Destination_Encoded</originalMessageControlId>
        <originalIdMapVariable></originalIdMapVariable>
      </responseValidationProperties>
    </outboundProperties>
  </transformer>
  <responseTransformer version="3.12.0">
    <elements/>
    <inboundDataType>HL7V2</inboundDataType>
    <outboundDataType>HL7V2</outboundDataType>
    <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
      <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
        <handleRepetitions>true</handleRepetitions>
        <handleSubcomponents>true</handleSubcomponents>
        <useStrictParser>false</useStrictParser>
        <useStrictValidation>false</useStrictValidation>
        <stripNamespaces>false</stripNamespaces>
        <segmentDelimiter>\\r</segmentDelimiter>
        <convertLineBreaks>true</convertLineBreaks>
      </serializationProperties>
      <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
        <useStrictParser>false</useStrictParser>
        <useStrictValidation>false</useStrictValidation>
        <segmentDelimiter>\\r</segmentDelimiter>
      </deserializationProperties>
      <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
        <splitType>MSH_Segment</splitType>
        <batchScript></batchScript>
      </batchProperties>
      <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
      <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
        <successfulACKCode>AA,CA</successfulACKCode>
        <errorACKCode>AE,CE</errorACKCode>
        <rejectedACKCode>AR,CR</rejectedACKCode>
        <validateMessageControlId>true</validateMessageControlId>
        <originalMessageControlId>Destination_Encoded</originalMessageControlId>
        <originalIdMapVariable></originalIdMapVariable>
      </responseValidationProperties>
    </inboundProperties>
    <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
      <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
        <handleRepetitions>true</handleRepetitions>
        <handleSubcomponents>true</handleSubcomponents>
        <useStrictParser>false</useStrictParser>
        <useStrictValidation>false</useStrictValidation>
        <stripNamespaces>false</stripNamespaces>
        <segmentDelimiter>\\r</segmentDelimiter>
        <convertLineBreaks>true</convertLineBreaks>
      </serializationProperties>
      <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
        <useStrictParser>false</useStrictParser>
        <useStrictValidation>false</useStrictValidation>
        <segmentDelimiter>\\r</segmentDelimiter>
      </deserializationProperties>
      <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
        <splitType>MSH_Segment</splitType>
        <batchScript></batchScript>
      </batchProperties>
      <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
      <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
        <successfulACKCode>AA,CA</successfulACKCode>
        <errorACKCode>AE,CE</errorACKCode>
        <rejectedACKCode>AR,CR</rejectedACKCode>
        <validateMessageControlId>true</validateMessageControlId>
        <originalMessageControlId>Destination_Encoded</originalMessageControlId>
        <originalIdMapVariable></originalIdMapVariable>
      </responseValidationProperties>
    </outboundProperties>
  </responseTransformer>
  <filter version="3.12.0">
    <elements/>
  </filter>
  <transportName>HTTP Sender</transportName>
  <mode>DESTINATION</mode>
  <enabled>true</enabled>
  <waitForPrevious>true</waitForPrevious>'''
fileWriterXML = '''<metaDataId>5</metaDataId>
      <name>File Writer</name>
      <properties class="com.mirth.connect.connectors.file.FileDispatcherProperties" version="3.12.0">
        <pluginProperties/>
        <destinationConnectorProperties version="3.12.0">
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
      <transformer version="3.12.0">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </transformer>
      <responseTransformer version="3.12.0">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </responseTransformer>
      <filter version="3.12.0">
        <elements/>
      </filter>
      <transportName>File Writer</transportName>
      <mode>DESTINATION</mode>
      <enabled>true</enabled>
      <waitForPrevious>true</waitForPrevious>'''
documentWriterXML = '''<metaDataId>4</metaDataId>
      <name>Document Writer</name>
      <properties class="com.mirth.connect.connectors.doc.DocumentDispatcherProperties" version="3.12.0">
        <pluginProperties/>
        <destinationConnectorProperties version="3.12.0">
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
      <transformer version="3.12.0">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </transformer>
      <responseTransformer version="3.12.0">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </responseTransformer>
      <filter version="3.12.0">
        <elements/>
      </filter>
      <transportName>Document Writer</transportName>
      <mode>DESTINATION</mode>
      <enabled>true</enabled>
      <waitForPrevious>true</waitForPrevious>'''
databaseWriterXML = '''<metaDataId>3</metaDataId>
      <name>Database Writer</name>
      <properties class="com.mirth.connect.connectors.jdbc.DatabaseDispatcherProperties" version="3.12.0">
        <pluginProperties/>
        <destinationConnectorProperties version="3.12.0">
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
      <transformer version="3.12.0">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </transformer>
      <responseTransformer version="3.12.0">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </responseTransformer>
      <filter version="3.12.0">
        <elements/>
      </filter>
      <transportName>Database Writer</transportName>
      <mode>DESTINATION</mode>
      <enabled>true</enabled>
      <waitForPrevious>true</waitForPrevious>'''
dicomSenderXML = '''<metaDataId>2</metaDataId>
      <name>DICOM Sender</name>
      <properties class="com.mirth.connect.connectors.dimse.DICOMDispatcherProperties" version="3.12.0">
        <pluginProperties/>
        <destinationConnectorProperties version="3.12.0">
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
      <transformer version="3.12.0">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </transformer>
      <responseTransformer version="3.12.0">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </responseTransformer>
      <filter version="3.12.0">
        <elements/>
      </filter>
      <transportName>DICOM Sender</transportName>
      <mode>DESTINATION</mode>
      <enabled>true</enabled>
      <waitForPrevious>true</waitForPrevious>'''
channelWriterXML = '''<metaDataId>1</metaDataId>
      <name>Channel Writer</name>
      <properties class="com.mirth.connect.connectors.vm.VmDispatcherProperties" version="3.12.0">
        <pluginProperties/>
        <destinationConnectorProperties version="3.12.0">
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
      <transformer version="3.12.0">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </transformer>
      <responseTransformer version="3.12.0">
        <elements/>
        <inboundDataType>HL7V2</inboundDataType>
        <outboundDataType>HL7V2</outboundDataType>
        <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </inboundProperties>
        <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
          <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
            <handleRepetitions>true</handleRepetitions>
            <handleSubcomponents>true</handleSubcomponents>
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <stripNamespaces>false</stripNamespaces>
            <segmentDelimiter>\\r</segmentDelimiter>
            <convertLineBreaks>true</convertLineBreaks>
          </serializationProperties>
          <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
            <useStrictParser>false</useStrictParser>
            <useStrictValidation>false</useStrictValidation>
            <segmentDelimiter>\\r</segmentDelimiter>
          </deserializationProperties>
          <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
            <splitType>MSH_Segment</splitType>
            <batchScript></batchScript>
          </batchProperties>
          <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
          <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
            <successfulACKCode>AA,CA</successfulACKCode>
            <errorACKCode>AE,CE</errorACKCode>
            <rejectedACKCode>AR,CR</rejectedACKCode>
            <validateMessageControlId>true</validateMessageControlId>
            <originalMessageControlId>Destination_Encoded</originalMessageControlId>
            <originalIdMapVariable></originalIdMapVariable>
          </responseValidationProperties>
        </outboundProperties>
      </responseTransformer>
      <filter version="3.12.0">
        <elements/>
      </filter>
      <transportName>Channel Writer</transportName>
      <mode>DESTINATION</mode>
      <enabled>true</enabled>
      <waitForPrevious>true</waitForPrevious>'''

# Source Connectors
webserviceListenerXML = '''<metaDataId>0</metaDataId>
    <name>sourceConnector</name>
    <properties class="com.mirth.connect.connectors.ws.WebServiceReceiverProperties" version="3.12.0">
      <pluginProperties>
        <com.mirth.connect.plugins.httpauth.NoneHttpAuthProperties version="3.12.0">
  <authType>NONE</authType>
        </com.mirth.connect.plugins.httpauth.NoneHttpAuthProperties>
      </pluginProperties>
      <listenerConnectorProperties version="3.12.0">
        <host>0.0.0.0</host>
        <port>8081</port>
      </listenerConnectorProperties>
      <sourceConnectorProperties version="3.12.0">
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
      <className>com.mirth.connect.connectors.ws.DefaultAcceptMessage</className>
      <serviceName>Mirth</serviceName>
      <soapBinding>DEFAULT</soapBinding>
    </properties>
    <transformer version="3.12.0">
      <elements/>
      <inboundDataType>HL7V2</inboundDataType>
      <outboundDataType>HL7V2</outboundDataType>
      <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
          <handleRepetitions>true</handleRepetitions>
          <handleSubcomponents>true</handleSubcomponents>
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <stripNamespaces>false</stripNamespaces>
          <segmentDelimiter>\\r</segmentDelimiter>
          <convertLineBreaks>true</convertLineBreaks>
        </serializationProperties>
        <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <segmentDelimiter>\\r</segmentDelimiter>
        </deserializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
          <splitType>MSH_Segment</splitType>
          <batchScript></batchScript>
        </batchProperties>
        <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
        <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
          <successfulACKCode>AA,CA</successfulACKCode>
          <errorACKCode>AE,CE</errorACKCode>
          <rejectedACKCode>AR,CR</rejectedACKCode>
          <validateMessageControlId>true</validateMessageControlId>
          <originalMessageControlId>Destination_Encoded</originalMessageControlId>
          <originalIdMapVariable></originalIdMapVariable>
        </responseValidationProperties>
      </inboundProperties>
      <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
          <handleRepetitions>true</handleRepetitions>
          <handleSubcomponents>true</handleSubcomponents>
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <stripNamespaces>false</stripNamespaces>
          <segmentDelimiter>\\r</segmentDelimiter>
          <convertLineBreaks>true</convertLineBreaks>
        </serializationProperties>
        <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <segmentDelimiter>\\r</segmentDelimiter>
        </deserializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
          <splitType>MSH_Segment</splitType>
          <batchScript></batchScript>
        </batchProperties>
        <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
        <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
          <successfulACKCode>AA,CA</successfulACKCode>
          <errorACKCode>AE,CE</errorACKCode>
          <rejectedACKCode>AR,CR</rejectedACKCode>
          <validateMessageControlId>true</validateMessageControlId>
          <originalMessageControlId>Destination_Encoded</originalMessageControlId>
          <originalIdMapVariable></originalIdMapVariable>
        </responseValidationProperties>
      </outboundProperties>
    </transformer>
    <filter version="3.12.0">
      <elements/>
    </filter>
    <transportName>Web Service Listener</transportName>
    <mode>SOURCE</mode>
    <enabled>true</enabled>
    <waitForPrevious>true</waitForPrevious>'''
fileReaderXML = '''<metaDataId>0</metaDataId>
    <name>sourceConnector</name>
    <properties class="com.mirth.connect.connectors.file.FileReceiverProperties" version="3.12.0">
      <pluginProperties/>
      <pollConnectorProperties version="3.12.0">
        <pollingType>INTERVAL</pollingType>
        <pollOnStart>false</pollOnStart>
        <pollingFrequency>82800000</pollingFrequency>
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
      <sourceConnectorProperties version="3.12.0">
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
      <host>google.com/fileDirectory</host>
      <fileFilter>*</fileFilter>
      <regex>false</regex>
      <directoryRecursion>false</directoryRecursion>
      <ignoreDot>true</ignoreDot>
      <anonymous>false</anonymous>
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
    <transformer version="3.12.0">
      <elements/>
      <inboundDataType>HL7V2</inboundDataType>
      <outboundDataType>HL7V2</outboundDataType>
      <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
          <handleRepetitions>true</handleRepetitions>
          <handleSubcomponents>true</handleSubcomponents>
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <stripNamespaces>false</stripNamespaces>
          <segmentDelimiter>\\r</segmentDelimiter>
          <convertLineBreaks>true</convertLineBreaks>
        </serializationProperties>
        <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <segmentDelimiter>\\r</segmentDelimiter>
        </deserializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
          <splitType>MSH_Segment</splitType>
          <batchScript></batchScript>
        </batchProperties>
        <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
        <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
          <successfulACKCode>AA,CA</successfulACKCode>
          <errorACKCode>AE,CE</errorACKCode>
          <rejectedACKCode>AR,CR</rejectedACKCode>
          <validateMessageControlId>true</validateMessageControlId>
          <originalMessageControlId>Destination_Encoded</originalMessageControlId>
          <originalIdMapVariable></originalIdMapVariable>
        </responseValidationProperties>
      </inboundProperties>
      <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
          <handleRepetitions>true</handleRepetitions>
          <handleSubcomponents>true</handleSubcomponents>
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <stripNamespaces>false</stripNamespaces>
          <segmentDelimiter>\\r</segmentDelimiter>
          <convertLineBreaks>true</convertLineBreaks>
        </serializationProperties>
        <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <segmentDelimiter>\\r</segmentDelimiter>
        </deserializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
          <splitType>MSH_Segment</splitType>
          <batchScript></batchScript>
        </batchProperties>
        <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
        <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
          <successfulACKCode>AA,CA</successfulACKCode>
          <errorACKCode>AE,CE</errorACKCode>
          <rejectedACKCode>AR,CR</rejectedACKCode>
          <validateMessageControlId>true</validateMessageControlId>
          <originalMessageControlId>Destination_Encoded</originalMessageControlId>
          <originalIdMapVariable></originalIdMapVariable>
        </responseValidationProperties>
      </outboundProperties>
    </transformer>
    <filter version="3.12.0">
      <elements/>
    </filter>
    <transportName>File Reader</transportName>
    <mode>SOURCE</mode>
    <enabled>true</enabled>
    <waitForPrevious>true</waitForPrevious>'''
dicomListenerXML = '''<metaDataId>0</metaDataId>
    <name>sourceConnector</name>
    <properties class="com.mirth.connect.connectors.dimse.DICOMReceiverProperties" version="3.12.0">
      <pluginProperties/>
      <listenerConnectorProperties version="3.12.0">
        <host>0.0.0.0</host>
        <port>104</port>
      </listenerConnectorProperties>
      <sourceConnectorProperties version="3.12.0">
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
      <applicationEntity></applicationEntity>
      <localHost></localHost>
      <localPort></localPort>
      <localApplicationEntity></localApplicationEntity>
      <soCloseDelay>50</soCloseDelay>
      <releaseTo>5</releaseTo>
      <requestTo>5</requestTo>
      <idleTo>60</idleTo>
      <reaper>10</reaper>
      <rspDelay>0</rspDelay>
      <pdv1>false</pdv1>
      <sndpdulen>16</sndpdulen>
      <rcvpdulen>16</rcvpdulen>
      <async>0</async>
      <bigEndian>false</bigEndian>
      <bufSize>1</bufSize>
      <defts>false</defts>
      <dest></dest>
      <nativeData>false</nativeData>
      <sorcvbuf>0</sorcvbuf>
      <sosndbuf>0</sosndbuf>
      <tcpDelay>true</tcpDelay>
      <keyPW></keyPW>
      <keyStore></keyStore>
      <keyStorePW></keyStorePW>
      <noClientAuth>true</noClientAuth>
      <nossl2>true</nossl2>
      <tls>notls</tls>
      <trustStore></trustStore>
      <trustStorePW></trustStorePW>
    </properties>
    <transformer version="3.12.0">
      <elements/>
      <inboundDataType>HL7V2</inboundDataType>
      <outboundDataType>HL7V2</outboundDataType>
      <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
          <handleRepetitions>true</handleRepetitions>
          <handleSubcomponents>true</handleSubcomponents>
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <stripNamespaces>false</stripNamespaces>
          <segmentDelimiter>\\r</segmentDelimiter>
          <convertLineBreaks>true</convertLineBreaks>
        </serializationProperties>
        <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <segmentDelimiter>\\r</segmentDelimiter>
        </deserializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
          <splitType>MSH_Segment</splitType>
          <batchScript></batchScript>
        </batchProperties>
        <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
        <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
          <successfulACKCode>AA,CA</successfulACKCode>
          <errorACKCode>AE,CE</errorACKCode>
          <rejectedACKCode>AR,CR</rejectedACKCode>
          <validateMessageControlId>true</validateMessageControlId>
          <originalMessageControlId>Destination_Encoded</originalMessageControlId>
          <originalIdMapVariable></originalIdMapVariable>
        </responseValidationProperties>
      </inboundProperties>
      <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
          <handleRepetitions>true</handleRepetitions>
          <handleSubcomponents>true</handleSubcomponents>
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <stripNamespaces>false</stripNamespaces>
          <segmentDelimiter>\\r</segmentDelimiter>
          <convertLineBreaks>true</convertLineBreaks>
        </serializationProperties>
        <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <segmentDelimiter>\\r</segmentDelimiter>
        </deserializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
          <splitType>MSH_Segment</splitType>
          <batchScript></batchScript>
        </batchProperties>
        <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
        <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
          <successfulACKCode>AA,CA</successfulACKCode>
          <errorACKCode>AE,CE</errorACKCode>
          <rejectedACKCode>AR,CR</rejectedACKCode>
          <validateMessageControlId>true</validateMessageControlId>
          <originalMessageControlId>Destination_Encoded</originalMessageControlId>
          <originalIdMapVariable></originalIdMapVariable>
        </responseValidationProperties>
      </outboundProperties>
    </transformer>
    <filter version="3.12.0">
      <elements/>
    </filter>
    <transportName>DICOM Listener</transportName>
    <mode>SOURCE</mode>
    <enabled>true</enabled>
    <waitForPrevious>true</waitForPrevious>'''
databaseReaderXML = '''<metaDataId>0</metaDataId>
    <name>sourceConnector</name>
    <properties class="com.mirth.connect.connectors.jdbc.DatabaseReceiverProperties" version="3.12.0">
      <pluginProperties/>
      <pollConnectorProperties version="3.12.0">
        <pollingType>INTERVAL</pollingType>
        <pollOnStart>false</pollOnStart>
        <pollingFrequency>82800000</pollingFrequency>
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
      <sourceConnectorProperties version="3.12.0">
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
      <driver>org.postgresql.Driver</driver>
      <url>www.google.com</url>
      <username>admin</username>
      <password>admin</password>
      <select>var dbConn;

try {
	dbConn = DatabaseConnectionFactory.createDatabaseConnection(&apos;org.postgresql.Driver&apos;,&apos;www.google.com&apos;,&apos;admin&apos;,&apos;admin&apos;);

	// You may access this result below with $(&apos;column_name&apos;)
	return result;
} finally {
	if (dbConn) { 
		dbConn.close();
	}
}</select>
      <update>// This update script will be executed once after all results have been processed.
var dbConn;

try {
	dbConn = DatabaseConnectionFactory.createDatabaseConnection(&apos;org.postgresql.Driver&apos;,&apos;www.google.com&apos;,&apos;admin&apos;,&apos;admin&apos;);

} finally {
	if (dbConn) { 
		dbConn.close();
	}
}</update>
      <useScript>true</useScript>
      <aggregateResults>false</aggregateResults>
      <cacheResults>true</cacheResults>
      <keepConnectionOpen>true</keepConnectionOpen>
      <updateMode>1</updateMode>
      <retryCount>3</retryCount>
      <retryInterval>10000</retryInterval>
      <fetchSize>1000</fetchSize>
      <encoding>DEFAULT_ENCODING</encoding>
    </properties>
    <transformer version="3.12.0">
      <elements/>
      <inboundTemplate encoding="base64">PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+DQo8cmVzdWx0Lz4NCg==</inboundTemplate>
      <inboundDataType>XML</inboundDataType>
      <outboundDataType>HL7V2</outboundDataType>
      <inboundProperties class="com.mirth.connect.plugins.datatypes.xml.XMLDataTypeProperties" version="3.12.0">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.xml.XMLSerializationProperties" version="3.12.0">
          <stripNamespaces>false</stripNamespaces>
        </serializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.xml.XMLBatchProperties" version="3.12.0">
          <splitType>Element_Name</splitType>
          <elementName></elementName>
          <level>1</level>
          <query></query>
          <batchScript></batchScript>
        </batchProperties>
      </inboundProperties>
      <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
          <handleRepetitions>true</handleRepetitions>
          <handleSubcomponents>true</handleSubcomponents>
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <stripNamespaces>false</stripNamespaces>
          <segmentDelimiter>\\r</segmentDelimiter>
          <convertLineBreaks>true</convertLineBreaks>
        </serializationProperties>
        <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <segmentDelimiter>\\r</segmentDelimiter>
        </deserializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
          <splitType>MSH_Segment</splitType>
          <batchScript></batchScript>
        </batchProperties>
        <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
        <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
          <successfulACKCode>AA,CA</successfulACKCode>
          <errorACKCode>AE,CE</errorACKCode>
          <rejectedACKCode>AR,CR</rejectedACKCode>
          <validateMessageControlId>true</validateMessageControlId>
          <originalMessageControlId>Destination_Encoded</originalMessageControlId>
          <originalIdMapVariable></originalIdMapVariable>
        </responseValidationProperties>
      </outboundProperties>
    </transformer>
    <filter version="3.12.0">
      <elements/>
    </filter>
    <transportName>Database Reader</transportName>
    <mode>SOURCE</mode>
    <enabled>true</enabled>
    <waitForPrevious>true</waitForPrevious>'''
tcpListenerXML = '''<metaDataId>0</metaDataId>
    <name>sourceConnector</name>
    <properties class="com.mirth.connect.connectors.tcp.TcpReceiverProperties" version="3.12.0">
      <pluginProperties/>
      <listenerConnectorProperties version="3.12.0">
        <host>0.0.0.0</host>
        <port>6661</port>
      </listenerConnectorProperties>
      <sourceConnectorProperties version="3.12.0">
        <responseVariable>Auto-generate (After source transformer)</responseVariable>
        <respondAfterProcessing>true</respondAfterProcessing>
        <processBatch>false</processBatch>
        <firstResponse>true</firstResponse>
        <processingThreads>1</processingThreads>
        <resourceIds class="linked-hash-map">
          <entry>
            <string>Default Resource</string>
            <string>[Default Resource]</string>
          </entry>
        </resourceIds>
        <queueBufferSize>1000</queueBufferSize>
      </sourceConnectorProperties>
      <transmissionModeProperties class="com.mirth.connect.plugins.mllpmode.MLLPModeProperties">
        <pluginPointName>MLLP</pluginPointName>
        <startOfMessageBytes>0B</startOfMessageBytes>
        <endOfMessageBytes>1C0D</endOfMessageBytes>
        <useMLLPv2>false</useMLLPv2>
        <ackBytes>06</ackBytes>
        <nackBytes>15</nackBytes>
        <maxRetries>2</maxRetries>
      </transmissionModeProperties>
      <serverMode>true</serverMode>
      <remoteAddress></remoteAddress>
      <remotePort></remotePort>
      <overrideLocalBinding>false</overrideLocalBinding>
      <reconnectInterval>5000</reconnectInterval>
      <receiveTimeout>0</receiveTimeout>
      <bufferSize>65536</bufferSize>
      <maxConnections>10</maxConnections>
      <keepConnectionOpen>true</keepConnectionOpen>
      <dataTypeBinary>false</dataTypeBinary>
      <charsetEncoding>DEFAULT_ENCODING</charsetEncoding>
      <respondOnNewConnection>0</respondOnNewConnection>
      <responseAddress></responseAddress>
      <responsePort></responsePort>
    </properties>
    <transformer version="3.12.0">
      <elements/>
      <inboundDataType>HL7V2</inboundDataType>
      <outboundDataType>HL7V2</outboundDataType>
      <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
          <handleRepetitions>true</handleRepetitions>
          <handleSubcomponents>true</handleSubcomponents>
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <stripNamespaces>false</stripNamespaces>
          <segmentDelimiter>\\r</segmentDelimiter>
          <convertLineBreaks>true</convertLineBreaks>
        </serializationProperties>
        <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <segmentDelimiter>\\r</segmentDelimiter>
        </deserializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
          <splitType>MSH_Segment</splitType>
          <batchScript></batchScript>
        </batchProperties>
        <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
        <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
          <successfulACKCode>AA,CA</successfulACKCode>
          <errorACKCode>AE,CE</errorACKCode>
          <rejectedACKCode>AR,CR</rejectedACKCode>
          <validateMessageControlId>true</validateMessageControlId>
          <originalMessageControlId>Destination_Encoded</originalMessageControlId>
          <originalIdMapVariable></originalIdMapVariable>
        </responseValidationProperties>
      </inboundProperties>
      <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
          <handleRepetitions>true</handleRepetitions>
          <handleSubcomponents>true</handleSubcomponents>
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <stripNamespaces>false</stripNamespaces>
          <segmentDelimiter>\\r</segmentDelimiter>
          <convertLineBreaks>true</convertLineBreaks>
        </serializationProperties>
        <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <segmentDelimiter>\\r</segmentDelimiter>
        </deserializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
          <splitType>MSH_Segment</splitType>
          <batchScript></batchScript>
        </batchProperties>
        <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
        <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
          <successfulACKCode>AA,CA</successfulACKCode>
          <errorACKCode>AE,CE</errorACKCode>
          <rejectedACKCode>AR,CR</rejectedACKCode>
          <validateMessageControlId>true</validateMessageControlId>
          <originalMessageControlId>Destination_Encoded</originalMessageControlId>
          <originalIdMapVariable></originalIdMapVariable>
        </responseValidationProperties>
      </outboundProperties>
    </transformer>
    <filter version="3.12.0">
      <elements/>
    </filter>
    <transportName>TCP Listener</transportName>
    <mode>SOURCE</mode>
    <enabled>true</enabled>
    <waitForPrevious>true</waitForPrevious>'''
jmsListenerXML = '''<metaDataId>0</metaDataId>
    <name>sourceConnector</name>
    <properties class="com.mirth.connect.connectors.jms.JmsReceiverProperties" version="3.12.0">
      <pluginProperties/>
      <useJndi>true</useJndi>
      <jndiProviderUrl>www.google.com</jndiProviderUrl>
      <jndiInitialContextFactory>FactoryExample</jndiInitialContextFactory>
      <jndiConnectionFactoryName>FactoryName</jndiConnectionFactoryName>
      <connectionFactoryClass></connectionFactoryClass>
      <connectionProperties class="linked-hash-map">
        <entry>
          <string>Property 1</string>
          <string>afsdve</string>
        </entry>
        <entry>
          <string>Property 2</string>
          <string>badasf</string>
        </entry>
      </connectionProperties>
      <username></username>
      <password></password>
      <destinationName>Destination</destinationName>
      <topic>false</topic>
      <clientId></clientId>
      <sourceConnectorProperties version="3.12.0">
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
      <selector></selector>
      <reconnectIntervalMillis>10000</reconnectIntervalMillis>
      <durableTopic>false</durableTopic>
    </properties>
    <transformer version="3.12.0">
      <elements/>
      <inboundDataType>HL7V2</inboundDataType>
      <outboundDataType>HL7V2</outboundDataType>
      <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
          <handleRepetitions>true</handleRepetitions>
          <handleSubcomponents>true</handleSubcomponents>
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <stripNamespaces>false</stripNamespaces>
          <segmentDelimiter>\\r</segmentDelimiter>
          <convertLineBreaks>true</convertLineBreaks>
        </serializationProperties>
        <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <segmentDelimiter>\\r</segmentDelimiter>
        </deserializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
          <splitType>MSH_Segment</splitType>
          <batchScript></batchScript>
        </batchProperties>
        <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
        <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
          <successfulACKCode>AA,CA</successfulACKCode>
          <errorACKCode>AE,CE</errorACKCode>
          <rejectedACKCode>AR,CR</rejectedACKCode>
          <validateMessageControlId>true</validateMessageControlId>
          <originalMessageControlId>Destination_Encoded</originalMessageControlId>
          <originalIdMapVariable></originalIdMapVariable>
        </responseValidationProperties>
      </inboundProperties>
      <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
          <handleRepetitions>true</handleRepetitions>
          <handleSubcomponents>true</handleSubcomponents>
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <stripNamespaces>false</stripNamespaces>
          <segmentDelimiter>\\r</segmentDelimiter>
          <convertLineBreaks>true</convertLineBreaks>
        </serializationProperties>
        <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <segmentDelimiter>\\r</segmentDelimiter>
        </deserializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
          <splitType>MSH_Segment</splitType>
          <batchScript></batchScript>
        </batchProperties>
        <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
        <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
          <successfulACKCode>AA,CA</successfulACKCode>
          <errorACKCode>AE,CE</errorACKCode>
          <rejectedACKCode>AR,CR</rejectedACKCode>
          <validateMessageControlId>true</validateMessageControlId>
          <originalMessageControlId>Destination_Encoded</originalMessageControlId>
          <originalIdMapVariable></originalIdMapVariable>
        </responseValidationProperties>
      </outboundProperties>
    </transformer>
    <filter version="3.12.0">
      <elements/>
    </filter>
    <transportName>JMS Listener</transportName>
    <mode>SOURCE</mode>
    <enabled>true</enabled>
    <waitForPrevious>true</waitForPrevious>'''
javascriptReaderXML = '''<metaDataId>0</metaDataId>
    <name>sourceConnector</name>
    <properties class="com.mirth.connect.connectors.js.JavaScriptReceiverProperties" version="3.12.0">
      <pluginProperties/>
      <pollConnectorProperties version="3.12.0">
        <pollingType>INTERVAL</pollingType>
        <pollOnStart>true</pollOnStart>
        <pollingFrequency>23000</pollingFrequency>
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
      <sourceConnectorProperties version="3.12.0">
        <responseVariable>None</responseVariable>
        <respondAfterProcessing>false</respondAfterProcessing>
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
      <script>logger.debug(&quot;Hello&quot;)
//test comment

var i = 0

i++

i = i * 10</script>
    </properties>
    <transformer version="3.12.0">
      <elements/>
      <inboundDataType>HL7V2</inboundDataType>
      <outboundDataType>HL7V2</outboundDataType>
      <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
          <handleRepetitions>true</handleRepetitions>
          <handleSubcomponents>true</handleSubcomponents>
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <stripNamespaces>false</stripNamespaces>
          <segmentDelimiter>\\r</segmentDelimiter>
          <convertLineBreaks>true</convertLineBreaks>
        </serializationProperties>
        <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <segmentDelimiter>\\r</segmentDelimiter>
        </deserializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
          <splitType>MSH_Segment</splitType>
          <batchScript></batchScript>
        </batchProperties>
        <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
        <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
          <successfulACKCode>AA,CA</successfulACKCode>
          <errorACKCode>AE,CE</errorACKCode>
          <rejectedACKCode>AR,CR</rejectedACKCode>
          <validateMessageControlId>true</validateMessageControlId>
          <originalMessageControlId>Destination_Encoded</originalMessageControlId>
          <originalIdMapVariable></originalIdMapVariable>
        </responseValidationProperties>
      </inboundProperties>
      <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
          <handleRepetitions>true</handleRepetitions>
          <handleSubcomponents>true</handleSubcomponents>
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <stripNamespaces>false</stripNamespaces>
          <segmentDelimiter>\\r</segmentDelimiter>
          <convertLineBreaks>true</convertLineBreaks>
        </serializationProperties>
        <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <segmentDelimiter>\\r</segmentDelimiter>
        </deserializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
          <splitType>MSH_Segment</splitType>
          <batchScript></batchScript>
        </batchProperties>
        <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
        <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
          <successfulACKCode>AA,CA</successfulACKCode>
          <errorACKCode>AE,CE</errorACKCode>
          <rejectedACKCode>AR,CR</rejectedACKCode>
          <validateMessageControlId>true</validateMessageControlId>
          <originalMessageControlId>Destination_Encoded</originalMessageControlId>
          <originalIdMapVariable></originalIdMapVariable>
        </responseValidationProperties>
      </outboundProperties>
    </transformer>
    <filter version="3.12.0">
      <elements/>
    </filter>
    <transportName>JavaScript Reader</transportName>
    <mode>SOURCE</mode>
    <enabled>true</enabled>
    <waitForPrevious>true</waitForPrevious>'''
httpListenerXML = '''<metaDataId>0</metaDataId>
    <name>sourceConnector</name>
    <properties class="com.mirth.connect.connectors.http.HttpReceiverProperties" version="3.12.0">
      <pluginProperties>
        <com.mirth.connect.plugins.httpauth.NoneHttpAuthProperties version="3.12.0">
  <authType>NONE</authType>
        </com.mirth.connect.plugins.httpauth.NoneHttpAuthProperties>
      </pluginProperties>
      <listenerConnectorProperties version="3.12.0">
        <host>0.0.0.0</host>
        <port>80</port>
      </listenerConnectorProperties>
      <sourceConnectorProperties version="3.12.0">
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
      <xmlBody>false</xmlBody>
      <parseMultipart>true</parseMultipart>
      <includeMetadata>false</includeMetadata>
      <binaryMimeTypes>application/.*(?&lt;!json|xml)$|image/.*|video/.*|audio/.*</binaryMimeTypes>
      <binaryMimeTypesRegex>true</binaryMimeTypesRegex>
      <responseContentType>text/plain</responseContentType>
      <responseDataTypeBinary>false</responseDataTypeBinary>
      <responseStatusCode></responseStatusCode>
      <responseHeaders class="linked-hash-map">
        <entry>
          <string>Property 1</string>
          <list>
            <string>adfce</string>
          </list>
        </entry>
      </responseHeaders>
      <responseHeadersVariable></responseHeadersVariable>
      <useResponseHeadersVariable>false</useResponseHeadersVariable>
      <charset>UTF-8</charset>
      <contextPath>baseContext/example</contextPath>
      <timeout>30000</timeout>
      <staticResources>
        <com.mirth.connect.connectors.http.HttpStaticResource>
          <contextPath>path1</contextPath>
          <resourceType>FILE</resourceType>
          <value>directory</value>
          <contentType>text/plain</contentType>
        </com.mirth.connect.connectors.http.HttpStaticResource>
        <com.mirth.connect.connectors.http.HttpStaticResource>
          <contextPath>path2</contextPath>
          <resourceType>DIRECTORY</resourceType>
          <value>face</value>
          <contentType>text/plain</contentType>
        </com.mirth.connect.connectors.http.HttpStaticResource>
        <com.mirth.connect.connectors.http.HttpStaticResource>
          <contextPath>path3</contextPath>
          <resourceType>CUSTOM</resourceType>
          <value>vaadsfea</value>
          <contentType>text/plain</contentType>
        </com.mirth.connect.connectors.http.HttpStaticResource>
      </staticResources>
    </properties>
    <transformer version="3.12.0">
      <elements/>
      <inboundDataType>XML</inboundDataType>
      <outboundDataType>HL7V2</outboundDataType>
      <inboundProperties class="com.mirth.connect.plugins.datatypes.xml.XMLDataTypeProperties" version="3.12.0">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.xml.XMLSerializationProperties" version="3.12.0">
          <stripNamespaces>false</stripNamespaces>
        </serializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.xml.XMLBatchProperties" version="3.12.0">
          <splitType>Element_Name</splitType>
          <elementName></elementName>
          <level>1</level>
          <query></query>
          <batchScript></batchScript>
        </batchProperties>
      </inboundProperties>
      <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
          <handleRepetitions>true</handleRepetitions>
          <handleSubcomponents>true</handleSubcomponents>
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <stripNamespaces>false</stripNamespaces>
          <segmentDelimiter>\\r</segmentDelimiter>
          <convertLineBreaks>true</convertLineBreaks>
        </serializationProperties>
        <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <segmentDelimiter>\\r</segmentDelimiter>
        </deserializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
          <splitType>MSH_Segment</splitType>
          <batchScript></batchScript>
        </batchProperties>
        <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
        <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
          <successfulACKCode>AA,CA</successfulACKCode>
          <errorACKCode>AE,CE</errorACKCode>
          <rejectedACKCode>AR,CR</rejectedACKCode>
          <validateMessageControlId>true</validateMessageControlId>
          <originalMessageControlId>Destination_Encoded</originalMessageControlId>
          <originalIdMapVariable></originalIdMapVariable>
        </responseValidationProperties>
      </outboundProperties>
    </transformer>
    <filter version="3.12.0">
      <elements/>
    </filter>
    <transportName>HTTP Listener</transportName>
    <mode>SOURCE</mode>
    <enabled>true</enabled>
    <waitForPrevious>true</waitForPrevious>'''
channelReaderXML = '''<metaDataId>0</metaDataId>
    <name>sourceConnector</name>
    <properties class="com.mirth.connect.connectors.vm.VmReceiverProperties" version="3.12.0">
      <pluginProperties/>
      <sourceConnectorProperties version="3.12.0">
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
    </properties>
    <transformer version="3.12.0">
      <elements/>
      <inboundDataType>HL7V2</inboundDataType>
      <outboundDataType>HL7V2</outboundDataType>
      <inboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
          <handleRepetitions>true</handleRepetitions>
          <handleSubcomponents>true</handleSubcomponents>
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <stripNamespaces>false</stripNamespaces>
          <segmentDelimiter>\\r</segmentDelimiter>
          <convertLineBreaks>true</convertLineBreaks>
        </serializationProperties>
        <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <segmentDelimiter>\\r</segmentDelimiter>
        </deserializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
          <splitType>MSH_Segment</splitType>
          <batchScript></batchScript>
        </batchProperties>
        <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
        <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
          <successfulACKCode>AA,CA</successfulACKCode>
          <errorACKCode>AE,CE</errorACKCode>
          <rejectedACKCode>AR,CR</rejectedACKCode>
          <validateMessageControlId>true</validateMessageControlId>
          <originalMessageControlId>Destination_Encoded</originalMessageControlId>
          <originalIdMapVariable></originalIdMapVariable>
        </responseValidationProperties>
      </inboundProperties>
      <outboundProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties" version="3.12.0">
        <serializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties" version="3.12.0">
          <handleRepetitions>true</handleRepetitions>
          <handleSubcomponents>true</handleSubcomponents>
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <stripNamespaces>false</stripNamespaces>
          <segmentDelimiter>\\r</segmentDelimiter>
          <convertLineBreaks>true</convertLineBreaks>
        </serializationProperties>
        <deserializationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties" version="3.12.0">
          <useStrictParser>false</useStrictParser>
          <useStrictValidation>false</useStrictValidation>
          <segmentDelimiter>\\r</segmentDelimiter>
        </deserializationProperties>
        <batchProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties" version="3.12.0">
          <splitType>MSH_Segment</splitType>
          <batchScript></batchScript>
        </batchProperties>
        <responseGenerationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties" version="3.12.0">
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
        <responseValidationProperties class="com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties" version="3.12.0">
          <successfulACKCode>AA,CA</successfulACKCode>
          <errorACKCode>AE,CE</errorACKCode>
          <rejectedACKCode>AR,CR</rejectedACKCode>
          <validateMessageControlId>true</validateMessageControlId>
          <originalMessageControlId>Destination_Encoded</originalMessageControlId>
          <originalIdMapVariable></originalIdMapVariable>
        </responseValidationProperties>
      </outboundProperties>
    </transformer>
    <filter version="3.12.0">
      <elements/>
    </filter>
    <transportName>Channel Reader</transportName>
    <mode>SOURCE</mode>
    <enabled>true</enabled>
    <waitForPrevious>true</waitForPrevious>'''

# Scheme Properties
sftpSchemePropXML = '''<passwordAuth>false</passwordAuth>
          <keyAuth>true</keyAuth>
          <keyFile>test pkaey</keyFile>
          <passPhrase>passpharse</passPhrase>
          <hostKeyChecking>yes</hostKeyChecking>
          <knownHostsFile>test.txt</knownHostsFile>
          <configurationSettings class="linked-hash-map">
            <entry>
              <string>Property1</string>
              <string>asde</string>
            </entry>
            <entry>
              <string>Property2</string>
              <string>adfac</string>
            </entry>
        </configurationSettings>'''
s3SchemePropXML = '''<useDefaultCredentialProviderChain>true</useDefaultCredentialProviderChain>
          <useTemporaryCredentials>false</useTemporaryCredentials>
          <duration>7200</duration>
          <region>us-east-1</region>
          <customHeaders class="linked-hash-map">
            <entry>
              <string>Property1</string>
              <list>
                <string>custom</string>
              </list>
            </entry>
            <entry>
              <string>Property2</string>
              <list>
                <string>another custom</string>
              </list>
            </entry>
          </customHeaders>'''
ftpSchemePropXML = '''<initialCommands>
            <string>NAMEFMT</string>
            <string>NAMEFMT</string>
          </initialCommands>'''
#endregion
