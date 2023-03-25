from typing import Type
from xml.etree import ElementTree

from .datatypes import HL7v2DataTypeProperties, datatypeProps
from .utilities import getXMLString
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
            for e in self.elements:
                elements += e.getXML(version)
            elements = "</elements>"
        
        xml = f'''{elements}
                {ElementTree.tostring(self.inboundTemplate, method='html',).decode() if self.inboundTemplate is not None else ''}
                {getXMLString(self.inboundDataType, "inboundDataType")}
                {getXMLString(self.outboundDataType, "outboundDataType")}
                <inboundProperties class="{self.inboundProperties.className}" version="{version}">
                    {self.inboundProperties.getXML(version)}
                </inboundProperties>
                <outboundProperties class="{self.outboundProperties.className}" version="{version}">
                    {self.outboundProperties.getXML(version)}
                </outboundProperties>
                {ElementTree.tostring(self.outboundTemplate, method='html',).decode() if self.outboundTemplate is not None else ''}'''
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
        
        self.name = self.getSafeText('name')
        self.sequenceNumber = self.getSafeText('sequenceNumber')
        self.enabled = self.getSafeText('enabled')

class DestinationSetFilterStep(TransformerStep):
    def __init__(self, uXml=None):
        TransformerStep.__init__(self, uXml)

        self.behavior = self.getSafeText('behavior')
        self.metaDataIds = self.getSafeText('metaDataIds')
        self.field = self.getSafeText('field')
        self.condition = self.getSafeText('condition')
        self.values = Values(self.root.find('values'))

class Values(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

        self.values = []

        for e in self.root.findall('./string'):
            self.values.append(e.text)

class ExternalScriptStep(TransformerStep):
    def __init__(self, uXml=None):
        TransformerStep.__init__(self, uXml)

        self.scriptPath = self.getSafeText('scriptPath')

class JavaScriptStep(TransformerStep):
    def __init__(self, uXml=None):
        TransformerStep.__init__(self, uXml)

        self.script = self.getSafeText('script')

class MapperStep(TransformerStep):
    def __init__(self, uXml=None):
        TransformerStep.__init__(self, uXml)

        self.variable = self.getSafeText('variable')
        self.mapping = self.getSafeText('mapping')
        self.defaultValue = self.getSafeText('defaultValue')
        self.scope = self.getSafeText('scope')
        self.replacements = []

        for e in self.root.findall('./replacements/org.apache.commons.lang3.tuple.ImmutablePair'):
            self.replacements.append((e.find('left').text, e.find('right').text))

class MessageBuilderStep(TransformerStep):
    def __init__(self, uXml=None):
        TransformerStep.__init__(self, uXml)

        self.messageSegment = self.getSafeText('messageSegment')
        self.mapping = self.getSafeText('mapping')
        self.defaultValue = self.getSafeText('defaultValue')
        self.replacements = []

        for e in self.root.findall('./replacements/org.apache.commons.lang3.tuple.ImmutablePair'):
            self.replacements.append((e.find('left').text, e.find('right').text))

class XsltStep(TransformerStep):
    def __init__(self, uXml=None):
        TransformerStep.__init__(self, uXml)

        self.sourceXml = self.getSafeText('sourceXml')
        self.resultVariable = self.getSafeText('resultVariable')
        self.template = self.getSafeText('template')
        self.useCustomFactory = self.getSafeText('useCustomFactory')
        self.customFactory = self.getSafeText('customFactory')

class IteratorStep(TransformerStep):
    def __init__(self, uXml=None):
        TransformerStep.__init__(self, uXml)

        self.properties = IteratorStepProperties(self.root.find('properties'))

class IteratorStepProperties(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

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


        