import shutil
from config import RAW_DATA_PATH

def upload_hospital_data(file_path):
    shutil.copy(file_path, f"{RAW_DATA_PATH}hospital_data.csv")
    print("✅ Hospital data uploaded")
