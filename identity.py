a = 1
if type(a) is int:
    print("true")
else:
    print("false")
b = 1.5
if type(b) is float:
    print("true")
else:
    print("false")
c = "hello"
d = "hello"
if ( c is d ):
    print("true")
d = "hi"
if (c is not d):
    print("false")            