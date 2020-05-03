# Ingest Failer
# Simulates a submission call back failure from the DLS for stuck SIPs
#
# The SIP Tool submits SIPs to be ingested by the AVRC ingest stream. 
# Once a SIP has been processed, and submission has either succeeded 
# or failed, a callback with that result is sent to the SIP Tool.
# In the vast majority of cases, the AVRC ingest stream and 
# the SIP Tool communicate reliably. When it does not, 
# the SIP will need to be force-failed using the AVSIP API. 
#
# christopher.weaver@bl.uk 21/04/2020

import api_requests
import sip_json



# class Gui(object):
    
#     def enter_SIP_ID(self):
#         pass

#     def enter_failure_msg(self):
#         pass


# class ApiRequests(object):

#     def __init__(self, sip_tool_addr):
#         self.sip_tool_addr = sip_tool_addr 
    
#     def GetJSON(self, SIP_ID):
        
#         pass

#     def PostCallBack(self):
#         pass

#     def SucessTest(self):
#         pass


# class sipJSON(object):

#     def __init__(self, pSIP_JSON):
# 		self.CallbackUri = pSIP_JSON['Submissions'][0]['CallbackUri']
# 		self.SamiCallNumber = pSIP_JSON['SamiCallNumber']
	
#      def get_submission_node(self):
#          pass

#      def get_first_submission_node(self):
#          pass


class SIP(sip_json.sipJSON):

    def __init__(self, SIP_ID):
        self.sip_id = SIP_ID
        self.ApiRequests = api_requests.ApiRequests()
        self.sip_json = self.ApiRequests.get_JSON(self.sip_id)
        super().__init__(self.SIP_JSON)
        # self.sipJSON = sip_json.sipJSON(self.SIP_JSON)
        # self.sipJSON = self.sipJSON(self.SIP_JSON)

    # def get_first_submission_node(self):
    #     # Use method from SIP_JSON object
    

    # def get_CallBackResult(self):
    #     pass

    # def get_ExternalID(self):
	# 	self.ExternalIdentifier = self.SIP_JSON['Submissions'][0]['ExternalIdentifier']

    # def get_CallBackURI(self):
    #     pass

class User_details(object):

    # get user details
    pass

my_SIP = SIP(40513)
print()