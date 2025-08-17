#!/usr/bin/env python3
"""
AI Text Corrector App
Simple program for text correction with Ollama
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
import requests
import json
import threading
import subprocess
import sys

class AITextCorrectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Text Corrector 🤖")
        self.root.geometry("700x600")
        self.root.configure(bg='#f0f0f0')
        
        # Status
        self.is_correcting = False
        self.supported_languages = {
            "English": "english",
            "German": "german", 
            "Spanish": "spanish",
            "French": "french",
            "Italian": "italian",
            "Portuguese": "portuguese",
            "Dutch": "dutch"
        }
        self.selected_language = "English"
        
        self.setup_ui()
        self.setup_hotkeys()
        
    def setup_ui(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="🤖 AI Text Corrector", 
            font=("Arial", 20, "bold"),
            bg='#f0f0f0',
            fg='#333'
        )
        title_label.pack(pady=20)
        
        # Language selection frame
        lang_frame = tk.Frame(self.root, bg='#f0f0f0')
        lang_frame.pack(pady=10)
        
        tk.Label(lang_frame, text="Target Language:", font=("Arial", 12, "bold"), bg='#f0f0f0').pack(side='left', padx=5)
        
        self.language_var = tk.StringVar(value=self.selected_language)
        language_combo = ttk.Combobox(
            lang_frame, 
            textvariable=self.language_var,
            values=list(self.supported_languages.keys()),
            state="readonly",
            width=15
        )
        language_combo.pack(side='left', padx=5)
        language_combo.bind('<<ComboboxSelected>>', self.on_language_change)
        
        # Instructions
        instruction = tk.Label(
            self.root,
            text="1. Enter text here or paste from clipboard\n2. Click 'Correct' or press Cmd+K\n3. Copy corrected text",
            font=("Arial", 12),
            bg='#f0f0f0',
            fg='#666'
        )
        instruction.pack(pady=10)
        
        # Input field
        tk.Label(self.root, text="Text to correct:", font=("Arial", 12, "bold"), bg='#f0f0f0').pack(anchor='w', padx=20)
        self.input_text = scrolledtext.ScrolledText(
            self.root,
            height=8,
            width=80,
            font=("Arial", 11),
            wrap=tk.WORD
        )
        self.input_text.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Buttons Frame
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=10)
        
        # Paste Button
        paste_btn = tk.Button(
            button_frame,
            text="📋 Paste from Clipboard",
            command=self.paste_from_clipboard,
            font=("Arial", 11),
            bg='#e0e0e0',
            padx=20
        )
        paste_btn.pack(side='left', padx=5)
        
        # Correct Button
        self.correct_btn = tk.Button(
            button_frame,
            text="✨ Correct Text (Cmd+K)",
            command=self.correct_text_async,
            font=("Arial", 11, "bold"),
            bg='#4CAF50',
            fg='white',
            padx=20
        )
        self.correct_btn.pack(side='left', padx=5)
        
        # Copy Button
        copy_btn = tk.Button(
            button_frame,
            text="📋 Copy to Clipboard",
            command=self.copy_to_clipboard,
            font=("Arial", 11),
            bg='#2196F3',
            fg='white',
            padx=20
        )
        copy_btn.pack(side='left', padx=5)
        
        # Clear Button
        clear_btn = tk.Button(
            button_frame,
            text="🗑️ Clear",
            command=self.clear_all,
            font=("Arial", 11),
            bg='#FF5722',
            fg='white',
            padx=20
        )
        clear_btn.pack(side='left', padx=5)
        
        # Output field
        tk.Label(self.root, text="Corrected text:", font=("Arial", 12, "bold"), bg='#f0f0f0').pack(anchor='w', padx=20, pady=(20,0))
        self.output_text = scrolledtext.ScrolledText(
            self.root,
            height=8,
            width=80,
            font=("Arial", 11),
            wrap=tk.WORD,
            bg='#f9f9f9'
        )
        self.output_text.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Status
        self.status_label = tk.Label(
            self.root,
            text="Ready",
            font=("Arial", 10),
            bg='#f0f0f0',
            fg='#666'
        )
        self.status_label.pack(pady=5)
        
    def setup_hotkeys(self):
        # Cmd+K Hotkey for correction
        self.root.bind('<Command-k>', lambda e: self.correct_text_async())
        self.root.bind('<Control-k>', lambda e: self.correct_text_async())
        
        # Cmd+V for paste
        self.root.bind('<Command-v>', lambda e: self.paste_from_clipboard())
        self.root.bind('<Control-v>', lambda e: self.paste_from_clipboard())
        
    def on_language_change(self, event):
        self.selected_language = self.language_var.get()
        self.status_label.config(text=f"Language changed to {self.selected_language}")
        
    def paste_from_clipboard(self):
        try:
            clipboard_text = subprocess.check_output(['pbpaste'], text=True)
            self.input_text.delete('1.0', tk.END)
            self.input_text.insert('1.0', clipboard_text)
            self.status_label.config(text="Text pasted from clipboard")
        except Exception as e:
            messagebox.showerror("Error", f"Could not read from clipboard: {str(e)}")
    
    def copy_to_clipboard(self):
        try:
            text = self.output_text.get('1.0', tk.END).strip()
            if text:
                subprocess.run(['pbcopy'], input=text, text=True)
                self.status_label.config(text="Text copied to clipboard")
            else:
                messagebox.showwarning("Warning", "No text to copy")
        except Exception as e:
            messagebox.showerror("Error", f"Could not copy to clipboard: {str(e)}")
    
    def clear_all(self):
        self.input_text.delete('1.0', tk.END)
        self.output_text.delete('1.0', tk.END)
        self.status_label.config(text="Text cleared")
    
    def correct_text_async(self):
        if self.is_correcting:
            return
            
        text = self.input_text.get('1.0', tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter text or paste from clipboard")
            return
            
        # Threading for UI responsiveness
        thread = threading.Thread(target=self.correct_text, args=(text,))
        thread.daemon = True
        thread.start()
    
    def get_system_prompt(self, language):
        """Get system prompt based on selected language"""
        prompts = {
            "english": "You are a text corrector for English texts. Correct only spelling and grammar in English. Return only the corrected text, no explanations or translations.",
            "german": "Du bist ein Korrektor für deutsche Texte. Korrigiere nur die Rechtschreibung und Grammatik auf Deutsch. Gib nur den korrigierten Text zurück, keine Erklärungen oder Übersetzungen.",
            "spanish": "Eres un corrector de textos en español. Corrige solo la ortografía y gramática en español. Devuelve solo el texto corregido, sin explicaciones o traducciones.",
            "french": "Vous êtes un correcteur de textes français. Corrigez uniquement l'orthographe et la grammaire en français. Retournez seulement le texte corrigé, sans explications ni traductions.",
            "italian": "Sei un correttore di testi italiani. Correggi solo l'ortografia e la grammatica in italiano. Restituisci solo il testo corretto, senza spiegazioni o traduzioni.",
            "portuguese": "Você é um corretor de textos em português. Corrija apenas a ortografia e gramática em português. Retorne apenas o texto corrigido, sem explicações ou traduções.",
            "dutch": "Je bent een tekstcorrector voor Nederlandse teksten. Corrigeer alleen spelling en grammatica in het Nederlands. Geef alleen de gecorrigeerde tekst terug, geen uitleg of vertalingen."
        }
        
        language_key = self.supported_languages.get(language, "english").lower()
        return prompts.get(language_key, prompts["english"])
    
    def correct_text(self, text):
        self.is_correcting = True
        self.root.after(0, lambda: self.status_label.config(text="AI is correcting text..."))
        self.root.after(0, lambda: self.correct_btn.config(text="⏳ Correcting...", state='disabled'))
        
        try:
            # Ollama API Call
            system_prompt = self.get_system_prompt(self.selected_language)
            
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
                
                # Clean up the response
                if corrected_text:
                    # Remove common AI prefixes
                    prefixes_to_remove = [
                        "Here is the corrected text:",
                        "Hier ist der korrigierte Text:",
                        "Aquí está el texto corregido:",
                        "Voici le texte corrigé:",
                        "Ecco il testo corretto:",
                        "Aqui está o texto corrigido:",
                        "Hier is de gecorrigeerde tekst:"
                    ]
                    
                    for prefix in prefixes_to_remove:
                        if corrected_text.lower().startswith(prefix.lower()):
                            corrected_text = corrected_text[len(prefix):].strip()
                    
                    # Remove quotes if they wrap the entire text
                    if corrected_text.startswith('"') and corrected_text.endswith('"'):
                        corrected_text = corrected_text[1:-1].strip()
                    
                    self.root.after(0, lambda: self.output_text.delete('1.0', tk.END))
                    self.root.after(0, lambda: self.output_text.insert('1.0', corrected_text))
                    self.root.after(0, lambda: self.status_label.config(text="Text successfully corrected"))
                else:
                    self.root.after(0, lambda: messagebox.showerror("Error", "No response received from AI"))
                    
            else:
                self.root.after(0, lambda: messagebox.showerror("Error", f"Ollama error: {response.status_code}"))
                
        except requests.exceptions.ConnectionError:
            self.root.after(0, lambda: messagebox.showerror("Error", "Connection to Ollama failed.\nIs Ollama running? (ollama serve)"))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"Unexpected error: {str(e)}"))
        finally:
            self.is_correcting = False
            self.root.after(0, lambda: self.correct_btn.config(text="✨ Correct Text (Cmd+K)", state='normal'))

def main():
    # Check if Python 3 is running
    if sys.version_info[0] < 3:
        print("Error: Python 3 is required!")
        sys.exit(1)
    
    # Create and start app
    root = tk.Tk()
    app = AITextCorrectorApp(root)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\nApp terminated.")
        sys.exit(0)

if __name__ == "__main__":
    main()
