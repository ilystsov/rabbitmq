import pika


class LogsProducer:
    def __init__(self, host: str) -> None:
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        self.exchange_name = "logs_exchange"
        self.channel.exchange_declare(exchange=self.exchange_name, exchange_type="direct")

    def _print_published(self, severity: str, message: str) -> None:
        print(f"[x] Sent {severity}: {message}")

    def produce(self, severity: str, message: str) -> None:
        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=severity,
            body=message,
        )
        self._print_published(severity, message)

    def stop(self) -> None:
        self.connection.close()
