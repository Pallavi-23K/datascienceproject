from dataclasses import dataclass
from pathlib import Path

#  normal class we need to use self to access the variables but in dataclass we don't need to use self to access the variables
@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
