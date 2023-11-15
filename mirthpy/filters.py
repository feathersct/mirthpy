from enum import Enum
from typing import Type

from .utilities import escape, getXMLString
from .mirthElement import MirthElement


class Filter(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

        self.elements = []
        
        if uXml is not None:
            if len(self.root.find('./elements').findall('./*')) > 0:
                for e in self.root.find('./elements').findall('./*'):
                    prop = rules(e.tag)
            
                    self.elements.append(prop(e))

    def getXML(self, version="3.12.0"):
        xml = '<elements/>'
        
        if len(self.elements) > 0:
            xml = '<elements>'
            i = 0
            for e in self.elements:
                e.sequenceNumber = i
                xml += '<{} version="{}">'.format(e.className, version)
                xml += e.getXML(version)
                xml += '</{}>'.format(e.className)
                i = i+1
            xml += '</elements>'

        return xml

class FilterRule(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)
        self.name = ''
        self.sequenceNumber = '' #get incremented for each element
        self.enabled = 'true'
        self.operator = ''#FilterOperator.AND.value #doesn't get included on the first element in the xml
        
        if uXml is not None:
            self.name = self.getSafeText('name')
            self.sequenceNumber = self.getSafeText('sequenceNumber')
            self.enabled = self.getSafeText('enabled')
            
            # the first rule doesn't have an operator
            if self.getSafeText('operator') is not None:
                self.operator = self.getSafeText('operator')

class RuleBuilderRule(FilterRule):
    def __init__(self, uXml=None):
        FilterRule.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.rulebuilder.RuleBuilderRule'
        self.values = []
        self.field = ''
        self.condition = FilterCondition.EXISTS.value

        if uXml is not None:
            self.field = self.getSafeText('field')
            self.condition = self.getSafeText('condition')

            for e in self.root.findall('./values/string'):
                self.values.append(e.text)

    def getXML(self, version="3.12.0"):
        name = 'Accept message if "{}" {}'.format(self.field, getConditionName(self.condition))
        if len(self.values) > 0:
            name += ' ' + " or ".join(self.values)

        valueXML = '<values/>'
        if len(self.values) > 0:
            valueXML = '<values>'
            for v in self.values:
                valueXML += "<string>{}</string>".format(escape(v))
            valueXML += '</values>'


        xml = ''
        xml += getXMLString(escape(name), 'name')
        xml += getXMLString(self.sequenceNumber, 'sequenceNumber')
        xml += getXMLString(self.enabled, 'enabled')
        xml += getXMLString(self.operator, 'operator', includeIfEmpty=False)
        xml += getXMLString(escape(self.field), 'field')
        xml += getXMLString(self.condition, 'condition')
        xml += valueXML

        return xml

class ExternalScriptRule(FilterRule):
    def __init__(self, uXml=None):
        FilterRule.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.scriptfilerule.ExternalScriptRule'
        self.scriptPath = ''

        if uXml is not None:
            self.scriptPath = self.getSafeText('scriptPath')

    def getXML(self, version="3.12.0"):
        xml = ""
        xml += getXMLString(self.sequenceNumber, 'sequenceNumber')
        xml += getXMLString(self.enabled, 'enabled')
        xml += getXMLString(self.operator, 'operator', includeIfEmpty=False)
        xml += getXMLString(self.scriptPath, "scriptPath")

        return xml
    
class JavaScriptRule(FilterRule):
    def __init__(self, uXml=None):
        FilterRule.__init__(self, uXml)
        self.className = 'com.mirth.connect.plugins.javascriptrule.JavaScriptRule'
        self.script = ''

        if uXml is not None:
            self.script = self.getSafeText('script')

    def getXML(self, version="3.12.0") -> str:
        xml = ""
        xml += getXMLString(self.name, 'name')
        xml += getXMLString(self.sequenceNumber, 'sequenceNumber')
        xml += getXMLString(self.enabled, 'enabled')
        xml += getXMLString(self.operator, 'operator', includeIfEmpty=False)
        xml += getXMLString(escape(self.script), "script")
        return xml

class IteratorRule(FilterRule):
    def __init__(self, uXml=None):
        FilterRule.__init__(self, uXml)
        self.className = 'com.mirth.connect.model.IteratorRule'

        self.properties = IteratorRuleProperties()

        if uXml is not None:
            self.properties = IteratorRuleProperties(self.root.find('properties'))

class IteratorRuleProperties(MirthElement):
    def __init__(self, uXml=None):
        MirthElement.__init__(self, uXml)

        self.target = ''
        self.indexVariable = ''
        self.prefixSubstitutions = []
        self.children = ''
        self.intersectIterations = ''
        self.breakEarly = ''

        if uXml is not None:
            self.target = self.getSafeText('target')
            self.indexVariable = self.getSafeText('indexVariable')

            for e in self.root.findall('./prefixSubstitutions/string'):
                self.prefixSubstitutions.append(e.text)

            self.children = self.getSafeText('children') 
            self.intersectIterations = self.getSafeText('intersectIterations')
            self.breakEarly = self.getSafeText('breakEarly')
        

def rules(c: str) -> Type:
    if c == "com.mirth.connect.plugins.rulebuilder.RuleBuilderRule":
        return RuleBuilderRule
    elif c == "com.mirth.connect.plugins.scriptfilerule.ExternalScriptRule":
        return ExternalScriptRule
    elif c == "com.mirth.connect.plugins.javascriptrule.JavaScriptRule":
        return JavaScriptRule
    elif c == "com.mirth.connect.model.IteratorRule":
        return IteratorRule
    else:
        return FilterRule


class FilterCondition(Enum):
    EXISTS = 'EXISTS'
    NOTEXISTS = 'NOT_EXIST'
    EQUALS = 'EQUALS'
    NOTEQUALS = 'NOT_EQUAL'
    CONTAINS = 'CONTAINS'
    NOTCONTAINS = 'NOT_CONTAIN'

class FilterOperator(Enum):
    AND = 'AND'
    OR = 'OR'

def getConditionName(condition):
    if condition == FilterCondition.EXISTS.value:
        return 'exists'
    elif condition == FilterCondition.NOTEXISTS.value:
        return 'does not exist'
    elif condition == FilterCondition.EQUALS.value:
        return 'equals'
    elif condition == FilterCondition.NOTEQUALS.value:
        return 'does not equal'
    elif condition == FilterCondition.CONTAINS.value:
        return 'contains'
    elif condition == FilterCondition.NOTCONTAINS.value:
        return 'does not contain'
    return ''