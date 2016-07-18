
import codecs

'''
quran = codecs.open('../Assets/QuranText/ayah.txt', 'r', encoding="utf-8")
'''

i = 0x600
while i <= 0x6ff:
    s = '<Char name=\"\"\tglyph=\"' + chr(i) + '\"\tunicode=\"' + hex(i) + '\"\tappCode=\"' + str(i - 0x600) + '\"/>'
    print(s)
    i = i + 1
