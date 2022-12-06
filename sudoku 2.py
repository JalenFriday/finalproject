

def Nonomino(size):
    import random
    mydict = {}
    r = 0
    while len(mydict) < 9:
        r += 1
        j = range(1, size+1)
        sequence = random.sample(j, len(j))

        sudoko = True
        for dictid,savedlist in mydict.items():
            if sudoko == False:
                break
            for a in savedlist:
                if sequence[savedlist.index(a)] == a:
                    sudoko = False
                    break
        if sudoko == True:

            mydict[len(mydict)] = sequence
    return mydict, r

returndict, total_tries = Nonomino(9)
for r,a in returndict.items():
    print( r,a )
