def palindrome(s):
  
  if s[0] == s[-1] :
    if len(s) == 1 or len(s) == 2:
      return True
    else :
      return palindorme(s[1:-1])
  else:
    return False
  pass

print(palindrome(input()))
