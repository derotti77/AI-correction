#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title AI Text Corrector
# @raycast.mode compact
# @raycast.packageName AI-Text-Corrector

# Optional parameters:
# @raycast.icon 🤖
# @raycast.description Automatically corrects text from clipboard using local AI
# @raycast.author derotti77
# @raycast.authorURL https://github.com/derotti77
# @raycast.argument1 {"type": "dropdown", "placeholder": "Language", "data": [{"title": "English", "value": "english"}, {"title": "German", "value": "german"}, {"title": "Spanish", "value": "spanish"}, {"title": "French", "value": "french"}, {"title": "Italian", "value": "italian"}, {"title": "Portuguese", "value": "portuguese"}, {"title": "Dutch", "value": "dutch"}], "optional": true}

"""
AI Text Corrector for Raycast
Automatic text correction with Ollama - International version
"""

import subprocess
import requests
import sys
import os

def get_system_prompt(language="english"):
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
    
    return prompts.get(language.lower(), prompts["english"])

def clean_ai_response(text, language="english"):
    """Clean common AI response prefixes based on language"""
    prefixes_to_remove = {
        "english": ["Here is the corrected text:", "The corrected text is:", "Corrected:", "Here you go:"],
        "german": ["Hier ist der korrigierte Text:", "Der korrigierte Text lautet:", "Korrigiert:", "Bitte schön:"],
        "spanish": ["Aquí está el texto corregido:", "El texto corregido es:", "Corregido:", "Aquí tienes:"],
        "french": ["Voici le texte corrigé:", "Le texte corrigé est:", "Corrigé:", "Voilà:"],
        "italian": ["Ecco il testo corretto:", "Il testo corretto è:", "Corretto:", "Ecco qui:"],
        "portuguese": ["Aqui está o texto corrigido:", "O texto corrigido é:", "Corrigido:", "Aqui está:"],
        "dutch": ["Hier is de gecorrigeerde tekst:", "De gecorrigeerde tekst is:", "Gecorrigeerd:", "Hier is het:"]
    }
    
    language_prefixes = prefixes_to_remove.get(language.lower(), prefixes_to_remove["english"])
    
    for prefix in language_prefixes:
        if text.lower().startswith(prefix.lower()):
            text = text[len(prefix):].strip()
    
    # Remove quotes if they wrap the entire text
    if text.startswith('"') and text.endswith('"'):
        text = text[1:-1].strip()
    
    return text

def correct_clipboard_text(language="english"):
    """Corrects text from clipboard and automatically inserts corrected text"""
    
    try:
        # Read text from clipboard
        text = subprocess.check_output(['pbpaste'], text=True).strip()
        
        if not text:
            print("❌ No text in clipboard")
            return False
            
        print(f"🔍 Correcting text in {language.capitalize()}...")
        
        # Correct text
        system_prompt = get_system_prompt(language)
        
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
                corrected_text = clean_ai_response(corrected_text, language)
                
                # Copy corrected text to clipboard
                subprocess.run(['pbcopy'], input=corrected_text, text=True)
                
                print(f"✅ Text corrected and copied to clipboard!")
                
                # Automatically paste
                subprocess.run([
                    'osascript', '-e', 
                    'tell application "System Events" to keystroke "v" using command down'
                ])
                
                print(f"📝 Original: {text[:50]}{'...' if len(text) > 50 else ''}")
                print(f"✨ Corrected: {corrected_text[:50]}{'...' if len(corrected_text) > 50 else ''}")
                
                return True
            else:
                print("❌ No response received from AI")
                return False
        else:
            print(f"❌ Ollama error: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Ollama is not running!")
        print("Please start: ollama serve")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    # Get language parameter from Raycast
    language = "english"  # default
    if len(sys.argv) > 1:
        language = sys.argv[1].lower()
    
    # Alternative: check environment variable
    if 'RAYCAST_ARGUMENT1' in os.environ:
        language = os.environ['RAYCAST_ARGUMENT1'].lower()
    
    success = correct_clipboard_text(language)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
