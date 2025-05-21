# TaxApp 1099 Portal

This is a TurboTax-style full-stack application built with:

- ✅ **FastAPI** (Python) backend
- ✅ **React + TypeScript + Tailwind CSS** frontend
- ✅ **PostgreSQL** or SQLite DB
- ✅ **JWT-based authentication**
- ✅ **Email confirmation with PDF attachment** (via SendGrid)
- ✅ **Render.com deployment ready**

## 🔧 Features

- Login, register, and forgot password flows
- Submit 1099-NEC forms
- PDF confirmation sent to email
- HashRouter support (`/#/login`, `/#/form`, etc.)
- Easily styled using Tailwind

## 🛠 Setup Instructions

1. Clone this repo

```bash
git clone https://github.com/keshavcpa01/taxapp-1099.git
cd taxapp-1099
```

2. Set up your environment variables on [Render.com](https://render.com):

- `SECRET_KEY`
- `SENDGRID_API_KEY`
- `DATABASE_URL`
- `REACT_APP_API_BASE_URL` (for frontend)

3. Backend setup (local dev):

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

4. Frontend setup:

```bash
cd frontend
npm install
npm run dev  # or npm run build for production
```

## 🚀 Deployment

Auto-deploy with [Render.com](https://render.com) using the `render.yaml` blueprint:

- Navigate to Render → New Blueprint → Connect this repo
- Set up environment variables
- Deploy both services

Enjoy your hosted 1099 submission app! 🎉
