# from googletrans import Translator

# translator = Translator()

# hindi_sent = "नमस्कार, धृति!"
# translation = translator.translate(hindi_sent,dest="en")
# translated_sentence = (f"{translation.text}")
# print(translated_sentence)

from cv2 import cv2
import numpy as np
import pytesseract
# from google.colab import cv2_imshow

img = cv2.imread('test2.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
reduced_noise = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,12)
# cv2.imshow("",reduced_noise)
# cv2.waitKey(0)
print("\nImage is loaded succesfully")

text=pytesseract.image_to_string(reduced_noise,lang='eng')
print("The text is :\n",text)