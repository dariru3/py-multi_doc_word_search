import os
import PyPDF2
import docx

def search_word_in_files(word, path):
    found_files = set()
    
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith((".pdf", ".docx")):
                if file.endswith(".pdf"):
                    with open(os.path.join(root, file), "rb") as f:
                        pdf = PyPDF2.PdfReader(f)
                        
                        for page in pdf.pages:
                            if word in page.extract_text():
                                found_files.add(file)
                
                elif file.endswith(".docx"):
                    doc = docx.Document(os.path.join(root, file))
                    
                    for para in doc.paragraphs:
                        if word in para.text:
                            found_files.add(file)
    
    for found_file in found_files:
        print(f"Found '{word}' in {found_file}")

def main():
    word = "nature"
    path = "test/"
    
    search_word_in_files(word, path)

if __name__ == "__main__":
    main()
