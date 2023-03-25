from .utilities import getXMLString
from .linkedHashMap import Entry, LinkedHashMap
from .mirthElement import MirthElement


class ChannelProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)

        self.clearGlobalChannelMap = 'true'
        self.messageStorageMode = 'DEVELOPMENT'
        self.encryptData = 'false'
        self.removeContentOnCompletion = 'false'
        self.removeOnlyFilteredOnCompletion = 'false'
        self.removeAttachmentsOnCompletion = 'false'
        self.initialState = 'STARTED'
        self.storeAttachments = 'true'
        self.attachmentProperties = AttachmentProperties()
        self.resourceIds = LinkedHashMap()

        entry = Entry()
        entry.string.append('Default Resource')
        entry.string.append('[Default Resource]')

        self.resourceIds.entry.append(entry)

        self.metaDataColumns = []

        if uXml is not None:
            self.clearGlobalChannelMap = self.getSafeText('clearGlobalChannelMap')
            self.messageStorageMode = self.getSafeText('messageStorageMode')
            self.encryptData = self.getSafeText('encryptData')
            self.removeContentOnCompletion = self.getSafeText('removeContentOnCompletion')
            self.removeOnlyFilteredOnCompletion = self.getSafeText('removeOnlyFilteredOnCompletion')
            self.removeAttachmentsOnCompletion = self.getSafeText('removeAttachmentsOnCompletion')
            self.initialState = self.getSafeText('initialState')
            self.storeAttachments = self.getSafeText('storeAttachments')
            self.attachmentProperties = AttachmentProperties(self.root.find('attachmentProperties'))
            self.resourceIds = LinkedHashMap(self.root.find('resourceIds'))
            
            for m in self.root.findall('./metaDataColumns/metaDataColumn'):
                self.metaDataColumns.append(MetaDataColumn(m))

    def getXML(self, version="3.12.0"):
        mdXml = "<metaDataColumns/>"

        if len(self.metaDataColumns) > 0:
            mdXml = '<metaDataColumns>'
            for m in self.metaDataColumns:
                mdXml += '<metaDataColumn>'
                mdXml += m.getXML(version)
                mdXml += '</metaDataColumn>'
            mdXml += '</metaDataColumns>'

        return f'''{getXMLString(self.clearGlobalChannelMap, "clearGlobalChannelMap")}
                    {getXMLString(self.messageStorageMode, "messageStorageMode")}
                    {getXMLString(self.encryptData, "encryptData")}
                    {getXMLString(self.removeContentOnCompletion, "removeContentOnCompletion")}
                    {getXMLString(self.removeOnlyFilteredOnCompletion, "removeOnlyFilteredOnCompletion")}
                    {getXMLString(self.removeAttachmentsOnCompletion, "removeAttachmentsOnCompletion")}
                    {getXMLString(self.initialState, "initialState")}
                    {getXMLString(self.storeAttachments, "storeAttachments")}
                    {mdXml}
                    <attachmentProperties version="{version}">
                        {self.attachmentProperties.getXML(version)}
                    </attachmentProperties>
                    <resourceIds class="linked-hash-map">
                        {self.resourceIds.getXML(version)}
                    </resourceIds>'''

class MetaDataColumn(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)
        self.name = ''
        self.type = 'STRING'
        self.mappingName = ''

        if uXml is not None:
            self.name = self.getSafeText('name')
            self.type = self.getSafeText('type')
            self.mappingName = self.getSafeText('mappingName')
    
    def getXML(self, version="3.12.0"):
        return f'''{getXMLString(self.name, "name")}
                    {getXMLString(self.type, "type")}
                    {getXMLString(self.mappingName, "mappingName")}'''
    

class AttachmentProperties(MirthElement):
    def __init__(self, uXml = None):
        MirthElement.__init__(self, uXml)

        self.type = 'None'
        self.properties = None

        if uXml is not None:
            self.type = self.getSafeText('type')
            self.properties = None #TODO: build out different properties and change getXML

    def getXML(self, version="3.12.0"):
        return f'''{getXMLString(self.type, "type")}
                    <properties/>'''