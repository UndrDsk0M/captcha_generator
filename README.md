# captcha generator
<hr>
this is a captcha generator made with pillow
it has three function in current version:
    1. Random Text Creator: randomText()
    2. Generate Image Captcha: generate()
    3. checks the entered Captcha: check()


```python
captcha_image, captcha_text = generate()
captcha_image.show()
client_ = input('Enter captcha: ')
if check(client_, captcha_text) :
    print('Loged in!')
else :
    print('Your are a damn robot')
    print(text)
    print('I KNEW YOU WERE A ROBOT!')
```
<hr>

## Instalation
1. `Pip install` not available yet!
2. 
    `git clone https://github.com/UndrDsk0M/captcha_generator`
    `pip install -r requirments.txt`
    `python3 captcha_generator.py` or use it as `from capcha_generator import *`



<hr>

- ## Update:
+ Got inline documents!
+ check function added!
+ rewriting with typing rules
+ adding an option to add lines in Image Captcha 
+ entering the text



# example1
![image](https://github.com/user-attachments/assets/41f91e05-a488-4ee9-bffb-ed45c68efe97)

# exmple2
![image](https://github.com/user-attachments/assets/a482c014-ce86-4cb5-a756-cd2e0cb1b05a)
