# SFTP to Azure ADLS Gen2 Ingestion Pipeline

Production-style Python project demonstrating secure ingestion from SFTP into Azure Data Lake Storage Gen2.

## Features
- SFTP via Paramiko
- Azure ADLS Gen2 via Azure SDK
- Environment config
- Docker-ready
- Clean architecture

## Run
```
pip install -r requirements.txt
cp .env.example .env
az login
python src/main.py
```
# sftp-to-adls-ingestion




