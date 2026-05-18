import os
# pyrefly: ignore [missing-import]
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_DIR = "../ml-pipeline/saved_model"
MODEL_NAME = "distilbert-base-uncased"

# Use CPU for backend inference to avoid GPU memory issues unless dedicated server
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class MentalHealthPredictor:
    def __init__(self):
        self.tokenizer = None
        self.model = None
        self.is_loaded = False
        self.id2label = {0: "Normal", 1: "Anxiety", 2: "Depression", 3: "Suicidal"}
        
        self.load_model()

    def load_model(self):
        try:
            print(f"Attempting to load model from {MODEL_DIR}...")
            # In a real deployed environment, the model weights would be present.
            # Here, we try to load them, but if they don't exist (because we skipped 3hr training),
            # we use a fallback mock mechanism to allow backend development.
            if os.path.exists(MODEL_DIR):
                self.tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
                self.model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)
                self.model.to(device)
                self.model.eval()
                self.is_loaded = True
                print("Model loaded successfully.")
            else:
                print(f"Warning: Model not found at {MODEL_DIR}. Using mock inference mode.")
                self.is_loaded = False
        except Exception as e:
            print(f"Error loading model: {str(e)}. Using mock inference mode.")
            self.is_loaded = False

    def predict(self, text: str):
        if not self.is_loaded:
            # Mock logic for demonstration/development
            return self._mock_predict(text)
            
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=128, padding=True)
        inputs = {k: v.to(device) for k, v in inputs.items()}
        
        with torch.no_grad():
            outputs = self.model(**inputs)
            
        logits = outputs.logits
        probabilities = torch.nn.functional.softmax(logits, dim=-1)[0].cpu().numpy()
        predicted_class_id = int(torch.argmax(logits, dim=-1)[0])
        
        predicted_class = self.id2label[predicted_class_id]
        confidence = float(probabilities[predicted_class_id])
        
        prob_dict = {self.id2label[i]: float(prob) for i, prob in enumerate(probabilities)}
        
        return predicted_class, confidence, prob_dict

    def _mock_predict(self, text: str):
        """A simple keyword-based mock for testing the backend UI flow without heavy ML models loaded."""
        text_lower = text.lower()
        if "kill" in text_lower or "die" in text_lower or "suicide" in text_lower or "end it" in text_lower:
            return "Suicidal", 0.95, {"Normal": 0.01, "Anxiety": 0.02, "Depression": 0.02, "Suicidal": 0.95}
        elif "sad" in text_lower or "depress" in text_lower or "empty" in text_lower or "worthless" in text_lower:
            return "Depression", 0.88, {"Normal": 0.05, "Anxiety": 0.07, "Depression": 0.88, "Suicidal": 0.00}
        elif "worry" in text_lower or "anxious" in text_lower or "panic" in text_lower or "scared" in text_lower:
            return "Anxiety", 0.85, {"Normal": 0.1, "Anxiety": 0.85, "Depression": 0.05, "Suicidal": 0.00}
        else:
            return "Normal", 0.90, {"Normal": 0.90, "Anxiety": 0.05, "Depression": 0.05, "Suicidal": 0.00}

predictor = MentalHealthPredictor()
