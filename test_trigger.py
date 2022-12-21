app_id  = "1527920"
key     = "a67fe69450ce733e2df9"
secret  = "93ebccb69d4ceb83afb5"
cluster = "mt1"

import pusher
import json

pusher_client = pusher.Pusher(app_id, key, secret, cluster)
pusher_client.trigger('quiet-lawn-868','event1', json.dumps({"from":"1"}))
pusher_client.trigger('quiet-lawn-868','event2', json.dumps({"from":"2"}))