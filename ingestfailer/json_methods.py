class JsonMethods():
    """Extracts various details from the pSIPs JSON"

    The majority of the methods in this class act upon the first result
    in the 'Submissions' list that has a callbackRawResult of False
    """

    def __init__(self, pSIP_JSON):
        """
        Parameters
        ----------
        pSIP_JSON: dict
            The JSON representing the pSIP
        """
        self.submissions = pSIP_JSON['Submissions']
        self.StepStates = pSIP_JSON['StepStates']
        self.SubmissionInProgress = pSIP_JSON['SubmissionInProgress']
        for node in self.submissions:
            if not node['CallbackRawResult']:
                self.stuck_submission = node
            else:
                self.stuck_submission = self.submissions[0]

    def get_submissions_node(self):
        return self.submissions

    def get_stuck_submission(self):
        return self.stuck_submission

    def get_CallBackMessage(self):
        return self.stuck_submission['CallbackMessage']

    def get_CallBackURI(self):
        self.callback_Uri = self.stuck_submission['CallbackUri']
        return self.callback_Uri

    def get_ExternalID(self):
        self.ExternalIdentifier = self.stuck_submission['ExternalIdentifier']
        return self.ExternalIdentifier

    def get_State(self):
        self.state = self.stuck_submission['State']
        return self.state

    def get_review_stepstate_id(self):
        for step in self.StepStates:
            if step['StepTitle'] == "Review":
                self.review_stepstate_id = step["StepStateId"]
                return self.review_stepstate_id
