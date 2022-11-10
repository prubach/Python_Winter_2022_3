from email_check import *

def check_email(email):
    if not email:
        return False
    email_text_array = email.split('.')
    email_text_array_length = len(email_text_array)
    if email_text_array_length < 4:
        return False
    symbol_count = 0
    for text in email_text_array:
        if '@' in text.strip('@'):
            symbol_count += 1
    return symbol_count == 1


for em in [email1, email2, email3, email4, email5, email6]:
    print(check_email(em))