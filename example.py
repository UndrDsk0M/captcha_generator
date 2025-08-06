from capcha_generator import *

captcha_image, captcha_text = generate()
captcha_image.show()
client_ = input('Enter captcha: ')
if check(client_, captcha_text) :
    print('Loged in!')
else :
    print('Your are a fucking robot')
    print(text)
