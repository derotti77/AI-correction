#!/bin/bash

# KI-Korrektur App Starter
cd "$(dirname "$0")"

# Prüfe ob Python 3 verfügbar ist
if ! command -v python3 &> /dev/null; then
    osascript -e 'display dialog "Python 3 ist nicht installiert!" with title "KI-Korrektur" buttons {"OK"} default button "OK"'
    exit 1
fi

# Prüfe ob Ollama läuft
if ! curl -s http://localhost:11434/api/generate &> /dev/null; then
    osascript -e 'display dialog "Ollama ist nicht gestartet!\n\nBitte starte erst Ollama:\nollama serve" with title "KI-Korrektur" buttons {"OK"} default button "OK"'
    exit 1
fi

# Starte die App
python3 ki-korrektur.py
