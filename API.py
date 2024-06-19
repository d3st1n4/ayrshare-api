import requests

GOOGLE_FONTS_API_URL = "https://www.googleapis.com/webfonts/v1/webfonts?"
API_KEY = "AIzaSyBE-k18H7iIsFdq5U7O2bX1tCTAFRjkEUc"

response = requests.get(GOOGLE_FONTS_API_URL, params={"key": API_KEY})
fonts_data = response.json()

for font in fonts_data["items"]:
  family_name = font["family"]
  subsets = font["subsets"]
  font_version = font["version"]

  print(f"Font family: {family_name}")
  print(f"Font subsets: {subsets}")
  print(f"Font version: {", ".join(variants)}\n")



