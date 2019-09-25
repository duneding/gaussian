#import statements
from datetime import datetime

from opsgenie import OpsGenie
from opsgenie.alert.requests import ListAlertsRequest
from opsgenie.config import Configuration
from opsgenie.errors import OpsGenieError

import src.configuration.config as config

config = Configuration(apikey=config.value(['opsgenie', 'apikey']))
client = OpsGenie(config)
stats = {}

def hits(alias):

    if alias in stats.keys():
        return stats[alias]['hits'] + 1
    else:
        return 1

create_after = datetime(2017, 1, 01)
created_before = datetime.now()
limit = 100

try:
    list_alerts_response = client.alert.\
        list_alerts(ListAlertsRequest(created_after=create_after, created_before=created_before, limit=limit))

    for alert in list_alerts_response.alerts:
        print "Id: ", alert.id
        print "Alias: ", alert.alias
        print "Message: ", alert.message
        print "Status: ", alert.status
        print "IsSeen: ", alert.is_seen
        print "Acknowledged: ", alert.acknowledged
        print "Created at: ", alert.created_at
        print "Updated at: ", alert.updated_at
        print "Tiny id: ", alert.tiny_id
        print "Owner: ", alert.owner
        print "------------------"

        stats[alert.alias] = {
                                "status": alert.status,
                                "is_seen": alert.is_seen,
                                "ack": alert.acknowledged,
                                "hits": hits(alert.alias)
                            }

except OpsGenieError as err:
    print "[ERROR]", err.message

for alert in sorted(stats, key=hits, reverse=True):
    print alert, " : ", stats[alert]["hits"]


