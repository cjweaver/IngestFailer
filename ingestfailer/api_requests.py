import requests



SIP_TOOL_ADDR = "https://avsip.ad.bl.uk/"
SIP_API = "api/SIP/"

# def __init__(self):
#     self.sip_tool_addr = SIP_TOOL_ADDR
#     self.sip_tool_api = SIP_API


def get_JSON(SIP_ID):
    r = requests.get(f"{SIP_TOOL_ADDR}{SIP_API}{SIP_ID}", verify=False)
    if r.status_code == 404:
        return None
    else:
        return r.json()


def post_callback(callback_URI, ark, message=None):
    body = {"outcome":"Failure"}
    body["logicalArk"] = ark
    body["externalIdentifier"] = ark

    if message == None:
            body["message"] = f"Forced timeout failure by username due to no callback received."
    else:
        body["message"] = message
    
    r = requests.post(callback_URI, json=body, verify=False)
    if r.status_code == 200:
        # Checks that the start of the response text for the digit 0 
        # (0 indicates a failure, which is what we want) and 
        # the failure message will be echoed back.
        return r.text.strip("\"\'").startswith('0')
    else:
        return False

# def submit_sip(self, sip_id, review_stepstate_id, user_id, submit=True):
#     r = requests.get(f"{ApiRequests.SIP_TOOL_ADDR}{ApiRequests.SIP_API}{SIP_ID}/Generate/{sip_id}/{stepstate_id}/{submit}/{user_id}", verify=False)
#     GET api/SIP/Generate/{sip_id}/{stepstate_id}/{submit}/{user_id} should be "true" (even though it's actually ignored, any pSIP id sent will be submitted).


# def test_callback(response):
    
#     """Checks that the start of the response text for the digit 0 
#     (0 indicates a failure, which is what we want) and 
#     the failure message will be echoed back.
#     """
#     # return any(map(lambda x: x == "0", response.text))
    

# my_app = ApiRequests()
# psip_json= my_app.get_JSON(40513)
# x = my_app.post_callback(psip_json['Submissions'][0]['CallbackUri'], psip_json['Submissions'][0]['ExternalIdentifier'], "Forced timeout failure by CWEAVER due to no callback received.")
# # my_app.post_callback("blahblah", "Ronsark")
# print(x)