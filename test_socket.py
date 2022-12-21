### creds ###
app_id = "1527920"
key = "a67fe69450ce733e2df9"
secret = "93ebccb69d4ceb83afb5"
cluster = "mt1"

### imports ###
import pusher_socket as pysher
import logging, sys, time

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(logging.Formatter('[%(asctime)s] %(message)s'))
logging.getLogger('').addHandler(console)


def my_func(*args, **kwargs): None

pusher = pysher.Pusher(key)
pusher.add('quiet-lawn-868', 'event1', my_func)
pusher.add('quiet-lawn-868', 'event2', my_func)
pusher.connect()

while True:
 time.sleep(1)