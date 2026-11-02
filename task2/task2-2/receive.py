import pika

creds = pika.PlainCredentials("dev", "dev")
params = pika.ConnectionParameters("localhost", 5672, "/", creds)
conn = pika.BlockingConnection(params)
ch = conn.channel()

ch.queue_declare(queue="hello")


def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")


ch.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)
print(" [*] Waiting for messages. To exit press CTRL+C")
ch.start_consuming()