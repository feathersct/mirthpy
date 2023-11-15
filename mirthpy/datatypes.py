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
        xml = '<serializationProperties class="{}" version="{}">'.format(self.serializationProperties.className, version)
        xml += self.serializationProperties.getXML(version)
        xml += '</serializationProperties>'
        xml += '<deserializationProperties class="{}" version="{}">'.format(self.deserializationProperties.className, version)
        xml += self.deserializationProperties.getXML(version)
        xml += '</deserializationProperties>'
        xml += '<batchProperties class="{}" version="{}">'.format(self.batchProperties.className, version)
        xml += self.batchProperties.getXML(version)
        xml += '</batchProperties>'
        xml += '<responseGenerationProperties class="{}" version="{}">'.format(self.responseGenerationProperties.className, version)
        xml += self.responseGenerationProperties.getXML(version)
        xml += '</responseGenerationProperties>'
        xml += '<responseValidationProperties class="{}" version="{}">'.format(self.responseValidationProperties.className, version)
        xml += self.responseValidationProperties.getXML(version)
        xml += '</responseValidationProperties>'

        return xml

class HL7V3DataTypeProperties(DataTypeProperties):
    def __init__(self, uXml=None):
        DataTypeProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.hl7v3.HL7V3DataTypeProperties'
        self.dataType = 'HL7V3'

        self.serializationProperties = HL7V3SerializationProperties()
        self.batchProperties = HL7V3BatchProperties()

        if uXml is not None:
            self.serializationProperties = HL7V3SerializationProperties(self.root.find('serializationProperties'))
            self.batchProperties = HL7V3BatchProperties(self.root.find('batchProperties'))

    def getXML(self, version="3.12.0"):
        xml = '<serializationProperties class="{}" version="{}">'.format(self.serializationProperties.className, version)
        xml += self.serializationProperties.getXML(version)
        xml += '</serializationProperties>'
        xml += '<batchProperties class="{}" version="{}">'.format(self.batchProperties.className, version)
        xml += self.batchProperties.getXML(version)
        xml += '</batchProperties>'

        return xml

class XMLDataTypeProperties(DataTypeProperties):
    def __init__(self, uXml=None):
        DataTypeProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.xml.XMLDataTypeProperties'
        self.dataType = 'XML'

        self.serializationProperties = XMLSerializationProperties()
        self.batchProperties = XMLBatchProperties()

        if uXml is not None:
            self.serializationProperties = XMLSerializationProperties(self.root.find('serializationProperties'))
            self.batchProperties = XMLBatchProperties(self.root.find('batchProperties'))

    def getXML(self, version="3.12.0"):
        xml = '<serializationProperties class="{}" version="{}">'.format(self.serializationProperties.className, version)
        xml += self.serializationProperties.getXML(version)
        xml += '</serializationProperties>'
        xml += '<batchProperties class="{}" version="{}">'.format(self.batchProperties.className, version)
        xml += self.batchProperties.getXML(version)
        xml += '</batchProperties>'
        return xml
    
class RawDataTypeProperties(DataTypeProperties):
    def __init__(self, uXml=None):
        DataTypeProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.raw.RawDataTypeProperties'
        self.dataType = 'RAW'

        self.batchProperties = RawBatchProperties()

        if uXml is not None:
            self.batchProperties = RawBatchProperties(self.root.find('batchProperties'))

    def getXML(self, version="3.12.0"):
        xml = '<batchProperties class="{}" version="{}">'.format(self.batchProperties.className, version)
        xml += self.batchProperties.getXML(version)
        xml += '</batchProperties>'
        return xml

