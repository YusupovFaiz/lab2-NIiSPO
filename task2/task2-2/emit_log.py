import sys
import pika

creds = pika.PlainCredentials("dev", "dev")
conn = pika.BlockingConnection(pika.ConnectionParameters("localhost", 5672, "/", creds))
ch = conn.channel()

ch.exchange_declare(exchange="logs", exchange_type="fanout")
message = " ".join(sys.argv[1:]) or "info: Hello World!"
ch.basic_publish(exchange="logs", routing_key="", body=message)
print(f" [x] Sent {message}")
conn.close()