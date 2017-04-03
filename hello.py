def fizz_buzz(argument):
  if argument<=0:
    return 'Invalid Argument'
  else:
    if argument % 3==0 and argument % 5==0:
      return 'fizzBuzz'
    elif argument % 5==0:
      return 'buzz'
 
    elif argument % 3==0:
      return 'fizz'
    elif argument % 3!=0 or argument % 5!=0:
      return argument
    else:
      return 'Invalid Argument'
    
  
  
 
    