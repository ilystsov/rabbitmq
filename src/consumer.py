import sys
from collections import defaultdict

import pika


class LogsConsumer:
    def __init__(self, host: str, severities: list[str]) -> None:
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        self.exchange_name = "logs_exchange"
        self.channel.exchange_declare(exchange=self.exchange_name, exchange_type="direct")
        self.queue_name = self.channel.queue_declare(queue="", exclusive=True).method.queue
        for severity in severities:
            self.channel.queue_bind(queue=self.queue_name, exchange=self.exchange_name, routing_key=severity)
        self.log_count = defaultdict(int)

    def callback(self, ch, method, properties, body):
        print(f'[x] Received "{body.decode()}" with key {method.routing_key}')
        self.log_count[method.routing_key] += 1
        print(", ".join(f"{key}: {value}" for key, value in self.log_count.items()))

    def consume(self) -> None:
        self.channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=self.callback,
            auto_ack=True,
        )
        self.channel.start_consuming()


if __name__ == "__main__":
    severities = sys.argv[1:]
    if not severities:
        sys.stderr.write(f"Usage: {sys.argv[0]} [debug] [info] [critical] [error]\n")
        sys.exit(1)

    logs_consumer = LogsConsumer(host="localhost", severities=severities)
    logs_consumer.consume()
