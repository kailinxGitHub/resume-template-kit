# Resume Template Kit

A comprehensive LaTeX-based resume system with an interactive generator tool for creating customized resume templates. This kit provides both automated generation and manual customization options for professional resume creation.

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎨 **Font Licensing**

The template uses open-source fonts with the following licenses:

- **Latin Modern Sans** (Default): OFL License - freely redistributable
- **Fira Sans**: Mozilla Public License - freely redistributable  
- **Roboto**: Apache License 2.0 - freely redistributable
- **Noto Sans**: Apache License 2.0 - freely redistributable
- **Source Sans Pro**: OFL License - freely redistributable
- **Cormorant Garamond**: OFL License - freely redistributable
- **Charter**: Public Domain - freely redistributable

All fonts included are open-source and can be freely distributed with this template.

## 🎯 **Resume Generator Tool**

A Python-based CLI tool that helps you create new resume templates with interactive customization options. This tool guides you through the process of setting up your basic resume information and then generates the necessary LaTeX files for further customization.

### **Generator Features**

- 🎯 **Interactive Setup**: Step-by-step prompts to collect your resume information
- 📧 **Contact Information**: Name, location, phone, email, LinkedIn, GitHub
- 🎓 **Education Details**: University, degree, GPA, coursework, competitions, clubs
- 💻 **Technical Skills**: Programming languages, frameworks, cloud tools, DevOps
- 💼 **Work Experience**: Company details, positions, bullet points
- 🚀 **Projects**: Project names, URLs, descriptions, bullet points
- 🔨 **Auto-generated Build Scripts**: Individual build scripts for each resume
- 📄 **LaTeX Integration**: Works with your existing LaTeX template system

### **Using the Generator**

#### **1. Run the Generator**
```bash
python3 create_resume.py
```

Or if you've made it executable:
```bash
./create_resume.py
```

#### **2. Follow the Interactive Prompts**

The tool will guide you through:

1. **Resume Name**: Choose a name for your resume file
2. **Contact Information**: Your personal details
3. **Education**: Academic background
4. **Technical Skills**: Programming and technical expertise
5. **Work Experience**: Job history with bullet points
6. **Projects**: Personal or academic projects

#### **3. Generated Files**

After completion, the tool creates:

- `specifics/[resume_name].tex` - Your main resume LaTeX file (copies the template)
- `specifics/[resume_name]_defaults.tex` - Your resume's default values
- `specifics/build_[resume_name].sh` - Individual build script

#### **4. Build Your Resume**

**Option 1: Build Individual Resume**
```bash
cd specifics
./build_[resume_name].sh
```

**Option 2: Build All Resumes**
```bash
./build.sh
```

### **Generator Example Workflow**

```bash
$ python3 create_resume.py

============================================================
🎯 RESUME GENERATOR
Create a new resume template with interactive customization
============================================================

Enter a name for your resume (e.g., 'my_resume'): john_doe_resume

Creating resume: john_doe_resume

Let's customize your resume step by step...

📧 CONTACT INFORMATION
------------------------------
Full Name: John Doe
City, State/Province: San Francisco, CA
Phone Number: +1 (555) 123-4567
Email Address: john.doe@email.com
LinkedIn URL (optional): https://linkedin.com/in/johndoe
GitHub URL (optional): https://github.com/johndoe

[... continues with education, skills, experience, projects ...]

============================================================
🎉 RESUME CREATED SUCCESSFULLY!
============================================================
📄 Resume file: specifics/john_doe_resume.tex
⚙️  Defaults file: specifics/john_doe_resume_defaults.tex
🔨 Build script: specifics/build_john_doe_resume.sh

📋 NEXT STEPS:
1. Review and edit the generated files in the 'specifics/' directory
2. Run the build script to generate your PDF:
   cd specifics && ./build_john_doe_resume.sh
3. Or use the main build script to build all resumes:
   ./build.sh

💡 TIP: You can further customize your resume by editing the LaTeX files directly!
============================================================
```

---

## 🏗️ **System Architecture**

This system allows you to maintain a single master resume with toggleable experiences and projects, enabling you to create customized versions for different applications.

### **Core Files:**
- `template.tex` - Master template with toggleable sections
- `defaults.tex` - All default values and content
- `build.sh` - Automated build script
- `create_resume.py` - Interactive resume generator
- `specifics/` - Folder containing resume files (both wrappers and generated)
- `output/` - Generated PDF files

### **How It Works:**
1. **Master Template**: Contains all sections with conditional rendering
2. **Default Values**: All content defined as variables with defaults
3. **Two Approaches**: 
   - **Wrapper Files**: Override only what's different, inherit everything else
   - **Generated Files**: Full template copy with separate defaults file
4. **Toggle System**: Enable/disable experiences and projects to control length

## 📁 **File Structure**

```
master/
├── create_resume.py          # 🎯 Interactive resume generator
├── template.tex             # 📄 Master template with toggles
├── defaults.tex             # ⚙️ All default values
├── build.sh                 # 🔨 Build script
├── specifics/               # 📁 Resume files
│   ├── coop.tex            # Standard co-op resume (wrapper)
│   ├── intern.tex          # Standard intern resume (wrapper)
│   ├── short_coop.tex      # 1-page co-op version (wrapper)
│   └── [generated].tex     # Generated by create_resume.py
└── output/                 # 📄 Generated PDFs
```

## 🎛️ **Toggle System**

