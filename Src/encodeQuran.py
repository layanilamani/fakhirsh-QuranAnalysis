
import codecs

quran = codecs.open('../Assets/QuranText/quran-simple-clean.txt', 'r', encoding="utf-8")

print("<Quran spaceCode = \"" + str(32 - 0x600) + "\">")

for ayat in quran:
    a = ayat.split('|')
    chapterNo   = a[0]
    ayahNo      = a[1]
    ayahText        = (a[2].split('\r'))[0]
    
    encodedAyah = ""
    i = 0
    for c in ayahText:
        if i < len(ayahText)-1:
            delimiter = ','
        else:
            delimiter = ''
        i = i + 1
        encodedAyah = encodedAyah + str(ord(c) - 0x600) + delimiter
    
    print("\t<Ayah chapterNo=\"" + a[0] + "\"\tayahNo=\"" + a[1] + "\"\ttext=\"" + encodedAyah + "\"/>")

print("</Quran>")

'''
i = 0x600
while i <= 0x6ff:
    s = '<Char name=\"\"\tglyph=\"' + chr(i) + '\"\tunicode=\"' + hex(i) + '\"\tappCode=\"' + str(i - 0x600) + '\"/>'
    print(s)
    i = i + 1
'''
