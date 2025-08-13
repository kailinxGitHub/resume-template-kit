#!/bin/bash

#-------------------------
# Resume Builder Script
# Builds all resume versions from LaTeX source
# Uses template.tex and defaults.tex as core files
#------------------------

echo "🧹 Cleaning old build artifacts..."
# Remove old PDF files and LaTeX auxiliary files
find . -name "*.pdf" -delete
find . -name "*.aux" -delete
find . -name "*.log" -delete
find . -name "*.out" -delete
find . -name "*.fls" -delete
find . -name "*.fdb_latexmk" -delete
find . -name "*.synctex.gz" -delete

echo "📄 Building all resume versions..."

# Automatically detect all .tex files in the specifics folder
resumes=($(find specifics -name "*.tex" -exec basename {} .tex \;))

# Build each resume from the root directory
for resume in "${resumes[@]}"; do
    echo "  Building $resume.tex..."
    
    # Compile from root directory, specifying the path to the .tex file
    # Log output to a specific file for this resume
    pdflatex -interaction=nonstopmode "specifics/$resume.tex" > "${resume}_build.log" 2>&1
    
    if [ $? -eq 0 ]; then
        echo "  ✅ $resume.pdf created successfully"
        # Move PDF to output directory
        mv "$resume.pdf" "output/"
        # Remove successful build log
        rm -f "${resume}_build.log"
    else
        echo "  ❌ Error building $resume.pdf - check ${resume}_build.log for details"
    fi
done

echo "🧹 Cleaning up auxiliary files..."
# Remove all LaTeX auxiliary files except PDFs and error logs
find . -name "*.aux" -delete
find . -name "*.log" -delete
find . -name "*.out" -delete
find . -name "*.fls" -delete
find . -name "*.fdb_latexmk" -delete
find . -name "*.synctex.gz" -delete

echo "📊 Build summary:"
echo "Generated PDFs:"
ls -la output/*.pdf 2>/dev/null || echo "No PDFs found"

# Check if there are any error logs
error_logs=$(find . -name "*_build.log" 2>/dev/null)
if [ -n "$error_logs" ]; then
    echo ""
    echo "⚠️  Error logs found:"
    echo "$error_logs"
    echo "Check these files for compilation errors."
else
    echo ""
    echo "🎉 Resume build complete! All PDFs are ready in the output/ directory."
fi
