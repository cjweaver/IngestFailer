import ingestfailer.api_requests
from ingestfailer.json_methods import JsonMethods


class Sip():
    """Conveient class to represent the pSIP

    The majority of the methods in this class are from JsonMethods
    (it has no pulic methods of its own) with a few other attributes derived
    directly from the pSIp JSON
    """

    def __init__(self, SIP_ID):
        """
        Parameters
        ----------
        SIP_ID: str
            The pSIP ID number
        """
        self.sip_id = SIP_ID
        self.sip_json = api_requests.get_JSON(self.sip_id)
        self.json_methods = JsonMethods(self.sip_json)
        self.SubmissionInProgress = self.json_methods.SubmissionInProgress
        self.review_stepstate_id = self.json_methods.get_review_stepstate_id()
        self.user_id = self.sip_json['UserId']
        self.sami_call_number = self.sip_json['SamiCallNumber']
        self.status = self.sip_json['Status']
