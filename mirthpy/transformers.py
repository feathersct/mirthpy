from typing import Type

from .datatypes import HL7v2DataTypeProperties, datatypeProps
from .utilities import escape, getXMLString
from .mirthElement import MirthElement

class Transformer(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)
        self.elements = []
        self.inboundTemplate = None
        self.outboundTemplate = None
        self.inboundProperties = HL7v2DataTypeProperties()
        self.inboundDataType = self.inboundProperties.dataType
        self.outboundProperties = HL7v2DataTypeProperties()
        self.outboundDataType = self.outboundProperties.dataType
        
        if uXml is not None:
            if len(self.root.find('./elements').findall('./*')) > 0:
                for e in self.root.find('./elements').findall('./*'):
                    prop = steps(e.tag)
            
                    self.elements.append(prop(e))

            inProp = datatypeProps(self.root.find('inboundProperties').attrib['class'])
            outProp = datatypeProps(self.root.find('outboundProperties').attrib['class'])

            self.inboundDataType = self.getSafeText('inboundDataType')
            self.outboundDataType = self.getSafeText('outboundDataType')
            self.inboundProperties = inProp(self.root.find('inboundProperties')) 
            self.outboundProperties = outProp(self.root.find('outboundProperties'))
            self.inboundTemplate = self.root.find('inboundTemplate')    #TODO: IMplement
            self.outboundTemplate = self.root.find('outboundTemplate')  #TODO: IMplement

    def getXML(self, version = '3.12.0'):
        if len(self.elements) == 0:
            elements = "<elements/>"
        else:
            elements = "<elements>"
            i = 0
            for e in self.elements:
                e.sequenceNumber = i
                elements += '<{} version="{}">'.format(e.className, version)
                elements += e.getXML(version)
                elements += '</{}>'.format(e.className)
                i = i+1
            elements += "</elements>"

        
        xml = elements
        xml += getXMLString(self.inboundTemplate, "inboundTemplate")
        xml += getXMLString(self.outboundTemplate,'outboundTemplate', includeIfEmpty=False)
        xml += getXMLString(self.inboundDataType, "inboundDataType")
        xml += getXMLString(self.outboundDataType, "outboundDataType", includeIfEmpty=False)
        xml += '<inboundProperties class="{}" version="{}">'.format(self.inboundProperties.className, version)
        xml += self.inboundProperties.getXML(version)
        xml += '</inboundProperties>'
        xml += '<outboundProperties class="{}" version="{}">'.format(self.outboundProperties.className, version)
        xml += self.outboundProperties.getXML(version)
        xml += '</outboundProperties>'
        return xml

