#!/bin/bash

# KI-Korrektur Daemon Starter
cd "$(dirname "$0")"

echo "🤖 Starte KI-Korrektur Daemon..."
echo "Tastenkürzel: Cmd+Shift+K"
echo "Beenden: Strg+C"

# Prüfe ob Ollama läuft
if ! curl -s http://localhost:11434/api/generate &> /dev/null; then
    echo "❌ Ollama ist nicht gestartet!"
    echo "Bitte starte erst: ollama serve"
    read -p "Drücke Enter zum Beenden..."
    exit 1
fi

# Starte Daemon
python3 ki-korrektur-daemon.py
