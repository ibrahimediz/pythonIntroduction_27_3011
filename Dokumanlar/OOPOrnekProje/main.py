import json

class Tools:
    #aynı id'den birden fazla olmamalı
    def idKontrol(self,liste,_id):
        if liste.count(_id) == 1:
            return True
        else:
            raise Exception("idKontrol",_id)
    #first_name, last_name alanları max 25 karater olmalı. Sonunda ve başında boşluk varsa silinmeli
        #-aynı zamanda invalid karatker kontrolü yapılabilir (alfabe dışı karakterler)
    def uzunlukKontrol(self,veri,uzunluk=25):
        if len(veri) <= uzunluk:
            return True
        else:
            raise Exception("uzunlukKontrol",veri)
    #email format kontrolü (...(min 3 karakter) @ x.y )
    def emailKontrol(self,veri,uzunluk=3):
        liste = veri.split("@")
        if len(liste) == 2:
            if len(liste[0]) >= uzunluk:
                if "." in liste[1]:
                    return True
        raise Exception("emailKontrol",veri)
    #salary sayısal bir değer olmalı. 15 digit'ten fazla olmamalı (VARCHAR2(17,2) uyumu için)
    def salaryKontrol(self,veri,uzunluk=15,ondalik=2):
        veri = str(veri)
        if "." in veri:
            result = len(veri.split("."))
        elif "," in veri:
            result = len(veri.split("."))
        else:
            result = [veri,"".zfill(ondalik)]
        if len(result[0]) <= uzunluk and len(result[1]) <= ondalik:
            return True
        else:
            raise Exception("salaryKontrol",veri)

class CheckLog:
    def __init__(self,logAdres,*args,**kwargs):
        self.adres = logAdres
        self.veri = self.dosyaJsonOku()

    def dosyaJsonOku(self):
        return json.load(open(self.adres))
    
    def checkLog(self):
        veri = self.veri
        errList = []
        ############
        idList = [item.get("id") for item in veri]
        for i in range(len(veri)):
            rec = veri[i]
            adres = f"log_{self.logTarihUret()}.csv"
            tool = Tools()
            liste = []
            try:
                liste.append(i)
                liste.append(tool.emailKontrol(rec.get("email")))
                liste.append(tool.salaryKontrol(rec.get("salary")))
                liste.append(tool.uzunlukKontrol(rec.get("first_name")))
                liste.append(tool.uzunlukKontrol(rec.get("last_name")))
                liste.append(tool.idKontrol(idList,rec.get("id")))
            except Exception as hata:
                print(i,hata,sep=";",file=open(adres,"a+"))
            finally:
                errList.append(liste)
        else:
            if not all(errList):
                print("Hatalar Var",adres,"dosyayı kontrol ediniz")
                print(filter(lambda x:errList[]))



    def logTarihUret(self):
        from datetime import datetime
        simdi = datetime.now()
        return "_".join(list(map(str,[simdi.year,simdi.month,simdi.day,simdi.hour])))


nesne1 = CheckLog("Dokumanlar/OrnekUygulama/json_mock_data.json")
nesne1.checkLog()