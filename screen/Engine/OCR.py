import string
import pytesseract
from PIL import Image, ImageOps, ImageFilter
from ..Services.Console_info import Console
from django.conf import settings
import cv2

class OCR:
    
    _temp_path = settings.PATHS["tmp"]
    tesseract_path = settings.PATHS["tesseract"]
    
    #_temp_path = "/usr/ptengine/PTengine/screen/static/temp/"

    def __init__(self) -> None:
        
        #pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
        pytesseract.pytesseract.tesseract_cmd = settings.PATHS["tesseract"]
        
        Console.info("Iniciando OCR")
        
        
        
    def convert(self, img_path):
        
        custom_config = r'--psm 6 -c tessedit_char_whitelist=0123456789'
        with Image.open(img_path) as img:
            img_to_gray = img.convert("L")  
            img_to_binary = img_to_gray.point(lambda p: p > 128 and 255)
            img_filtered = img_to_binary.filter(ImageFilter.MedianFilter())
            img_scaled = img_filtered.resize((img_filtered.width * 2, img_filtered.height * 2))
            img_scaled.save(f"{self._temp_path}binary.png")
            
            price = pytesseract.image_to_string(img_scaled, config=custom_config)

            Console.info(f"Precio obtenido : {price}")

        if price == "":
            img_to_gray = img.convert("L")  
            img_to_binary = img_to_gray.point(lambda p: p > 128 and 255)
            img_to_binary.save(f"{self._temp_path}binary.png")
             
            price = pytesseract.image_to_string(img_to_binary, config=custom_config)
            Console.info(f"Imagen convertida a string directamente : {price}")
        try:
                   
            return self._clean_string(price)
        
        except Exception as e:
            
            Console.warning("No se puedo convetir {price} a numeros")
            
            
    def _clean_string(self, string : string):
        
        delete_chars = " .,$"
        clean_string = string
        for char in delete_chars:
            clean_string = clean_string.replace(char, '')
        
        prince_float = float(clean_string)
        
        return prince_float
    
    def validate_number(self, path_img_cut) -> bool:
        
        path_img = f"{self._temp_path}img_cut_validate.png"
        with Image.open(path_img_cut) as img:
           img_to_binary = img.point(lambda p: p > 128 and 255)
           img_to_binary.save(path_img)
           
           price_convert = self.convert(path_img)
           
           if isinstance(price_convert, (int, float)):
               Console.success(f"Precio convertido analizado, si es un numero valido {price_convert}")
               return {"status" : True, "price" : price_convert}
           else:
               
               Console.warning(f"El precio convertido no es un numero{price_convert}")
               return {"status" : False, "price" : price_convert}
    
    def validate_consistency(self, price_convert, price_db):
        price_c = price_convert["price"]
        margin_factor = 0.2
        margin = price_c  * margin_factor
        
        if abs(price_db - price_c) <= margin:
            
            Console.info(f"Consistencia de precios correcta db : {price_db}, convert: {price_c }, margen: {margin}")
            return True
        else:
            
            Console.warning(f"Consistencia de precios Incorrecta db : {price_db}, convert: {price_c }, margen: {margin}")
            return False