# Contributing zu KI-Korrektur

Vielen Dank für dein Interesse an der Mitarbeit! 🎉

## 🚀 Schnellstart für Entwickler

1. **Repository forken**
2. **Klonen**:
   ```bash
   git clone https://github.com/dein-username/ki-korrektur.git
   cd ki-korrektur
   ```
3. **Development Setup**:
   ```bash
   # Ollama installieren
   brew install ollama
   
   # Modell laden
   ollama pull mistral
   
   # Ollama starten
   ollama serve
   ```

## 📂 Projekt-Struktur

```
KI-Korrektur-App/
├── README.md                    # Haupt-Dokumentation
├── LICENSE                      # MIT License
├── install.sh                   # Installations-Skript
├── .gitignore                   # Git Ignore-Regeln
├── CONTRIBUTING.md              # Diese Datei
├── KI-Korrektur.app/           # macOS App Bundle
│   └── Contents/
│       ├── Info.plist          # App-Metadaten
│       ├── MacOS/
│       │   └── KI-Korrektur    # Haupt-Executable (Shell)
│       └── Resources/
│           └── ki-korrektur-fast.sh  # Korrektur-Logik
└── docs/                       # Zusätzliche Dokumentation
```

## 🛠 Entwicklung

### Lokales Testen

```bash
# Text in Zwischenablage kopieren
echo "Das ist einn testt" | pbcopy

# Skript direkt testen
./KI-Korrektur.app/Contents/Resources/ki-korrektur-fast.sh

# Oder App testen
open KI-Korrektur.app
```

### Code-Änderungen

- **Korrektur-Logik**: `KI-Korrektur.app/Contents/Resources/ki-korrektur-fast.sh`
- **App-Starter**: `KI-Korrektur.app/Contents/MacOS/KI-Korrektur`
- **App-Konfiguration**: `KI-Korrektur.app/Contents/Info.plist`

## 🎯 Beitrag-Bereiche

### 🐛 Bug Fixes
- Encoding-Probleme bei Sonderzeichen
- Ollama-Verbindungsfehler
- macOS-Kompatibilität

### ✨ Features
- Unterstützung für andere Sprachen
- Verschiedene LLM-Modelle
- Tastenkürzel-Integration
- GUI-Version

### 📚 Dokumentation
- Bessere README
- Video-Tutorials
- FAQ-Sektion

### 🧪 Tests
- Automatisierte Tests
- Edge-Case-Behandlung
- Performance-Tests

## 📝 Commit-Konventionen

Verwende aussagekräftige Commit-Messages:

```
feat: Neue Funktion hinzufügen
fix: Bug beheben
docs: Dokumentation aktualisieren
style: Code-Formatierung
refactor: Code umstrukturieren
test: Tests hinzufügen
chore: Build-Prozess oder Tools
```

Beispiele:
```bash
git commit -m "feat: Unterstützung für llama3.2 Model"
git commit -m "fix: Encoding-Problem bei Umlauten"
git commit -m "docs: Installation für Linux hinzufügen"
```

## 🔄 Pull Request Prozess

1. **Feature Branch erstellen**:
   ```bash
   git checkout -b feature/amazing-feature
   ```

2. **Änderungen committen**:
   ```bash
   git add .
   git commit -m "feat: Add amazing feature"
   ```

3. **Push und PR erstellen**:
   ```bash
   git push origin feature/amazing-feature
   ```

4. **Pull Request auf GitHub öffnen**

### PR Checkliste

- [ ] Code funktioniert lokal
- [ ] Dokumentation aktualisiert
- [ ] Commit-Messages sind aussagekräftig
- [ ] Keine unnötigen Dateien committed
- [ ] Issue-Referenz hinzugefügt (falls vorhanden)

## 🐛 Bug Reports

Verwende die GitHub Issue-Templates:

**Bug Report sollte enthalten:**
- macOS Version
- Ollama Version
- Schritte zur Reproduktion
- Erwartetes vs. tatsächliches Verhalten
- Screenshots/Logs falls relevant

## 💡 Feature Requests

**Feature Request sollte enthalten:**
- Problem-Beschreibung
- Vorgeschlagene Lösung
- Alternativen
- Use Cases

## 🤝 Code of Conduct

- Sei respektvoll und konstruktiv
- Hilf anderen beim Lernen
- Teile Wissen gerne
- Hab Spaß am Projekt! 🎉

## 🆘 Hilfe benötigt?

- **Issues**: Für Bugs und Feature-Requests
- **Discussions**: Für allgemeine Fragen
- **GitHub Wiki**: Für ausführliche Dokumentation

## 🙏 Danke!

Jeder Beitrag ist wertvoll - egal ob Code, Dokumentation, Bug-Reports oder Feature-Ideen!

**Happy Coding! 🚀**
