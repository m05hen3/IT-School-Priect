import yaml
import os

def read_vars():
    if os.path.exists("vars.yml"):
        with open("vars.yml", "r") as f:
            return yaml.safe_load(f)
    return {}

def save_vars(vars_data):
    with open("vars.yml", "w") as f:
        yaml.dump(vars_data, f)

vars_data = read_vars()

print("Introduceti datele pentru generarea inventory.ini. Apasati tasta Enter pentru a pastra valoarea existenta in paranteze")

remote_host = input(f"Remote Host IP [{vars_data.get('remote_host','')}]: ") or vars_data.get("remote_host", "127.0.0.1")
remote_user = input(f"Remote User [{vars_data.get('remote_user', '')}]: ") or vars_data.get("remote_user", "root")
remote_key_path = input(f"SSH Private Key Path [{vars_data.get('remote_key_path', '~/.ssh/id_rsa')}]: ") or vars_data.get("remote_key_path", "~/.ssh/id_rsa")

vars_data.update({
    "remote_host": remote_host,
    "remote_user": remote_user,
    "remote_key_path": remote_key_path
})

save_vars(vars_data)

inventory_content = f"""[remote]
{remote_host} ansible_user={remote_user} ansible_ssh_private_key_file={remote_key_path}
"""

with open("inventory.ini", "w") as f:
    f.write(inventory_content)

print("Fisierul inventory.ini a fost generat")
print(inventory_content)