from PIL import Image, ImageDraw, ImageFont
from os import getcwd
import random
import string

def generate(text="HelloWorld", x=500, y=200, hard=True):
    
    r, g, b = random.randint(200,255),random.randint(200,255),random.randint(150,255) 
    main_dir = getcwd()

    image = Image.new("RGB", (x, y), (r, g, b))
    edit_image = ImageDraw.Draw(image)

    cycle = random.randint(15, 20)
    for i in range(0, cycle):
        circle_size = random.randint(10,100)
        pos_x       = random.randint(0, (x-20))
        pos_y       = random.randint(0, (y-20))
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        width = random.randint(1, 5)
        edit_image.circle((pos_x, pos_y), radius=circle_size, outline=color, width=width)

    fonts = ['fonts/Carmitta.ttf', 'fonts/Lemon Shake Shake.ttf', 'fonts/Meditative.ttf', 'fonts/Pusing Kali.ttf', 'fonts/Southport.ttf']

    x_index = 10
    y_index = y / 2
    for char in text:
        
        font_name = random.choice(fonts)
        font_path = (f"{main_dir}/{font_name}") if (__name__=='__main__') else font_name
        print(font_path)
        font = ImageFont.truetype(font_path, x/10) 
        if hard:
            color = (0, 0, 0) if random.choice([True, False]) else (255, 255, 255) 
        else :
            color = (0, 0, 0)
        edit_image.text((x_index, y_index), char, fill=color, font=font)
        x_index += x/10

    return image
    
def RandomText(number=True, lowercase_char=True, uppercase_char=False, symbol=False, other=[]):
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
                raise TypeError("RandomText func got an incorrect 'other'\nother should be a list created by one chars item, example: other= ['!', 'X', ' ', 'خ']")
    chars = (random.choices(chars, k=10))
    random_text = ''
    for char in chars :
        random_text += char 
    return random_text    

text = RandomText()

generate(text=text, hard=False).show()
x = input('Enter captcha: ')
if x == text :
    print('Loged in!')
else :
    print('Your are fucking robot')
    print(text)