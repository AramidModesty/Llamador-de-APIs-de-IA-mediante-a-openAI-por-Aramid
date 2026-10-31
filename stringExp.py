def worker():
    if "a".isalpha() and ")".isidentifier():
        print("works")
for i in dir(str):
    if(i.startswith("is")):
        print(i,":",getattr(str,i)("("))
