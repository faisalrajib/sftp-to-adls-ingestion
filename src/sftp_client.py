import paramiko

class SFTPClient:
    def __init__(self, host, port, username, password):
        self.transport = paramiko.Transport((host, port))
        self.transport.connect(username=username, password=password)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

    def list_files(self, remote_path):
        return self.sftp.listdir(remote_path)

    def download_file_to_memory(self, remote_path):
        with self.sftp.open(remote_path, "rb") as f:
            return f.read()

    def close(self):
        self.sftp.close()
        self.transport.close()
