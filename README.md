# Word Search in PDF and DOCX Files

This Python script searches for a specific word in PDF and DOCX files within a given directory and its subdirectories, printing the names of the files containing the word.

## Dependencies

To run this script, you will need to have the following Python packages installed:

- PyPDF2: A Python library for reading and writing PDF files.
- python-docx: A Python library for creating and updating Microsoft Word (.docx) files.

You can install these packages using pip:

```
pip install PyPDF2
pip install python-docx
```

## Usage

The script can be executed by running `python <script_name>.py` in your terminal/command prompt.

To search for a word, modify the following lines in the `main()` function:

```python
word = "your_search_word_here"
path = "your_directory_here/"
```

Replace `"your_search_word_here"` with the word you want to search for and `"your_directory_here/"` with the path to the directory containing the files.

## Functionality

The script defines two main functions:

1. `search_word_in_files(word, path)`:
   - Takes two arguments: `word` (the word to search for) and `path` (the path to the directory containing the files).
   - Searches for the given word in all PDF and DOCX files in the specified directory and its subdirectories.
   - If the word is found in a file, the file's name is added to the `found_files` set.
   - Finally, the script prints the names of the files containing the word.

2. `main()`:
   - Calls the `search_word_in_files(word, path)` function with the specified word and path.

The script is executed by calling the `main()` function when it's run as the main module.
