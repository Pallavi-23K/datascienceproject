import os
import urllib.request as request
from src.datascience import logger
import zipfile
from src.datascience.entity.config_entity import DataIngestionConfig

# component DataIngestion
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
# Downloading the zip file from the source URL and saving it to the local data file path specified in the configuration. If the file already exists, it logs that information instead of downloading it again.
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url= self.config.source_URL,
                filename= self.config.local_data_file
            )
            logger.info(f"{filename} downloaded! with following info: \n{headers}")
        else:
            logger.info(f"FIle already exists")

    def extract_zip_file(self):
        """
        zip_file_path:str
        Extracts the zip file into data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok= True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
              zip_ref.extractall(unzip_path
        )