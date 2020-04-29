import requests


# https://avsip.ad.bl.uk/api/SIP/SubmissionCallback/ark%5E%7B81055%7Bvdc_100094409157!0x000002/2020-04-09T09%5E11%5E49Z



class ApiRequests(object):

    SIP_TOOL_ADDR = "https://avsip.ad.bl.uk/"
    SIP_API = "api/SIP/"


    # def __init__(self):
    #     self.sip_tool_addr = SIP_TOOL_ADDR
    #     self.sip_tool_api = SIP_API

    def get_JSON(self, SIP_ID):
        r = requests.get(f"{self.SIP_TOOL_ADDR}{self.SIP_API}{SIP_ID}", verify=False)
        if r.status_code == 404:
            return None
        return r.json()

    def post_callback(self, callback_URI, ark, message=None):
        self.body = {"outcome":"Failure"}
        self.body["logicalArk"] = ark
        self.body["externalIdentifier"] = ark

        if message == None:
                self.body["message"] = f"Forced timeout failure by {username} due to no callback received."
        else:
            self.body["message"] = message
        
        r = requests.post(callback_URI, json=self.body, verify=False)
        if r.status_code == 200:
            self.response = r
            return self.test_callback()
        else:
            self.response = None

    def test_callback(self):
        
        """Checks the text of the response for the digit 0 
        (0 indicates a failure, which is what we want) and 
        the failure message will be echoed back.
        """
        return any(map(lambda x: x == "0", self.response.text))
        

my_app = ApiRequests()
psip_json= my_app.get_JSON(40513)
x = my_app.post_callback(psip_json['Submissions'][0]['CallbackUri'], psip_json['Submissions'][0]['ExternalIdentifier'], "Forced timeout failure by CWEAVER due to no callback received.")
# my_app.post_callback("blahblah", "Ronsark")
print(x)