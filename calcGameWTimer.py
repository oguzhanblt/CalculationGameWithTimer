import random
import time
from threading import Timer
from tkinter.tix import Tree
from pytimedinput import timedInteger

rastgele_islem=random.randint(1,4)
rastgele_sayi1=random.randint(0,9)
rastgele_sayi2=random.randint(0,9)

toplama_islemi=(rastgele_sayi1+rastgele_sayi2)
cikarma_islemi=(rastgele_sayi1-rastgele_sayi2)
carpma_islemi=(rastgele_sayi1*rastgele_sayi2)
bolme_islemi=(rastgele_sayi1/rastgele_sayi2)

toplama_islemi="1"
cikarma_islemi="2"
carpma_islemi="3"
bolme_islemi="4"

soru_hakki=10
w=0
while (w != soru_hakki):

    rastgele_islem=random.randint(1,4)
    rastgele_sayi1=random.randint(0,9)
    rastgele_sayi2=random.randint(0,9)

    w+=1
    if (rastgele_islem==1):
        print("{} {} {} = ".format(rastgele_sayi1,"+",rastgele_sayi2))
        a, timedOut=timedInteger(prompt="Cevaplamak için 3 saniyeniz var.",timeout=3,allowNegative=True)
        if(timedOut):
            print("süreniz doldu")
            continue 

        if(a==rastgele_sayi1+rastgele_sayi2):
            print("Doğru cevap.")
        else:
            print("Yanlış cevap.")
    elif (rastgele_islem==2):
        print("{} {} {} = ".format(rastgele_sayi1,"-",rastgele_sayi2))
        a, timedOut=timedInteger(prompt="Cevaplamak için 3 saniyeniz var.",timeout=3,allowNegative=True)
        if(timedOut):
            print("süreniz doldu")
            continue 
        if(a==rastgele_sayi1-rastgele_sayi2):
            print("Doğru cevap.")
        else:
            print("Yanlış cevap.")
    elif (rastgele_islem==3):
        print("{} {} {} = ".format(rastgele_sayi1,"*",rastgele_sayi2))
        a, timedOut=timedInteger(prompt="Cevaplamak için 3 saniyeniz var.",timeout=3,allowNegative=True)
        if(timedOut):
            print("süreniz doldu")
            continue 
        
        if(a==rastgele_sayi1*rastgele_sayi2):
            print("Doğru cevap.")
        else:
            print("Yanlış cevap.")
    else:
        if (rastgele_sayi2==0 or rastgele_sayi1%rastgele_sayi2!=0):
            w-=1
            continue
        else:
            print("{} {} {} = ".format(rastgele_sayi1,"/",rastgele_sayi2))
            a, timedOut=timedInteger(prompt="Cevaplamak için 3 saniyeniz var.",timeout=3,allowNegative=True)
            if(timedOut):
                print("süreniz doldu")
                continue 
            if(a==rastgele_sayi1/rastgele_sayi2):
                print("Doğru cevap.")
            else:
                print("Yanlış cevap.")
        print("Soru hakkınız bitti.")
        exit()