head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None
            }
        }
    }
}

#prendo la head, faccio next e mi va nel blocco successivo, poi next e mi va in quello dopo ancora ed infine prendo il valore,
#quindi va da 11 a 3 e poi 23 (qeuesta non è una LL ma un dictionary, la scruttura è questa però)
print(head['next']['next']['value']) 
