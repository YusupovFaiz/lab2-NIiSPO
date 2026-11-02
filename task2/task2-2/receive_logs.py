import pika

creds = pika.PlainCredentials("dev", "dev")
conn = pika.BlockingConnection(pika.ConnectionParameters("localhost", 5672, "/", creds))
ch = conn.channel()

ch.exchange_declare(exchange="logs", exchange_type="fanout")

result = ch.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue
ch.queue_bind(exchange="logs", queue=queue_name)

print(" [*] Waiting for logs. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print(f" [x] {body.decode()}")


ch.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
ch.start_consuming()