# """
# bu notebook diziler ile alakalıdır
# """
# print(__doc__) # doc string

# def fonk():
#     """
#     bu fonksiyon boş
#     """
#     pass


# fonk()



import sys
print(*sys.path,sep="\n")
# /workspace/pythonIntroduction_27_3011
# /home/gitpod/.pyenv/versions/3.12.0/lib/python312.zip
# /home/gitpod/.pyenv/versions/3.12.0/lib/python3.12
# /home/gitpod/.pyenv/versions/3.12.0/lib/python3.12/lib-dynload
# /workspace/pythonIntroduction_27_3011/test/lib/python3.12/site-packages


# def fonk(a:int,b:int)->None:
#     """
#     Bu bir fonksiyon boş bir fonksiyon
#     a => int
#     b => int
#     """
#     print("Merhaba")
# fonk

# def topla(a,b):
#     islem = "+"
#     return a,b,a+b,islem
# def cikar(a,b):
#     islem = "-"
#     return a,b,a-b,islem
# def bolme(a,b):
#     islem = "/"
#     return a,b,a/b,islem
# def carp(a,b):
#     islem = "*"
#     return a,b,a*b,islem
# def kuvvet(a,b):
#     islem = "**"
#     return a,b,a**b,islem
# def modulus(a,b):
#     islem = "%"
#     return a,b,a%b,islem



def hesapMak():
    menu = """
    ##########
    1. Toplama
    2. Çıkarma
    3. Bölme
    4. Çarpma
    5. Kuvvet
    6. Mode Alma
    7. Çıkış
    İşlem Seçiniz:
    """
    # (lambda x,y:x,y,x+y,"+")
    # fonkList = [topla,cikar,bolme,carp,kuvvet,modulus]
    fonkList=[(lambda x,y:(x,y,x+y,"+")), # toplama
    (lambda x,y:(x,y,x-y,"-")), # çıkarma
    (lambda x,y:(x,y,x/y,"/")), # bölme
    (lambda x,y:(x,y,x*y,"*")), # carpma
    (lambda x,y:(x,y,x**y,"**")), # kuvvet
    (lambda x,y:(x,y,x%y,"%"))] # modulus
    #            0.     1.    2.    3.       4.     5. 
    islem = 0
    while islem != 7:
        islem = input(menu)
        if islem and islem.isdigit():
            islem = int(islem)
            if islem in range(1,len(fonkList)+1):
                a = input("1. Sayıyı Giriniz:")
                b = input("2. Sayıyı Giriniz:")
                if (a and b) and (a.isdigit() and a.isdigit()):
                    sonuc = fonkList[islem-1](int(a),int(b))
                    print(f"{sonuc[0]} {sonuc[3]} {sonuc[1]} = {sonuc[2]}")
                else:
                    print("Veri Girişi Hatası")
            elif islem != 7:
                print("İşlem Seçimi Hatası")
        else:
            print("İşlem Girişi Hatası")
    else:
        print("İyi Günler Dileriz")

hesapMak()