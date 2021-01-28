def LongOrShort():
    mode= input("ENTER 'S' TO SHORTEN OR 'E' TO EXPAND :-") 
    if mode.upper() =='S' :
        import pyshorteners
        p = pyshorteners.Shortener()
        url=input("enter url to be shortened : ")
        chota=(p.tinyurl.short(url))
        print("shortened url :-",chota)
    if mode.upper() =='E':
        import pyshorteners
        p = pyshorteners.Shortener()
        url=input("enter url to be expanded : ")
        print("expanded url :-",p.tinyurl.expand(url))

LongOrShort()
