#!/usr/bin/env python3

import os
import time
import shutil
import hashlib
import logging
from datetime import datetime

LOG_FILE = "system-state.log"
BACKUP_DIR = os.getenv("BACKUP_DIR", "backup")
BACKUP_INTERVAL = int(os.getenv("BACKUP_INTERVAL", 5))

# Configurare logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s %(levelname)s: %(message)s]',
    datefmt='%Y-%m-%d %H:%M:%S'
)


# Daca nu exista directorul de backup il creeam 
os.makedirs(BACKUP_DIR, exist_ok=True)

def file_checksum(path):
    """Retunreaza checksum-ul MD5 al fisierului."""
    try:
        with open(path, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()
    except FileNotFoundError:
        logging.warning(f"fisierul {path} nu exista pentru calcul checksum.")
        return None
    except Exception as e:
        logging.error(f"Eroare la citirea fisierului {path} pentru checksum: {e}")
        return None
    
def backup_file():
    """Face backup daca fisierul s-a modificat"""
    prev_checksum = None

    while True:
        try:
            if os.path.exists(LOG_FILE):
                current_checksum = file_checksum(LOG_FILE)
                if current_checksum is None:
                    logging.warning(f"Nu s-a putut calcula checksum pentru {LOG_FILE}")
                elif current_checksum != prev_checksum:
                    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    backup_name = f"system-state-{timestamp}.log"
                    dest_path = os.path.join(BACKUP_DIR, backup_name)
                    shutil.copy2(LOG_FILE, dest_path)
                    logging.info(f"Backup creat: {dest_path}")
                    prev_checksum = current_checksum
                else:
                    logging.info("Nicio modificare, nu fac backup")
            else: 
                logging.warning(f"{LOG_FILE} nu exista.")
        except Exception as e:
            logging.error(f"Eroare la backup: {e}")
        time.sleep(BACKUP_INTERVAL)

if __name__ == "__main__":
    logging.info(f"Backup script pornit. Interval = {BACKUP_INTERVAL}s, director = {BACKUP_DIR}")
    backup_file()