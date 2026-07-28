
# 🛡️ Bug-Tracker-Bugify02

> **Enterprise-Grade Bug Tracking and Management System**
> *B.U.G.I.F.Y. - Bug Upload, Generation, Investigation, Fixing, and Yield*

![Version](https://img.shields.io/badge/Webpage_Version-v1.0.0-0284c7?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0+-lightgrey?style=for-the-badge&logo=flask)
![MongoDB](https://img.shields.io/badge/MongoDB_Atlas-47A248?style=for-the-badge&logo=mongodb)

---
<img width="1880" height="946" alt="Screenshot 2026-07-28 131148" src="https://github.com/user-attachments/assets/8c4d61d3-6f9e-45de-8d22-900529dd37a5" />

## 🎯 Project Objective
**Bug-Tracker-Bugify02** is designed to provide development teams with a centralized, highly responsive, and visually intuitive platform to track software defects. The objective is to streamline the entire lifecycle of a bug—from initial reporting and investigation to resolution and deployment—ensuring high productivity and software quality.

---

## 🔐 User Role & Access Control
The application currently operates on a single-tier administrative access model designed for internal team management.

* **Role:** System Administrator / Manager
* **Authentication:** Secured via a custom-built premium login screen.
* **Default Credentials:** 
  * **Username:** `admin`
  * **Password:** `1234`
* **Access Level:** Full CRUD (Create, Read, Update, Delete) permissions across all database records, dashboard analytics, and kanban boards.

---

## 🛠️ Technology Stack

| Layer | Technologies Used |
| :--- | :--- |
| **Backend** | Python, Flask (Web Framework) |
| **Database** | MongoDB Atlas (Cloud NoSQL), `pymongo`, `dnspython` |
| **Frontend** | HTML5, CSS3 (Custom Sea Blue Theme), Vanilla JavaScript |
| **Data Visualization** | Chart.js |
| **Icons & UI Assets**| FontAwesome 6.4.0 |

---

## ✨ Key Features and Workflows

* **Dynamic Analytics Dashboard:** Real-time metrics and progress tracking using visual charts.
* **Kanban Progress Board:** Visual ticket management with categorized statuses (`Open`, `In-Progress`, `Recheck`, `Paused`, `Resolved`, `Closed`).
* **RESTful API Integration:** Seamless async communication between the frontend interface and MongoDB backend (`/api/tickets`).
* **Theme Customization:** Built-in Dark/Light mode toggle for optimal user experience.
* **Automated Ticket Generation:** Auto-assigns unique IDs (e.g., `BUG-4592`) and timestamps upon ticket creation.
* **Live Audit Trails:** Tracks creation and modification dates for transparent team accountability.

---

## 💻 Local Setup & Installation

Follow these steps to configure the application on your local development machine.

### 1. Start Local Server
Ensure your MongoDB Atlas URI is correctly configured inside `app.py` before initializing the local environment.

### 2. Setup Virtual Environment
It is best practice to isolate your project dependencies. Navigate to your project folder in your terminal and run:
```bash
python -m venv venv

```

Activate the environment:

* **Windows:** `venv\Scripts\activate`
* **Mac/Linux:** `source venv/bin/activate`

### 3. Install Dependencies

With your virtual environment active, install the required Python packages from your `requirements.txt`:

```bash
pip install -r requirements.txt

```

### 4. Run the Application

Execute the main script to boot the local Flask server:

```bash
python app.py

```

Upon starting, the terminal will attempt a server selection timeout check. If successful, you will see a confirmation block:

```text
========================================
✅ DATABASE CONNECTED SUCCESSFULLY
========================================
 * Running on [http://127.0.0.1:5001](http://127.0.0.1:5001)

```

### 5. Access the Portal

Open your preferred web browser and navigate to:
**👉 `http://127.0.0.1:5001/**`
You will be greeted by the Bugify Login Screen. Enter the default admin credentials to access the system.

---

## 🧪 API Testing (Postman)

🚀 **Postman API Testing Guide**

* 🟢 **GET** `/api/tickets` ➔ Retrieve all active bug tickets from the database.
* 🟡 **POST** `/api/tickets` ➔ Create a new ticket (requires JSON body).
* 🔵 **PUT** & 🔴 **DELETE** `/api/tickets/<id>` ➔ Update or delete a specific ticket by its ID.

---

## 🗂️ GitHub Version Control & Webpage Version

### Webpage Version

* **Current Release:** `v1.0.0 (Stable)`
* **Status:** Active Development
* **Environment:** Local / Development

### Version Control Workflow

This project utilizes Git for version control. The standard workflow for deploying future updates:

1. `git pull origin main` *(Sync the latest changes from the remote repository)*
2. `git checkout -b feature/new-update` *(Create a new working branch)*
3. `git add .` *(Stage your modifications)*
4. `git commit -m "Descriptive commit message"` *(Commit changes locally)*
5. `git push origin feature/new-update` *(Push the branch to GitHub)*
6. Open a **Pull Request** on GitHub for code review before merging into the main branch.

---

## 🔒 Security Best Practices

To maintain data integrity and security, please ensure the following:

* **Environment Variables:** Never commit plain-text credentials (like your `MONGO_URI` connection string) to public repositories. Use a `.env` file alongside `python-dotenv` to manage secrets locally.
* **Gitignore:** Ensure your `.env` and `venv/` folders are added to your `.gitignore` file before pushing code.
* **Database Access:** Restrict your MongoDB network access (IP Whitelisting) via the Atlas dashboard and enforce strong, secure passwords for database users.

---




```
