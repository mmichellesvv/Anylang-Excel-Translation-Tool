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
af - Afrikaans
sq - Albanian
ar - Arabic
hy - Armenian
bn - Bengali
bs - Bosnian
ca - Catalan
hr - Croatian
cs - Czech
da - Danish
nl - Dutch
en - English
eo - Esperanto
et - Estonian
fi - Finnish
fr - French
de - German
el - Greek
gu - Gujarati
ht - Haitian Creole
ha - Hausa
he - Hebrew
hi - Hindi
hu - Hungarian
is - Icelandic
id - Indonesian
it - Italian
ja - Japanese
jw - Javanese
kn - Kannada
km - Khmer
ko - Korean
la - Latin
lv - Latvian
lt - Lithuanian
lb - Luxembourgish
mk - Macedonian
ml - Malayalam
mn - Mongolian
mr - Marathi
my - Myanmar (Burmese)
ne - Nepali
no - Norwegian
or - Odia
ps - Pashto
fa - Persian
pl - Polish
pt - Portuguese
pa - Punjabi
ro - Romanian
ru - Russian
sm - Samoan
gd - Scottish Gaelic
sr - Serbian
st - Sesotho
sn - Shona
sd - Sindhi
si - Sinhala
sk - Slovak
sl - Slovenian
so - Somali
es - Spanish
su - Sundanese
sw - Swahili
sv - Swedish
tg - Tajik
ta - Tamil
te - Telugu
th - Thai
tr - Turkish
uk - Ukrainian
ur - Urdu
vi - Vietnamese
cy - Welsh
xh - Xhosa
yi - Yiddish
yo - Yoruba
zu - Zulu

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
