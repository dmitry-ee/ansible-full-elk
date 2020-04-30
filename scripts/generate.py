import requests

logstash_port = 5000
total_messages = 500

for x in range(0, total_messages):
  requests.api.put("http://localhost:{}".format(logstash_port), data="message {}".format(x))