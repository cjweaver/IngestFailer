import requests

SIP_TOOL_ADDR = "https://avsip.ad.bl.uk/"
SIP_API = "api/SIP/"

def get_JSON(SIP_ID):
    response = requests.get(f"{SIP_TOOL_ADDR}{SIP_API}{SIP_ID}", verify=False)
    if response.status_code == 404:
        return None
    return response.json()


def post_callback(callback_URI, ark, message=None):
    body = {"outcome":"Failure"}
    body["logicalArk"] = ark
    body["externalIdentifier"] = ark

    if message is None:
        body["message"] = f"Forced timeout failure by username due to no callback received."
    else:
        body["message"] = message

    response = requests.post(callback_URI, json=body, verify=False)
    if response.status_code == 200:
        # Checks the start of the response text for the digit 0
        # (0 indicates a failure, which is what we want) and
        # the failure message will be echoed back.
        return response.text.strip("\"\'").startswith('0')
    return False
