# 🤖 AI Text Corrector

**Simple macOS app for automatic German text correction using local AI**

![macOS](https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white)
![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-FF6B35?style=for-the-badge)
[![GitHub](https://img.shields.io/badge/GitHub-@derotti77-181717?style=for-the-badge&logo=github)](https://github.com/derotti77)
[![TikTok](https://img.shields.io/badge/TikTok-@derotti77-000000?style=for-the-badge&logo=tiktok)](https://tiktok.com/@derotti77)

## 🚀 Features

- ✅ **One-Click Correction**: Simply copy text, start app, done!
- ✅ **Automatic Insertion**: Corrected text gets inserted directly
- ✅ **Self-Terminating**: App closes automatically after correction
- ✅ **Local AI**: Works completely offline with Ollama
- ✅ **German Language**: Specialized for German spelling and grammar
- ✅ **No GUI**: Runs silently in background
- ✅ **Fast**: Correction in seconds

## 🎯 Workflow

```
Copy text → Start app → Text inserted → App terminates
    ⌘C        Click         ✨            💨
```

1. **Copy text** (⌘C)
2. **Start app** (Double-click "AI Text Corrector")
3. **Done!** - Corrected text gets automatically inserted
4. **App terminates itself**

## 📋 Prerequisites

- **macOS** (tested on macOS 12+)
- **[Ollama](https://ollama.ai/)** installed and running
- **Mistral Model** loaded

### Installing Prerequisites

```bash
# Install Ollama (if not already installed)
brew install ollama

# Start Ollama
ollama serve

# Load Mistral model (in new terminal)
ollama pull mistral
```

## 🔧 Installation

### Option 1: Direct Installation

1. Clone repository:
```bash
git clone https://github.com/derotti77/ai-text-corrector.git
cd ai-text-corrector
```

2. Install app:
```bash
./install.sh
```

### Option 2: Manual

1. Download and extract repository
2. Copy `AI-Text-Corrector.app` to `/Applications` folder
3. Make app executable:
```bash
chmod +x /Applications/AI-Text-Corrector.app/Contents/MacOS/AI-Text-Corrector
```

## 🎮 Usage

1. **Write text** with errors: "Das ist einn testt mit felern"
2. **Select and copy text** (⌘C)
3. **Start AI Text Corrector app** (Double-click)
4. **Automatically inserted**: "Das ist ein Test mit Fehlern"

## 🏢 Structure

```
AI-Text-Corrector.app/
├── Contents/
│   ├── Info.plist          # App configuration
│   ├── MacOS/
│   │   └── AI-Text-Corrector  # Main executable
│   └── Resources/
│       └── ai-text-corrector.sh  # Correction script
```

## ⚙️ Configuration

The correction script can be customized:

- **Change model**: In `ai-text-corrector.sh` change `model` from `mistral` to another Ollama model
- **Adapt prompt**: Modify the `SYSTEM_PROMPT` for other languages or behaviors

## 🐛 Troubleshooting

### App startet nicht
- Überprüfen ob Ollama läuft: `curl http://localhost:11434/api/generate`
- Permissions prüfen: `chmod +x /Applications/KI-Korrektur.app/Contents/MacOS/KI-Korrektur`

### Korrektur funktioniert nicht
- Mistral Model prüfen: `ollama list`
- Falls nicht vorhanden: `ollama pull mistral`

### Komische Zeichen im Output
- Das Skript filtert bereits die meisten Sonderzeichen
- Bei Problemen anderes Model probieren: `ollama pull llama3.2`

## 🤝 Contributing

Beiträge sind willkommen! 

1. Fork das Repository
2. Erstelle einen Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Committe deine Änderungen (`git commit -m 'Add some AmazingFeature'`)
4. Push den Branch (`git push origin feature/AmazingFeature`)
5. Öffne einen Pull Request

## 📝 License

Dieses Projekt steht unter der MIT License - siehe [LICENSE](LICENSE) Datei für Details.

## 🙏 Danksagungen

- [Ollama](https://ollama.ai/) für das großartige lokale LLM Framework
- [Mistral AI](https://mistral.ai/) für das Sprachmodell
- Alle Contributor zu diesem Projekt

## 📞 Support

Bei Fragen oder Problemen:
- Öffne ein [Issue](https://github.com/username/ki-korrektur/issues)
- Diskutiere in den [Discussions](https://github.com/username/ki-korrektur/discussions)

---

**Entwickelt mit ❤️ für die deutsche Sprache**
