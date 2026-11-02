import os
import shutil
import random

DATA_DIR = "/var/data"
RESULT_DIR = "/var/result"

if __name__ == "__main__":
    files = [
        os.path.join(DATA_DIR, name)
        for name in os.listdir(DATA_DIR)
        if os.path.isfile(os.path.join(DATA_DIR, name))
    ]
    if files:
        chosen = random.choice(files)
        dst = os.path.join(RESULT_DIR, "data.txt")
        shutil.copy(chosen, dst)
        print(f"[worker1] Chosen file: {chosen}")
        print(f"[worker1] Copied to:   {dst}")
    else:
        print("[worker1] No files in /var/data")