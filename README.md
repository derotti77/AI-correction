# 🤖 AI Text Corrector

**Simple macOS app for automatic text correction using local AI - Now with multilingual support!**

![macOS](https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Ollama](https://img.shields.io/badge/Ollama-FF6B35?style=for-the-badge)
[![GitHub](https://img.shields.io/badge/GitHub-@derotti77-181717?style=for-the-badge&logo=github)](https://github.com/derotti77)
[![TikTok](https://img.shields.io/badge/TikTok-@derotti77-FF0050?style=for-the-badge&logo=tiktok&logoColor=white)](https://tiktok.com/@derotti77)

## 🌐 Supported Languages

- 🇺🇸 **English** - Grammar and spelling correction
- 🇩🇪 **German** - Rechtschreibung und Grammatikkorrektur  
- 🇪🇸 **Spanish** - Corrección de ortografía y gramática
- 🇫🇷 **French** - Correction d'orthographe et de grammaire
- 🇮🇹 **Italian** - Correzione di ortografia e grammatica
- 🇵🇹 **Portuguese** - Correção de ortografia e gramática
- 🇳🇱 **Dutch** - Spelling- en grammaticacorrectie

## 🚀 Features

- ✅ **One-Click Correction**: Simply copy text, run app, done!
- ✅ **Automatic Insertion**: Corrected text gets inserted directly
- ✅ **Self-Terminating**: App closes automatically after correction
- ✅ **Local AI**: Works completely offline with Ollama
- ✅ **Multilingual**: Support for 7 languages
- ✅ **No GUI Required**: Runs silently in background
- ✅ **Raycast Integration**: Perfect for hotkey workflows
- ✅ **Fast**: Correction in seconds

## 🎯 Workflow

```
Copy text → Run corrector → Text automatically replaced
    ⌘C         🤖              ✨
```

1. **Copy text** (⌘C) - Select and copy text with errors
2. **Run AI corrector** - Via Raycast hotkey or direct execution
3. **Done!** - Corrected text gets automatically inserted
4. **App terminates itself**

## 📋 Prerequisites

- **macOS** (tested on macOS 12+)
- **[Ollama](https://ollama.ai/)** installed and running
- **Python 3.7+** (usually pre-installed on macOS)
- **Mistral Model** (or compatible model)

### Installing Prerequisites

```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Start Ollama service
ollama serve

# Pull the Mistral model (in new terminal)
ollama pull mistral

# Optional: Pull other models for better performance
ollama pull llama3.2
ollama pull qwen2.5
```

## 🔧 Installation Options

### Option 1: Raycast Integration (Recommended ⭐)

Perfect for productivity workflows with hotkey support:

```bash
# Clone repository
git clone https://github.com/derotti77/ai-text-corrector.git
cd ai-text-corrector

# Make Raycast script executable
chmod +x raycast-ai-corrector.py

# Copy to Raycast scripts folder
mkdir -p ~/raycast-scripts
cp raycast-ai-corrector.py ~/raycast-scripts/
```

**Setup in Raycast:**
1. Open Raycast (`⌘ + Space`)
2. Type "Script Commands" 
3. Add script directory: `~/raycast-scripts`
4. Assign hotkey (e.g., `⌘ + Shift + K`)

### Option 2: GUI Application

For users who prefer a visual interface:

```bash
# Run the GUI version
python3 ai-corrector.py
```

### Option 3: Command Line

For terminal users and scripting:

```bash
# Make executable
chmod +x raycast-ai-corrector.py

# Run directly (corrects clipboard content)
./raycast-ai-corrector.py english

# Or with different language
./raycast-ai-corrector.py german
```

## 🎮 Usage Examples

### English Correction
```
Input:  "This is an exemple with speling erors"
Output: "This is an example with spelling errors"
```

### German Correction
```
Input:  "Das ist einn Beispil mit Felern"
Output: "Das ist ein Beispiel mit Fehlern"
```

### Spanish Correction
```
Input:  "Este es un ejenplo con errorres"
Output: "Este es un ejemplo con errores"
```

## 🏗️ Project Structure

```
ai-text-corrector/
├── ai-corrector.py              # GUI application with language selection
├── raycast-ai-corrector.py      # Raycast integration script
├── ki-korrektur.py             # Original German version
├── install.sh                  # Installation script
├── README.md                   # German documentation
├── README-ENGLISH.md           # English documentation
├── LICENSE                     # MIT License
└── setup/
    ├── setup-git.sh           # Git repository setup
    └── start-daemon.sh        # Daemon startup script
```

## ⚙️ Configuration

### Model Selection

You can change the AI model in the scripts:

```python
# In the payload section, change:
"model": "mistral"

# To any installed Ollama model:
"model": "llama3.2"
"model": "qwen2.5"
"model": "codellama"
```

### Custom Prompts

Modify system prompts for specific use cases:

```python
# Example: Formal writing style
system_prompt = "You are a professional text editor. Correct spelling and grammar while maintaining a formal, professional tone. Return only the corrected text."

# Example: Casual writing style  
system_prompt = "You are a casual text corrector. Fix errors while keeping the informal, friendly tone. Return only the corrected text."
```

### Language-Specific Models

For better accuracy, use language-specific models:

```bash
# German
ollama pull llama3.2:8b-instruct-german

# Spanish  
ollama pull llama3.2:8b-instruct-spanish

# French
ollama pull llama3.2:8b-instruct-french
```

## 🐛 Troubleshooting

### App won't start
```bash
# Check if Ollama is running
curl http://localhost:11434/api/generate

# Start Ollama if not running
ollama serve
```

### No correction happening
```bash
# Check available models
ollama list

# Pull Mistral if missing
ollama pull mistral

# Test model directly
ollama run mistral "Correct this: 'This is an exemple'"
```

### Clipboard issues
```bash
# Test clipboard access
echo "test" | pbcopy
pbpaste

# Check app permissions in System Preferences > Privacy
```

### Python/Module errors
```bash
# Install required modules
pip3 install requests

# Check Python version (needs 3.7+)
python3 --version
```

## 🎛️ Advanced Usage

### Batch Processing
```bash
# Process multiple files
for file in *.txt; do
    cat "$file" | pbcopy
    ./raycast-ai-corrector.py english
    pbpaste > "corrected_$file"
done
```

### API Integration
```python
# Use as module in other Python scripts
from raycast_ai_corrector import correct_clipboard_text

# Correct text programmatically
result = correct_clipboard_text("english")
```

### Custom Hotkeys with Automator
1. Open **Automator**
2. Create **Quick Action**
3. Add **Run Shell Script**
4. Script: `/usr/bin/python3 ~/raycast-scripts/raycast-ai-corrector.py english`
5. Save and assign hotkey in **System Preferences**

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/yourusername/ai-text-corrector.git`
3. **Create** feature branch: `git checkout -b feature/amazing-feature`
4. **Make** your changes
5. **Test** thoroughly
6. **Commit**: `git commit -m 'Add amazing feature'`
7. **Push**: `git push origin feature/amazing-feature`  
8. **Create** Pull Request

### Development Setup
```bash
# Clone for development
git clone https://github.com/derotti77/ai-text-corrector.git
cd ai-text-corrector

# Install development dependencies
pip3 install -r requirements-dev.txt

# Run tests
python3 -m pytest tests/

# Format code
black *.py
```

## 🌟 Feature Requests

Planned features:
- [ ] **Browser Extension** - Correct text in web forms
- [ ] **VS Code Extension** - Integrate with code editor
- [ ] **Mobile App** - iOS/Android companion
- [ ] **Team Dictionary** - Shared custom corrections
- [ ] **Statistics Dashboard** - Track correction patterns
- [ ] **Voice Integration** - Dictate and auto-correct

## 📈 Performance Tips

### Faster Models
```bash
# Use smaller, faster models for basic corrections
ollama pull llama3.2:1b    # Very fast, basic corrections
ollama pull phi3:mini      # Balanced speed/quality
```

### Memory Optimization
```bash
# Limit Ollama memory usage
OLLAMA_MAX_LOADED_MODELS=1 ollama serve

# Use GPU acceleration (if available)
OLLAMA_GPU_LAYERS=50 ollama serve
```

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai/) - Amazing local LLM framework
- [Mistral AI](https://mistral.ai/) - Powerful language models
- [Raycast](https://raycast.com/) - Perfect productivity launcher
- All contributors to this project
- The open-source community

## 📞 Support & Community

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/derotti77/ai-text-corrector/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/derotti77/ai-text-corrector/discussions)
- 📚 **Documentation**: [Wiki](https://github.com/derotti77/ai-text-corrector/wiki)
- 💬 **Community**: [Discord Server](https://discord.gg/your-server)

## 🎯 Use Cases

### Content Creators
- Blog posts and articles
- Social media content
- Video descriptions
- Newsletter writing

### Students & Academics
- Essays and papers
- Research notes
- Thesis writing
- Email communication

### Business Professionals
- Email correspondence
- Reports and presentations
- Documentation
- Meeting notes

### Developers
- Code comments
- README files
- Documentation
- Git commit messages

---

**🚀 Developed with ❤️ for the international community**

**⭐ Star this repository if it helps you write better!**
