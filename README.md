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
    + `git clone https://github.com/UndrDsk0M/captcha_generator`
    + `pip install -r requirments.txt`
    + `python3 captcha_generator.py` or use it as `from capcha_generator import *`



<hr>

- ## Update:
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




