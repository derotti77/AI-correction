#!/bin/bash

# KI-Korrektur Schnellstart
# Liest, korrigiert und fügt Text ohne Benutzerinteraktion

# Text aus der Zwischenablage lesen
TEXT=$(pbpaste)

# Überprüfen, ob Text in der Zwischenablage ist
if [ -z "$TEXT" ]; then
    echo "❌ Kein Text in der Zwischenablage"
    exit 1
fi

# Korrektur mit Ollama
SYSTEM_PROMPT="Du bist ein Korrektor für deutsche Texte. Korrigiere nur die Rechtschreibung und Grammatik auf Deutsch. Gib nur den korrigierten Text zurück, keine Erklärungen oder Übersetzungen."
JSON_PAYLOAD=$(jq -n --arg model "mistral" --arg system "$SYSTEM_PROMPT" --arg prompt "$TEXT" '{model: $model, system: $system, prompt: $prompt, stream: false}')

# Anfrage an Ollama senden
RESPONSE=$(curl -s -X POST http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d "$JSON_PAYLOAD" | \
  jq -r '.response // empty')

# Sicherstellen, dass RESPONSE nicht leer ist
if [ -n "$RESPONSE" ] && [ "$RESPONSE" != "null" ]; then
    # Korrigierten Text in die Zwischenablage kopieren
    echo "$RESPONSE" | pbcopy
    
    # Den korrigierten Text automatisch einfügen
    osascript -e 'tell application "System Events" to keystroke "v" using command down'
    echo "✅ Text korrigiert und eingefügt!"
else
    echo "❌ Fehler bei der Korrektur"
    exit 1
fi
