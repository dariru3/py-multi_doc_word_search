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
                        pdf = PyPDF2.PdfFileReader(f)
                        
                        if pdf.isEncrypted:
                            try:
                                pdf.decrypt('')
                            except:
                                print(f"Failed to decrypt {file}. Skipping...")
                                continue
                        
                        for page in range(pdf.getNumPages()):
                            if word in pdf.getPage(page).extractText():
                                found_files.add(file)
                
                elif file.endswith(".docx"):
                    doc = docx.Document(os.path.join(root, file))
                    
                    for para in doc.paragraphs:
                        if word in para.text:
                            found_files.add(file)
    
    for found_file in found_files:
        print(f"Found '{word}' in {found_file}")

def main():
    word = "your_search_word"
    path = "your_directory_path"
    
    search_word_in_files(word, path)

if __name__ == "__main__":
    main()
