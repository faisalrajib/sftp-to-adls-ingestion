from config import Config
from sftp_client import SFTPClient
from adls_client import ADLSClient

def main():
    print("Starting SFTP → ADLS ingestion")

    sftp = SFTPClient(
        Config.SFTP_HOST,
        Config.SFTP_PORT,
        Config.SFTP_USER,
        Config.SFTP_PASSWORD
    )

    adls = ADLSClient(Config.AZURE_STORAGE_ACCOUNT)

    files = sftp.list_files(Config.SFTP_REMOTE_PATH)

    for file in files:
        print(f"Processing: {file}")
        remote_path = f"{Config.SFTP_REMOTE_PATH}/{file}"
        data = sftp.download_file_to_memory(remote_path)

        adls.upload_bytes(
            Config.AZURE_CONTAINER,
            Config.AZURE_DIRECTORY,
            file,
            data
        )

        print(f"Uploaded: {file}")

    sftp.close()
    print("Done.")

if __name__ == "__main__":
    main()
