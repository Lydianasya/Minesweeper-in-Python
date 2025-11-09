#HURİYE DURSUN
import random
maks_puan= 0
onceki_puan=0
while True:
    print("...MAYIN TARLASI OYUNUNA HOŞGELDİNİZ...")
    while True:
        boyut=int(input("İstediğiniz oyun alanı boyutunu giriniz:"))
        if boyut<10:
            print("Lütfen 10 veya 10'dan büyük bir tam sayı giriniz")
        else:
            break

    gizli=[['?' for _ in range(boyut)] for _ in range(boyut)]
    acik=[['?' for _ in range(boyut)]for _ in range(boyut)]

    mayin_orani=0.3
    mayin_sayisi= int((boyut ** 2) * mayin_orani)

    mayinlar = [["_" for _ in range(boyut)] for _ in range(boyut)] #kolay mod mayınları(%30)
    mayin = 0
    while mayin < mayin_sayisi:   #burada rastgele mayınlı bir liste oluşturuyoruz
        x, y = random.randint(0, boyut-1), random.randint(0, boyut-1)
        if mayinlar[x][y] == "_":  # Eğer o konumda mayın yoksa
            mayinlar[x][y] = "X"
            mayin += 1

    mayin_orani_zor=0.7
    mayin_sayisi_zor=int((boyut ** 2) * mayin_orani_zor)

    mayinlar_zor= [["_" for _ in range(boyut)] for _ in range(boyut)] #zor mod mayınları(%70)
    mayin =0
    while mayin < mayin_sayisi_zor :
        x, y = random.randint(0,boyut-1), random.randint(0,boyut-1)
        if mayinlar_zor[x][y] == "_" :
            mayinlar_zor[x][y] = "X"
            mayin+=1

    while True:
        secim=int(input("1-)KOLAY GİZLİ MOD(%30)\n2-)ZOR GİZLİ MOD(%70)\n3-)AÇIK MOD\nOYNAMAK İSTEDİĞİNİZ MODU GİRİNİZ:"))
        if secim!=1 and secim!=2 and secim!=3 :
            print("!LÜTFEN GEÇERLİ BİR SEÇİM YAPINIZ(1-2-3)!")
        else:
            break

    # kolay gizli mod seçildiğindeki durum
    if secim==1 :
        puan=0
        while True:
            for satir in gizli :
                print(" ".join(satir)) #Güncel listeyi basacak her zaman
            while True:
                x,y= map(int, input("seçmek istediğiniz koordinatı giriniz(x y):").split())
                if (x<=0 or y<=0) or (x>boyut or y>boyut):
                    print("Alanın dışında bir koordinat seçtiniz!")
                elif gizli[x-1][y-1]!="?":
                    print("Daha önce bu noktayı girdiniz!")
                else:
                    break

            if mayinlar[x-1][y-1]== "X" : #mayina basılan durum
                for i in range(boyut):
                    for j in range(boyut):
                        if mayinlar[i][j]=="X":
                            gizli[i][j] = mayinlar[i][j]
                for satir in gizli :
                    print(" ".join(satir))
                print("MAALESEF KAYBETTİNİZ")
                print(f"PUANINIZ:{puan}")
                print(f"ÖNCEKİ PUANINIZ:{onceki_puan}")
                if puan > maks_puan:
                    maks_puan = puan
                print(f"EN YÜKSEK PUANINIZ:{maks_puan}")
                break
            else:# mayına basılmayan durum
                puan+=1
                sayac_mayin=0
                if (x == boyut and y == 1) or (x == boyut and y == boyut):  # alt koseler
                    for i in range(2):
                        for j in range(2):
                            yeni_x = x - i
                            if y == 1:
                                yeni_y = y + j
                            else:
                                yeni_y = y - j
                            if mayinlar[yeni_x - 1][yeni_y - 1] == "X":
                                sayac_mayin += 1
                elif (x==1 and y==1) or (x==1 and y==boyut) :   #ust koseler
                    for i in range(2) :
                        for j in range(2):
                            yeni_x= x+i
                            if y==1:
                                yeni_y= y+j
                            else:
                                yeni_y= y-j
                            if mayinlar[yeni_x-1][yeni_y-1]=="X" :
                                sayac_mayin+=1
                elif 1<x<boyut and (y==1 or y==boyut): #sag sol kenar sutunlar
                    for i in range(-1,2):
                        for j in range(2):
                            yeni_x= x+i
                            if y==1 :
                                yeni_y = y+j
                            else:
                                yeni_y= y-j
                            if mayinlar[yeni_x-1][yeni_y-1]=="X" :
                                sayac_mayin+=1
                elif 1<y<boyut and (x==1 or x==boyut) : # alt ust kenar satırlar
                    for i in range(2):
                        for j in range(-1,2) :
                            yeni_y = y+j
                            if x==1 :
                                yeni_x= x+i
                            else:
                                yeni_x= x-i
                            if mayinlar[yeni_x-1][yeni_y-1]=="X" :
                                sayac_mayin+=1
                else: #ortadaki durumlar
                    for i in range(-1,2) :
                        for j in range(-1,2) :
                            yeni_x, yeni_y= x+i, y+j
                            if mayinlar[yeni_x-1][yeni_y-1]=="X" :
                                sayac_mayin+=1
                gizli[x-1][y-1]=str(sayac_mayin)
            sayac_sayi = 0
            for i in range(boyut):
                for j in range(boyut):
                    if gizli[i][j] != "?":
                        sayac_sayi += 1
            if sayac_sayi == boyut * boyut - mayin_sayisi:
                for satir in gizli :
                    print(" ".join(satir))
                print("OYUNU KAZANDINIZ TEBRİKLER")
                print(f"PUANINIZ:{puan}")
                print(f"ÖNCEKİ PUANINIZ:{onceki_puan}")
                if puan > maks_puan:
                    maks_puan = puan
                print(f"EN YÜKSEK PUANINIZ:{maks_puan}")
                break
        onceki_puan = puan
    #gizli zor modun seçildiği durum
    elif secim==2 :
        puan=0
        while True:
            for satir in gizli:
                print(" ".join(satir))
            while True:
                x,y= map(int, input("seçmek istediğiniz koordinatı giriniz(x y):").split())
                if (x<=0 or y<=0) or (x>boyut or y>boyut) :
                    print("Alanın dışında bir koordinat seçtiniz!")
                elif gizli[x-1][y-1]!="?":
                    print("Daha önce bu noktayı girdiniz!")
                else:
                    break
            if mayinlar_zor[x-1][y-1]== "X" : #mayina basılan durum
                for i in range(boyut):
                    for j in range(boyut):
                        if mayinlar_zor[i][j]=="X":
                            gizli[i][j] = mayinlar_zor[i][j]
                for satir in gizli :
                    print(" ".join(satir))
                print("MAALESEF KAYBETTİNİZ")
                print(f"PUANINIZ:{puan}")
                print(f"ÖNCEKİ PUANINIZ:{onceki_puan}")
                if puan > maks_puan:
                    maks_puan = puan
                print(f"EN YÜKSEK PUANINIZ:{maks_puan}")
                break
            else:# mayına basılmayan durum
                puan+=1
                sayac_mayin=0
                if (x == boyut and y == 1) or (x == boyut and y == boyut):  # alt koseler
                    for i in range(2):
                        for j in range(2):
                            yeni_x = x - i
                            if y == 1:
                                yeni_y = y + j
                            else:
                                yeni_y = y - j
                            if mayinlar_zor[yeni_x - 1][yeni_y - 1] == "X":
                                sayac_mayin += 1
                elif (x==1 and y==1) or (x==1 and y==boyut) :   #ust koseler
                    for i in range(2) :
                        for j in range(2):
                            yeni_x= x+i
                            if y==1:
                                yeni_y= y+j
                            else:
                                yeni_y= y-j
                            if mayinlar_zor[yeni_x-1][yeni_y-1]=="X" :
                                sayac_mayin += 1
                elif 1<x<boyut and (y==1 or y==boyut): #sag sol kenar sutunlar
                    for i in range(-1,2):
                        for j in range(2):
                            yeni_x= x+i
                            if y==1 :
                                yeni_y = y+j
                            else:
                                yeni_y= y-j
                            if mayinlar_zor[yeni_x-1][yeni_y-1]=="X" :
                                sayac_mayin += 1
                elif 1<y<boyut and (x==1 or x==boyut) : # alt ust kenar satırlar
                    for i in range(2):
                        for j in range(-1,2) :
                            yeni_y = y+j
                            if x==1 :
                                yeni_x= x+i
                            else:
                                yeni_x= x-i
                            if mayinlar_zor[yeni_x-1][yeni_y-1]=="X" :
                                sayac_mayin+=1
                else: #ortadaki durumlar
                    for i in range(-1,2) :
                        for j in range(-1,2) :
                            yeni_x, yeni_y= x+i, y+j
                            if mayinlar_zor[yeni_x-1][yeni_y-1]=="X" :
                                sayac_mayin+=1
                gizli[x - 1][y - 1] = str(sayac_mayin)
            sayac_sayi = 0
            for i in range(boyut):
                for j in range(boyut):
                    if gizli[i][j] != "?":
                        sayac_sayi += 1
            if sayac_sayi == boyut * boyut - mayin_sayisi_zor:
                for satir in gizli :
                    print(" ".join(satir))
                print("OYUNU KAZANDINIZ TEBRİKLER")
                print(f"PUANINIZ:{puan}")
                print(f"ÖNCEKİ PUANINIZ:{onceki_puan}")
                if puan > maks_puan:
                    maks_puan = puan
                print(f"EN YÜKSEK PUANINIZ:{maks_puan}")
                break
        onceki_puan= puan
    # acık mod secildigindeki durum
    elif secim==3:
        puan=0
        for i in range(boyut):
            for j in range(boyut):
                if mayinlar[i][j] == "X":
                    acik[i][j] = mayinlar[i][j]
        while True:

            for satir in acik :
                print(" ".join(satir))
            while True:
                x, y = map(int, input("seçmek istediğiniz koordinatı giriniz(x y):").split())
                if (x <= 0 or y <= 0) or (x > boyut or y > boyut):
                    print("Alanın dışında bir koordinat seçtiniz!")
                elif acik[x - 1][y - 1] != "?" and acik[x - 1][y - 1] !="X":
                    print("Daha önce bu noktayı girdiniz!")
                else:
                    break
            if acik[x-1][y-1] == "X" : #mayına basilan durum
                print("MAALESEF KAYBETTİNİZ")
                print(f"PUANINIZ:{puan}")
                print(f"ÖNCEKİ PUANINIZ:{onceki_puan}")
                if puan > maks_puan:
                    maks_puan = puan
                print(f"EN YÜKSEK PUANINIZ:{maks_puan}")
                break
            else: #mayına basılmayan durum
                puan+=1
                sayac_mayin=0
                if (x==boyut and y==1) or (x==boyut and y==boyut) : #alt koseler
                    for i in range(2) :
                        for j in range(2) :
                            yeni_x= x-i
                            if y==1:
                                yeni_y= y+j
                            else:
                                yeni_y= y-j
                            if acik[yeni_x-1][yeni_y-1]=="X":
                                sayac_mayin+=1
                elif (x==1 and y==1) or (x==1 and y==boyut) :   #ust koseler
                    for i in range(2) :
                        for j in range(2):
                            yeni_x= x+i
                            if y==1:
                                yeni_y= y+j
                            else:
                                yeni_y= y-j
                            if acik[yeni_x-1][yeni_y-1]=="X" :
                                sayac_mayin+=1
                elif 1<x<boyut and (y==1 or y==boyut): #sag sol kenar sutunlar
                    for i in range(-1,2):
                        for j in range(2):
                            yeni_x= x+i
                            if y==1 :
                                yeni_y = y+j
                            else:
                                yeni_y= y-j
                            if acik[yeni_x-1][yeni_y-1]=="X" :
                                sayac_mayin+=1
                elif 1<y<boyut and (x==1 or x==boyut) : # alt ust kenar satırlar
                    for i in range(2):
                        for j in range(-1,2) :
                            yeni_y = y+j
                            if x==1 :
                                yeni_x= x+i
                            else:
                                yeni_x= x-i
                            if acik[yeni_x-1][yeni_y-1]=="X" :
                                sayac_mayin+=1
                else: #ortadaki durumlar
                    for i in range(-1,2) :
                        for j in range(-1,2) :
                            yeni_x, yeni_y= x+i, y+j
                            if acik[yeni_x-1][yeni_y-1]=="X" :
                                sayac_mayin+=1
                acik[x-1][y-1]= str(sayac_mayin)
            sayac_sayi = 0
            for i in range(boyut):
                for j in range(boyut):
                    if acik[i][j] != "?" and acik[i][j]!= "X":
                        sayac_sayi += 1
            if sayac_sayi == (boyut ** 2) - mayin_sayisi: # KAZANILMA DURUMU
                for satir in acik:
                    print(" ".join(satir))
                print("OYUNU KAZANDINIZ TEBRİKLER")
                print(f"PUANINIZ:{puan}")
                print(f"ÖNCEKİ PUANINIZ:{onceki_puan}")
                if puan > maks_puan:
                    maks_puan = puan
                print(f"EN YÜKSEK PUANINIZ:{maks_puan}")
                break
        onceki_puan = puan
    while True:
        tercih=int(input("1-)TEKRAR OYNA\n2-)ÇIKIŞ\nTERCİHİNİZİ YAPINIZ:"))
        if tercih not in [1,2]:
            print("GEÇERLİ BİR GİRİŞ YAPINIZ!(1-2)")
        else:
            break
    if tercih==2:
        break