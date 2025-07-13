#!/usr/bin/env python3
"""
KI-Korrektur App
Einfaches Programm zur Textkorrektur mit Ollama
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests
import json
import threading
import subprocess
import sys

class KIKorrekturApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KI-Korrektur 🤖")
        self.root.geometry("600x500")
        self.root.configure(bg='#f0f0f0')
        
        # Status
        self.is_correcting = False
        
        self.setup_ui()
        self.setup_hotkey()
        
    def setup_ui(self):
        # Titel
        title_label = tk.Label(
            self.root, 
            text="🤖 KI-Korrektur", 
            font=("Arial", 20, "bold"),
            bg='#f0f0f0',
            fg='#333'
        )
        title_label.pack(pady=20)
        
        # Anleitung
        instruction = tk.Label(
            self.root,
            text="1. Text hier eingeben oder Zwischenablage verwenden\n2. 'Korrigieren' klicken oder Cmd+K drücken\n3. Korrigierten Text kopieren",
            font=("Arial", 12),
            bg='#f0f0f0',
            fg='#666'
        )
        instruction.pack(pady=10)
        
        # Eingabefeld
        tk.Label(self.root, text="Text zum korrigieren:", font=("Arial", 12, "bold"), bg='#f0f0f0').pack(anchor='w', padx=20)
        self.input_text = scrolledtext.ScrolledText(
            self.root,
            height=8,
            width=70,
            font=("Arial", 11),
            wrap=tk.WORD
        )
        self.input_text.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Buttons Frame
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=10)
        
        # Zwischenablage Button
        paste_btn = tk.Button(
            button_frame,
            text="📋 Aus Zwischenablage",
            command=self.paste_from_clipboard,
            font=("Arial", 11),
            bg='#e0e0e0',
            padx=20
        )
        paste_btn.pack(side='left', padx=5)
        
        # Korrigieren Button
        self.correct_btn = tk.Button(
            button_frame,
            text="✨ Korrigieren (Cmd+K)",
            command=self.correct_text_async,
            font=("Arial", 11, "bold"),
            bg='#4CAF50',
            fg='white',
            padx=20
        )
        self.correct_btn.pack(side='left', padx=5)
        
        # Kopieren Button
        copy_btn = tk.Button(
            button_frame,
            text="📋 Kopieren",
            command=self.copy_to_clipboard,
            font=("Arial", 11),
            bg='#2196F3',
            fg='white',
            padx=20
        )
        copy_btn.pack(side='left', padx=5)
        
        # Ausgabefeld
        tk.Label(self.root, text="Korrigierter Text:", font=("Arial", 12, "bold"), bg='#f0f0f0').pack(anchor='w', padx=20, pady=(20,0))
        self.output_text = scrolledtext.ScrolledText(
            self.root,
            height=8,
            width=70,
            font=("Arial", 11),
            wrap=tk.WORD,
            bg='#f9f9f9'
        )
        self.output_text.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Status
        self.status_label = tk.Label(
            self.root,
            text="Bereit",
            font=("Arial", 10),
            bg='#f0f0f0',
            fg='#666'
        )
        self.status_label.pack(pady=5)
        
    def setup_hotkey(self):
        # Cmd+K Hotkey
        self.root.bind('<Command-k>', lambda e: self.correct_text_async())
        self.root.bind('<Control-k>', lambda e: self.correct_text_async())
        
    def paste_from_clipboard(self):
        try:
            clipboard_text = subprocess.check_output(['pbpaste'], text=True)
            self.input_text.delete('1.0', tk.END)
            self.input_text.insert('1.0', clipboard_text)
            self.status_label.config(text="Text aus Zwischenablage eingefügt")
        except Exception as e:
            messagebox.showerror("Fehler", f"Konnte nicht aus Zwischenablage lesen: {str(e)}")
    
    def copy_to_clipboard(self):
        try:
            text = self.output_text.get('1.0', tk.END).strip()
            if text:
                subprocess.run(['pbcopy'], input=text, text=True)
                self.status_label.config(text="Text in Zwischenablage kopiert")
            else:
                messagebox.showwarning("Warnung", "Kein Text zum Kopieren vorhanden")
        except Exception as e:
            messagebox.showerror("Fehler", f"Konnte nicht in Zwischenablage kopieren: {str(e)}")
    
    def correct_text_async(self):
        if self.is_correcting:
            return
            
        text = self.input_text.get('1.0', tk.END).strip()
        if not text:
            messagebox.showwarning("Warnung", "Bitte Text eingeben oder aus Zwischenablage einfügen")
            return
            
        # Threading für UI-Responsivität
        thread = threading.Thread(target=self.correct_text, args=(text,))
        thread.daemon = True
        thread.start()
    
    def correct_text(self, text):
        self.is_correcting = True
        self.root.after(0, lambda: self.status_label.config(text="KI korrigiert Text..."))
        self.root.after(0, lambda: self.correct_btn.config(text="⏳ Korrigiere...", state='disabled'))
        
        try:
            # Ollama API Call
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
                    
                    self.root.after(0, lambda: self.output_text.delete('1.0', tk.END))
                    self.root.after(0, lambda: self.output_text.insert('1.0', corrected_text))
                    self.root.after(0, lambda: self.status_label.config(text="Text erfolgreich korrigiert"))
                else:
                    self.root.after(0, lambda: messagebox.showerror("Fehler", "Keine Antwort von der KI erhalten"))
                    
            else:
                self.root.after(0, lambda: messagebox.showerror("Fehler", f"Ollama Fehler: {response.status_code}"))
                
        except requests.exceptions.ConnectionError:
            self.root.after(0, lambda: messagebox.showerror("Fehler", "Verbindung zu Ollama fehlgeschlagen.\nIst Ollama gestartet? (ollama serve)"))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Fehler", f"Unerwarteter Fehler: {str(e)}"))
        finally:
            self.is_correcting = False
            self.root.after(0, lambda: self.correct_btn.config(text="✨ Korrigieren (Cmd+K)", state='normal'))

def main():
    # Prüfe ob Python 3 läuft
    if sys.version_info[0] < 3:
        print("Fehler: Python 3 wird benötigt!")
        sys.exit(1)
    
    # Erstelle und starte App
    root = tk.Tk()
    app = KIKorrekturApp(root)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\nApp beendet.")
        sys.exit(0)

if __name__ == "__main__":
    main()