class DelimitedDataTypeProperties(DataTypeProperties):
    def __init__(self, uXml=None):
        DataTypeProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.delimited.DelimitedDataTypeProperties'
        self.dataType = 'DELIMITED'
        self.serializationProperties = DelimitedSerializationProperties()
        self.deserializationProperties = DelimitedDeserializationProperties()
        self.batchProperties = DelimitedBatchProperties()

        if uXml is not None:
            self.serializationProperties = DelimitedSerializationProperties(self.root.find('serializationProperties'))
            self.deserializationProperties = DelimitedDeserializationProperties(self.root.find('deserializationProperties'))
            self.batchProperties = DelimitedBatchProperties(self.root.find('batchProperties'))

    def getXML(self, version="3.12.0"):
        xml = '<serializationProperties class="{}" version="{}">'.format(self.serializationProperties.className, version)
        xml += self.serializationProperties.getXML(version)
        xml += '</serializationProperties>'
        xml += '<deserializationProperties class="{}" version="{}">'.format(self.deserializationProperties.className, version)
        xml += self.deserializationProperties.getXML(version)
        xml += '</deserializationProperties>'
        xml += '<batchProperties class="{}" version="{}">'.format(self.batchProperties.className, version)
        xml += self.batchProperties.getXML(version)
        xml += '</batchProperties>'
        return xml

class EDIDataTypeProperties(DataTypeProperties):
    def __init__(self, uXml=None):
        DataTypeProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.edi.EDIDataTypeProperties'
        self.dataType = 'EDI/X12'

        self.serializationProperties = EDISerializationProperties()
        self.batchProperties = DelimitedBatchProperties()

        if uXml is not None:
            self.serializationProperties = EDISerializationProperties(self.root.find('serializationProperties'))
            self.batchProperties = EDIBatchProperties(self.root.find('batchProperties'))

    def getXML(self, version="3.12.0"):
        xml = '<serializationProperties class="{}" version="{}">'.format(self.serializationProperties.className, version)
        xml += self.serializationProperties.getXML(version)
        xml += '</serializationProperties>'
        xml += '<batchProperties class="{}" version="{}">'.format(self.batchProperties.className, version)
        xml += self.batchProperties.getXML(version)
        xml += '</batchProperties>'
        return xml

class DICOMDataTypeProperties(DataTypeProperties):
    def __init__(self, uXml=None):
        DataTypeProperties.__init__(self, uXml)
        self.dataType = 'DICOM'
        self.className = 'com.mirth.connect.plugins.datatypes.dicom.DICOMDataTypeProperties'

        # this data type doesn't have any properties

class JSONDataTypeProperties(DataTypeProperties):
    def __init__(self, uXml=None):
        DataTypeProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.json.JSONDataTypeProperties'
        self.dataType = 'JSON'

        self.batchProperties = JSONBatchProperties()

        if uXml is not None:
            self.batchProperties = JSONBatchProperties(self.root.find('batchProperties'))

    def getXML(self, version="3.12.0"):
        xml = '<batchProperties class="{}" version="{}">'.format(self.batchProperties.className, version)
        xml += self.batchProperties.getXML(version)
        xml += '</batchProperties>'
        return xml

class NCPDPDataTypeProperties(DataTypeProperties):
    def __init__(self, uXml=None):
        DataTypeProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.ncpdp.NCPDPDataTypeProperties'
        self.dataType = 'NCPDP'

        self.serializationProperties = NCPDPSerializationProperties()
        self.deserializationProperties = NCPDPDeserializationProperties()
        self.batchProperties = NCPDPBatchProperties()

        if uXml is not None:
            self.serializationProperties = NCPDPSerializationProperties(self.root.find('serializationProperties'))
            self.deserializationProperties = NCPDPDeserializationProperties(self.root.find('deserializationProperties'))
            self.batchProperties = NCPDPBatchProperties(self.root.find('batchProperties'))

    def getXML(self, version="3.12.0"):
        xml = '<serializationProperties class="{}" version="{}">'.format(self.serializationProperties.className, version)
        xml += self.serializationProperties.getXML(version)
        xml += '</serializationProperties>'
        xml += '<deserializationProperties class="{}" version="{}">'.format(self.deserializationProperties.className, version)
        xml += self.deserializationProperties.getXML(version)
        xml += '</deserializationProperties>'
        xml += '<batchProperties class="{}" version="{}">'.format(self.batchProperties.className, version)
        xml += self.batchProperties.getXML(version)
        xml += '</batchProperties>'

        return xml

