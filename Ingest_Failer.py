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

from api_requests import ApiRequests
from json_methods import json_methods




# Is the SIP stuck or has it actually failed with callback error message?




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


class SIP(object):

    def __init__(self, SIP_ID):
        self.sip_id = SIP_ID
        self.sip_json = ApiRequests.get_JSON(self.sip_id)
        self.json_methods = json_methods(self.sip_json)
        self.SubmissionInProgress = self.json_methods.SubmissionInProgress
        self.review_stepstate_id =self.json_methods
        self.user_id = self.sip_json['UserId']
        self.sami_call_number = self.sip_json['SamiCallNumber']
        self.status = self.sip_json['Status']


    

class User_details(object):

    # get user details
    pass

# my_SIP = SIP(486476)
# print(my_SIP.SubmissionInProgress)
# print()