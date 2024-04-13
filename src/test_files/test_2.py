"""
Тестовый файл, в котором отправляется 0 логов типа debug, 5 типа info, 15 типа error, 3 типа critical.
Ожидаемый итоговый (последний) вывод метрики в потребителях:
 - Потребитель 1 (debug, info, error, critical): info: 5, error: 15, critical: 3
 - Потребитель 2 (debug, info): info: 5
 - Потребитель 3 (critical): critical: 3
 - Потребитель 4 (error): error: 15
"""

import src.producer

logs_producer = src.producer.LogsProducer(host="localhost")

for _ in range(5):
    logs_producer.produce(severity="info", message="Info message")
for _ in range(15):
    logs_producer.produce(severity="error", message="Error message")
for _ in range(3):
    logs_producer.produce(severity="critical", message="Critical message")

logs_producer.stop()
