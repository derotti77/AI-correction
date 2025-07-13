#!/usr/bin/env python3
"""
KI-Korrektur Daemon
Unsichtbares Hintergrundprogramm das auf Cmd+Shift+K wartet
"""

import subprocess
import requests
import json
import threading
import time
import signal
import sys
from pynput import keyboard
from pynput.keyboard import Key, KeyCode

class KIKorrekturDaemon:
    def __init__(self):
        self.is_running = True
        self.is_correcting = False
        self.combination = {Key.cmd, Key.shift, KeyCode.from_char('k')}
        self.pressed = set()
        
    def on_press(self, key):
        self.pressed.add(key)
        
        # Prüfe ob die richtige Kombination gedrückt wurde
        if self.combination.issubset(self.pressed):
            if not self.is_correcting:
                threading.Thread(target=self.correct_clipboard_text, daemon=True).start()
    
    def on_release(self, key):
        try:
            self.pressed.remove(key)
        except KeyError:
            pass
            
        # Beende das Programm mit Esc (für Debug)
        if key == Key.esc:
            print("Daemon beendet.")
            return False
    
    def correct_clipboard_text(self):
        """Korrigiert Text aus Zwischenablage und fügt korrigierten Text automatisch ein"""
        if self.is_correcting:
            return
            
        self.is_correcting = True
        
        try:
            # Text aus Zwischenablage lesen
            text = subprocess.check_output(['pbpaste'], text=True).strip()
            
            if not text:
                print("Kein Text in Zwischenablage")
                return
                
            print(f"Korrigiere: '{text}'")
            
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
                
                # Nur ersten Satz nehmen und bereinigen
                if corrected_text:
                    corrected_text = corrected_text.split('.')[0].strip()
                    
                    # Korrigierten Text in Zwischenablage kopieren
                    subprocess.run(['pbcopy'], input=corrected_text, text=True)
                    
                    # Automatisch einfügen (Cmd+V)
                    time.sleep(0.1)  # Kurz warten
                    subprocess.run(['osascript', '-e', 'tell application "System Events" to keystroke "v" using command down'])
                    
                    print(f"Korrigiert zu: '{corrected_text}'")
                else:
                    print("Keine Antwort von KI erhalten")
            else:
                print(f"Ollama Fehler: {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print("Ollama ist nicht gestartet!")
        except Exception as e:
            print(f"Fehler: {e}")
        finally:
            self.is_correcting = False
    
    def start(self):
        """Startet den Daemon"""
        print("🤖 KI-Korrektur Daemon gestartet")
        print("Tastenkürzel: Cmd+Shift+K")
        print("Beenden: Drücke Esc oder Ctrl+C")
        print("Läuft im Hintergrund...")
        
        # Keyboard Listener starten
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as listener:
            try:
                listener.join()
            except KeyboardInterrupt:
                print("\nDaemon beendet.")
                return

def signal_handler(sig, frame):
    """Signal Handler für sauberes Beenden"""
    print("\nDaemon beendet.")
    sys.exit(0)

def main():
    # Signal Handler registrieren
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Daemon starten
    daemon = KIKorrekturDaemon()
    daemon.start()

if __name__ == "__main__":
    main()