class FhirDataTypeProperties(DataTypeProperties):
    def __init__(self, uXml=None):
        DataTypeProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.fhir.shared.FhirDataTypeProperties'
        self.dataType = 'FHIR'

        self.serializationProperties = FhirSerializationProperties()
        self.deserializationProperties = FhirDeserializationProperties()
        self.batchProperties = FhirBatchProperties()

        if uXml is not None:
            self.serializationProperties = FhirSerializationProperties(self.root.find('serializationProperties'))
            self.deserializationProperties = FhirDeserializationProperties(self.root.find('deserializationProperties'))
            self.batchProperties = FhirBatchProperties(self.root.find('batchProperties'))

    def getXML(self, version="3.12.0"):
        xml = '<serializationProperties class="{}" version="{}">'.format(self.serializationProperties.className, version)
        xml += self.serializationProperties.getXML(version)
        xml += '</serializationProperties>'
        xml += '<deserializationProperties class="{}" version="{}">'.format(self.deserializationProperties.className, version)
        xml += self.deserializationProperties.getXML(version)
        xml += '</deserializationProperties>'
        xml += '<batchProperties class="{}" version="{}">'.format(self.batchProperties.className, version)
        xml += self.batchProperties.getXML(version)
        xml += '</batchProperties>'

        return xml

def datatypeProps(c: str) -> Type:
    if c == "com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DataTypeProperties":
        return HL7v2DataTypeProperties
    elif c == "com.mirth.connect.plugins.datatypes.hl7v3.HL7V3DataTypeProperties":
        return HL7V3DataTypeProperties
    elif c == "com.mirth.connect.plugins.datatypes.xml.XMLDataTypeProperties":
        return XMLDataTypeProperties
    elif c == "com.mirth.connect.plugins.datatypes.raw.RawDataTypeProperties":
        return RawDataTypeProperties
    elif c == "com.mirth.connect.plugins.datatypes.delimited.DelimitedDataTypeProperties":
        return DelimitedDataTypeProperties
    elif c == "com.mirth.connect.plugins.datatypes.dicom.DICOMDataTypeProperties":
        return DICOMDataTypeProperties
    elif c == "com.mirth.connect.plugins.datatypes.edi.EDIDataTypeProperties":
        return EDIDataTypeProperties
    elif c == "com.mirth.connect.plugins.datatypes.json.JSONDataTypeProperties":
        return JSONDataTypeProperties
    elif c == "com.mirth.connect.plugins.datatypes.ncpdp.NCPDPDataTypeProperties":
        return NCPDPDataTypeProperties
    elif c == 'com.mirth.connect.plugins.datatypes.fhir.shared.FhirDataTypeProperties':
        return FhirDataTypeProperties
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
        xml = getXMLString(self.handleRepetitions, "handleRepetitions")
        xml += getXMLString(self.handleSubcomponents, "handleSubcomponents")
        xml += getXMLString(self.useStrictParser, "useStrictParser")
        xml += getXMLString(self.useStrictValidation, "useStrictValidation")
        xml += getXMLString(self.stripNamespaces, "stripNamespaces")
        xml += getXMLString(self.segmentDelimiter, "segmentDelimiter")
        xml += getXMLString(self.convertLineBreaks, "convertLineBreaks")

        return xml

class HL7V3SerializationProperties(SerializationProperties):
    def __init__(self, uXml=None):
        SerializationProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.hl7v3.HL7V3SerializationProperties'

        self.stripNamespaces = 'false'

        if uXml is not None:
            self.stripNamespaces = self.getSafeText('stripNamespaces')

    def getXML(self, version="3.12.0"):
        xml = getXMLString(self.stripNamespaces, "stripNamespaces")

        return xml
    
class XMLSerializationProperties(SerializationProperties):
    def __init__(self, uXml=None):
        SerializationProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.xml.XMLSerializationProperties'

        self.stripNamespaces = 'false'

        if uXml is not None:
            self.stripNamespaces = self.getSafeText('stripNamespaces')

    def getXML(self, version="3.12.0"):
        xml = getXMLString(self.stripNamespaces, "stripNamespaces")
        return xml
    
