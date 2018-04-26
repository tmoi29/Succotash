#Tiffany Moi
#SoftDev2 pd7
#K15 -- Do You Even List?
#2018-04-26   

from math import log 

def threshold(passw):
    upper = [x for x in passw if x.isupper()]
    lower = [x for x in passw if x.islower()]
    num = [x for x in passw if x.isdigit()]
    return (len(upper) != 0 and len(lower) != 0 and len(num) != 0)

print threshold("lol124U") # should be True
print threshold("lol123") # should be False

def scale(passw):
    upper = [x for x in passw if x.isupper()]
    lower = [x for x in passw if x.islower()]
    num = [x for x in passw if x.isdigit()]
    char = [x for x in passw if ".?!&#,;:-_*".find(x) >= 0]
    if len(upper) == 0 or len(lower)== 0 or len(num)==0 or len(char)==0:
        return 1
    else:
        return int(log(len(passw), 10) * 3 + log(len(num),8)*3 + log(len(char),8) * 4)
    
print scale("lol124U")
    
print scale("lol-*&124Uasjflkdjflkjas;")