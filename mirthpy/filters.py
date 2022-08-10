from typing import Type
from .mirthElement import MirthElement


class Filter(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.elements = []
        
        if len(self.root.find('./elements').findall('./*')) > 0:
            for e in self.root.find('./elements').findall('./*'):
                prop = rules(e.tag)
        
                self.elements.append(prop(e))

class FilterRule(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)
        
        self.name = self.getSafeText('name')
        self.sequenceNumber = self.getSafeText('sequenceNumber')
        self.enabled = self.getSafeText('enabled')
        self.operator = self.getSafeText('operator')

class RuleBuilderRule(FilterRule):
    def __init__(self, uXml):
        FilterRule.__init__(self, uXml)

        self.field = self.getSafeText('field')
        self.condition = self.getSafeText('condition')
        self.values = []

        for e in self.root.findall('./values/string'):
            self.values.append(e.text)

class ExternalScriptRule(FilterRule):
    def __init__(self, uXml):
        FilterRule.__init__(self, uXml)

        self.scriptPath = self.getSafeText('scriptPath')

class JavaScriptRule(FilterRule):
    def __init__(self, uXml):
        FilterRule.__init__(self, uXml)

        self.script = self.getSafeText('script')

class IteratorRule(FilterRule):
    def __init__(self, uXml):
        FilterRule.__init__(self, uXml)

        self.properties = IteratorRuleProperties(self.root.find('properties'))

class IteratorRuleProperties(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.target = self.getSafeText('target')
        self.indexVariable = self.getSafeText('indexVariable')
        self.prefixSubstitutions = []

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


        
