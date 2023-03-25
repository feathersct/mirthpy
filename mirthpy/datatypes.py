from typing import Type
from .utilities import escape, getXMLString
from .mirthElement import MirthElement

#region Data Type Properties
class DataTypeProperties(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

class HL7v2DataTypeProperties(DataTypeProperties):
    def __init__(self, uXml=None):
        DataTypeProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties'
        self.dataType = 'HL7V2'
        self.serializationProperties = HL7v2SerializationProperties()
        self.deserializationProperties = HL7v2DeserializationProperties()
        self.batchProperties = HL7v2BatchProperties()
        self.responseGenerationProperties = HL7v2ResponseGenerationProperties()
        self.responseValidationProperties = HL7v2ResponseValidationProperties()

        if uXml is not None:
            self.serializationProperties = HL7v2SerializationProperties(self.root.find('serializationProperties'))
            self.deserializationProperties = HL7v2DeserializationProperties(self.root.find('deserializationProperties'))
            self.batchProperties = HL7v2BatchProperties(self.root.find('batchProperties'))
            self.responseGenerationProperties = HL7v2ResponseGenerationProperties(self.root.find('responseGenerationProperties'))
            self.responseValidationProperties = HL7v2ResponseValidationProperties(self.root.find('responseValidationProperties'))

    def getXML(self, version="3.12.0"):
        xml = f'''<serializationProperties class="{self.serializationProperties.className}" version="{version}">
                    {self.serializationProperties.getXML(version)}
                </serializationProperties>
                <deserializationProperties class="{self.deserializationProperties.className}" version="{version}">
                    {self.deserializationProperties.getXML(version)}
                </deserializationProperties>
                <batchProperties class="{self.batchProperties.className}" version="{version}">
                    {self.batchProperties.getXML(version)}
                </batchProperties>
                <responseGenerationProperties class="{self.responseGenerationProperties.className}" version="{version}">
                    {self.responseGenerationProperties.getXML(version)}
                </responseGenerationProperties>
                <responseValidationProperties class="{self.responseValidationProperties.className}" version="{version}">
                    {self.responseValidationProperties.getXML(version)}
                </responseValidationProperties>
            '''
        return xml

class XMLDataTypeProperties(DataTypeProperties):
    def __init__(self, uXml=None):
        DataTypeProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.xml.XMLDataTypeProperties'
        self.serializationProperties = XMLSerializationProperties()
        self.batchProperties = XMLBatchProperties()

        if uXml is not None:
            self.serializationProperties = XMLSerializationProperties(self.root.find('serializationProperties'))
            self.batchProperties = XMLBatchProperties(self.root.find('batchProperties'))

    def getXML(self, version="3.12.0"):
        xml = f'''<serializationProperties class="{self.serializationProperties.className}" version="{version}">
                    {self.serializationProperties.getXML(version)}
                </serializationProperties>
                <batchProperties class="{self.batchProperties.className}" version="{version}">
                    {self.batchProperties.getXML(version)}
                </batchProperties>
            '''
        return xml

def datatypeProps(c: str) -> Type:
    if c == "com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties":
        return HL7v2DataTypeProperties
    elif c == "com.mirth.connect.plugins.datatypes.xml.XMLDataTypeProperties":
        return XMLDataTypeProperties
    else:
        return DataTypeProperties
#endregion

#region SerializationProperties
class SerializationProperties(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

class HL7v2SerializationProperties(SerializationProperties):
    def __init__(self, uXml=None):
        SerializationProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties'

        self.handleRepetitions = 'true'
        self.handleSubcomponents = 'true'
        self.useStrictParser = 'false'
        self.useStrictValidation = 'false'
        self.stripNamespaces = 'false'
        self.segmentDelimiter = '\\r'
        self.convertLineBreaks = 'true'

        if uXml is not None:
            self.handleRepetitions = self.getSafeText('handleRepetitions')
            self.handleSubcomponents = self.getSafeText('handleSubcomponents')
            self.useStrictParser = self.getSafeText('useStrictParser')
            self.useStrictValidation = self.getSafeText('useStrictValidation')
            self.stripNamespaces = self.getSafeText('stripNamespaces')
            self.segmentDelimiter = self.getSafeText('segmentDelimiter')
            self.convertLineBreaks = self.getSafeText('convertLineBreaks')

    def getXML(self, version="3.12.0"):
        xml = f'''{getXMLString(self.handleRepetitions, "handleRepetitions")}
                {getXMLString(self.handleSubcomponents, "handleSubcomponents")}
                {getXMLString(self.useStrictParser, "useStrictParser")}
                {getXMLString(self.useStrictValidation, "useStrictValidation")}
                {getXMLString(self.stripNamespaces, "stripNamespaces")}
                {getXMLString(self.segmentDelimiter, "segmentDelimiter")}
                {getXMLString(self.convertLineBreaks, "convertLineBreaks")}'''
        return xml
    
class XMLSerializationProperties(SerializationProperties):
    def __init__(self, uXml=None):
        SerializationProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.xml.XMLSerializationProperties'

        self.stripNamespaces = 'false'

        if uXml is not None:
            self.stripNamespaces = self.getSafeText('stripNamespaces')

    def getXML(self, version="3.12.0"):
        xml = f'''{getXMLString(self.stripNamespaces, "stripNamespaces")}'''
        return xml
    
def serializationProps(c: str) -> Type:
    if c == "com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties":
        return HL7v2SerializationProperties
    elif c == "com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties":
        return XMLSerializationProperties
    else:
        return SerializationProperties
#endregion

#region Deserialization Properties
class DeserializationProperties(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

class HL7v2DeserializationProperties(DeserializationProperties):
    def __init__(self, uXml=None):
        DeserializationProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties'

        self.useStrictParser = 'false'
        self.useStrictValidation = 'false'
        self.segmentDelimiter = '\\r'

        if uXml is not None:
            self.useStrictParser = self.getSafeText('useStrictParser')
            self.useStrictValidation = self.getSafeText('useStrictValidation')
            self.segmentDelimiter = self.getSafeText('segmentDelimiter')

    def getXML(self, version="3.12.0"):
        xml = f'''{getXMLString(self.useStrictParser, "useStrictParser")}
                {getXMLString(self.useStrictValidation, "useStrictValidation")}
                {getXMLString(self.segmentDelimiter, "segmentDelimiter")}'''
        return xml
    
def deserializationProps(c: str) -> Type:
    if c == "com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties":
        return HL7v2DeserializationProperties
    else:
        return DeserializationProperties
#endregion

#region Batch Properties
class BatchProperties(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

class HL7v2BatchProperties(BatchProperties):
    def __init__(self, uXml=None):
        BatchProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties'

        self.splitType = 'MSH_Segment'
        self.batchScript = ''

        if uXml is not None:
            self.splitType = self.getSafeText('splitType')
            self.batchScript = self.getSafeText('batchScript')

    def getXML(self, version="3.12.0"):
        xml = f'''{getXMLString(self.splitType, "splitType")}
                {getXMLString(self.batchScript, "batchScript")}'''
        return xml
    
class XMLBatchProperties(BatchProperties):
    def __init__(self, uXml=None):
        BatchProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.xml.XMLBatchProperties'

        self.splitType = 'Element_Name'
        self.elementName = ''
        self.level = '1'
        self.query = ''
        self.batchScript = ''

        if uXml is not None:
            self.splitType = self.getSafeText('splitType')
            self.elementName = self.getSafeText('elementName')
            self.level = self.getSafeText('level')
            self.query = self.getSafeText('query')
            self.batchScript = self.getSafeText('batchScript')

    def getXML(self, version="3.12.0"):
        xml = f'''{getXMLString(self.splitType, "splitType")}
                {getXMLString(self.elementName, "elementName")}
                {getXMLString(self.level, "level")}
                {getXMLString(self.query, "query")}
                {getXMLString(self.batchScript, "batchScript")}'''
        return xml

def batchProps(c: str) -> Type:
    if c == "com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties":
        return HL7v2BatchProperties
    elif c == "com.mirth.connect.plugins.datatypes.xml.XMLBatchProperties":
        return XMLBatchProperties
    else:
        return BatchProperties
#endregion

#region Response Generation Properties
class ResponseGenerationProperties(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

class HL7v2ResponseGenerationProperties(ResponseGenerationProperties):
    def __init__(self, uXml=None):
        ResponseGenerationProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties'

        self.segmentDelimiter = '\\r'
        self.successfulACKCode = 'AA'
        self.successfulACKMessage = ''
        self.errorACKCode = 'AE'
        self.errorACKMessage = 'An Error Occurred Processing Message.'
        self.rejectedACKCode = 'AR'
        self.rejectedACKMessage = 'Message Rejected.'
        self.msh15ACKAccept = 'false'
        self.dateFormat = 'yyyyMMddHHmmss.SSS'

        if uXml is not None:
            self.segmentDelimiter = self.getSafeText('segmentDelimiter')
            self.successfulACKCode = self.getSafeText('successfulACKCode')
            self.successfulACKMessage = self.getSafeText('successfulACKMessage')
            self.errorACKCode = self.getSafeText('errorACKCode')
            self.errorACKMessage = self.getSafeText('errorACKMessage')
            self.rejectedACKCode = self.getSafeText('rejectedACKCode')
            self.rejectedACKMessage = self.getSafeText('rejectedACKMessage')
            self.msh15ACKAccept = self.getSafeText('msh15ACKAccept')
            self.dateFormat = self.getSafeText('dateFormat')

    def getXML(self, version="3.12.0"):
        xml = f'''{getXMLString(self.segmentDelimiter, "segmentDelimiter")}
        {getXMLString(self.successfulACKCode, "successfulACKCode")}
        {getXMLString(self.successfulACKMessage, "successfulACKMessage")}
        {getXMLString(self.errorACKCode, "errorACKCode")}
        {getXMLString(self.errorACKMessage, "errorACKMessage")}
        {getXMLString(self.rejectedACKCode, "rejectedACKCode")}
        {getXMLString(self.rejectedACKMessage, "rejectedACKMessage")}
        {getXMLString(self.msh15ACKAccept, "msh15ACKAccept")}
        {getXMLString(self.dateFormat, "dateFormat")}'''

        return xml
    
def genProps(c: str) -> Type:
    if c == "com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseGenerationProperties":
        return HL7v2ResponseGenerationProperties
    else:
        return ResponseGenerationProperties
#endregion

#region Response Validation Properties
class ResponseValidationProperties(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

class HL7v2ResponseValidationProperties(ResponseValidationProperties):
    def __init__(self, uXml=None):
        ResponseValidationProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties'
        
        self.successfulACKCode = 'AA,CA'
        self.errorACKCode = 'AE,CE'
        self.rejectedACKCode = 'AR,CR'
        self.validateMessageControlId = 'true'
        self.originalMessageControlId = 'Destination_Encoded'
        self.originalIdMapVariable = ''

        if uXml is not None:
            self.successfulACKCode = self.getSafeText('successfulACKCode')
            self.errorACKCode = self.getSafeText('errorACKCode')
            self.rejectedACKCode = self.getSafeText('rejectedACKCode')
            self.validateMessageControlId = self.getSafeText('validateMessageControlId')
            self.originalMessageControlId = self.getSafeText('originalMessageControlId')
            self.originalIdMapVariable = self.getSafeText('originalIdMapVariable')

    def getXML(self, version="3.12.0"):
        xml = f'''{getXMLString(self.successfulACKCode, "successfulACKCode")}
        {getXMLString(self.errorACKCode, "errorACKCode")}
        {getXMLString(self.rejectedACKCode, "rejectedACKCode")}
        {getXMLString(self.validateMessageControlId, "validateMessageControlId")}
        {getXMLString(self.originalMessageControlId, "originalMessageControlId")}
        {getXMLString(self.originalIdMapVariable, "originalIdMapVariable")}'''

        return xml

def validProps(c: str) -> Type:
    if c == "com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties":
        return HL7v2ResponseValidationProperties
    else:
        return ResponseValidationProperties

#endregion