class DelimitedSerializationProperties(SerializationProperties):
    def __init__(self, uXml=None):
        SerializationProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.delimited.DelimitedSerializationProperties'

        self.columnDelimiter = ','
        self.recordDelimiter = '\\n'
        self.quoteToken = '"'
        self.escapeWithDoubleQuote = 'true'
        self.quoteEscapeToken = '\\'
        self.numberedRows = 'false'
        self.ignoreCR = 'true'

        if uXml is not None:
            self.columnDelimiter = self.getSafeText('columnDelimiter')
            self.recordDelimiter = self.getSafeText('recordDelimiter')
            self.quoteToken = self.getSafeText('quoteToken')
            self.escapeWithDoubleQuote = self.getSafeText('escapeWithDoubleQuote')
            self.quoteEscapeToken = self.getSafeText('quoteEscapeToken')
            self.numberedRows = self.getSafeText('numberedRows')
            self.ignoreCR = self.getSafeText('ignoreCR')

    def getXML(self, version="3.12.0"):
        xml = getXMLString(self.columnDelimiter, "columnDelimiter")
        xml += getXMLString(self.recordDelimiter, "recordDelimiter")
        xml += getXMLString(escape(self.quoteToken), "quoteToken")
        xml += getXMLString(self.escapeWithDoubleQuote, "escapeWithDoubleQuote")
        xml += getXMLString(self.quoteEscapeToken, "quoteEscapeToken")
        xml += getXMLString(self.numberedRows, "numberedRows")
        xml += getXMLString(self.ignoreCR, "ignoreCR")
        return xml
    
class EDISerializationProperties(SerializationProperties):
    def __init__(self, uXml=None):
        SerializationProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.edi.EDISerializationProperties'

        self.segmentDelimiter = '~'
        self.elementDelimiter = '*'
        self.subelementDelimiter = ':'
        self.inferX12Delimiters = 'true'

        if uXml is not None:
            self.segmentDelimiter = self.getSafeText('segmentDelimiter')
            self.elementDelimiter = self.getSafeText('elementDelimiter')
            self.subelementDelimiter = self.getSafeText('subelementDelimiter')
            self.inferX12Delimiters = self.getSafeText('inferX12Delimiters')

    def getXML(self, version="3.12.0"):
        xml = getXMLString(self.segmentDelimiter, "segmentDelimiter")
        xml += getXMLString(self.elementDelimiter, "elementDelimiter")
        xml += getXMLString(self.subelementDelimiter, "subelementDelimiter")
        xml += getXMLString(self.inferX12Delimiters, "inferX12Delimiters")
        return xml
    
class NCPDPSerializationProperties(SerializationProperties):
    def __init__(self, uXml=None):
        SerializationProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.ncpdp.NCPDPSerializationProperties'

        self.segmentDelimiter = '0x1E'
        self.groupDelimiter = '0x1D'
        self.fieldDelimiter = '0x1C'

        if uXml is not None:
            self.segmentDelimiter = self.getSafeText('segmentDelimiter')
            self.groupDelimiter = self.getSafeText('groupDelimiter')
            self.fieldDelimiter = self.getSafeText('fieldDelimiter')

    def getXML(self, version="3.12.0"):
        xml = getXMLString(self.segmentDelimiter, "segmentDelimiter")
        xml += getXMLString(self.groupDelimiter, "groupDelimiter")
        xml += getXMLString(self.fieldDelimiter, "fieldDelimiter")
        return xml

class FhirSerializationProperties(SerializationProperties):
    def __init__(self, uXml=None):
        SerializationProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.fhir.shared.FhirSerializationProperties'

        self.serializationType = 'JSON'
        self.fhirVersion = 'R4'

        if uXml is not None:
            self.serializationType = self.getSafeText('serializationType')
            self.fhirVersion = self.getSafeText('fhirVersion')

    def getXML(self, version="3.12.0"):
        xml = getXMLString(self.serializationType, "serializationType")
        xml += getXMLString(self.fhirVersion, "fhirVersion")
        return xml


