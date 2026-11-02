import time
import pika

creds = pika.PlainCredentials("dev", "dev")
conn = pika.BlockingConnection(pika.ConnectionParameters("localhost", 5672, "/", creds))
ch = conn.channel()

ch.queue_declare(queue="task_queue", durable=True)


def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    time.sleep(body.count(b"."))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


ch.basic_qos(prefetch_count=1)
ch.basic_consume(queue="task_queue", on_message_callback=callback)
print(" [*] Waiting for messages. To exit press CTRL+C")
ch.start_consuming()