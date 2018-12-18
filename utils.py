import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAKIud4ZBU84BAGiul6z9IAwtZC6J42R65jpk4lNJGY9GG1iCi8oIZBhJipYj8omZAqCuzGy2wp02I4onAZBjjmWkwrpO7MsNjzaOCbQgyLGqU3pLIkTv8Dk7GZCZBVCydSn8dVTHhWbDeYw9ycIdAoT6DMaJppY8GHKrj1QdLGo9aMuYMCrOMX"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_photo_message(id, location):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {    
          "attachment":{
            "type":"image", 
            "payload":{
              "url":location, 
              "is_reusable": True
             }
           }
         }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
