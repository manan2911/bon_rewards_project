# BON Rewards Backend

This project simulates BON’s reward flow:
Users receive a mock gift card reward **only if they have paid their last 3 credit card bills on time**.

---

## 🚀 Tech Stack

* **Backend:** Django + Django REST Framework
* **Database:** PostgreSQL (Render)
* **Deployment:** Render (Free tier)
* **Language:** Python 3.13

---

## 📌 Features

* API to simulate **users, bills, and rewards**
* Tracks **due dates** and **payment dates**
* Business logic:

  * If a user pays **last 3 bills on or before the due date**, they receive a **reward**.
  * Reward example: `$10 Amazon Gift Card`
* Preloaded with **mock data** (users, bills, rewards).

---

## 🔧 Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/manan2911/bon_rewards_project.git
cd bon_rewards_project
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Seed initial data

```bash
python manage.py shell < seed.py
```

### 6. Run server

```bash
python manage.py runserver
```

Your app will be available at:
👉 [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

---

## 🌍 Deployed Version

👉 [BON Rewards API (Render)](https://your-render-app-url.com/api/)

---

## 📂 API Endpoints

| Endpoint                   | Method | Description                        |
| -------------------------- | ------ | ---------------------------------- |
| `/api/users/`              | GET    | List all users                     |
| `/api/bills/`              | GET    | List all bills                     |
| `/api/rewards/`            | GET    | List all rewards                   |
| `/api/pay-bill/<bill_id>/` | POST   | Pay a bill (triggers reward logic) |
