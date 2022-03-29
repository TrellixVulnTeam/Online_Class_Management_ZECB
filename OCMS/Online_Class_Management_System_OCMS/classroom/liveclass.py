import json
import requests
import jwt
from time import time

API_KEY = 'm8mpOJZ8QIakPgQ89ENtIw'
API_SEC = 'aid1os9JE1sca9zclNNu809x5DFybYLBZTLP'


# userId = 'you can get your user Id by running the getusers()'
userId = 'me'
# your zoom live meeting id, it is optional though
meetingId = 83781439159

# create a function to generate a token using the pyjwt library


def generateToken():
    return jwt.encode(
        # Create a payload of the token containing API Key & expiration time
        {'iss': API_KEY, 'exp': time() + 5000},
        # Secret used to generate token signature
        API_SEC,
        # Specify the hashing alg
        algorithm='HS256'
        # Convert token to utf-8
    )
    # send a request with headers including a token

# this is the json data that you need to fill as per your requirement to create zoom meeting, look up here for documentation
# https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/meetingcreate


meetingdetails = {"topic": "My Title",
                  "duration": "45",
                  "timezone": "Europe/Madrid",
                  "start_time": "2019-06-14T10: 21: 57",
                  "agenda": "test",
                  "type": 2,

                  "recurrence": {"type": 1,
                                 "repeat_interval": 1
                                 },
                  "settings": {"host_video": "False",
                               "join_before_host": "true",
                               "watermark": "true",
                               "participant_video": "true",
                               "audio": "voip",
                               "auto_recording": "cloud",
                               "mute_upon_entry": "False",
                               "waiting_room": "False",
                               "show_share_button": "true",
                                "who_can_share_screen": "all",
                               #    "who_can_share_screen_when_someone_is_sharing":"all",
                                "screen_sharing": "true"
                               }
                  }


def createMeeting(meetingName):  # sourcery skip: avoid-builtin-shadow
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {generateToken()}',
    }
    meetingdetails["topic"] = meetingName
    r = requests.post(
        f'https://api.zoom.us/v2/users/{userId}/meetings', headers=headers, data=json.dumps(meetingdetails))

    dict = r.json()

    return dict["join_url"]
