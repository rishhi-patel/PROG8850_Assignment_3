# Flask Login App – Docker, Dev-Container, Ansible

## TL;DR
```bash
# Run containers with ansible
ansible-playbook -i ansible/inventory.ini ansible/playbook.yml
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

## ⚙️ Dev Container (VS Code)
Open folder in VS Code → "Reopen in Container".  
You’ll get:
- Python 3 + Pip
- MySQL tools
- Ansible preinstalled
- Required extensions auto-installed

## ✅ Environment Variables
Set in `docker-compose.yml`:

| Variable | Default |
|----------|---------|
| `MYSQL_USER` | root |
| `MYSQL_PASSWORD` | yourpassword |
| `MYSQL_DATABASE` | login_db |
| `MYSQL_HOST` | db |

---

Made for **PROG8850 – Assignment 3** by Rishi.
