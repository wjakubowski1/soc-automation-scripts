# SOC Automation & Security Scripts

Witaj w moim repozytorium! Jest to zbiór skryptów i narzędzi, które tworze i dodaje w ramach zapisywania podstaw automatyzacji zadań dla działu SOC (Security Operations Center) oraz Blue Teamu. 

## Struktura projektów:

* **`/bash-log-analyzer`** - Skrypt w systemie Linux (Bash), który automatycznie parsuje logi systemowe (`auth.log`) i wyciąga adresy IP atakujących metodą Brute Force po protokole SSH.
* **`/python-vt-checker`** - Skrypt w Pythonie integrujący się z API VirusTotal. Sprawdza wytypowane adresy IP pod kątem ich reputacji i flaguje potencjalne zagrożenia.

## Technologie i narzędzia:
* Bash (grep, awk, sort, uniq)
* Python 3 (requests, venv, obsługa API)
* Git / GitHub
* Linux Ubuntu