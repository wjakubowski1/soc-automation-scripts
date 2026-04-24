#!/bin/bash

# Skrypt analizujący logi SSH i zliczający nieudane próby logowania.
# Zmienna przechowująca ścieżkę do pliku logów
LOG_FILE="auth_test.log"

echo "=========================================="
echo " RAPORT BEZPIECZEŃSTWA: NIEUDANE LOGOWANIA "
echo "=========================================="

# Sprawdzamy czy plik istnieje
if [ ! -f "$LOG_FILE" ]; then
    echo "Błąd: Nie znaleziono pliku $LOG_FILE"
    exit 1
fi

echo "Ilość prób | Adres IP Atakującego"
echo "------------------------------------------"

# Nasza magiczna komenda
cat "$LOG_FILE" | grep "Failed" | awk '{print $11}' | sort | uniq -c | sort -nr

echo "=========================================="
echo " Analiza zakończona."