# 🚀 Quick Start Guide - AI Text Corrector

**Get up and running in 2 minutes!**

## ⚡ Super Quick Setup

### 1. Install & Run (30 seconds)
```bash
# Make installer executable and run
chmod +x install-english.sh
./install-english.sh
```

### 2. Test It (30 seconds)
```bash
# Copy this text with errors:
echo "This is an exemple with speling erors and gramar mistakes" | pbcopy

# Run the corrector
python3 ai-corrector.py
```

### 3. Raycast Integration (60 seconds)
```bash
# Set up Raycast (if you have it)
mkdir -p ~/raycast-scripts
cp raycast-ai-corrector.py ~/raycast-scripts/
```

Then in Raycast:
1. `⌘ + Space` → "Script Commands"
2. Add directory: `~/raycast-scripts`
3. Set hotkey: `⌘ + Shift + K`

## 🎯 How to Use

### Method 1: GUI App (Easiest)
1. Run: `python3 ai-corrector.py`
2. Type or paste text
3. Select language
4. Click "Correct"
5. Copy result

### Method 2: Raycast (Fastest)
1. Copy text with errors (`⌘ + C`)
2. Press your hotkey (e.g., `⌘ + Shift + K`)
3. Text automatically replaced! ✨

### Method 3: Command Line
```bash
# Copy text first, then:
./raycast-ai-corrector.py english
./raycast-ai-corrector.py german
./raycast-ai-corrector.py spanish
```

## 🌐 Language Examples

### 🇺🇸 English
```
Input:  "This exemple has speling erors"
Output: "This example has spelling errors"
```

### 🇩🇪 German  
```
Input:  "Das ist einn Beispil mit Felern"
Output: "Das ist ein Beispiel mit Fehlern"
```

### 🇪🇸 Spanish
```
Input:  "Este ejenplo tien errorres"
Output: "Este ejemplo tiene errores"
```

## 🔧 Troubleshooting (If Something Goes Wrong)

### Ollama Not Running?
```bash
ollama serve
# Keep this terminal open
```

### Missing Models?
```bash
ollama pull mistral
```

### Python Errors?
```bash
pip3 install requests
```

### Can't Find Scripts?
```bash
chmod +x *.py
```

## 💡 Pro Tips

- **Better for Raycast**: Use `⌘ + Shift + K` as hotkey - easy to remember!
- **Different Languages**: The app auto-detects most languages
- **Longer Texts**: Works best with 1-3 sentences at a time
- **Custom Models**: Edit the script to use `llama3.2` or other models

## 🎉 That's It!

You're ready to correct text in 7 languages with AI! 

**Need help?** Check the full `README-ENGLISH.md` for advanced features.

---
**Made with ❤️ for productivity enthusiasts**
