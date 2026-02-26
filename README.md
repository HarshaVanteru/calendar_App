📅 Calendar Scheduler – Google SSO Based Multi-User Scheduling System

A full-stack calendar scheduling application that allows users to authenticate using Google Single Sign-On (SSO) and create/manage events directly in their Google Calendar.

This project demonstrates secure OAuth 2.0 authentication, token management, multi-user backend architecture, and Google Calendar API integration using FastAPI.

🚀 Features
🔐 Google SSO Authentication

OAuth 2.0 Authorization Code Flow

OpenID Connect identity verification

Secure state validation (CSRF protection)

Automatic user creation upon first login

👥 Multi-User Support

Each user logs in with their own Google account

Tokens stored separately per user

Isolated calendar access

🔑 Secure Token Handling

Stores:

Google access token

Google refresh token

Token expiry

Automatically refreshes expired access tokens

Uses JWT for application-level authentication

📆 Calendar Functionality

Create new calendar events

List upcoming events

Supports timezone handling

ISO 8601 datetime format compliance

🏗️ Architecture Overview
User (Browser)
    ↓
React Frontend
    ↓
FastAPI Backend
    ↓
Google OAuth Server
    ↓
Google Calendar API
🔄 Complete Workflow
1️⃣ Google SSO Login Flow

User clicks “Login with Google”

Backend generates:

Authorization URL

Secure random state

User is redirected to Google

User grants permission

Google redirects to /auth/google/callback

Backend:

Validates state

Exchanges authorization code for tokens

Stores tokens in database

Generates application JWT

User redirected to frontend dashboard

2️⃣ Event Creation Flow

Frontend sends:

POST /calendar/create

with JWT token

Backend:

Verifies JWT

Fetches user’s Google tokens

Builds Calendar API service

Inserts event into Google Calendar

Google stores event in user’s primary calendar

3️⃣ Upcoming Events Flow

Frontend calls:

GET /calendar/events

Backend:

Validates JWT

Fetches Google tokens

Calls Google Calendar API

Filters and formats events

Returns simplified event list

🛠️ Tech Stack
Backend

FastAPI

SQLAlchemy

SQLite

Google Auth OAuthlib

Google API Python Client

JWT Authentication

Passlib (bcrypt)

Frontend

React

Axios

LocalStorage (JWT storage)

📂 Project Structure
calendar_app/
│
├── app/
│   ├── auth/
│   │   ├── google.py
│   │   └── jwt.py
│   │
│   ├── calendar/
│   │   ├── routes.py
│   │   └── service.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── google_token.py
│   │
│   ├── utils/
│   │   └── dependencies.py
│   │
│   ├── database.py
│   ├── config.py
│   └── main.py
│
├── credentials.json
├── .env
└── README.md
🔐 Environment Variables (.env)
DATABASE_URL=sqlite:///./app.db
SECRET_KEY=your_jwt_secret
ALGORITHM=HS256
GOOGLE_REDIRECT_URI=http://localhost:8000/auth/google/callback
🔑 Google Cloud Setup

Create project in Google Cloud Console

Enable Google Calendar API

Configure OAuth Consent Screen

Create OAuth Client ID

Add redirect URI:

http://localhost:8000/auth/google/callback

Download credentials.json

📡 API Endpoints
🔐 Authentication
Start Google Login
GET /auth/google/login
Callback (Handled Automatically)
GET /auth/google/callback
📅 Calendar
Create Event
POST /calendar/create

Query Parameters:

title

start_time (ISO format)

end_time (ISO format)

Example:

2026-02-26T17:00:00
List Upcoming Events
GET /calendar/events

Returns:

[
  {
    "id": "event_id",
    "summary": "Meeting",
    "start": "2026-02-26T17:00:00+05:30"
  }
]
⏰ Time Handling

Uses timezone-aware datetime

ISO 8601 format

UTC-based comparisons

Supports Asia/Kolkata timezone

🔒 Security Measures

OAuth 2.0 Authorization Code Flow

State validation for CSRF protection

HTTP-only cookies for state storage

Secure token storage in backend only

JWT-based protected APIs

Refresh token support for long-term access

🧠 Key Concepts Implemented

OAuth 2.0 Client Registration

Authorization Code Flow

OpenID Connect

Token exchange mechanism

Access vs Refresh tokens

Multi-user backend design

External API integration

Secure session management

🧪 How to Run
1️⃣ Install dependencies
pip install -r requirements.txt
2️⃣ Run backend
uvicorn app.main:app --reload
3️⃣ Run frontend
npm run dev
🎯 What This Project Demonstrates

Real-world Google API integration

Secure authentication architecture

Production-ready OAuth handling

Multi-user backend logic

Proper separation of frontend and backend responsibilities

📌 Future Improvements

Event update and delete APIs

Recurring events support

Google Meet auto-link creation

Deployment with HTTPS

Production token encryption

Role-based access
