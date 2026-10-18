def near_ten(num):
  if num % 10 >= 0-2 and num % 10 <= 0+2:
      return True
  if num % 10 >= 10-2 and num % 10 <= 10+2:
      return True

  return False
    
    
near_ten(12)