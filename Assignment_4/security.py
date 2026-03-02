import re

def hide_phone_numbers(text):
    # Replace 10-digit numbers
    text = re.sub(r'\b\d{10}\b', '[REDACTED]', text)
    
    # Replace numbers starting with +84 followed by digits
    text = re.sub(r'\+84\d+', '[REDACTED]', text)
    
    return text
text = input("Please type your phone number: +84")
print(hide_phone_numbers(text)) 