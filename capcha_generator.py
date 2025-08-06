from PIL import Image, ImageDraw, ImageFont
import logging
from os import getcwd
import random
import string

def randomText(length:int=6, number:bool=True, lowercase_char:bool=True, 
               uppercase_char:bool=False, symbol:bool=False, other=[]) -> str:
    """this function create a random text that can pass to generate function to create captcha

    Args:
        length (int, optional): _the length of the random text_. Defaults to 6.
        number (bool, optional): _do you want to include numbers too or not_. Defaults to True.
        lowercase_char (bool, optional): _do you want to include lowercase-chars or not_. Defaults to True.
        uppercase_char (bool, optional): _do you want to include uppercase-chars or not_. Defaults to False.
        symbol (bool, optional): _do you want to include random symbols as #@$%^ or not_. Defaults to False.
        other (list, optional): _a list of other chars you want to use_. Defaults to [].
    
    Raise:
        TypeError: when you enter others in the wrong way
    Returns:
        str: a random generated text
    """
    chars = []
    if number:
        for int in range(0, 9):
            chars.append(str(int))
    if lowercase_char:
        for char in string.ascii_lowercase:
            chars.append(str(char))
    if uppercase_char:
        for char in string.ascii_uppercase:
            chars.append(str(char))
    if symbol:
        for char in string.punctuation:
            chars.append(str(char))
    if len(other) > 0:
        for item in other:
            if len(item) == 1: 
                chars.append(str(item))
            else :
                raise TypeError("randomText func got an incorrect 'other'\nother should be a list created by one chars item, example: other= ['!', 'width', ' ', 'خ']")
    chars = (random.choices(chars, k=length))
    random_text:str = ""
    for char in chars :
        random_text += char 
    return random_text    

def generate(text:str="randomText", width:int=500, height:int=200,
             incld_circle:bool=True, incld_line:bool=True, random_fcolor:bool=False) -> (object, str):
    """This function will create a image captcha

    Args:
        text (str): the text content of the captcha. Defaults to the `randomText()` function.
        width (int, optional): width of the output image. Defaults to 500.
        height (int, optional): heigth of the output image. Defaults to 200.
        incld_circle (bool, optional): including random circles to captcha. Defaults to True.
        incld_line (bool, optional): including random lines to captcha. Defaults to True.
        random_fcolor (bool, optional): when you on it, it randomly choose the font color black/white. Defaults to False.

    Returns:
        object: it returns a pillow object 
        you can even open it with `.show()`
        str: with the original text
    """
    if text == "randomText" :
        text = randomText()
        
    r, g, b = random.randint(200,255),random.randint(200,255),random.randint(150,255) 
    main_dir:str = getcwd()

    image = Image.new("RGB", (width, height), (r, g, b))
    edit_image = ImageDraw.Draw(image)

    cycle:int = random.randint(5, 10)
    for i in range(0, cycle):
        if incld_circle:
            #drawing random circles
            circle_size:int = random.randint(10,100)
            pos_x:int = random.randint(0, (width-20))
            pos_y:int = random.randint(0, (height-20))
            color:[int, int, int] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            border:int = random.randint(1, 5)
            edit_image.circle((pos_x, pos_y), radius=circle_size, outline=color, width=border)
        if incld_line:
            #drawing random lines
            start_x:int = random.randint(10, width)
            start_y:int = random.randint(10, height) 
            end_x:int = random.randint(10, width)
            end_y:int =  random.randint(10, height) 
            shape:[[int, int], [int, int]] = [(start_x, start_y), (end_x, end_y)]
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            border = random.randint(1, 10)
            edit_image.line(shape, fill=color, width=border)
    fonts = ['fonts/Carmitta.ttf', 'fonts/Lemon Shake Shake.ttf', 'fonts/Meditative.ttf', 'fonts/Pusing Kali.ttf', 'fonts/Southport.ttf']

    between_space = width / (len(text) + 1)
    x_index = between_space
    y_index = height / 2
    for char in text:
        # setting the text in image 
        font_name = random.choice(fonts)
        font_path = (f"{main_dir}/{font_name}") if (__name__=='__main__') else font_name
        logging.info(font_path)
        font = ImageFont.truetype(font_path, width/10) 
        if random_fcolor:
            color = (0, 0, 0) if random.choice([True, False]) else (255, 255, 255) 
        else :
            color = (0, 0, 0)
        edit_image.text((x_index, y_index), char, fill=color, font=font)
        x_index += between_space

    return image, text
    
    
def check(usr_input:str, captcha_content:str) -> bool:
    """A func to checks if client entered the exact capctha

    Args:
        usr_input (str): _the client enterd text_
        captcha_content (str): _the captcha text_

    Returns:
        bool: _description_
    """
    if usr_input == captcha_content :
        return True
    else :
        return False


if __name__ == "__main__":
    captcha_image, captcha_text = generate()
    captcha_image.show()
    client_ = input('Enter captcha: ')
    if check(client_, captcha_text) :
        print('Loged in!')
    else :
        print('Your are a fucking robot')
        print(text)
