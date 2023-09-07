import csv
from fpdf import FPDF

from importlib.resources import files, as_file


class Translator:
    def __init__(self):

        self.dict_file = as_file(files('data.symbols').joinpath('sun_dictionary.csv'))
        with as_file(files('data.fonts').joinpath('SUN7_8_1210.ttf')) as file:
            self.font_path = file
        self.sun_symbols = self.create_dict()

    def create_dict(self):

        sun_dict = {}
        with self.dict_file as dict_file:
            with open(dict_file) as file:
                reader = csv.reader(file)
                for row in reader:
                    sun_dict[row[0]] = row[1]

        return sun_dict

    def translateText(self, text):

        string_translated = []
        no_translation = []

        for word in text.split():
            if word in self.sun_symbols:
                string_translated.append(self.sun_symbols[word])
            else:
                word_capitalized = word.capitalize()
                word_lower = word.lower()
                if word_capitalized in self.sun_symbols:
                    string_translated.append(self.sun_symbols[word_capitalized])
                elif word_lower in self.sun_symbols:
                    string_translated.append(self.sun_symbols[word_lower])
                else:
                    no_translation.append(word)

        translated = (' '.join(string_translated))
        return translated

    def saveToPdf(self, text, save_file):
        pdf = FPDF(format="letter", unit="in")
        print(self.font_path)
        pdf.add_font(
            'SUN7_8_1210', '',
            fname=self.font_path)
        pdf.set_font('SUN7_8_1210', '', size=14)
        pdf.add_page()
        pdf.multi_cell(w=0, txt=text)
        pdf.output(save_file)
