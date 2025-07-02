# Flask Login App – Docker, Dev-Container, Ansible

## TL;DR
```bash
# Run containers with ansible
ansible-playbook up.yml
```
```bash
# Run containers with ansible
ansible-playbook down.yml
```

### Or plain Docker Compose
```bash
docker compose up --build
```

### Run Selenium test
```bash
python test_login.py
```

---

## 🧾 Project Structure

```
.
├── app.py                 # Flask app
├── Dockerfile             # Image with Python + deps
├── docker-compose.yml     # Runs Flask and MySQL
├── requirements.txt
├── setup.sql              # Creates MySQL database and users table
├── test_login.py          # Selenium test
├── templates/
│   └── login.html         # Basic login form
├── ansible/
│   ├── inventory.ini
│   ├── playbook.yml
│   └── requirements.yml
└── .devcontainer/
    └── devcontainer.json  # VS Code container config
```
