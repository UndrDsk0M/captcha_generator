# captcha generator

```python
from capcha_generator import *

text = RandomText() #args: number=True, lowercase_char=True, uppercase_char=False, symbol=False, other=[]

generate(text=text, hard=False).show()
x = input('Enter captcha: ')
if x == text :
    print('Loged in!')
else :
    print('Your are fucking robot')
    print(text)
text = 
```


### example1
![image](https://github.com/user-attachments/assets/41f91e05-a488-4ee9-bffb-ed45c68efe97)

### exmple2
![image](https://github.com/user-attachments/assets/a482c014-ce86-4cb5-a756-cd2e0cb1b05a)
