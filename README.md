# 🧪 PROG8850 – Assignment 3: End-to-End Web App Automation with Selenium & Docker

This project demonstrates a full-stack login web application with automated end-to-end testing using Selenium WebDriver. The setup uses Docker Compose to run the application, MySQL database, and Selenium Chrome Driver in isolated containers, while the test script runs from the Codespace host.

---

## 📦 Project Structure

```
PROG8850_Assignment_3/
├── app.py               # Simple login form with DB insert
├── test_login.py        # Selenium + DB test script (run from host)
├── docker-compose.yml   # Defines app, db, selenium services
└── README.md            # You're looking at it!
```

---

## 🚀 How to Run

### 1. Start All Services

```bash
docker compose up -d --build
```

This will start:

- 🧠 `db`: MySQL 8.4 (with a `login_db` database)
- 🌐 `app`: Flask web server on port `5000`
- 🤖 `selenium`: Standalone Chrome with WebDriver on port `4444`

---

### 2. Run the Test

In your Codespace terminal (outside Docker), run:

```bash
python test_login.py
```

This will:

1. Use Selenium to open the login page.
2. Submit `testuser` / `testpass`.
3. Verify the data was inserted into MySQL.
4. Output: `✅  Test passed.` if successful.

---

### 3. Shut Down and Cleanup

```bash
docker compose down -v
```

This stops and removes all containers and volumes.

---

## 📋 Notes

- **All services run in Docker** for consistency and portability.
- **Test runs from host** for simplicity in debugging and output.
- Flask binds to `0.0.0.0:5000`, MySQL is exposed on `3306`, and Selenium WebDriver is exposed on `4444`.
- The Selenium container already includes Chrome and WebDriver.
- Python test script uses `ChromeOptions` with `--headless=new` for clean CI-friendly testing.

---

## 📸 Sample Output

```
$ python test_login.py
✅  Test passed.
```

---

## 👤 Author

**Rishikumar Patel [8972657]**
Conestoga College – PROG8850
