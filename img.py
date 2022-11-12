
def ender(get):  # for ending the game
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
    get = "complite"
    ender(get)
except ModuleNotFoundError:
    print("module 'requests' is not installed")
    get = "fail"
    ender(get)


