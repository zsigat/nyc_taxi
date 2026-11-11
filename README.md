# Start services

## Airflow

Start all services in docker containers:

```bash
docker compose up
```

Open WebUI:
```
http://localhost:8080
```

## PySpark

Activate virtual environment:
```bash
source .venv/bin/activate
```

Start the service:
```bash
pyspark
```
Open WebUI:
```
http://localhost:4040
```

# Extra resources

## Airflow

> ### Fundamentals
> 
> Basic example: [Airflow 101](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html)
>
> See `dags/hello.py`

## PySpark

> ### API Reference
>
> Descriptions and examples: [API Reference](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/spark_session.html)


# Fix for possible issues

## Compromised Secrets

### Generating new values

```python
# FERNET_KEY
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
# SECRET_KEY and JWT_SECRET (run twice, use different values)
python -c "import secrets; print(secrets.token_urlsafe(32))"
```