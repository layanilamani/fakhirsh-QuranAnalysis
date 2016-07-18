
import codecs

# Palindrome ayahs
quran = codecs.open('../Assets/QuranText/quran-simple-clean.txt', 'r', encoding="utf-8")
count = 0
for ayat in quran:
    a = ayat.split('|')
    chapterNo   = a[0]
    ayahNo      = a[1]
    ayahText    = (a[2].split('\r'))[0].replace(" ", "")
    
    s = ayahText[1:]

    if s == s[::-1]:
        print("Chapter: " + str(chapterNo) + " verse: " + str(ayahNo) + ", length: " + str(len(ayahText)) + " Text: " + ayahText)
        count = count + 1

print("Total palindromes: ", count)



'''
# ayah length frequencies
for i in range(690):
    count = 0
    quran = codecs.open('../Assets/QuranText/quran-simple-clean.txt', 'r', encoding="utf-8")
    for ayat in quran:
        a = ayat.split('|')
        chapterNo   = a[0]
        ayahNo      = a[1]
        ayahText        = (a[2].split('\r'))[0]

        if len(ayahText) == i:
            #print("Chapter: " + str(chapterNo) + " verse: " + str(ayahNo) + ", length: " + str(len(ayahText)) + "Text: " + ayahText)
            count = count + 1

    print(i, count)
'''


'''
# Longest ayah + ayahs of length == 19

quran = codecs.open('../Assets/QuranText/quran-simple-clean.txt', 'r', encoding="utf-8")

maxChap = 0
maxAyah = 0
maxLen = 0
maxAyahText = ""

count = 0
for ayat in quran:
    a = ayat.split('|')
    chapterNo   = a[0]
    ayahNo      = a[1]
    ayahText        = (a[2].split('\r'))[0]

    if len(ayahText) == 19:
        print("Chapter: " + str(chapterNo) + " verse: " + str(ayahNo) + ", length: " + str(len(ayahText)) + "Text: " + ayahText)
        count = count + 1    

    
    encodedAyah = ""
    i = 0
    for c in ayahText:
        if maxLen < len(ayahText) and len(ayahText) > 3 :
            maxLen = len(ayahText)
            maxAyahText = ayahText
            maxChap = chapterNo
            maxAyah = ayahNo
   
print("Chapter: " + maxChap + " verse: " + str(maxAyah) + ", length: " + str(len(maxAyahText)) + "\nText: " + maxAyahText)

print("Total matching verses: ", count)
'''

'''
i = 0x600
while i <= 0x6ff:
    s = '<Char name=\"\"\tglyph=\"' + chr(i) + '\"\tunicode=\"' + hex(i) + '\"\tappCode=\"' + str(i - 0x600) + '\"/>'
    print(s)
    i = i + 1
'''
