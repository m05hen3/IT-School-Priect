# IT-School-Priect
*Proiect examen curs DevOps - IT School 2025*

## Platforma de Monitorizare a starii sistemului

### Descriere
Acest proiect este o platforma de tip DevOps pentru monitorizarea starii unui sistem informatic.

---

### Functionalitati implementate

1. **monitor.sh** 
    - Colecteaza la intervale regulate (la interval configurabil, default = 5 secunde) informatii despre:
        - Utilizare CPU
        - Utilizarea memoriei 
        - Numarul de procese active
        - Utilizarea discului
    - Scrie aceste informatii in fisierul "system-state.log", suprascriind continutul anterior.
    - Include loguri relevante pentru depanare si monitorizare

2. **backup.py**
    - Monitorizeaza modificarile din fisierul "system-state.log"
    - Realizeaza backup doar daca fisierul a fost modificat, salvand copii in directorul "backup/" cu timestamp in nume.
    - Intervalul de backup si directorul pot fi configurate prin variabile de mediu "BACKUP_INTERVAL" si "BACUP_DIR".
    - Logging detaliat pentru succes, avertismente si erori.

3. **Containerizare cu Docker si Docker Compose**
    - Ambele scripturi sunt impachetate in containere Docker.
    - Configuratie unificata prin "docker-compose.yml" pentru rulare locala usoara.
    - Loguri accesibile prin comenzi Docker standard.

4. **Automatizare Ansible**
    - Script pentru generarea inventarului Ansible
    - Playbook pentru instalarea Docker pe host-ul remote
    - Playbook pentru deploy-ul platformei

---

### Instructiuni

1. **Clonare repository**
    ```bash
    git clone https://github.com/m05hen3/IT-School-Priect.git
    cd IT-School-Priect
    ```
    
2. **Rulare locala manuala (pentru testare rapida)**
    - Pornire monitor:
    ```bash
    chmod +x. scripts/monitor.sh
    INTERVAL=2 ./scripts/monitor.sh
    ```
    - Pornire backup in alt terminal (in paralel):
    ```bash
    mkdir -p backup
    BACKUP_INTERVAL=3 BACKUP_DIR=backup python3 scripts/backup.py
    ```

3. **Rulare cu Docker Compose**
    - Build imagini:
    ```bash
    docker compose build --no-cache
    ```
    - Pornire containere:
    ```bash
    docker compose up -d
    ```
    - Vizualizare log monitor:
    ```bash
    docker compose logs -f monitor
    ```
    - Vizualizare log backup:
    ```bash
    docker compose logs -f backup
    ```
    - Verificare continut backup:
    ```bash
    ls backup/
    ```
    - Oprire containere:
    ```bash
    docker compose down
    ```

4. **Automatizare deploy cu Ansible**
    - Generare inventory pentru host-ul remote:
    ```bash
    cd devops-monitoring/ansible
    python3 generate_inventory.py
    ```
    - Instalare Docker pe remote:
    ```bash
    ansible-playbook -i inventory.ini playbooks/install-docker.yml
    ```
    - Deploy platforma pe remote:
    ```bash
    ansible-playbook -i inventory.ini playbooks/deploy.yml
    ```

---

### Structura proiectuluidocker compose down

```plaintext
IT-School-Priect/
|__ devops-monitoring/
    |__ ansible/
    |   |__ playbooks/
    |   |   |__ deploy.yml
    |   |   |__ install-docker.yml
    |   |__ generate_inventory.py
    |   |__ inventory.ini
    |   |__ vars.yml
    |__ backup/                     # Directorul unde se salveaza backup-urile
    |__ docker/
    |   |__ backup/
    |   |   |__ Dockerfile          # Dockerfile pentru container backup
    |   |__ monitor/
    |       |__ Dockerfile          # Dockerfile pentru container monitor
    |__ jenkins/
    |__ scripts/
    |   |__ backup.py
    |   |__ monitor.sh
    |__ terraform/
    |__ docker-compose.yml
    |__ system-state.log
    |__ README.md
```

---

### Tehnologii utilizate:

```plaintext
    - **Bash** - scriptul de monitorizare (monitor.sh)
    - **Python** - scriptul de backup (backup.py)
    - **GIT** - Versionare
    - **Docker & Docker Compose** - Containerizarea si orchestrarea serviciilor
```

---