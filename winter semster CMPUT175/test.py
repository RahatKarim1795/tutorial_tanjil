def reverse(s):
  if len(s) == 1:
    return s
  else:
    return(s[-1] + reverse(s[:-1]))
  
# print(reverse("oranges"))

def reverse1(s):
  if len(s) == 1:
    return s
  else:
    return s[-1] + reverse1(s[1:-1]) + s[0]
  
print(reverse1("oranges"))

def funca():
    a=1
def funcb():
    funca()

# s ="jshsa"
# print(s[-1])