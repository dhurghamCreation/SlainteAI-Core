import re

def clean_clinical_text(text):
    """Removes extra whitespace and non-standard characters from HSE PDFs."""
    # Remove multiple newlines
    text = re.sub(r'\n+', '\n', text)
    # Remove weird artifacts like page numbers or footer symbols
    text = re.sub(r'Page \d+ of \d+', '', text)
    return text.strip()

def format_priority(val):
    """Helper to convert 1/0 to 'High/Low' for reports."""
    return "High Priority" if val == 1 else "Low Priority"