def checkChild(age):
 if age>10:
      raise Exception("this is not child")
 else:
    print("ok")

try:
  x =15
  if x>10:
      raise Exception("Num is greater than 10")
  else:
    print("num is fine..")
except Exception as e:
    print("Error.",e)


try:
    checkChild(15)
except Exception as e:
    print("Error",e)
else:
    print("this is child..validated")