# Ingest Failer
# Simulates a submission call back failure from the DLS for stuck SIPs
# christopher.weaver@bl.uk 21/04/2020

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


class sipJSON(object):

    def __init__(self, pSIP_JSON):
		self.CallbackUri = pSIP_JSON['Submissions'][0]['CallbackUri']
		self.SamiCallNumber = pSIP_JSON['SamiCallNumber']
	
     def get_submission_node(self):
         pass

     def get_first_submission_node(self):
         pass


class SIP(object):

    def __init__(self, SIP_ID):
        self.SIP_ID = SIP_ID
        self.SIP_JSON = ApiRequests.GetJSON(self.SIP_ID)

    def get_first_submission_node(self):
        # Use method from SIP_JSON object
    

    def get_CallBackResult(self):
        pass

    def get_ExternalID(self):
		self.ExternalIdentifier = self.SIP_JSON['Submissions'][0]['ExternalIdentifier']

    def get_CallBackURI(self):
        pass

class User_details(object):

    # get user details
    pass
