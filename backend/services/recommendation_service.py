def get_recommendations(predicted_class: str, is_emergency: bool = False):
    recommendations = []
    
    if predicted_class == "Normal":
        recommendations = [
            "Maintain your healthy routine.",
            "Continue engaging in activities you enjoy.",
            "Practice daily gratitude to maintain a positive mindset.",
            "Keep up with regular exercise and a balanced diet."
        ]
    elif predicted_class == "Anxiety":
        recommendations = [
            "Try the 4-7-8 breathing exercise: Inhale for 4s, hold for 7s, exhale for 8s.",
            "Limit caffeine and sugar intake.",
            "Practice mindfulness or guided meditation for 10 minutes.",
            "Consider writing down your worries in a journal to get them out of your head.",
            "Engage in light physical activity like a walk or yoga."
        ]
    elif predicted_class == "Depression":
        recommendations = [
            "Reach out to a close friend or family member, even just for a chat.",
            "Try to accomplish one small task today (e.g., making your bed).",
            "Spend at least 15 minutes outside in the sunlight.",
            "Consider seeking support from a professional therapist or counselor.",
            "Be kind to yourself and avoid self-criticism."
        ]
    elif predicted_class == "Suicidal":
        recommendations = [
            "PLEASE REACH OUT FOR HELP IMMEDIATELY. You are not alone.",
            "Call the National Suicide Prevention Lifeline at 988 (US) or your local emergency number.",
            "Text HOME to 741741 to connect with a Crisis Counselor 24/7.",
            "Go to the nearest hospital emergency room.",
            "Contact a trusted friend, family member, or healthcare professional right now."
        ]
    
    return recommendations
