# excel-anylang-translator

Here is a description focused solely on the Excel translation tool:

---

# Excel Translation Tool

Repo provides a Python script for translating the contents of Excel files between different languages.

## Features

- **Automatic File Detection:** The script automatically detects the first Excel file in the current directory.
- **Language Translation:** Translates text from one language to another using the `translate` library.
- **Progress Indicator:** Displays a progress indicator while processing the translation.
- **Output Naming:** Saves the translated file with a prefix indicating the target language.

## Installation

To install the required libraries, run:
```bash
python 3.11.9
pip install translate pandas
```
## Catalogue Translation
Look into - **catalogue.txt**

## Usage

Run the translation script from the command line as follows:
```bash
python translate_excel.py [from_lang] [to_lang]
```
- `from_lang`: The language code of the source language (e.g., `"ru"` for Russian).
- `to_lang`: The language code of the target language (e.g., `"uk"` for Ukrainian).

### Example

To translate an Excel file from Russian to English:
```bash
python translate_excel.py ru uk
```

This will process the first `.xlsx` file found in the directory and save the translated file with a prefix indicating the target language.

## License

This project is licensed under the MIT License - see the MIT.md file for details.

---
