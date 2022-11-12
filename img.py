
def ender(get):
    print("task ",get)
    exitf = input("press enter to exit")
    exit()

try:
    import requests
    url = input("enter the img url")
    dump = requests.get(url).content
    f=open("img.jpg","wb")
    f.write(dump)
    f.close()
    ender("complite")
except ModuleNotFoundError:
    print("module 'requests' is not installed")
    ender("fail")


