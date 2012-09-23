x = int(raw_input("Please enter an year: "))
#if x.isdigit()==false:

#print "Enter the number!"      

if (x%400) ==0:
print 'Visokosn'
elif (x%100) == 0:
print 'NE Visokosn'
elif (x%4) == 0:
print 'Visokosn'
else:
print 'NE Visokosn'