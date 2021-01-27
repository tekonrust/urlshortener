def LongOrShort(long,short):
    if short is not None and long is None: 
        import pyshorteners
        p = pyshorteners.Shortener()
        url=input("enter url to be shortened : ")
        chota=(p.tinyurl.short(url))
        print("shortened url :-",chota)
    elif long is not None and short is None:
        import pyshorteners
        p = pyshorteners.Shortener()
        url=input("enter url to be expanded : ")
        print("expanded url :-",p.tinyurl.expand(url))

LongOrShort(1,None)
LongOrShort(None,1)
