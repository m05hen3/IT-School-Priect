import yaml
import os

VARS_FILE = "vars.yml"
INVENTORY_FILE = "inventory.ini"

def read_vars():
    if os.path.exists("vars.yml"):
        with open(VARS_FILE, "r") as f:
            return yaml.safe_load(f)
    return {}

def save_vars(vars_data):
    with open(VARS_FILE, "w") as f:
        yaml.dump(vars_data, f)

vars_data = read_vars()

print("Introduceti datele pentru generarea inventory.ini. Apasati tasta Enter pentru a pastra valoarea existenta in paranteze")

remote_host = input(f"Remote Host IP [{vars_data.get('remote_host','')}]: ") or vars_data.get("remote_host", "127.0.0.1")
remote_user = input(f"Remote User [{vars_data.get('remote_user', '')}]: ") or vars_data.get("remote_user", "root")

vars_data.update({
    "remote_host": remote_host,
    "remote_user": remote_user
})

save_vars(vars_data)

inventory_content = f"""[remote]
remote1 ansible_host={remote_host} ansible_user={remote_user}
"""

with open("inventory.ini", "w") as f:
    f.write(inventory_content)

print("Fisierul inventory.ini a fost generat")
print(inventory_content)