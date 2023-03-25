from .mirthDate import MirthDate
from .linkedHashMap import LinkedHashMap, LinkedHashMapMessage
from .mirthElement import MirthElement

class Messages(MirthElement):
    def __init__(self, listXML):
        MirthElement.__init__(self, listXML)

        messages = self.root
        self.messages = []

        for c in messages.findall('./message'):
            self.messages.append(Message(c))

class Message(MirthElement):
    def __init__(self, uXml):
        MirthElement.__init__(self, uXml)

        self.serverId = self.getSafeText('serverId')
        self.channelId = self.getSafeText('channelId')
        self.receivedDate = MirthDate(self.root.find('receivedDate'))
        self.processed = self.getSafeText('processed')
        self.connectorMessages = LinkedHashMapMessage(self.root.find('connectorMessages'))
        self.messageId = self.getSafeText('messageId')
        # self.int = self.getSafeText('int')
        # self.status = self.getSafeText('status')
        # self.sourceMapContent = self.getSafeText('sourceMapContent')
        # 
        # self.connectorMapContent = self.getSafeText('connectorMapContent')
        # self.channelMapContent = self.getSafeText('channelMapContent')
        # self.responseMapContent = self.getSafeText('responseMapContent')
        # self.metaDataMap = self.getSafeText('metaDataMap')
        # self.processingErrorContent = self.getSafeText('processingErrorContent')
        # self.postProcessorErrorContent = self.getSafeText('postProcessorErrorContent')
        # self.responseErrorContent = self.getSafeText('responseErrorContent')
        # 
        
        


# <list>
#   <message>
#     <serverId>5bddc01d-8c3c-4e54-addf-e4bca19ebf80</serverId>
#     <channelId>817981d9-ba88-4524-8f44-5a432a0adb4b</channelId>
#     <receivedDate>
#       <time>1643771776323</time>
#       <timezone>America/Denver</timezone>
#     </receivedDate>
#     <processed>true</processed>
#     <connectorMessages class="linked-hash-map">
#       <entry>
#         <int>1</int>
#         <connectorMessage>
#           <messageId>1</messageId>
#           <metaDataId>0</metaDataId>
#           <channelId>f760d41f-7071-4af8-a730-0084230e3cc3</channelId>
#           <channelName>Channel 1</channelName>
#           <serverId>a5df0a7a-5a6e-4459-b518-0517c8795bb3</serverId>
#           <receivedDate>
#             <time>1643771776323</time>
#             <timezone>America/Denver</timezone>
#           </receivedDate>
#           <status>SENT</status>
#           <sourceMapContent>
#             <encrypted>false</encrypted>
#             <content class="map"/>
#           </sourceMapContent>
#           <connectorMapContent>
#             <encrypted>false</encrypted>
#             <content class="map"/>
#           </connectorMapContent>
#           <channelMapContent>
#             <encrypted>false</encrypted>
#             <content class="map"/>
#           </channelMapContent>
#           <responseMapContent>
#             <encrypted>false</encrypted>
#             <content class="map"/>
#           </responseMapContent>
#           <metaDataMap/>
#           <processingErrorContent>
#             <encrypted>false</encrypted>
#           </processingErrorContent>
#           <postProcessorErrorContent>
#             <encrypted>false</encrypted>
#           </postProcessorErrorContent>
#           <responseErrorContent>
#             <encrypted>false</encrypted>
#           </responseErrorContent>
#           <errorCode>0</errorCode>
#           <sendAttempts>0</sendAttempts>
#           <chainId>0</chainId>
#           <orderId>0</orderId>
#         </connectorMessage>
#       </entry>
#     </connectorMessages>
#   </message>
# </list>