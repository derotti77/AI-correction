#!/bin/bash

# Git Repository Setup für KI-Korrektur
# Bereitet das Projekt für GitHub vor

echo "🚀 KI-Korrektur GitHub Setup"
echo "============================="
echo

# Prüfe ob Git installiert ist
if ! command -v git &> /dev/null; then
    echo "❌ Git ist nicht installiert!"
    echo "   Installiere Git mit: brew install git"
    exit 1
fi

echo "✅ Git gefunden"

# Initialisiere Git Repository (falls noch nicht vorhanden)
if [ ! -d ".git" ]; then
    echo "📦 Initialisiere Git Repository..."
    git init
else
    echo "✅ Git Repository bereits vorhanden"
fi

# Füge alle Dateien hinzu
echo "📁 Füge Dateien hinzu..."
git add .

# Erstelle ersten Commit
echo "💾 Erstelle Initial Commit..."
git commit -m "feat: Initial commit - KI-Korrektur macOS App

- Automatische deutsche Textkorrektur mit Ollama
- Ein-Klick-Korrektur mit automatischem Einfügen
- Selbstbeendende macOS App
- Lokale KI mit Mistral Model
- Keine GUI, läuft im Hintergrund"

echo
echo "🎉 Repository ist bereit für GitHub!"
echo
echo "📝 Nächste Schritte:"
echo "1. Gehe zu https://github.com/new"
echo "2. Erstelle ein neues Repository namens 'ki-korrektur'"
echo "3. Führe diese Befehle aus:"
echo
echo "   git remote add origin https://github.com/DEIN-USERNAME/ki-korrektur.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo
echo "🔗 Ersetze 'DEIN-USERNAME' mit deinem GitHub Username"
echo
echo "✨ Danach ist dein Projekt auf GitHub verfügbar!"
echo
echo "📋 Repository-Features:"
echo "   - ✅ README.md mit vollständiger Dokumentation"
echo "   - ✅ MIT License"
echo "   - ✅ .gitignore für macOS"
echo "   - ✅ Contributing Guidelines"
echo "   - ✅ Installations-Skript"
echo "   - ✅ Saubere Projekt-Struktur"
echo
echo "🎯 Nach dem Upload kannst du:"
echo "   - Issues für Bug-Reports erstellen"
echo "   - Wiki für ausführliche Docs nutzen"
echo "   - Releases für Versionen erstellen"
echo "   - Andere Entwickler einladen"
echo
echo "Happy Coding! 🚀"