def serializationProps(c: str) -> Type:
    if c == "com.mirth.connect.plugins.datatypes.hl7v2.HL7v2SerializationProperties":
        return HL7v2SerializationProperties
    elif c == "com.mirth.connect.plugins.datatypes.hl7v3.HL7V3SerializationProperties":
        return HL7V3SerializationProperties
    elif c == "com.mirth.connect.plugins.datatypes.xml.XMLSerializationProperties":
        return XMLSerializationProperties
    elif c == "com.mirth.connect.plugins.datatypes.delimited.DelimitedSerializationProperties":
        return DelimitedSerializationProperties
    elif c == "com.mirth.connect.plugins.datatypes.edi.EDISerializationProperties":
        return EDISerializationProperties
    elif c == "com.mirth.connect.plugins.datatypes.ncpdp.NCPDPSerializationProperties":
        return NCPDPSerializationProperties
    elif c == "com.mirth.connect.plugins.datatypes.fhir.shared.FhirSerializationProperties":
        return FhirSerializationProperties
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
        xml = getXMLString(self.useStrictParser, "useStrictParser")
        xml += getXMLString(self.useStrictValidation, "useStrictValidation")
        xml += getXMLString(self.segmentDelimiter, "segmentDelimiter")
        return xml

class DelimitedDeserializationProperties(DeserializationProperties):
    def __init__(self, uXml=None):
        DeserializationProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.delimited.DelimitedDeserializationProperties'

        self.columnDelimiter = ','
        self.recordDelimiter = '\\n'
        self.quoteToken = '"'
        self.escapeWithDoubleQuote = 'true'
        self.quoteEscapeToken = '\\'

        if uXml is not None:
            self.columnDelimiter = self.getSafeText('columnDelimiter')
            self.recordDelimiter = self.getSafeText('recordDelimiter')
            self.quoteToken = self.getSafeText('quoteToken')
            self.escapeWithDoubleQuote = self.getSafeText('escapeWithDoubleQuote')
            self.quoteEscapeToken = self.getSafeText('quoteEscapeToken')

    def getXML(self, version="3.12.0"):
        xml = getXMLString(self.columnDelimiter, "columnDelimiter")
        xml += getXMLString(self.recordDelimiter, "recordDelimiter")
        xml += getXMLString(escape(self.quoteToken), "quoteToken")
        xml += getXMLString(self.escapeWithDoubleQuote, "escapeWithDoubleQuote")
        xml += getXMLString(self.quoteEscapeToken, "quoteEscapeToken")
        return xml

class NCPDPDeserializationProperties(DeserializationProperties):
    def __init__(self, uXml=None):
        DeserializationProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.ncpdp.NCPDPDeserializationProperties'

        self.segmentDelimiter = '0x1E'
        self.groupDelimiter = '0x1D'
        self.fieldDelimiter = '0x1C'
        self.useStrictValidation = 'false'

        if uXml is not None:
            self.segmentDelimiter = self.getSafeText('segmentDelimiter')
            self.groupDelimiter = self.getSafeText('groupDelimiter')
            self.fieldDelimiter = self.getSafeText('fieldDelimiter')
            self.useStrictValidation = self.getSafeText('useStrictValidation')

    def getXML(self, version="3.12.0"):
        xml = getXMLString(self.segmentDelimiter, "segmentDelimiter")
        xml += getXMLString(self.groupDelimiter, "groupDelimiter")
        xml += getXMLString(self.fieldDelimiter, "fieldDelimiter")
        xml += getXMLString(self.useStrictValidation, "useStrictValidation")
        return xml

class FhirDeserializationProperties(DeserializationProperties):
    def __init__(self, uXml=None):
        DeserializationProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.fhir.shared.FhirDeserializationProperties'

        self.serializationType = 'JSON'

        if uXml is not None:
            self.serializationType = self.getSafeText('serializationType')

    def getXML(self, version="3.12.0"):
        xml = getXMLString(self.serializationType, "serializationType")
        return xml
    

