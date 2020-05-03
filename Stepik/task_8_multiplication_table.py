a = int (input ())
b = int (input ())
c = int (input ())
d = int (input ())
b += 1
d += 1
for z in range (c,d,1):
    print ('\t', z , end='')
print ()
for i in range (a,b,1):
    print (i,'\t', end='')
    #print (c,'\t', end='')
    for j in range (c,d,1):
        print (i*j,'\t', end='')
    print ()
