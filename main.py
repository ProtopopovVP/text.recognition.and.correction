import cv2, pytesseract, enchant, difflib
from enchant.checker import SpellChecker

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('data/image3.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

config = r'--oem 3 --psm 6'
recognized_string = pytesseract.image_to_string(img, config=config)

corrected_string = recognized_string

checker = SpellChecker("en_US")
dictionary = enchant.Dict("en_US")
checker.set_text(corrected_string)

for i in checker:
    woi = i.word;
    suggestions = set(dictionary.suggest(woi))
    sim = dict()
    for word in suggestions:
        measure = difflib.SequenceMatcher(None, woi, word).ratio()
        sim[measure] = word
    suggested_word = sim[max(sim.keys())]
    corrected_string = corrected_string.replace(woi, suggested_word)

print(recognized_string)
print(corrected_string)
