<div align="center">

<img src="https://img.shields.io/badge/Folio-Library%20Management%20System-4a6fa5?style=for-the-badge&logo=bookstack&logoColor=white" alt="Folio" />

# 📚 Folio — Library Store Management System

**A full-stack digital library platform for browsing, managing, and ordering books — built with FastAPI, vanilla JS, and a relational database backend.**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Node.js](https://img.shields.io/badge/Node.js-Frontend%20Dev-339933?style=flat-square&logo=nodedotjs&logoColor=white)](https://nodejs.org)
[![JWT](https://img.shields.io/badge/Auth-JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white)](https://jwt.io)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)

[Features](#-features) • [Architecture](#-architecture) • [Getting Started](#-getting-started) • [API Docs](#-api-documentation) • [Screenshots](#-screenshots) • [Contributing](#-contributing)

---

</div>

## 🌟 Overview

**Folio** is a production-style Library Store Management System that demonstrates end-to-end full-stack development — from a RESTful FastAPI backend with JWT-secured endpoints to a dynamic, multi-page vanilla JavaScript frontend. The project simulates a real-world digital bookstore with role-based access control, book search, cart management, order processing, and an admin dashboard.

> Built as a Database Management Systems project, Folio goes beyond academia — featuring real authentication flows, a proxied dev server, live-reload infrastructure, and a multi-role admin hierarchy.

---

## ✨ Features

### 👤 Customer-Facing
- 🔍 **Smart Book Search** — Search by title, author, or genre with real-time results
- 📖 **Detailed Book Pages** — Rich book detail views with animated spine-color theming
- 🛒 **Shopping Cart** — Add/remove books with persistent session management
- 📦 **Order Management** — Place and track orders with full history
- 🔐 **Auth System** — Secure register/login with JWT tokens

### 🛠️ Admin Panel
- 📊 **Admin Dashboard** — Overview of inventory, orders, and users
- 📝 **Book Management** — Add, edit, delete books from the catalog
- 👥 **User Management** — View and manage registered users
- 📋 **Order Processing** — Review and update order statuses
- 💡 **AI Suggestions** — Admin suggestions panel for smart catalog curation
- 🔑 **Super Admin Controls** — Elevated privileges with separate seeding and init scripts

### ⚙️ Technical Highlights
- ⚡ **FastAPI Backend** — Async Python API running on `http://127.0.0.1:7000`
- 🔄 **Live Dev Proxy** — Node.js dev server proxying `/api/*` to FastAPI
- 🧬 **JWT Authentication** — Stateless, secure token-based sessions
- 🗃️ **Relational Database** — Full DBMS integration with structured schemas
- 📡 **RESTful API Design** — Clean endpoint structure with proper HTTP semantics

---

## 🏗️ Architecture

```
Library-Store-DBMS_proj/
│
├── backend/                    # FastAPI Python backend
│   ├── src/
│   │   └── search_books/       # Book search module
│   │       ├── by_author_or_name.py
│   │       └── __init__.py
│   ├── app.py                  # Main FastAPI application entry
│   ├── demo.py
│   ├── init_super_admin.py     # Super admin seeding script
│   ├── seed_admin.py           # Admin seeding utility
│   ├── router.py               # API route definitions
│   ├── requirements.txt        # Python dependencies
│   ├── venv/                   # Python virtual environment
│   └── .env                    # Environment config (not committed)
│
├── frontend/                   # Vanilla JS + HTML/CSS frontend
│   ├── css/                    # Stylesheets
│   ├── js/                     # JavaScript modules
│   │   ├── api.js
│   │   ├── admin.js
│   │   └── search.js
│   ├── index.html              # Landing page
│   ├── search.html             # Book search & browse
│   ├── book_details.html       # Individual book view
│   ├── cart.html               # Shopping cart
│   ├── order.html / orders.html
│   ├── login.html / register.html
│   ├── admin.html              # Admin dashboard
│   ├── admin_suggestions.html
│   ├── super_admin.html
│   ├── support.html / support_dashboard.html
│   ├── reviews.html
│   ├── server.js               # Node dev server with API proxy
│   ├── package.json
│   └── node_modules/
│
└── README.md
```

### System Design

```
┌─────────────────────────────────────────────────────┐
│                   Browser (Client)                   │
│          Vanilla JS · HTML · CSS                     │
└─────────────────────┬───────────────────────────────┘
                      │ HTTP requests
                      ▼
┌─────────────────────────────────────────────────────┐
│           Node.js Dev Server (:5000)                 │
│     Serves static files + proxies /api/* → :7000    │
└─────────────────────┬───────────────────────────────┘
                      │ proxied API calls
                      ▼
┌─────────────────────────────────────────────────────┐
│           FastAPI Backend (:7000)                    │
│   Routes · Auth (JWT) · Business Logic · ORM        │
└─────────────────────┬───────────────────────────────┘
                      │ SQL queries
                      ▼
┌─────────────────────────────────────────────────────┐
│           Relational Database (DBMS)                 │
│     Books · Users · Orders · Cart · Reviews         │
└─────────────────────────────────────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

| Tool | Version |
|------|---------|
| Python | 3.11+ |
| Node.js | 18+ |
| npm | 9+ |
| Git | any |

---

### 1. Clone the Repository

```bash
git clone https://github.com/Debtanu2005/Library-store-DBMS_proj.git
cd Library-store-DBMS_proj
```

---

### 2. Backend Setup

```bash
cd backend

# Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file in the `backend/` directory:

```env
SECRET_KEY=your_super_secret_key_here_min_32_chars
DATABASE_URL=sqlite:///./library.db    # or your DB connection string
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> ⚠️ **Note:** The HMAC secret key must be at least 32 bytes long for security.

Seed initial admin users:

```bash
# Seed a regular admin
python seed_admin.py

# Initialize a super admin
python init_super_admin.py
```

Start the backend:

```bash
uvicorn app:app --host 0.0.0.0 --port 7000 --reload
```

The API will be live at **`http://127.0.0.1:7000`**

---

### 3. Frontend Setup

```bash
cd ../frontend

# Install dependencies
npm install

# Start the dev server
npm run dev
```

The frontend will be available at **`http://localhost:5000`**

The Node server proxies all `/api/*` requests to the FastAPI backend automatically.

---

### 4. Access the App

| URL | Description |
|-----|-------------|
| `http://localhost:5000` | Customer-facing storefront |
| `http://localhost:5000/admin.html` | Admin dashboard |
| `http://localhost:5000/super_admin.html` | Super admin panel |
| `http://127.0.0.1:7000/docs` | FastAPI interactive API docs (Swagger UI) |
| `http://127.0.0.1:7000/redoc` | ReDoc API documentation |

---

## 📡 API Documentation

FastAPI auto-generates interactive documentation available at `/docs` when the backend is running.

### Key Endpoint Groups

| Prefix | Description |
|--------|-------------|
| `/api/auth` | Register, login, token refresh |
| `/api/books` | Browse, search, get book details |
| `/api/cart` | Add, remove, view cart items |
| `/api/orders` | Place and track orders |
| `/api/admin` | Admin CRUD for books, users, orders |
| `/api/reviews` | Book reviews and ratings |

### Authentication

All protected routes require a JWT Bearer token in the `Authorization` header:

```http
Authorization: Bearer <your_jwt_token>
```

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend Framework** | FastAPI (Python) |
| **Authentication** | JWT (via `python-jose`) |
| **Frontend** | Vanilla JavaScript, HTML5, CSS3 |
| **Dev Server** | Node.js + HPM Proxy Middleware |
| **Database** | Relational DBMS (SQL) |
| **Package Management** | pip (backend), npm (frontend) |
| **Hot Reload** | Uvicorn + StatReload (backend), npm dev (frontend) |

---

## 🗺️ Roadmap

- [ ] PostgreSQL migration with Alembic migrations
- [ ] User review & rating system (UI)
- [ ] Email notifications for order status
- [ ] Dockerized deployment (`docker-compose.yml`)
- [ ] Unit & integration tests (pytest + httpx)
- [ ] Pagination and advanced search filters
- [ ] Wishlist feature

---

## 🤝 Contributing

Contributions are welcome! Here's how to get involved:

<!-- 1. **Fork** the repository
2. **Create** your feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request -->

Please make sure your code is clean, documented, and tested before submitting.

---

## 👨‍💻 Author

**Debtanu Das**

[![GitHub](https://img.shields.io/badge/GitHub-Debtanu2005-181717?style=flat-square&logo=github)](https://github.com/Debtanu2005)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ by Debtanu Das · © 2026 Folio · All rights reserved

*"A reader lives a thousand lives before he dies."*

</div>