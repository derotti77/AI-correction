#!/bin/bash

# KI-Korrektur Installation Script
# Installiert die macOS App automatisch

echo "🤖 KI-Korrektur Installation"
echo "=============================="
echo

# Prüfe ob macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "❌ Fehler: Diese App funktioniert nur auf macOS"
    exit 1
fi

# Prüfe ob Ollama installiert ist
if ! command -v ollama &> /dev/null; then
    echo "⚠️  Ollama ist nicht installiert."
    echo "   Installiere Ollama mit: brew install ollama"
    echo "   Oder von: https://ollama.ai/"
    exit 1
fi

echo "✅ Ollama gefunden"

# Prüfe ob Ollama läuft
if ! curl -s http://localhost:11434/api/generate &> /dev/null; then
    echo "⚠️  Ollama läuft nicht."
    echo "   Starte Ollama mit: ollama serve"
    echo "   (In einem separaten Terminal)"
fi

# Prüfe ob Mistral Model verfügbar ist
if ! ollama list | grep -q mistral; then
    echo "⚠️  Mistral Model nicht gefunden."
    echo "   Lade das Model mit: ollama pull mistral"
fi

echo "📦 Installiere KI-Korrektur App..."

# Erstelle App Struktur
mkdir -p "/Applications/KI-Korrektur.app/Contents/MacOS"
mkdir -p "/Applications/KI-Korrektur.app/Contents/Resources"

# Kopiere Dateien
cp KI-Korrektur.app/Contents/Info.plist "/Applications/KI-Korrektur.app/Contents/"
cp KI-Korrektur.app/Contents/MacOS/KI-Korrektur "/Applications/KI-Korrektur.app/Contents/MacOS/"
cp KI-Korrektur.app/Contents/Resources/ki-korrektur-fast.sh "/Applications/KI-Korrektur.app/Contents/Resources/"

# Setze Berechtigungen
chmod +x "/Applications/KI-Korrektur.app/Contents/MacOS/KI-Korrektur"
chmod +x "/Applications/KI-Korrektur.app/Contents/Resources/ki-korrektur-fast.sh"

echo "✅ KI-Korrektur erfolgreich installiert!"
echo
echo "🎯 Verwendung:"
echo "1. Text kopieren (⌘C)"
echo "2. KI-Korrektur App starten (Doppelklick)"
echo "3. Korrigierter Text wird automatisch eingefügt!"
echo
echo "📍 Die App findest du im Applications Ordner"
echo
echo "🔧 Vergiss nicht:"
echo "   - Ollama starten: ollama serve"
echo "   - Mistral laden: ollama pull mistral"
echo
echo "🎉 Viel Spaß mit der KI-Korrektur!"
