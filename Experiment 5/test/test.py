import sys

def disp_size(text:str):
    print(text, ' ', sys.getsizeof(text.encode('utf-8')))

disp_size("1")
disp_size("12")
disp_size("123")

disp_size("a")
disp_size("ab")
disp_size("abc")

disp_size("你")
disp_size("你好")
disp_size("你好呀")


