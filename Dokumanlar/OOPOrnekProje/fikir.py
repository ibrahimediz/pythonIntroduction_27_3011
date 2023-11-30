#aynı id'den birden fazla olmamalı
#first_name, last_name alanları max 25 karater olmalı. Sonunda ve başında boşluk varsa silinmeli
    #-aynı zamanda invalid karatker kontrolü yapılabilir (alfabe dışı karakterler)
#email format kontrolü (...(min 3 karakter) @ x.y )
#salary sayısal bir değer olmalı. 15 digit'ten fazla olmamalı (VARCHAR2(17,2) uyumu için)
#currency_code => 3 karakter olmalı, str olmalı
#update_dışındaki alanlar boş olmamalı
#gönderilen kayıtlarda eksik kolon olmamalı
#parse edilemeyen ozel bir karakter gelirse nasil davraniyor ?
#raw datamiz var, bir sekilde siralamasi kaymis olabiliyor, bir kolon eksik gelip shift etmis olabiliyor, bunu yakalabilir miyiz? 
#json da olmaz ama csv ya da txt de belli bir ayirac var, data icerisinde bu ayirac geliyor
#################


#aynı id'den birden fazla olmamalı
def idKontrol(liste,_id):
    if liste.count(_id) == 1:
        return True
    else:
        raise Exception("idKontrol",_id)
#first_name, last_name alanları max 25 karater olmalı. Sonunda ve başında boşluk varsa silinmeli
    #-aynı zamanda invalid karatker kontrolü yapılabilir (alfabe dışı karakterler)
def uzunlukKontrol(veri,uzunluk=25):
    if len(veri) <= uzunluk and veri.isalpha():
        return True
    else:
        raise Exception("uzunlukKontrol",veri)
#email format kontrolü (...(min 3 karakter) @ x.y )
def emailKontrol(veri,uzunluk=3):
    liste = veri.split("@")
    if len(liste) == 2:
        if len(liste[0]) >= uzunluk:
            if "." in liste[1]:
                return True
    raise Exception("emailKontrol",veri)
#salary sayısal bir değer olmalı. 15 digit'ten fazla olmamalı (VARCHAR2(17,2) uyumu için)
def salaryKontrol(veri,uzunluk=15,ondalik=2):
    if "." in veri:
        result = len(veri.split("."))
    elif "," in veri:
        result = len(veri.split("."))
    else:
        result = [veri,"".zfill(ondalik)]
    if result[0] <= uzunluk and result <= ondalik:
        return True
    else:
        raise Exception("salaryKontrol",veri)
            
