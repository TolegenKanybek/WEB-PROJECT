def front_back(str):
      if len(str) <= 1:
          return str
  
  m = str[1:len(str)-1] 
  
  
  return str[len(str)-1] + m + str[0]