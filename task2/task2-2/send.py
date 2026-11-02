import pika

creds = pika.PlainCredentials("dev", "dev")
params = pika.ConnectionParameters("localhost", 5672, "/", creds)
conn = pika.BlockingConnection(params)
ch = conn.channel()

ch.queue_declare(queue="hello")
ch.basic_publish(exchange="", routing_key="hello", body="Hello World!")
print(" [x] Sent 'Hello World!'")
conn.close()