def deserializationProps(c: str) -> Type:
    if c == "com.mirth.connect.plugins.datatypes.hl7v2.HL7v2DeserializationProperties":
        return HL7v2DeserializationProperties
    elif c == "com.mirth.connect.plugins.datatypes.delimited.DelimitedDeserializationProperties":
        return DelimitedDeserializationProperties
    elif c == "com.mirth.connect.plugins.datatypes.ncpdp.NCPDPDeserializationProperties":
        return NCPDPDeserializationProperties
    elif c == "com.mirth.connect.plugins.datatypes.fhir.shared.FhirDeserializationProperties":
        return FhirDeserializationProperties
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
        xml = getXMLString(self.splitType, "splitType")
        xml += getXMLString(self.batchScript, "batchScript")
        return xml
    
class HL7V3BatchProperties(BatchProperties):
    def __init__(self, uXml=None):
        BatchProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.hl7v3.HL7V3BatchProperties'

        self.splitType = 'JavaScript'
        self.batchScript = ''

        if uXml is not None:
            self.splitType = self.getSafeText('splitType')
            self.batchScript = self.getSafeText('batchScript')

    def getXML(self, version="3.12.0"):
        xml = getXMLString(self.splitType, "splitType")
        xml += getXMLString(self.batchScript, "batchScript")
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
        xml = getXMLString(self.splitType, "splitType")
        xml += getXMLString(self.elementName, "elementName")
        xml += getXMLString(self.level, "level")
        xml += getXMLString(self.query, "query")
        xml += getXMLString(self.batchScript, "batchScript")

        return xml
    
class RawBatchProperties(BatchProperties):
    def __init__(self, uXml=None):
        BatchProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.raw.RawBatchProperties'

        self.splitType = 'JavaScript'
        self.batchScript = ''

        if uXml is not None:
            self.splitType = self.getSafeText('splitType')
            self.batchScript = self.getSafeText('batchScript')

    def getXML(self, version="3.12.0"):
        xml = getXMLString(self.splitType, "splitType")
        xml += getXMLString(self.batchScript, "batchScript")

        return xml
    
class DelimitedBatchProperties(BatchProperties):
    def __init__(self, uXml=None):
        BatchProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.delimited.DelimitedBatchProperties'

        self.splitType = 'JavaScript'
        self.batchSkipRecords = '0'
        self.batchMessageDelimiter = ''
        self.batchMessageDelimiterIncluded = 'false'
        self.batchGroupingColumn = ''
        self.batchScript = ''

        if uXml is not None:
            self.splitType = self.getSafeText('splitType')
            self.batchSkipRecords = self.getSafeText('batchSkipRecords')
            self.batchMessageDelimiter = self.getSafeText('batchMessageDelimiter')
            self.batchMessageDelimiterIncluded = self.getSafeText('batchMessageDelimiterIncluded')
            self.batchGroupingColumn = self.getSafeText('batchGroupingColumn')
            self.batchScript = self.getSafeText('batchScript')

    def getXML(self, version="3.12.0"):
        xml = getXMLString(self.splitType, "splitType")
        xml += getXMLString(self.batchSkipRecords, "batchSkipRecords")
        xml += getXMLString(self.batchMessageDelimiter, "batchMessageDelimiter")
        xml += getXMLString(self.batchMessageDelimiterIncluded, "batchMessageDelimiterIncluded")
        xml += getXMLString(self.batchGroupingColumn, "batchGroupingColumn")
        xml += getXMLString(self.batchScript, "batchScript")

        return xml

class EDIBatchProperties(BatchProperties):
    def __init__(self, uXml=None):
        BatchProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.edi.EDIBatchProperties'

        self.splitType = 'JavaScript'
        self.batchScript = ''

        if uXml is not None:
            self.splitType = self.getSafeText('splitType')
            self.batchScript = self.getSafeText('batchScript')

    def getXML(self, version="3.12.0"):
        xml = getXMLString(self.splitType, "splitType")
        xml += getXMLString(self.batchScript, "batchScript")

        return xml

