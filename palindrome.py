#xndir 1 
#bary polinom e ardyoq

bar="abba"
bar1="adcf"
bar2='asdfg'
bar3="abcba"

def polinom(bar):
    for i in range(len(bar)//2):
        if bar[i]!=bar[len(bar)-i-1]:
            return "no"
    return "yes"

# print(polinom(bar))
# print(polinom(bar1))
# print(polinom(bar2))
# print(polinom(bar3))


#xndir 2
#naxadasutyan amenaerkar polinomy

text = "aba sadfgsahsdjj abba fg fghhgf kllk"
l1=text.split()

l = ["aba", "sadfgsahsdjj", "abba", "fg", "fghhgf", "kllk"]

def polinom_l(l):
    len_ =0
    bar_ =" "
    for bar in l:
        t=1
        for i in range(len(bar)//2):
            if bar[i]!=bar[len(bar)-i-1]:
                t=0
                break
        if t==1 and len(bar)>len_:
            len_=len(bar)
            bar_=bar
    return len_, bar_

# print(polinom_l(l1))


#xndir 3 
#texti amenaerkar polinomy


text = "abasadfgsahsdjjabbafgfghhgfkllk"
# text ="12345"

def polinom_t(text):
    n = len(text)
    barer = [] 
    for i in range(1,n):
        for j in range(n,i,-1):
            # print(i,j, text[i-1:j])
            barer.append(text[i-1:j])
    return polinom_l(barer)
  
print(polinom_t(text))