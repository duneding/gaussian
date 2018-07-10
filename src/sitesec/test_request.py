from threading import Thread

import requests

import config

url_fake = config.value(['device_profile', 'url_fake'])
url_success_kvs = config.value(['device_profile', 'url_success_kvs'])
url_success_legacy = config.value(['device_profile', 'url_success_legacy'])
url_not_found = config.value(['device_profile', 'url_not_found'])


def action(n):
    # sleep(n)
    try:
        while 1:
            response = requests.get(url_fake)
            print response.status_code

            response = requests.get(url_success_kvs)
            print response.status_code

            response = requests.get(url_not_found)
            print response.status_code

            response = requests.get(url_success_legacy)
            print response.status_code

            # time.sleep(randint(0, 1))
    except:
        print "[ERROR]"


subprocesoA = Thread(target=action, args=(5,))
subprocesoB = Thread(target=action, args=(5,))
subprocesoC = Thread(target=action, args=(5,))
subprocesoD = Thread(target=action, args=(5,))
subprocesoE = Thread(target=action, args=(5,))
subprocesoF = Thread(target=action, args=(5,))
subprocesoG = Thread(target=action, args=(5,))
subprocesoH = Thread(target=action, args=(5,))

subprocesoI = Thread(target=action, args=(5,))
subprocesoJ = Thread(target=action, args=(5,))
subprocesoK = Thread(target=action, args=(5,))
subprocesoL = Thread(target=action, args=(5,))
subprocesoM = Thread(target=action, args=(5,))
subprocesoN = Thread(target=action, args=(5,))
subprocesoO = Thread(target=action, args=(5,))
subprocesoP = Thread(target=action, args=(5,))

subprocesoA.start()
subprocesoB.start()
subprocesoC.start()
subprocesoD.start()
subprocesoE.start()
subprocesoF.start()
subprocesoG.start()
subprocesoH.start()

subprocesoI.start()
subprocesoJ.start()
subprocesoK.start()
subprocesoL.start()
subprocesoM.start()
subprocesoN.start()
subprocesoO.start()
subprocesoP.start()

subprocesoA.join()
subprocesoB.join()
subprocesoC.join()
subprocesoD.join()
subprocesoE.join()
subprocesoF.join()
subprocesoG.join()
subprocesoH.join()

subprocesoI.join()
subprocesoJ.join()
subprocesoK.join()
subprocesoL.join()
subprocesoM.join()
subprocesoN.join()
subprocesoO.join()
subprocesoP.join()
