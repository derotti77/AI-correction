#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title KI Text Korrektur
# @raycast.mode compact
# @raycast.packageName KI-Korrektur

# Optional parameters:
# @raycast.icon 🤖
# @raycast.description Korrigiert deutschen Text aus der Zwischenablage automatisch
# @raycast.author derotti77
# @raycast.authorURL https://github.com/derotti77

"""
KI-Korrektur für Raycast
Automatische deutsche Textkorrektur mit Ollama
"""

import subprocess
import requests
import sys

def correct_clipboard_text():
    """Korrigiert Text aus Zwischenablage und fügt korrigierten Text automatisch ein"""
    
    try:
        # Text aus Zwischenablage lesen
        text = subprocess.check_output(['pbpaste'], text=True).strip()
        
        if not text:
            print("❌ Kein Text in Zwischenablage")
            return False
            
        print(f"🔍 Korrigiere Text...")
        
        # Text korrigieren
        system_prompt = "Du bist ein Korrektor für deutsche Texte. Korrigiere nur die Rechtschreibung und Grammatik auf Deutsch. Gib nur den korrigierten Text zurück, keine Erklärungen oder Übersetzungen."
        
        payload = {
            "model": "mistral",
            "system": system_prompt,
            "prompt": text,
            "stream": False
        }
        
        response = requests.post(
            "http://localhost:11434/api/generate",
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            corrected_text = data.get('response', '').strip()
            
            # Text bereinigen
            if corrected_text:
                # Entferne häufige AI-Zusätze
                corrected_text = corrected_text.replace('"', '').strip()
                if corrected_text.startswith("Hier ist der korrigierte Text:"):
                    corrected_text = corrected_text.replace("Hier ist der korrigierte Text:", "").strip()
                
                # Korrigierten Text in Zwischenablage kopieren
                subprocess.run(['pbcopy'], input=corrected_text, text=True)
                
                print(f"✅ Text korrigiert und in Zwischenablage kopiert!")
                
                # Automatisch einfügen
                subprocess.run([
                    'osascript', '-e', 
                    'tell application "System Events" to keystroke "v" using command down'
                ])
                
                return True
            else:
                print("❌ Keine Antwort von KI erhalten")
                return False
        else:
            print(f"❌ Ollama Fehler: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Ollama ist nicht gestartet!")
        print("Bitte starte: ollama serve")
        return False
    except Exception as e:
        print(f"❌ Fehler: {e}")
        return False

def main():
    success = correct_clipboard_text()
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
