# 在位于屏幕中央且宽度合适的方框内打印一个句子

sentence = input("Sentence: ")

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2  #整除向下圆整

print() #空行
#左边left_margin个空格，左上角一个‘+’号，然后（box_width-2）个‘-’号，右上角一个‘+’号
print(' ' * left_margin + '+' + '-' *(box_width - 2) + '+')
print(' ' * left_margin + '|' + ' ' * text_width + '|')
print(' ' * left_margin + '|' +      sentence     + '|')
print(' ' * left_margin + '|' + ' ' * text_width + '|')
print(' ' * left_margin + '+' + '-' *(box_width - 2) + '+')
#左边left_margin个空格，左下角一个‘+’号，然后（box_width-2）个‘-’号，右下角一个‘+’号
print()#空行
