"""
Тестовый файл, в котором отправляется по одному логу каждого типа: debug, info, error, critical.
Ожидаемый итоговый (последний) вывод метрики в потребителях:
 - Потребитель 1 (debug, info, error, critical): debug: 1, info: 1, critical: 1, error: 1
 - Потребитель 2 (debug, info): debug: 1, info: 1
 - Потребитель 3 (critical): critical: 1
 - Потребитель 4 (error): error: 1
"""

import src.producer

logs_producer = src.producer.LogsProducer(host="localhost")

logs_producer.produce(severity="debug", message="Debug message")
logs_producer.produce(severity="info", message="Info message")
logs_producer.produce(severity="critical", message="Critical message")
logs_producer.produce(severity="error", message="Error message")

logs_producer.stop()