class Elements(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

        self.elements = []
        
        if len(self.root.findall('./*')) > 0:
            for e in self.root.findall('./*'):
                prop = steps(e.tag)
                
                self.elements.append(prop(e))

class TransformerStep(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)
        self.name = ''
        self.sequenceNumber = '0'
        self.enabled = 'true'
    
        if uXml is not None:
            self.name = self.getSafeText('name')
            self.sequenceNumber = self.getSafeText('sequenceNumber')
            self.enabled = self.getSafeText('enabled')

class DestinationSetFilterStep(TransformerStep):
    def __init__(self, uXml=None):
        TransformerStep.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.destinationsetfilter.DestinationSetFilterStep'
        self.behavior = 'REMOVE'
        self.metaDataIds = MetaDataIds()
        self.field = ''
        self.condition = 'EXISTS'
        self.values = Values()

        if uXml is not None:
            self.behavior = self.getSafeText('behavior')
            self.metaDataIds = MetaDataIds(self.root.find('metaDataIds'))
            self.field = self.getSafeText('field')
            self.condition = self.getSafeText('condition')
            self.values = Values(self.root.find('values'))
    
    def getXML(self, version="3.12.0") -> str:
        xml = ""
        xml += getXMLString(escape(self.name), 'name', includeIfEmpty=False)
        xml += getXMLString(self.sequenceNumber, 'sequenceNumber')
        xml += getXMLString(self.enabled, 'enabled')
        xml += getXMLString(self.behavior, "behavior")
        xml += self.metaDataIds.getXML(version)
        xml += getXMLString(self.field, "field")
        xml += getXMLString(self.condition, "condition")
        xml += self.values.getXML(version)
        return xml

class MetaDataIds(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)
        self.ints = []

        if uXml is not None:
            for e in self.root.findall('./int'):
                self.ints.append(e.text)
    
    def getXML(self, version="3.12.0"):
        xml = "<metaDataIds>"
        for v in self.ints:
            xml += "<int>{}</int>".format(v)
        xml += "</metaDataIds>"
        return xml


class Values(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

        self.values = []

        for e in self.root.findall('./string'):
            self.values.append(e.text)

    def getXML(self, version="3.12.0"):
        xml = "<values>"
        for v in self.values:
            xml += "<string>{}</string>".format(escape(v))
        xml += "</values>"
        return xml

class ExternalScriptStep(TransformerStep):
    def __init__(self, uXml=None):
        TransformerStep.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.scriptfilestep.ExternalScriptStep'

        self.scriptPath = ''

        if uXml is not None:
            self.scriptPath = self.getSafeText('scriptPath')

    def getXML(self, version="3.12.0") -> str:
        xml = ""
        xml += getXMLString(escape(self.name), 'name', includeIfEmpty=False)
        xml += getXMLString(self.sequenceNumber, 'sequenceNumber')
        xml += getXMLString(self.enabled, 'enabled')
        xml += getXMLString(escape(self.scriptPath), "scriptPath")
        return xml

class JavaScriptStep(TransformerStep):
    def __init__(self, uXml=None):
        TransformerStep.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.javascriptstep.JavaScriptStep'
        self.script = ''

        if uXml is not None:
            self.script = self.getSafeText('script')

    def getXML(self, version="3.12.0") -> str:
        xml = ""
        xml += getXMLString(escape(self.name), 'name', includeIfEmpty=False)
        xml += getXMLString(self.sequenceNumber, 'sequenceNumber')
        xml += getXMLString(self.enabled, 'enabled')
        xml += getXMLString(escape(self.script), "script")
        return xml

class MapperStep(TransformerStep):
    def __init__(self, uXml=None):
        TransformerStep.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.mapper.MapperStep'
        self.variable = ''
        self.mapping = ''
        self.defaultValue = ''
        self.scope = 'CHANNEL'
        self.replacements = []

        if uXml is not None:
            self.variable = self.getSafeText('variable')
            self.mapping = self.getSafeText('mapping')
            self.defaultValue = self.getSafeText('defaultValue')
            self.scope = self.getSafeText('scope')
            self.replacements = []

            for e in self.root.findall('./replacements/org.apache.commons.lang3.tuple.ImmutablePair'):
                self.replacements.append((e.find('left').text, e.find('right').text))

    def getXML(self, version="3.12.0") -> str:
        if len(self.replacements) > 0:
            replacementXML = "<replacements>"
            for r in self.replacements:
                replacementXML += "<org.apache.commons.lang3.tuple.ImmutablePair>"
                replacementXML += '<left class="string">{}</left>'.format(r[0])
                replacementXML += '<right class="string">{}</right>'.format(r[1])
                replacementXML += "</org.apache.commons.lang3.tuple.ImmutablePair>"
            replacementXML += "</replacements>"
            
        else:
            replacementXML = "<replacements/>"

        xml = ""
        xml += getXMLString(self.variable, 'name')
        xml += getXMLString(self.sequenceNumber, 'sequenceNumber')
        xml += getXMLString(self.enabled, 'enabled')
        xml += getXMLString(self.variable, 'variable')
        xml += getXMLString(self.mapping, 'mapping')
        xml += getXMLString(self.defaultValue, 'defaultValue')
        xml += replacementXML
        xml += getXMLString(self.scope, 'scope')
        return xml

class MessageBuilderStep(TransformerStep):
    def __init__(self, uXml=None):
        TransformerStep.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.messagebuilder.MessageBuilderStep'

        self.messageSegment = ''
        self.mapping = ''
        self.defaultValue = ''
        self.replacements = []

        if uXml is not None:
            self.messageSegment = self.getSafeText('messageSegment')
            self.mapping = self.getSafeText('mapping')
            self.defaultValue = self.getSafeText('defaultValue')
            self.replacements = []

            for e in self.root.findall('./replacements/org.apache.commons.lang3.tuple.ImmutablePair'):
                self.replacements.append((e.find('left').text, e.find('right').text))
    
    def getXML(self, version="3.12.0") -> str:
        if len(self.replacements) > 0:
            replacementXML = "<replacements>"
            for r in self.replacements:
                replacementXML += "<org.apache.commons.lang3.tuple.ImmutablePair>"
                replacementXML += '<left class="string">{}</left>'.format(r[0])
                replacementXML += '<right class="string">{}</right>'.format(r[1])
                replacementXML += "</org.apache.commons.lang3.tuple.ImmutablePair>"
            replacementXML += "</replacements>"
            
        else:
            replacementXML = "<replacements/>"

        xml = ""
        xml += getXMLString(self.name, 'name')
        xml += getXMLString(self.sequenceNumber, 'sequenceNumber')
        xml += getXMLString(self.enabled, 'enabled')
        xml += getXMLString(self.messageSegment, 'messageSegment')
        xml += getXMLString(self.mapping, 'mapping')
        xml += getXMLString(self.defaultValue, 'defaultValue')
        xml += replacementXML
        return xml

class XsltStep(TransformerStep):
    def __init__(self, uXml=None):
        TransformerStep.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.xsltstep.XsltStep'

        self.sourceXml = ''
        self.resultVariable = ''
        self.template = ''
        self.useCustomFactory = ''
        self.customFactory = ''

        if uXml is not None:
            self.sourceXml = self.getSafeText('sourceXml')
            self.resultVariable = self.getSafeText('resultVariable')
            self.template = self.getSafeText('template')
            self.useCustomFactory = self.getSafeText('useCustomFactory')
            self.customFactory = self.getSafeText('customFactory')

class IteratorStep(TransformerStep):
    def __init__(self, uXml=None):
        TransformerStep.__init__(self, uXml)
        self.className = 'com.mirth.connect.model.IteratorStep'

        self.properties = IteratorStepProperties()

        if uXml is not None:
            self.properties = IteratorStepProperties(self.root.find('properties'))

class IteratorStepProperties(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

        self.target = ''
        self.indexVariable = ''
        self.prefixSubstitutions = []
        self.children = []

        if uXml is not None:
            self.target = self.getSafeText('target')
            self.indexVariable = self.getSafeText('indexVariable')
            self.prefixSubstitutions = []

            for e in self.root.findall('./prefixSubstitutions/string'):
                self.prefixSubstitutions.append(e.text)

            self.children = []
            
            if len(self.root.find('./children').findall('./*')) > 0:
                for e in self.root.find('./children').findall('./*'):
                    prop = steps(e.tag)
                    
                    self.children.append(prop(e))


def steps(c: str) -> Type:
    if c == "com.mirth.connect.plugins.destinationsetfilter.DestinationSetFilterStep":
        return DestinationSetFilterStep
    elif c == "com.mirth.connect.plugins.scriptfilestep.ExternalScriptStep":
        return ExternalScriptStep
    elif c == "com.mirth.connect.plugins.javascriptstep.JavaScriptStep":
        return JavaScriptStep
    elif c == "com.mirth.connect.plugins.mapper.MapperStep":
        return MapperStep
    elif c == "com.mirth.connect.plugins.messagebuilder.MessageBuilderStep":
        return MessageBuilderStep
    elif c == "com.mirth.connect.plugins.xsltstep.XsltStep":
        return XsltStep
    elif c == "com.mirth.connect.model.IteratorStep":
        return IteratorStep
    else:
        return TransformerStep


        