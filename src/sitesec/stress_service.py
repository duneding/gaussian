from threading import Thread

import requests

url = 'http://localhost:8080/login_events'
data = '''{
  "msg": {
    "user_id": 1,
    "device_id": "59de08676c602d4f86795dac",
    "exact_id": "59a71849114e060267c89d2e",
    "ip": "201.208.158.105",
    "site_id": "MLV",
    "date": "2017-11-17T15:03:43.759-04:00",
    "device_profile_session": "armor.6f743c0959630db6a07b2e59bf5d8a2302f3833876342d2f2b53039968f4d568227f4c179d5c17fb3c7209205e496bc92781020e6f172ad686e013669f9dd3ee00db3e7d98d28a102cf4377d3a1c9377.45890970a4fbc5b4be9d016b90f75d8a",
    "login_otp": false,
    "login_type": "EXPLICIT",
    "rba_scoring_id": "f76b9c5399a98542996439050f8f51e71afba13b77791200e9bb67f9baac39a50101cf89f6d4e8540e20216b52ffdee4",
    "msl_tx": "aFi4sgBLx89FExHkNXRjkLjDlRzrPTMLI9rZ0FVFVdrAwdZIM",
    "ftid": "MJd6bA3UFDj27xnGC8cguuvDKQUxLfGb-1510292753237",
    "_d2id": "f72c9663-e85e-4e0e-9bda-2b90706cfcae"
  }
}'''


def post(n):
    # sleep(n)
    try:
        while 1:
            response = requests.post(url, data=data)
            print response.status_code
    except:
        print "[ERROR]"


subprocesoA = Thread(target=post, args=(5,))
subprocesoB = Thread(target=post, args=(5,))
subprocesoC = Thread(target=post, args=(5,))
subprocesoD = Thread(target=post, args=(5,))
subprocesoE = Thread(target=post, args=(5,))
subprocesoF = Thread(target=post, args=(5,))
subprocesoG = Thread(target=post, args=(5,))
subprocesoH = Thread(target=post, args=(5,))

subprocesoA.start()
subprocesoB.start()
subprocesoC.start()
subprocesoD.start()
subprocesoE.start()
subprocesoF.start()
subprocesoG.start()
subprocesoH.start()

subprocesoA.join()
subprocesoB.join()
subprocesoC.join()
subprocesoD.join()
subprocesoE.join()
subprocesoF.join()
subprocesoG.join()
subprocesoH.join()
