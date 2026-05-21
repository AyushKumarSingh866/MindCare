import pandas as pd
import numpy as np
from datasets import load_dataset, Dataset
import re

def clean_text(text):
    """Clean the input text."""
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#','', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def create_synthetic_dataset():
    """
    Creates a synthetic dataset for demonstration and initial pipeline setup.
    In a real scenario, this would load real datasets (Reddit, GoEmotions, etc.)
    and map them to our 4 categories.
    """
    print("Generating synthetic dataset for initial pipeline testing...")
    
    data = {
        'text': [
            "I feel completely fine today, just a normal day.",
            "I'm so worried about my upcoming exams, my heart is racing.",
            "I feel so empty and sad all the time. Nothing brings me joy anymore.",
            "I can't take this anymore, I want to end it all.",
            "Everything is going great, I had a lovely walk.",
            "I'm constantly overthinking and feeling stressed about everything.",
            "I don't have the energy to get out of bed. I feel worthless.",
            "There is no point in living, I just want to die.",
            "Had a good lunch with friends.",
            "I'm terrified of social situations, I get panic attacks.",
            "Life is just a meaningless void.",
            "Please help me, I have pills and I'm thinking about taking them all."
        ],
        'label': [
            0, # Normal
            1, # Anxiety
            2, # Depression
            3, # Suicidal
            0,
            1,
            2,
            3,
            0,
            1,
            2,
            3
        ]
    }
    
    # Let's multiply this dataset to have enough samples for training loop to run without errors
    df = pd.DataFrame(data)
    df = pd.concat([df] * 50, ignore_index=True) # 600 samples
    
    # Shuffle
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    df['text'] = df['text'].apply(clean_text)
    
    return Dataset.from_pandas(df)

def get_processed_dataset():
    """Returns a split huggingface DatasetDict"""
    dataset = create_synthetic_dataset()
    # Split into train and test
    dataset = dataset.train_test_split(test_size=0.2, seed=42)
    return dataset

if __name__ == "__main__":
    ds = get_processed_dataset()
    print("Dataset created successfully.")
    print(f"Train size: {len(ds['train'])}")
    print(f"Test size: {len(ds['test'])}")
