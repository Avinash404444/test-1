import re

text = """
Contact us at support@gmail.com or call 9876543210.
Visit https://www.srmist.edu.in for more information.
"""
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
phone_numbers = re.findall(r"\b\d{10}\b", text)
urls = re.findall(r"https?://[^\s]+", text)
print("Email Addresses:")
for email in emails:
    print(email)
print("\nPhone Numbers:")
for phone in phone_numbers:
    print(phone)
print("\nURLs:")
for url in urls:
    print(url)
