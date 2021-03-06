x='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }

min=1000000
length = len(x)
#print(length)

for j in range(1,255):
    cipher=""
    for i in range(0,length,2):
        str=""
        str+=x[i]
        str+=x[i+1]
        cipher+=chr(int(str, 16) ^ j)
    score=0
    for i in character_frequencies:
        count = 0
        for k in cipher:
            if(k==i):
                count = count+1
        score = score + (character_frequencies[i]-count/len(cipher))**2
    #checking for minimum value of score
    if(min>score):
        min=score
        key=j
    #print(cipher)

cipher=""
for i in range(0,length,2):
    str=""
    str+=x[i]
    str+=x[i+1]
    cipher+=chr(int(str, 16) ^ key)
    score=0
    for i in character_frequencies:
        count = 0
        for k in cipher:
            if(k==i):
                count = count+1
        score = score + (character_frequencies[i]-count/len(cipher))**2

print("message",cipher)
print("score",score)
print("key:",key)
