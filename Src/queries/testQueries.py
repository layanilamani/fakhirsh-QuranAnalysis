
import codecs

# Split each ayah into words
quran = codecs.open('../../Assets/QuranText/quran-simple-clean.txt', 'r', encoding="utf-8")

ayahCount = 0
wordCount = 0
w = 0
for ayat in quran:
    a = ayat.split('|')
    chapterNo   = a[0]
    ayahNo      = a[1]
    ayahText    = (a[2].split('\r'))[0]

    ayahWords   = ayahText.split(' ')
    w += len(ayahWords)
    uniqueWords = set(ayahWords)
    
    wordCount += len(uniqueWords)
    ayahCount += 1


print("Total Ayas: ", ayahCount)
print("Total Unique Words: ", wordCount)
print("Total Words: ", w)

