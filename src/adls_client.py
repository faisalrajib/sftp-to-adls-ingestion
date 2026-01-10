from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import DataLakeServiceClient

class ADLSClient:
    def __init__(self, account_name):
        self.credential = DefaultAzureCredential()
        self.service_client = DataLakeServiceClient(
            account_url=f"https://{account_name}.dfs.core.windows.net",
            credential=self.credential
        )

    def upload_bytes(self, container, directory, filename, data: bytes):
        file_system = self.service_client.get_file_system_client(container)
        dir_client = file_system.get_directory_client(directory)
        file_client = dir_client.create_file(filename)

        file_client.append_data(data, offset=0, length=len(data))
        file_client.flush_data(len(data))
