
import codecs

# Split each ayah into words
quran = codecs.open('../../Assets/QuranText/quran-simple-clean.txt', 'r', encoding="utf-8")

ayahCount = 0
uniqueWordCount = 0
totalWordCount = 0

uniqueWords = set()

for ayat in quran:
    a = ayat.split('|')
    chapterNo   = a[0]
    ayahNo      = a[1]
    ayahText    = (a[2].split('\r'))[0]

    ayahWords   = ayahText.split(' ')
    
    uniqueWords.update(ayahWords)

    totalWordCount += len(ayahWords)    
    ayahCount += 1


print(uniqueWords)
uniqueWordCount += len(uniqueWords)

print("Total Ayas: ", ayahCount)
print("Total Unique Words: ", uniqueWordCount)
print("Total Words: ", totalWordCount)

