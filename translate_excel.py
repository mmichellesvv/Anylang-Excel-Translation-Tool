import os
import argparse
import pandas as pd
from translate import Translator


def translate_excel(wait, froml, tol):
    files_in_directory = os.listdir()

    excel_files = [f for f in files_in_directory if f.endswith('.xlsx')]

    if not excel_files:
        print("No Excel files found in the directory.")
        return

    input_file = excel_files[0]
    print(f"\nFILENAME: {input_file}\n\n{wait}")


    df = pd.read_excel(input_file)

    translator = Translator(from_lang=froml, to_lang=tol)

    def translating(text):
        if isinstance(text, str):
            return translator.translate(text)
        return text

    # Translate each column of the DataFrame
    translated_df = df.apply(lambda col: col.map(translating))

    output_file = f'{tol}_{input_file}'

    translated_df.to_excel(output_file, index=False)
    print(f"\nTRANSLATION SUCCESSFUL. The file has been saved as {output_file}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Translate the first found Excel file in the directory from one language to another.")
    parser.add_argument('from_lang', type=str, help='Language code of the source language (e.g., "ru" for Russian)')
    parser.add_argument('to_lang', type=str, help='Language code of the target language (e.g., "uk" for Ukrainian)')

    args = parser.parse_args()
    wait = "- Your request is being processed, this could take a little while..."

    translate_excel(wait, args.from_lang, args.to_lang)

# pip install translate, pip install pandas in terminal
# play - python translate_excel.py ru uk