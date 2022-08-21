# Programação para Sistemas Paralelos e Distribuidos

## Trabalho 2 - PySparkStreamming e Kafka

### 1 - Conecção com Netcat

Supondo que voce já tem o Apache Spark instalado e configurado, para executar faça:

Abrir um terminal e executar o comando 

```bash
$ nc -lk 9999
```

Abrir outro terminal e executar o programa

```bash
$ ./bin/spark-submit spark-kafka/word-count-stream.py localhost 9999
```

### 2 - Spark + Kafka