class JSONBatchProperties(BatchProperties):
    def __init__(self, uXml=None):
        BatchProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.json.JSONBatchProperties'

        self.splitType = 'JavaScript'
        self.batchScript = ''

        if uXml is not None:
            self.splitType = self.getSafeText('splitType')
            self.batchScript = self.getSafeText('batchScript')

    def getXML(self, version="3.12.0"):
        xml = getXMLString(self.splitType, "splitType")
        xml += getXMLString(self.batchScript, "batchScript")

        return xml

class NCPDPBatchProperties(BatchProperties):
    def __init__(self, uXml=None):
        BatchProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.ncpdp.NCPDPBatchProperties'

        self.splitType = 'JavaScript'
        self.batchScript = ''

        if uXml is not None:
            self.splitType = self.getSafeText('splitType')
            self.batchScript = self.getSafeText('batchScript')

    def getXML(self, version="3.12.0"):
        xml = getXMLString(self.splitType, "splitType")
        xml += getXMLString(self.batchScript, "batchScript")

        return xml

class FhirBatchProperties(BatchProperties):
    def __init__(self, uXml=None):
        BatchProperties.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.datatypes.fhir.shared.FhirBatchProperties'

        self.splitType = 'JavaScript'
        self.batchScript = ''

        if uXml is not None:
            self.splitType = self.getSafeText('splitType')
            self.batchScript = self.getSafeText('batchScript')

    def getXML(self, version="3.12.0"):
        xml = getXMLString(self.splitType, "splitType")
        xml += getXMLString(escape(self.batchScript), "batchScript")

        return xml

def batchProps(c: str) -> Type:
    if c == "com.mirth.connect.plugins.datatypes.hl7v2.HL7v2BatchProperties":
        return HL7v2BatchProperties
    elif c == "com.mirth.connect.plugins.datatypes.hl7v3.HL7V3BatchProperties":
        return HL7V3BatchProperties
    elif c == "com.mirth.connect.plugins.datatypes.xml.XMLBatchProperties":
        return XMLBatchProperties
    elif c == "com.mirth.connect.plugins.datatypes.raw.RawBatchProperties":
        return RawBatchProperties
    elif c == "com.mirth.connect.plugins.datatypes.delimited.DelimitedBatchProperties":
        return DelimitedBatchProperties
    elif c == "com.mirth.connect.plugins.datatypes.edi.EDIBatchProperties":
        return EDIBatchProperties
    elif c == "com.mirth.connect.plugins.datatypes.json.JSONBatchProperties":
        return JSONBatchProperties
    elif c == "com.mirth.connect.plugins.datatypes.ncpdp.NCPDPBatchProperties":
        return NCPDPBatchProperties
    elif c == "com.mirth.connect.plugins.datatypes.fhir.shared.FhirBatchProperties":
        return FhirBatchProperties
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
        xml = getXMLString(self.segmentDelimiter, "segmentDelimiter")
        xml += getXMLString(self.successfulACKCode, "successfulACKCode")
        xml += getXMLString(self.successfulACKMessage, "successfulACKMessage")
        xml += getXMLString(self.errorACKCode, "errorACKCode")
        xml += getXMLString(self.errorACKMessage, "errorACKMessage")
        xml += getXMLString(self.rejectedACKCode, "rejectedACKCode")
        xml += getXMLString(self.rejectedACKMessage, "rejectedACKMessage")
        xml += getXMLString(self.msh15ACKAccept, "msh15ACKAccept")
        xml += getXMLString(self.dateFormat, "dateFormat")

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
        xml = getXMLString(self.successfulACKCode, "successfulACKCode")
        xml += getXMLString(self.errorACKCode, "errorACKCode")
        xml += getXMLString(self.rejectedACKCode, "rejectedACKCode")
        xml += getXMLString(self.validateMessageControlId, "validateMessageControlId")
        xml += getXMLString(self.originalMessageControlId, "originalMessageControlId")
        xml += getXMLString(self.originalIdMapVariable, "originalIdMapVariable")

        return xml

def validProps(c: str) -> Type:
    if c == "com.mirth.connect.plugins.datatypes.hl7v2.HL7v2ResponseValidationProperties":
        return HL7v2ResponseValidationProperties
    else:
        return ResponseValidationProperties

#endregion