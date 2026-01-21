import shutil
from pathlib import Path
from .config import RAW_DATA_PATH

def upload_hospital_data(file_path):
    src = Path(file_path).resolve()
    dest_dir = Path(RAW_DATA_PATH).resolve()
    dest_dir.mkdir(parents=True, exist_ok=True)

    dest = dest_dir / "hospital_data.csv"

    if src == dest:
        print("ℹ️ Hospital data already in raw folder, skipping copy")
        return

    shutil.copy(src, dest)
    print("✅ Hospital data copied successfully")
