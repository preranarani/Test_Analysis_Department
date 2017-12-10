
L1 = ['a', 'b', 'c','e','h','m','d','k']
L2 = ['b', 'd','m','r']
temp=''
for i in L1:
    for j in L2:
        if(i==j):
            print "common elements",j
            temp=j
    if(i!=temp):   
       print "elements present in L1 and not in L2",i  