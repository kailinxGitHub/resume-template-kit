# Dependencies for Resume Template Kit

This document lists all the dependencies required to run the Resume Template Kit system.

## 🐍 **Python Dependencies**

### **Required Python Version:**
- **Python 3.6 or higher** (tested with Python 3.9.6)

### **Python Standard Library Modules Used:**
The `create_resume.py` script only uses Python standard library modules:
- `os` - Operating system interface
- `sys` - System-specific parameters and functions
- `pathlib.Path` - Object-oriented filesystem paths
- `re` - Regular expression operations
- `datetime` - Basic date and time types

**No external Python packages are required!** The generator tool is self-contained.

## 📄 **LaTeX Dependencies**

### **Required LaTeX Distribution:**
- **TeX Live** (recommended) or **MiKTeX** (Windows)
- **MacTeX** (macOS) - includes TeX Live

### **Required LaTeX Packages:**
The following packages are used in `template.tex`:

#### **Core LaTeX Packages:**
- `article` - Document class (built-in)
- `latexsym` - LaTeX symbols
- `fullpage` - Full page layout
- `titlesec` - Section formatting
- `marvosym` - Marvosym symbols
- `color` - Color support
- `verbatim` - Verbatim text
- `enumitem` - List formatting
- `hyperref` - Hyperlinks and PDF metadata
- `fancyhdr` - Page headers and footers
- `babel` - Language support
- `tabularx` - Extended table features

#### **Font Packages:**
- `fontenc` - Font encoding
- `lmodern` - Latin Modern fonts (default)
- `glyphtounicode` - Unicode support

#### **Alternative Font Options (Optional):**
- `tgheros` - Helvetica-like fonts
- `FiraSans` - Mozilla Fira Sans
- `roboto` - Google Roboto
- `noto-sans` - Google Noto Sans
- `sourcesanspro` - Adobe Source Sans Pro
- `CormorantGaramond` - Cormorant Garamond
- `charter` - Charter font

### **LaTeX Compiler:**
- **pdflatex** - PDF generation from LaTeX source

## 🖥️ **System Dependencies**

### **Operating System Support:**
- **macOS** (tested on macOS 12+)
- **Linux** (Ubuntu, Debian, CentOS, etc.)
- **Windows** (with WSL or native LaTeX installation)

### **Shell Requirements:**
- **Bash** - For running `build.sh` script
- **find** - File searching utility
- **mkdir** - Directory creation
- **ls** - File listing
- **rm** - File removal
- **mv** - File moving

### **File System:**
- **Read/Write permissions** for the project directory
- **Execute permissions** for shell scripts

## 📦 **Installation Instructions**

### **1. Python Installation:**

#### **macOS:**
```bash
# Python is usually pre-installed
python3 --version

# If not installed, use Homebrew:
brew install python3
```

#### **Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

#### **Windows:**
Download from [python.org](https://www.python.org/downloads/)

### **2. LaTeX Installation:**

#### **macOS:**
```bash
# Install MacTeX (includes TeX Live)
brew install --cask mactex

# Or download from: https://www.tug.org/mactex/
```

#### **Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install texlive-full
sudo apt install texlive-latex-extra
```

#### **Windows:**
- Download and install [MiKTeX](https://miktex.org/)
- Or use [TeX Live](https://www.tug.org/texlive/)

### **3. Verify Installation:**

```bash
# Check Python
python3 --version

# Check LaTeX
pdflatex --version

# Check if build script is executable
chmod +x build.sh
```

## 🔧 **Optional Dependencies**

### **Development Tools (Optional):**
- **Git** - Version control
- **VS Code** or **TeXstudio** - LaTeX editing
- **PDF viewer** - For viewing generated resumes

### **Font Dependencies (Optional):**
If you want to use alternative fonts, ensure they're installed:

#### **System Fonts:**
- **Helvetica** - Usually pre-installed on macOS
- **Arial** - Usually pre-installed on Windows

#### **Open Source Fonts:**
- **Fira Sans** - Download from [Mozilla](https://github.com/mozilla/Fira)
- **Roboto** - Download from [Google Fonts](https://fonts.google.com/specimen/Roboto)
- **Noto Sans** - Download from [Google Fonts](https://fonts.google.com/noto/specimen/Noto+Sans)
- **Source Sans Pro** - Download from [Adobe](https://github.com/adobe-fonts/source-sans-pro)

## 🚀 **Quick Start Verification**

After installation, verify everything works:

```bash
# 1. Test Python generator
python3 create_resume.py --help

# 2. Test LaTeX compilation
pdflatex --version

# 3. Test build script
./build.sh

# 4. Check generated PDFs
ls output/*.pdf
```

## ❗ **Troubleshooting**

### **Common Issues:**

1. **"pdflatex: command not found"**
   - Install LaTeX distribution (TeX Live, MiKTeX, or MacTeX)

2. **"Permission denied" for build.sh**
   - Run: `chmod +x build.sh`

3. **Missing LaTeX packages**
   - Install full TeX Live distribution
   - Or install specific packages: `sudo apt install texlive-latex-extra`

4. **Python not found**
   - Install Python 3.6+ from [python.org](https://www.python.org/downloads/)

### **Platform-Specific Notes:**

#### **macOS:**
- MacTeX provides the most complete LaTeX installation
- Python 3 is usually pre-installed

#### **Linux:**
- Use package manager for LaTeX installation
- Consider using `texlive-full` for complete package set

#### **Windows:**
- MiKTeX provides automatic package installation
- Consider using WSL for better shell script compatibility

## 📋 **Summary**

**Minimum Requirements:**
- Python 3.6+
- LaTeX distribution (TeX Live/MiKTeX/MacTeX)
- Bash shell
- Basic file system permissions

**No external Python packages required!** The system is designed to be self-contained and easy to set up.
