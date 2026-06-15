x = "fantastic"

def myfunc() :
    x ="awsome"
    print("Python is" + x)

myfunc()

print("Python is" + x)

# jo variable function ke bhar bante h vo global variable hote h or jo function ke andar bante h vo local variables hote h
# global variable ka use hum poore code m kr skte h pr local  variables sirf function ke andar use kr skte h agar bhahr kiya to eroor aygi

# pr agar hum function ke andar variable bana kr usko pure code m use krna chahte h then we can use the global keyword.....see the following code below..



def isvar() :
    global x
    x=6

isvar()
print(x)