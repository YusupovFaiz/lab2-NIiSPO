import sys
import pika

creds = pika.PlainCredentials("dev", "dev")
conn = pika.BlockingConnection(pika.ConnectionParameters("localhost", 5672, "/", creds))
ch = conn.channel()

ch.queue_declare(queue="task_queue", durable=True)
message = " ".join(sys.argv[1:]) or "Hello World!"
ch.basic_publish(
    exchange="",
    routing_key="task_queue",
    body=message,
    properties=pika.BasicProperties(delivery_mode=2),
)
print(f" [x] Sent {message}")
conn.close()