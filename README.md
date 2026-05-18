# AI-Powered Mental Health Prediction System

A comprehensive system designed to analyze textual input and predict mental health states (Normal, Anxiety, Depression, Suicidal) using a fine-tuned Deep Learning Transformer model.

## Features
- **Transformer NLP Engine:** Uses PyTorch and Hugging Face Transformers for state-of-the-art text classification.
- **FastAPI Backend:** High-performance, async backend.
- **React + Tailwind Frontend:** Modern, clean, and empathetic UI design.
- **MongoDB:** Stores prediction histories and user data securely.
- **Dockerized Setup:** Simple one-command deployment.
- **Safety First:** Immediate emergency alerts and helpline display for critical predictions.

## Setup & Deployment

### Prerequisites
- Docker & Docker Compose
- Node.js (for local frontend dev)
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

### Model Training Pipeline
To retrain the model on new data:
1. `cd ml-pipeline`
2. `pip install -r requirements.txt`
3. `python model_training.py --train`
*(Note: Requires significant compute/GPU for full training).*

## Ethical Disclaimer
This system is provided for educational and research purposes. It is **not** a substitute for professional medical diagnosis, advice, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.