### **Experience Toggles:**
- `\def\exponeenabled{1}` - Show Experience 1
- `\def\exptwoenabled{1}` - Show Experience 2  
- `\def\expthreeenabled{1}` - Show Experience 3

### **Project Toggles:**
- `\def\projectoneenabled{1}` - Show Edge Detection project
- `\def\projecttwoenabled{1}` - Show AI Chatbot project

### **Usage Examples:**

**Full Resume (All experiences):**
```latex
\def\exponeenabled{1}
\def\exptwoenabled{1}
\def\expthreeenabled{1}
\def\projectoneenabled{1}
\def\projecttwoenabled{1}
```

**Short Resume (1 experience):**
```latex
\def\exponeenabled{1}
\def\exptwoenabled{0}
\def\expthreeenabled{0}
\def\projectoneenabled{1}
\def\projecttwoenabled{0}
```

**Web Development Focused:**
```latex
\def\exponeenabled{1}  % Keep web development experience
\def\exptwoenabled{0}  % Hide research experience
\def\expthreeenabled{1} % Keep startup experience
```

## 🚀 **Usage**

### **Building All Resumes:**
```bash
bash build.sh
```

### **Creating a New Resume Version:**

#### **Option 1: Using the Generator (Recommended)**
```bash
python3 create_resume.py
```
Follow the interactive prompts to create a new resume template.

#### **Option 2: Manual Creation**

1. **Create wrapper file** in `specifics/` folder:
```latex
%-------------------------
% My Custom Resume
%------------------------

% Include default values first
\input{defaults.tex}

% Override only what's different
\def\email{my.email@example.com}
\def\languages{JavaScript, TypeScript, Python, HTML, CSS}

% Toggle experiences
\def\exponeenabled{1}
\def\exptwoenabled{0}
\def\expthreeenabled{1}

% Include master template
\input{template.tex}
```

**Note**: The generator creates files differently - it copies the full template and creates a separate defaults file, while manual creation uses the wrapper approach.

2. **The build script automatically detects** and builds your new file!

### **Customizing Content:**

**Override any variable** from `defaults.tex`:
```latex
% Change technical skills
\def\languages{JavaScript, TypeScript, Python, HTML, CSS}

% Change experience content
\def\exponeitemone{My customized experience description}

% Change project details
\def\projectoneitemone{My customized project description}
```

## 🎯 **Benefits**

### **Flexibility:**
- ✅ **Toggle Experiences**: Show/hide to control resume length
- ✅ **Customize Content**: Override any variable as needed
- ✅ **Inherit Defaults**: Only specify what's different
- ✅ **Auto-Detection**: Build script finds all resume files
- ✅ **Interactive Generator**: Easy setup for new users

### **Maintainability:**
- ✅ **Single Source**: Update content once in `defaults.tex`
- ✅ **Modular Design**: Each experience/project is independent
- ✅ **Clean Structure**: Clear separation of concerns

### **Efficiency:**
- ✅ **Quick Customization**: Minimal code for new versions
- ✅ **Length Control**: Easy 1-page vs multi-page versions
- ✅ **Focus Control**: Show relevant experiences per application
- ✅ **Automated Setup**: Generator handles initial configuration

## 📝 **Example Use Cases**

### **1. Standard Applications:**
- Use `coop.tex` or `intern.tex` (all experiences enabled)

### **2. 1-Page Applications:**
- Use `short_coop.tex` (only most recent experience)

### **3. Role-Specific Applications:**
- Create `webdev_resume.tex` for web development positions
- Create `fullstack_resume.tex` for full-stack positions
- Create `data_science_resume.tex` for data science positions

### **4. Company-Specific Customization:**
- Create `tech_company_resume.tex` with company-specific content
- Create `startup_resume.tex` with startup-focused content

## 🔧 **Advanced Features**

### **Error Logging:**
- Failed compilations create detailed log files
- Successful builds clean up automatically
- Build summary shows which files had errors

### **Automatic Detection:**
- Build script finds all `.tex` files in `specifics/`
- No need to update build script when adding new resumes
- Clean separation of build logic and content

### **Generator Features:**
- Interactive prompts for easy setup
- Automatic file generation and organization
- Individual build scripts for each resume
- Comprehensive documentation and help
- Creates standalone files (not wrappers)

## 📋 **Prerequisites**

- Python 3.6 or higher (for the generator)
- LaTeX installation (pdflatex)
- Your existing resume template system

## 🛠️ **Troubleshooting**

### **Common Issues**

1. **Permission Denied**: Make sure the script is executable
   ```bash
   chmod +x create_resume.py
   ```

2. **LaTeX Not Found**: Ensure pdflatex is installed
   ```bash
   which pdflatex
   ```

3. **Build Errors**: Check the generated LaTeX files for syntax errors

### **Getting Help**

- Review the generated files for any syntax issues
- Check the build logs for specific error messages
- Ensure all required LaTeX packages are installed

## 💡 **Tips**

- **Resume Names**: Use descriptive names like `software_engineer_resume` or `data_scientist_resume`
- **Bullet Points**: Be specific and use action verbs for experience and projects
- **Skills**: Group related skills together (e.g., "Python, JavaScript, TypeScript")
- **URLs**: Include full URLs for LinkedIn and GitHub profiles
- **LaTeX Knowledge**: Basic LaTeX knowledge helps with advanced customization
- **File Types**: Generator creates standalone files, manual creation uses wrapper approach

This system gives you maximum flexibility while maintaining clean, maintainable code!

---

**Happy Resume Building! 🎉**
