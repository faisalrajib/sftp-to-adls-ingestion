import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SFTP_HOST = os.getenv("SFTP_HOST")
    SFTP_PORT = int(os.getenv("SFTP_PORT", "22"))
    SFTP_USER = os.getenv("SFTP_USER")
    SFTP_PASSWORD = os.getenv("SFTP_PASSWORD")
    SFTP_REMOTE_PATH = os.getenv("SFTP_REMOTE_PATH")

    AZURE_STORAGE_ACCOUNT = os.getenv("AZURE_STORAGE_ACCOUNT")
    AZURE_CONTAINER = os.getenv("AZURE_CONTAINER")
    AZURE_DIRECTORY = os.getenv("AZURE_DIRECTORY")
