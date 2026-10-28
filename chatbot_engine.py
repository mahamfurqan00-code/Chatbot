"""Rule-based hospital FAQ chatbot adapted from the original notebook."""
import re
from difflib import SequenceMatcher

FAQ = {
    "hello": "Hi! Welcome to ABC General Hospital. How can I help you?",
    "what is your name": "I'm the ABC General Hospital FAQ Assistant.",
    "how are you": "I'm doing well, thank you. How can I help you today?",
    "what is the name of the hospital": (
        "Welcome to ABC General Hospital. We aim to provide high-quality healthcare "
        "services with experienced doctors, modern facilities, and compassionate care."
    ),
    "where is the hospital located": (
        "The sample hospital is listed at Main Boulevard, Lahore, Pakistan. "
        "Please verify the address with the hospital before travelling."
    ),
    "what are your working hours": (
        "The sample FAQ lists outpatient services from 8:00 AM to 8:00 PM, "
        "Monday to Saturday. Emergency services are listed as available 24/7. "
        "Please confirm current hours with the hospital."
    ),
    "is the hospital open 24/7": (
        "The sample FAQ says the Emergency Department operates 24 hours a day. "
        "Please contact the hospital to confirm current arrangements."
    ),
    "how can i contact the hospital": (
        "The original sample FAQ lists +92-42-12345678 and info@abchospital.com. "
        "These are demonstration details; verify the real contact information before use."
    ),
    "do you provide ambulance services": (
        "The sample FAQ says ambulance services are available 24/7. "
        "For a real emergency, contact your local emergency service immediately."
    ),
    "how do i book an appointment": (
        "You can ask the hospital reception about appointment booking by phone, "
        "through its official website, or in person."
    ),
    "can i book an appointment online": (
        "Online booking depends on the hospital's actual services. Please check its "
        "official website or contact reception."
    ),
    "can i cancel or reschedule my appointment": (
        "Please contact the hospital reception or use its official appointment portal "
        "to ask about cancellation or rescheduling."
    ),
    "what documents should i bring for my appointment": (
        "Commonly useful items include identification, previous medical records, "
        "current prescriptions, insurance details if applicable, and appointment confirmation. "
        "Confirm the requirements with the hospital."
    ),
    "which doctors are available today": (
        "Doctor availability changes. Please contact reception or consult the hospital's "
        "official schedule for current availability."
    ),
    "do you have specialist doctors": (
        "The sample FAQ mentions specialties such as cardiology, dermatology, pediatrics, "
        "gynecology, orthopedics, neurology, ENT, ophthalmology, and dentistry. "
        "Confirm the currently available specialties with the hospital."
    ),
    "how long is the waiting time": (
        "Waiting times depend on the doctor's schedule and patient volume. Contact reception "
        "for an estimate and consider arriving a little before your appointment."
    ),
    "do you have a laboratory": (
        "The sample FAQ describes laboratory services such as blood and urine testing. "
        "Confirm available tests and opening hours with the hospital."
    ),
    "how long does it take to receive laboratory test results": (
        "Turnaround time depends on the test. The sample FAQ says many routine results may "
        "be available within 24 hours, but please confirm timing with the laboratory."
    ),
    "do you have a pharmacy": (
        "The sample FAQ describes an in-house pharmacy. Please verify its availability and "
        "opening hours with the hospital."
    ),
    "do you accept health insurance": (
        "Insurance acceptance depends on the provider and plan. Contact the hospital billing "
        "department to confirm coverage before your visit."
    ),
    "what payment methods do you accept": (
        "Payment methods vary. Contact the hospital billing department to confirm accepted "
        "cash, card, bank transfer, or digital payment options."
    ),
    "what should i do in a medical emergency": (
        "If someone may be in immediate danger, contact local emergency services or go to "
        "the nearest emergency department now. This FAQ bot cannot assess emergencies."
    ),
    "how can i provide feedback about the hospital": (
        "You can ask reception about the patient feedback form, or contact the hospital's "
        "official customer-service team."
    ),
    "bye": "Thank you for visiting ABC General Hospital FAQ Assistant. Take care!",
}

THRESHOLD = 0.60
FALLBACK = (
    "Sorry, I couldn't find a reliable answer to that question. Please contact the "
    "hospital reception for accurate information."
)

def normalize_text(text):
    """Lowercase text, remove punctuation, and collapse repeated whitespace."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)
    return re.sub(r"\s+", " ", text)

def find_best_match(user_question, faq=FAQ):
    normalized_input = normalize_text(user_question)
    if not normalized_input:
        return None, 0.0

    best_key, best_score = None, 0.0
    for question in faq:
        normalized_question = normalize_text(question)
        if normalized_question == normalized_input:
            return question, 1.0
        if normalized_question in normalized_input or normalized_input in normalized_question:
            # Avoid treating tiny inputs such as "a" as a high-confidence match.
            if len(normalized_input) >= 4:
                return question, 1.0
        score = SequenceMatcher(None, normalized_input, normalized_question).ratio()
        if score > best_score:
            best_key, best_score = question, score
    return best_key, best_score

def get_answer(user_input, faq=FAQ):
    key, score = find_best_match(user_input, faq)
    if key is not None and score >= THRESHOLD:
        return faq[key], key, score
    return FALLBACK, None, score

def suggested_questions():
    return [
        "Where is the hospital located?",
        "What are your working hours?",
        "How do I book an appointment?",
        "What should I do in a medical emergency?",
    ]
