"""
Тестовый файл, в котором отправляется по 3 лога типов critical и error.
Ожидаемый итоговый (последний) вывод метрики в потребителях:
 - Потребитель 1 (debug, info, error, critical): critical: 3, error: 3
 - Потребитель 2 (debug, info):
 - Потребитель 3 (critical): critical: 3
 - Потребитель 4 (error): error: 3
Второй потребитель ничего не выводит, поскольку не получает соответствующих логов.
"""

import src.producer

logs_producer = src.producer.LogsProducer(host="localhost")

for _ in range(3):
    logs_producer.produce(severity="critical", message="Critical message")
    logs_producer.produce(severity="error", message="Error message")

logs_producer.stop()
