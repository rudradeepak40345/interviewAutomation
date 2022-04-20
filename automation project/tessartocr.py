import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
img = cv2.imread(r"C:\Users\DELL\OneDrive\Desktop\0001.jpg")
#img = cv2.resize(img,(400, 450))
##cv2.imshow(r"C:\Users\DELL\OneDrive\Desktop\picpic.png", img)
text = pytesseract.image_to_string(img)
strr = text.lower()
print(strr)
arr = strr.split()
s = len(arr)
# 
if "html" in strr:
    print("this guy knows HTML!!")

cv2.waitKey(0)
cv2.destroyAllWindows()