# 🧠 MindCare — AI-Powered Mental Health Prediction System

A comprehensive system designed to analyze textual input and predict mental health states (**Normal, Anxiety, Depression, Suicidal**) using a fine-tuned Deep Learning Transformer model.

## 🌐 Live Demo

| Service | URL |
|---------|-----|
| 🔵 **Frontend (Vercel)** | [https://mindcare1-self.vercel.app](https://mindcare1-self.vercel.app) |
| 🟣 **Backend API (Render)** | [https://mindcare-api-f5dg.onrender.com](https://mindcare-api-f5dg.onrender.com) |
| 📖 **API Docs (Swagger)** | [https://mindcare-api-f5dg.onrender.com/docs](https://mindcare-api-f5dg.onrender.com/docs) |

> ⚠️ The backend is hosted on Render's free tier and may take ~30 seconds to respond after a period of inactivity (cold start). Please be patient on the first request.

---

## ✨ Features

- **Transformer NLP Engine:** Uses PyTorch and Hugging Face Transformers for state-of-the-art text classification.
- **FastAPI Backend:** High-performance, async REST API.
- **React + Tailwind Frontend:** Modern, clean, and empathetic UI design.
- **JWT Authentication:** Secure user registration and login.
- **Prediction History:** Dashboard showing past analyses and statistics.
- **Dockerized Setup:** Simple one-command local deployment.
- **Safety First:** Immediate emergency alerts and helpline display for critical predictions.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 18, Vite, Tailwind CSS, Framer Motion |
| Backend | FastAPI, Python 3.10, Uvicorn |
| ML Model | PyTorch, Hugging Face Transformers (DistilBERT) |
| Auth | JWT (python-jose), Passlib |
| Database | MongoDB (Motor async driver) |
| Deployment | Vercel (frontend) + Render (backend) |

---

## 🚀 Local Setup & Deployment

### Prerequisites
- Docker & Docker Compose
- Node.js 20+ (for local frontend dev)
- Python 3.10+ (for local backend dev)

### Running with Docker (Recommended)
1. Ensure Docker is running.
2. From the root directory, run:
   ```bash
   docker-compose up --build
   ```
3. Access the application:
   - Frontend: `http://localhost:5173`
   - Backend API Docs: `http://localhost:8000/docs`

### Running Locally (without Docker)

**Backend:**
```bash
cd backend
pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

---

## ☁️ Cloud Deployment

This project is deployed using:
- **Frontend → [Vercel](https://vercel.com):** Auto-deploys on every push to `main`
- **Backend → [Render](https://render.com):** Docker-based deployment, auto-deploys on every push to `main`

### Environment Variables

**Vercel (Frontend):**
| Variable | Value |
|----------|-------|
| `VITE_API_URL` | `https://mindcare-api-f5dg.onrender.com/api` |

**Render (Backend):**
| Variable | Value |
|----------|-------|
| `SECRET_KEY` | Your secret key (auto-generated) |

---

## 🤖 Model Training Pipeline

To retrain the model on new data:
1. `cd ml-pipeline`
2. `pip install -r requirements.txt`
3. `python model_training.py --train`

*(Note: Requires significant compute/GPU for full training.)*

---

## ⚠️ Ethical Disclaimer

This system is provided for **educational and research purposes only**. It is **not** a substitute for professional medical diagnosis, advice, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

**If you are in crisis, please contact emergency services or a mental health helpline immediately.**
