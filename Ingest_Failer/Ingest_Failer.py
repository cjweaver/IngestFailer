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
from json_methods import json_methods


class SIP(object):

    def __init__(self, SIP_ID):
        self.sip_id = SIP_ID
        self.sip_json = api_requests.get_JSON(self.sip_id)
        self.json_methods = json_methods(self.sip_json)
        self.SubmissionInProgress = self.json_methods.SubmissionInProgress
        self.review_stepstate_id =self.json_methods.get_review_stepstate_id()
        self.user_id = self.sip_json['UserId']
        self.sami_call_number = self.sip_json['SamiCallNumber']
        self.status = self.sip_json['Status']
