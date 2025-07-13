#!/usr/bin/env python3
"""
KI-Korrektur - Einfache Version
Läuft einmal, korrigiert Text aus Zwischenablage und fügt automatisch ein
"""

import subprocess
import requests
import time

def correct_clipboard_text():
    """Korrigiert Text aus Zwischenablage und fügt korrigierten Text automatisch ein"""
    
    try:
        # Text aus Zwischenablage lesen
        text = subprocess.check_output(['pbpaste'], text=True).strip()
        
        if not text:
            print("❌ Kein Text in Zwischenablage")
            return False
            
        print(f"🔍 Korrigiere: '{text}'")
        
        # Text korrigieren
        system_prompt = "Du bist ein Korrektor für deutsche Texte. Korrigiere nur die Rechtschreibung und Grammatik auf Deutsch. Gib nur den korrigierten Text zurück, keine Erklärungen oder Übersetzungen."
        
        payload = {
            "model": "mistral",
            "system": system_prompt,
            "prompt": text,
            "stream": False
        }
        
        print("🤖 Sende an KI...")
        response = requests.post(
            "http://localhost:11434/api/generate",
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            corrected_text = data.get('response', '').strip()
            
            # Nur ersten Satz nehmen und bereinigen
            if corrected_text:
                corrected_text = corrected_text.split('.')[0].strip()
                
                # Korrigierten Text in Zwischenablage kopieren
                subprocess.run(['pbcopy'], input=corrected_text, text=True)
                
                print(f"✅ Korrigiert zu: '{corrected_text}'")
                print("📋 Text in Zwischenablage - jetzt einfach Cmd+V drücken!")
                
                # Optional: Automatisch einfügen nach kurzer Pause
                print("⏳ Füge in 2 Sekunden automatisch ein...")
                time.sleep(2)
                subprocess.run(['osascript', '-e', 'tell application "System Events" to keystroke "v" using command down'])
                print("✨ Automatisch eingefügt!")
                
                return True
            else:
                print("❌ Keine Antwort von KI erhalten")
                return False
        else:
            print(f"❌ Ollama Fehler: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Ollama ist nicht gestartet!")
        print("   Bitte starte: ollama serve")
        return False
    except Exception as e:
        print(f"❌ Fehler: {e}")
        return False

def main():
    print("🤖 KI-Korrektur")
    print("================")
    print("1. Kopiere Text mit Cmd+C")
    print("2. Starte dieses Programm")
    print("3. Text wird automatisch korrigiert und eingefügt!")
    print()
    
    success = correct_clipboard_text()
    
    if success:
        print("\n🎉 Fertig!")
    else:
        print("\n❌ Fehler beim Korrigieren")
        input("Drücke Enter zum Beenden...")

if __name__ == "__main__":
    main()
