def fizz_buzz():
	i=int(input('Enter any number'))
    
	if i% 15 == 0:
        	print("FizzBuzz")
        	

    
	elif i% 3 == 0:
        	print("Fizz")
        	

   
	elif i % 5 == 0:
        	print("Buzz")
        	
	else:
		print(i)
   
	

fizz_buzz()
