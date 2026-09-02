# 🤖 Personal AI Assistant

An AI-powered personal assistant built with **n8n** and **Google Gemini** that helps manage **Gmail, Google Calendar, and personal finances** using natural-language commands.

## ✨ Features

### 📧 Gmail
- Get a single email
- Get multiple emails
- Send emails

### 📅 Google Calendar
- Get calendar events
- Create calendar events
- Get calendar information

### 💰 Finance Tracking
Uses **Google Sheets** to manage financial records.

- Add expenses
- Read financial records
- Perform calculations on financial data

## 🧠 AI Agent

The assistant uses **Google Gemini** as the AI model.

The AI Agent understands the user's request and selects the appropriate tool to perform the requested task.

```text
                        User
                          │
                          ▼
                      Webhook
                          │
                          ▼
                    ┌───────────┐
                    │ AI Agent  │
                    │  Gemini   │
                    └─────┬─────┘
                          │
             ┌────────────┼────────────┐
             │            │            │
             ▼            ▼            ▼
           Gmail       Calendar      Finance
             │            │            │
             ▼            ▼            ▼
           Gmail       Google       Google
                       Calendar      Sheets