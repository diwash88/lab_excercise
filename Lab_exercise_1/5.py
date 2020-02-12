a = int(input('Enter number of students in first class'))
e = int(input('Enter number of students in second class'))
f = int(input('Enter number of students in third class'))

b = a//2
c = a/2
d = b+1
if b >=c :
	y = b
	print('the number of bench required in first class is ' +str(b))
if b != c:
	y = d
	print('the number of bench required in first class is ' +str(d))	

g=e//2
h=e/2
i=g+1

if g==h :
	z = g
	print('the number of bench required in second class is ' +str(g))
if g!=h :
	z = i
	print('the number of bench required in first class is ' +str(i) )	

j = f//2
k = f/2
l = j+1

if j==k :
	x = j
	print('the number of bench required in third class is ' +str(j))
if j!=k :
	x = l
	print('the number of bench required in third class is ' +str(l))	


w = x+y+x

print('The total number of required bench to purchase is ' +str(w))	




