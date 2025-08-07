# captchaSaz (generator)
<br>
<div align="center">
  <img src="https://img.shields.io/pypi/l/captchaSaz">
  <img src="https://img.shields.io/badge/_auth-undrdskm-blue">
  <img src="https://img.shields.io/pypi/dw/captchaSaz">
  <img src="https://img.shields.io/pypi/pyversions/captchaSaz">
</div>
<hr>
this is a captcha generator made with pillow.
it has three function in current version:

1 . Random Text Creator: randomText() 

2. Generate Image Captcha: generate()

3. Checks the entered Captcha: check()

 
<br>

## Usage

```python
from captchaSaz import *

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
1. ### Pypi
   + `pip install captchaSaz==2.0.4` is available now!
   + `from captchaSaz import *`
   + `generate()`


2. ### Github Clone
    + `git clone https://github.com/UndrDsk0M/captcha_generator`
    + `pip install -r requirments.txt`
    + `python3 captcha_generator.py` or use it as `from capcha_generator import *`



<hr>

- ## Update:
+ now available in pypi packeges!
+ path issue fixed
+ Got inline documents!
+ check function added!
+ rewriting with typing rules
+ adding an option to add lines in Image Captcha 
+ entering the text



# demo: 
<img width="500" height="200" alt="tmp7929o9wm" src="https://github.com/user-attachments/assets/c3394a3c-a819-4398-b729-3f9d83d450fa" />
<img width="500" height="200" alt="tmpqcdr0em7" src="https://github.com/user-attachments/assets/dd04485f-86d2-47f1-b0ee-7251a3c67d61" />
<img width="500" height="200" alt="tmpe99ew9rc" src="https://github.com/user-attachments/assets/4b456d54-333f-4d28-8c20-c0bcbe6c55aa" />
<img width="500" height="200" alt="tmpgc958lbk" src="https://github.com/user-attachments/assets/741c8887-77a9-40c2-82ea-f038bae16092" />

<br>
<hr> 

### links

made by <a href="https://gravatar.com/fantasticcherryblossomef40d159a8">ehsan(undrdsk0m)</a>

<a href="">MIT License</a>

Copyright (c) 2025 <a href="https://gravatar.com/fantasticcherryblossomef40d159a8">UndrDsk0M</a>
