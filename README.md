# SSH Log Analyzer

Prosty skrypt napisany w Bashu, stworzony w ramach nauki automatyzacji zadań w dziale SOC (Blue Team). 

## Co robi ten skrypt?
Skrypt przeszukuje logi systemowe Linuxa (`/var/log/auth.log` lub pliki testowe) pod kątem nieudanych prób logowania po protokole SSH. 
Wykorzystuje potoki (pipes) oraz narzędzia systemowe takie jak `grep`, `awk`, `sort` i `uniq`, aby wyciągnąć i zliczyć adresy IP potencjalnych atakujących (Brute Force).

## Jak uruchomić?
1. Nadaj uprawnienia do wykonywania: `chmod +x analizator.sh`
2. Uruchom skrypt: `./analizator.sh`