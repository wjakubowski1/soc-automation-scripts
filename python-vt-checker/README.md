# VirusTotal IP Checker

Prosty, ale skuteczny skrypt napisany w Pythonie, który automatyzuje pracę analityka SOC. Zamiast ręcznie wklejać podejrzane adresy IP na stronę VirusTotal, skrypt robi to za nas przez API.

## Funkcje:
* Bezpieczne zaczytywanie klucza API z ukrytego pliku `.env`.
* Łączenie się z API VirusTotal (wersja v3) przy użyciu biblioteki `requests`.
* Odkodowywanie odpowiedzi w formacie JSON.
* Wyświetlanie czytelnego werdyktu w terminalu (ile silników uznało adres za złośliwy).

## Jak uruchomić?
1. Sklonuj repozytorium.
2. Stwórz plik `.env` i dodaj w nim swój klucz: `VT_API_KEY=twój_klucz`
3. Stwórz i aktywuj wirtualne środowisko: `python3 -m venv venv` oraz `source venv/bin/activate`
4. Zainstaluj wymagania: `pip install requests`
5. Uruchom skrypt: `python3 vt_checker.py`