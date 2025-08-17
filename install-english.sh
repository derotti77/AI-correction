#!/bin/bash

# AI Text Corrector - Installation Script
# International version with multilingual support

echo "🤖 AI Text Corrector Installation"
echo "================================="
echo "International version with multilingual support"
echo

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_success() { echo -e "${GREEN}✅ $1${NC}"; }
print_error() { echo -e "${RED}❌ $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
print_info() { echo -e "${BLUE}ℹ️  $1${NC}"; }

# Check if running on macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    print_error "This installer is designed for macOS only"
    exit 1
fi

print_success "Running on macOS"

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is not installed!"
    print_info "Please install Python 3 from https://python.org"
    exit 1
fi

print_success "Python 3 found: $(python3 --version)"

# Check if pip3 is available
if ! command -v pip3 &> /dev/null; then
    print_warning "pip3 not found, installing..."
    python3 -m ensurepip --default-pip
fi

# Install required Python packages
print_info "Installing required Python packages..."
pip3 install requests 2>/dev/null
if [ $? -eq 0 ]; then
    print_success "Python dependencies installed"
else
    print_warning "Some dependencies may not have installed correctly"
fi

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    print_warning "Ollama is not installed"
    echo "Would you like to install Ollama now? (y/n)"
    read -r response
    if [[ "$response" =~ ^[Yy]$ ]]; then
        print_info "Installing Ollama..."
        curl -fsSL https://ollama.ai/install.sh | sh
        if [ $? -eq 0 ]; then
            print_success "Ollama installed successfully"
        else
            print_error "Failed to install Ollama"
            exit 1
        fi
    else
        print_warning "Skipping Ollama installation"
        print_info "You can install it later with: curl -fsSL https://ollama.ai/install.sh | sh"
    fi
else
    print_success "Ollama is already installed"
fi

# Check if Ollama is running
if ! curl -s http://localhost:11434/api/version > /dev/null; then
    print_warning "Ollama is not running"
    print_info "Starting Ollama service..."
    
    # Try to start Ollama in background
    nohup ollama serve > /dev/null 2>&1 &
    
    # Wait a few seconds for startup
    sleep 3
    
    if curl -s http://localhost:11434/api/version > /dev/null; then
        print_success "Ollama service started"
    else
        print_warning "Could not start Ollama automatically"
        print_info "Please run 'ollama serve' in another terminal"
    fi
else
    print_success "Ollama is running"
fi

# Check for required models
print_info "Checking for AI models..."

if ollama list | grep -q "mistral"; then
    print_success "Mistral model is installed"
else
    print_warning "Mistral model not found"
    echo "Would you like to download the Mistral model now? (~4.4GB) (y/n)"
    read -r response
    if [[ "$response" =~ ^[Yy]$ ]]; then
        print_info "Downloading Mistral model... This may take a while"
        ollama pull mistral
        if [ $? -eq 0 ]; then
            print_success "Mistral model downloaded successfully"
        else
            print_error "Failed to download Mistral model"
        fi
    else
        print_warning "Skipping model download"
        print_info "You can download it later with: ollama pull mistral"
    fi
fi

# Make scripts executable
print_info "Setting up executable permissions..."
chmod +x ai-corrector.py 2>/dev/null
chmod +x raycast-ai-corrector.py 2>/dev/null
chmod +x ki-korrektur.py 2>/dev/null
chmod +x ki-korrektur-simple.py 2>/dev/null
print_success "Scripts made executable"

# Setup Raycast integration
echo
echo "Would you like to set up Raycast integration? (y/n)"
read -r response
if [[ "$response" =~ ^[Yy]$ ]]; then
    RAYCAST_SCRIPTS_DIR="$HOME/raycast-scripts"
    
    # Create Raycast scripts directory
    mkdir -p "$RAYCAST_SCRIPTS_DIR"
    
    # Copy Raycast script
    if [ -f "raycast-ai-corrector.py" ]; then
        cp raycast-ai-corrector.py "$RAYCAST_SCRIPTS_DIR/"
        print_success "Raycast script installed to $RAYCAST_SCRIPTS_DIR"
        print_info "Next steps for Raycast setup:"
        print_info "1. Open Raycast (⌘ + Space)"
        print_info "2. Type 'Script Commands'"
        print_info "3. Add script directory: $RAYCAST_SCRIPTS_DIR"
        print_info "4. Assign a hotkey (e.g., ⌘ + Shift + K)"
    else
        print_error "Raycast script not found"
    fi
else
    print_info "Skipping Raycast setup"
fi

# Test the installation
echo
print_info "Testing installation..."

# Test GUI version
if python3 -c "import tkinter; print('GUI support: OK')" 2>/dev/null; then
    print_success "GUI version ready"
else
    print_warning "GUI version may not work (tkinter issues)"
fi

# Test API connection
if python3 -c "import requests; requests.get('http://localhost:11434/api/version', timeout=2)" 2>/dev/null; then
    print_success "API connection test passed"
else
    print_warning "API connection test failed - make sure Ollama is running"
fi

# Installation summary
echo
echo "🎉 Installation Complete!"
echo "========================"
echo
print_success "Available versions:"
echo "  📱 GUI Application:     python3 ai-corrector.py"
echo "  🚀 Raycast Integration: ~/raycast-scripts/raycast-ai-corrector.py"
echo "  ⌨️  Command Line:        ./raycast-ai-corrector.py [language]"
echo
print_success "Supported languages:"
echo "  🇺🇸 English   🇩🇪 German    🇪🇸 Spanish   🇫🇷 French"
echo "  🇮🇹 Italian   🇵🇹 Portuguese 🇳🇱 Dutch"
echo
print_success "Quick start:"
echo "  1. Copy some text with errors"
echo "  2. Run: python3 ai-corrector.py"
echo "  3. Or use Raycast hotkey if configured"
echo
print_info "For more information, see README-ENGLISH.md"
print_info "Report issues at: https://github.com/derotti77/ai-text-corrector/issues"
echo
print_success "Happy text correcting! 🚀"
