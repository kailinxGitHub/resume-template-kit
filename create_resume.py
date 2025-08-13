#!/usr/bin/env python3
"""
Resume Generator CLI Tool
Creates new resume templates with interactive customization options
"""

import os
import sys
from pathlib import Path
import re
from datetime import datetime

class ResumeGenerator:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.specifics_dir = self.project_root / "specifics"
        self.output_dir = self.project_root / "output"
        self.template_file = self.project_root / "template.tex"
        
    def print_banner(self):
        """Display welcome banner"""
        print("=" * 60)
        print("🎯 RESUME GENERATOR")
        print("Create a new resume template with interactive customization")
        print("=" * 60)
        print()
    
    def get_user_input(self, prompt, default="", required=True):
        """Get user input with validation"""
        while True:
            if default:
                user_input = input(f"{prompt} (default: {default}): ").strip()
                if not user_input:
                    user_input = default
            else:
                user_input = input(f"{prompt}: ").strip()
            
            if not required or user_input:
                return user_input
            print("❌ This field is required. Please try again.")
    
    def get_contact_info(self):
        """Collect basic contact information"""
        print("\n📧 CONTACT INFORMATION")
        print("-" * 30)
        
        contact_info = {}
        contact_info['name'] = self.get_user_input("Full Name")
        contact_info['location'] = self.get_user_input("City, State/Province")
        contact_info['phone'] = self.get_user_input("Phone Number")
        contact_info['email'] = self.get_user_input("Email Address")
        contact_info['linkedin'] = self.get_user_input("LinkedIn URL (optional)", required=False)
        contact_info['github'] = self.get_user_input("GitHub URL (optional)", required=False)
        
        return contact_info
    
    def get_education_info(self):
        """Collect education information"""
        print("\n🎓 EDUCATION")
        print("-" * 30)
        
        education = {}
        education['university'] = self.get_user_input("University/Institution Name")
        education['dates'] = self.get_user_input("Dates (e.g., Sep 2023 -- May 2027)")
        education['degree'] = self.get_user_input("Degree and Major")
        education['gpa'] = self.get_user_input("GPA (e.g., 3.6/4.0)")
        education['location'] = self.get_user_input("University Location")
        education['coursework'] = self.get_user_input("Relevant Coursework (comma-separated)")
        education['competitions'] = self.get_user_input("Competitions/Awards (optional)", required=False)
        education['clubs'] = self.get_user_input("Clubs/Organizations (optional)", required=False)
        
        return education
    
    def get_technical_skills(self):
        """Collect technical skills"""
        print("\n💻 TECHNICAL SKILLS")
        print("-" * 30)
        
        skills = {}
        skills['languages'] = self.get_user_input("Programming Languages (comma-separated)")
        skills['frameworks'] = self.get_user_input("Frameworks & Libraries (comma-separated)")
        skills['cloud_databases'] = self.get_user_input("Cloud & Databases (comma-separated)")
        skills['devops_tools'] = self.get_user_input("DevOps & Tools (comma-separated)")
        
        return skills
    
    def get_experience_info(self):
        """Collect work experience information"""
        print("\n💼 WORK EXPERIENCE")
        print("-" * 30)
        
        experiences = []
        experience_count = 0
        
        while True:
            add_experience = input(f"\nAdd experience #{experience_count + 1}? (y/n): ").lower().strip()
            if add_experience != 'y':
                break
            
            print(f"\n--- Experience #{experience_count + 1} ---")
            experience = {}
            experience['company'] = self.get_user_input("Company Name")
            experience['dates'] = self.get_user_input("Employment Dates")
            experience['position'] = self.get_user_input("Job Title")
            experience['location'] = self.get_user_input("Location")
            
            # Get bullet points
            print("\nEnter bullet points (press Enter twice to finish):")
            bullet_points = []
            while True:
                bullet = input(f"Bullet point {len(bullet_points) + 1}: ").strip()
                if not bullet:
                    break
                bullet_points.append(bullet)
            
            experience['bullet_points'] = bullet_points
            experiences.append(experience)
            experience_count += 1
        
        return experiences
    
    def get_project_info(self):
        """Collect project information"""
        print("\n🚀 PROJECTS")
        print("-" * 30)
        
        projects = []
        project_count = 0
        
        while True:
            add_project = input(f"\nAdd project #{project_count + 1}? (y/n): ").lower().strip()
            if add_project != 'y':
                break
            
            print(f"\n--- Project #{project_count + 1} ---")
            project = {}
            project['name'] = self.get_user_input("Project Name")
            project['url'] = self.get_user_input("Project URL (optional)", required=False)
            project['dates'] = self.get_user_input("Project Dates")
            
            # Get bullet points
            print("\nEnter bullet points (press Enter twice to finish):")
            bullet_points = []
            while True:
                bullet = input(f"Bullet point {len(bullet_points) + 1}: ").strip()
                if not bullet:
                    break
                bullet_points.append(bullet)
            
            project['bullet_points'] = bullet_points
            projects.append(project)
            project_count += 1
        
        return projects
    
    def generate_latex_content(self, contact_info, education, skills, experiences, projects):
        """Generate LaTeX content from collected information"""
        
        # Build content using string concatenation to avoid f-string issues
        content = []
        
        # Header Information
        content.append("% Header Information")
        content.append(f"\\def\\name{{{contact_info['name']}}}")
        content.append(f"\\def\\location{{{contact_info['location']}}}")
        content.append(f"\\def\\phone{{{contact_info['phone']}}}")
        content.append(f"\\def\\email{{{contact_info['email']}}}")
        
        if contact_info['linkedin']:
            linkedin_short = contact_info['linkedin'].replace('https://', '').replace('www.', '')
            content.append(f"\\def\\linkedinurl{{{contact_info['linkedin']}}}")
            content.append(f"\\def\\linkedintext{{{linkedin_short}}}")
        else:
            content.append("\\def\\linkedinurl{}")
            content.append("\\def\\linkedintext{}")
        
        if contact_info['github']:
            github_short = contact_info['github'].replace('https://', '').replace('www.', '')
            content.append(f"\\def\\githuburl{{{contact_info['github']}}}")
            content.append(f"\\def\\githubtext{{{github_short}}}")
        else:
            content.append("\\def\\githuburl{}")
            content.append("\\def\\githubtext{}")
        
        # Education
        content.append("")
        content.append("% Education")
        content.append(f"\\def\\university{{{education['university']}}}")
        content.append(f"\\def\\universitydates{{{education['dates']}}}")
        content.append(f"\\def\\degree{{{education['degree']}}}")
        content.append(f"\\def\\gpa{{{education['gpa']}}}")
        content.append(f"\\def\\universitylocation{{{education['location']}}}")
        content.append(f"\\def\\coursework{{{education['coursework']}}}")
        
        if education['competitions']:
            content.append(f"\\def\\competitions{{{education['competitions']}}}")
        else:
            content.append("\\def\\competitions{}")
        
        if education['clubs']:
            content.append(f"\\def\\clubs{{{education['clubs']}}}")
        else:
            content.append("\\def\\clubs{}")
        
        # Technical Skills
        content.append("")
        content.append("% Technical Skills")
        content.append(f"\\def\\languages{{{skills['languages']}}}")
        content.append(f"\\def\\frameworks{{{skills['frameworks']}}}")
        content.append(f"\\def\\clouddatabases{{{skills['cloud_databases']}}}")
        content.append(f"\\def\\devopstools{{{skills['devops_tools']}}}")
        
        # Experience sections
        for i, exp in enumerate(experiences, 1):
            exp_num = {1: 'one', 2: 'two', 3: 'three'}.get(i, str(i))
            content.append("")
            content.append(f"% Experience {i}")
            content.append(f"\\def\\exp{exp_num}enabled{{1}}")
            content.append(f"\\def\\exp{exp_num}company{{{exp['company']}}}")
            content.append(f"\\def\\exp{exp_num}dates{{{exp['dates']}}}")
            content.append(f"\\def\\exp{exp_num}position{{{exp['position']}}}")
            content.append(f"\\def\\exp{exp_num}location{{{exp['location']}}}")
            
            for j, bullet in enumerate(exp['bullet_points'], 1):
                item_name = 'one' if j == 1 else 'two' if j == 2 else 'three' if j == 3 else 'four' if j == 4 else 'five'
                content.append(f"\\def\\exp{exp_num}item{item_name}{{{bullet}}}")
            
            # Fill remaining bullet points with empty content
            for j in range(len(exp['bullet_points']) + 1, 6):
                item_name = 'one' if j == 1 else 'two' if j == 2 else 'three' if j == 3 else 'four' if j == 4 else 'five'
                content.append(f"\\def\\exp{exp_num}item{item_name}{{}}")
        
        # Disable unused experience slots
        for i in range(len(experiences) + 1, 4):
            exp_num = {1: 'one', 2: 'two', 3: 'three'}[i]
            content.append("")
            content.append(f"% Experience {i} (disabled)")
            content.append(f"\\def\\exp{exp_num}enabled{{0}}")
        
        # Project sections
        for i, proj in enumerate(projects, 1):
            proj_num = {1: 'one', 2: 'two'}.get(i, str(i))
            content.append("")
            content.append(f"% Project {i}")
            content.append(f"\\def\\project{proj_num}enabled{{1}}")
            
            if proj['url']:
                url_line = "\\def\\project" + proj_num + "url{\\href{" + proj['url'] + "}{\\underline{\\textbf{" + proj['name'] + "}}}}"
                content.append(url_line)
            else:
                url_line = "\\def\\project" + proj_num + "url{\\underline{\\textbf{" + proj['name'] + "}}}"
                content.append(url_line)
            
            content.append(f"\\def\\project{proj_num}dates{{{proj['dates']}}}")
            
            for j, bullet in enumerate(proj['bullet_points'], 1):
                item_name = 'one' if j == 1 else 'two' if j == 2 else 'three' if j == 3 else 'four' if j == 4 else 'five'
                content.append(f"\\def\\project{proj_num}item{item_name}{{{bullet}}}")
            
            # Fill remaining bullet points with empty content
            for j in range(len(proj['bullet_points']) + 1, 6):
                item_name = 'one' if j == 1 else 'two' if j == 2 else 'three' if j == 3 else 'four' if j == 4 else 'five'
                content.append(f"\\def\\project{proj_num}item{item_name}{{}}")
        
        # Disable unused project slots
        for i in range(len(projects) + 1, 3):
            proj_num = {1: 'one', 2: 'two'}[i]
            content.append("")
            content.append(f"% Project {i} (disabled)")
            content.append(f"\\def\\project{proj_num}enabled{{0}}")
        
        return "\n".join(content)
    
    def create_resume_files(self, resume_name, latex_content):
        """Create the resume files"""
        
        # Create specifics directory if it doesn't exist
        self.specifics_dir.mkdir(exist_ok=True)
        
        # Create the main resume .tex file
        resume_file = self.specifics_dir / f"{resume_name}.tex"
        
        # Read template and create the new resume file
        with open(self.template_file, 'r') as f:
            template_content = f.read()
        
        with open(resume_file, 'w') as f:
            f.write(template_content)
        
        # Create the defaults file for this resume
        defaults_file = self.specifics_dir / f"{resume_name}_defaults.tex"
        with open(defaults_file, 'w') as f:
            f.write(f"""%-------------------------
% Default Resume Values for {resume_name}
% Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
%------------------------

{latex_content}
""")
        
        # Create a build script for this specific resume
        build_script = self.specifics_dir / f"build_{resume_name}.sh"
        with open(build_script, 'w') as f:
            f.write(f"""#!/bin/bash

# Build script for {resume_name} resume
echo "Building {resume_name} resume..."

# Compile the resume
pdflatex -interaction=nonstopmode "{resume_name}.tex"

if [ $? -eq 0 ]; then
    echo "✅ {resume_name}.pdf created successfully"
    # Move PDF to output directory
    mkdir -p ../output
    mv "{resume_name}.pdf" "../output/"
    
    # Clean up auxiliary files
    rm -f *.aux *.log *.out *.fls *.fdb_latexmk *.synctex.gz
else
    echo "❌ Error building {resume_name}.pdf"
fi
""")
        
        # Make build script executable
        os.chmod(build_script, 0o755)
        
        return resume_file, defaults_file, build_script
    
    def run(self):
        """Main execution flow"""
        self.print_banner()
        
        # Get resume name
        resume_name = self.get_user_input("Enter a name for your resume (e.g., 'my_resume'): ")
        resume_name = re.sub(r'[^a-zA-Z0-9_]', '_', resume_name.lower())
        
        print(f"\nCreating resume: {resume_name}")
        print("\nLet's customize your resume step by step...")
        
        # Collect all information
        contact_info = self.get_contact_info()
        education = self.get_education_info()
        skills = self.get_technical_skills()
        experiences = self.get_experience_info()
        projects = self.get_project_info()
        
        # Generate LaTeX content
        latex_content = self.generate_latex_content(contact_info, education, skills, experiences, projects)
        
        # Create files
        resume_file, defaults_file, build_script = self.create_resume_files(resume_name, latex_content)
        
        # Success message
        print("\n" + "=" * 60)
        print("🎉 RESUME CREATED SUCCESSFULLY!")
        print("=" * 60)
        print(f"📄 Resume file: {resume_file}")
        print(f"⚙️  Defaults file: {defaults_file}")
        print(f"🔨 Build script: {build_script}")
        print("\n📋 NEXT STEPS:")
        print("1. Review and edit the generated files in the 'specifics/' directory")
        print("2. Run the build script to generate your PDF:")
        print(f"   cd specifics && ./build_{resume_name}.sh")
        print("3. Or use the main build script to build all resumes:")
        print("   ./build.sh")
        print("\n💡 TIP: You can further customize your resume by editing the LaTeX files directly!")
        print("=" * 60)

def main():
    """Main entry point"""
    try:
        generator = ResumeGenerator()
        generator.run()
    except KeyboardInterrupt:
        print("\n\n❌ Operation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
