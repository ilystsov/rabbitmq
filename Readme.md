# ДЗ 6. RabbitMQ
### Инструкция по запуску
В отдельных окнах терминала запустим 4
консьюмера:
```bash
poetry run python3 -m src.consumer debug info critical error
```
```bash
poetry run python3 -m src.consumer debug info
```
```bash
poetry run python3 -m src.consumer critical 
```
```bash
poetry run python3 -m src.consumer error
```
Далее запустим тестовые файлы, которые 
запустят продюсера:
```bash
poetry run python3 -m src.test_files.test_1
```
```bash
poetry run python3 -m src.test_files.test_2
```
```bash
poetry run python3 -m src.test_files.test_3
```
>*Примечание*: для получения ожидаемого 
> вывода метрик перед каждым запуском 
> тестовых файлов необходимо перезапускать 
> консьюмеры.