import requests
import os

# Wczytywanie klucza z ukrytego pliku .env
# Jeśli z jakiegoś powodu nie zadziała, Python użyje "BRAK_KLUCZA"
API_KEY = os.popen('grep VT_API_KEY .env | cut -d "=" -f2').read().strip()

# Przykładowy adres IP który chcemy sprawdzić
IP_TO_CHECK = "8.8.8.8" 

print("==========================================")
print(f"Sprawdzanie IP: {IP_TO_CHECK} w bazie VirusTotal...")
print("==========================================")

# Przygotowujemy zapytanie do serwera
url = f"https://www.virustotal.com/api/v3/ip_addresses/{IP_TO_CHECK}"
headers = {
    "accept": "application/json",
    "x-apikey": API_KEY
}

# Zapytanie
response = requests.get(url, headers=headers)

# Jeśli serwer odpowiedział poprawnie
if response.status_code == 200:
    # Odkodowujemy odpowiedź
    data = response.json()
    stats = data['data']['attributes']['last_analysis_stats']
    
    malicious = stats['malicious'] # Ilość antywirusów, które uznały to za wirusa
    harmless = stats['harmless']   # Ilość antywirusów, które uznały to za bezpieczne
    
    print(f"Wynik skanowania: {malicious} silników uznało ten adres za złośliwy.")
    print(f"Bezpieczne według: {harmless} silników.")
    
    if malicious > 0:
        print("UWAGA! Ten adres IP jest potencjalnie niebezpieczny!")
    else:
        print("Adres wygląda na bezpieczny.")
else:
    print(f"Błąd połączenia! Kod statusu: {response.status_code}")