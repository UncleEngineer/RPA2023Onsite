from songline import Sendline

token = 'kG89J4K7BxUM5GTynIufN7njtbUPxDH5XSdKgJ5ERf2'

m = Sendline(token)

# m.sendtext('สวัสดี')
# m.sticker(118,1,'เย้')
# m.sendimage('https://www.khaosod.co.th/wpapp/uploads/2021/04/23-%E0%B8%AA%E0%B8%A0%E0%B8%B2%E0%B8%9E%E0%B8%AD%E0%B8%B2%E0%B8%81%E0%B8%B2%E0%B8%A8%E0%B8%A7%E0%B8%B1%E0%B8%99%E0%B8%99%E0%B8%B5%E0%B9%89.jpg')
# m.sendimage_file('test.png')

file = 'C:\\Users\\User\\OneDrive\\Desktop\\Basic Python\\test.png'
file = r'C:\Users\User\OneDrive\Desktop\Basic Python\test.png'

import os
path = os.getcwd()
filepath = os.path.join(path,'test.png')
m.sendimage_file(filepath)

#m.sendimage_file(file)