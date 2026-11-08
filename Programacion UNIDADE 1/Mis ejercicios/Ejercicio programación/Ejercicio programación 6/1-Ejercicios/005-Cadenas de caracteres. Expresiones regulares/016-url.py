import re

url = "https://www.heverton.com"
nourl = "caca de la vaca"

patron = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$"

print(bool(re.fullmatch(patron, url)))    # True
print(bool(re.fullmatch(patron, nourl)))  # False