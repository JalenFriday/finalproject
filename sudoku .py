




def Nonomino(size):
    print ( 'welcome to our nonomino sudoko puzzle!')
    import random
    mydict = {}
    r = 0
    
    while len(mydict) < 9:
        r += 1
        j = range(1, size+1)
        sequence = random.sample(j, len(j))
        mydict[len(mydict)] = sequence
        
    return mydict, r

returndict, total_tries = Nonomino(9)
for r,a in returndict.items():
    print( r, a)
print ( 'thank you for watching!')



