import json

class sipJSON(object):
    
    def __init__(self, pSIP_JSON):
        self.sami_call_number = pSIP_JSON['SamiCallNumber']
        self.submissions_node = pSIP_JSON['Submissions']
        # What happens if there is no Null result
        #  i.e the SIP is fine. Need a try/Except clause
        for node in self.submissions_node:
            if not node['CallbackRawResult']:
                self.stuck_submission = node
	
    def get_submissions_node(self):
        return self.submissions_node

    def get_stuck_submission(self):
        return self.stuck_submission

    # def get_CallBackResult(self):
    #     pass

    def get_ExternalID(self):
        self.ExternalIdentifier = self.stuck_submission['ExternalIdentifier']
        return self.ExternalIdentifier

    def get_CallBackURI(self):
        self.callback_Uri = self.stuck_submission['CallbackUri']
        return self.callback_Uri
            




# with open('C1274-70_C1274-72.json') as f:
#     my_json = sipJSON(json.load(f))
#     print(my_json.sami_call_number)
#     print(my_json.get_CallBackURI())
#     # print(my_json.get_stuck_submission())
#     print(my_json.get_ExternalID())

# # SIP.Submission[first listed (should be the most recent)].CallbackRawResult == null
# # SubmissionInProgress