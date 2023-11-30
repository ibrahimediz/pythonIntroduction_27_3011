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

    def tarihKontrol(self,veri,sep="."):
        liste = veri.split(sep)
        if len(liste) == 3:
            gun = liste[0] if int(liste[0]) in range (1,32) else "--"
            ay = liste[1] if int(liste[1]) in range (1,13) else "--"
            yil = liste[2] if len(liste[2]) == 4 and liste[2].isdigit() else "--"
            sonuc = sep.join([gun,ay,yil])
            if sonuc.count("--") != 0:
                raise Exception("tarihKontrol",{sonuc})
            else:
                return True


class CheckLogJson:
    def __init__(self,logAdres,*args,**kwargs):
        self.adres = logAdres
        self.veri = self.dosyaJsonOku()

    def dosyaJsonOku(self):
        return json.load(open(self.adres))
    
    def checkLog(self):
        veri = self.veri
        errList = []
        recList = []
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
                liste.append(tool.tarihKontrol(rec.get("insert_date")))
                liste.append(tool.tarihKontrol(rec.get("update_date")))
                recList.append(rec)
            except Exception as hata:
                print(i,hata,sep=";",file=open(adres,"a+"))
                errList.append(liste)    
        else:
            d1 = open("ornek.json","w+")
            # print(json.dumps(recList))
            d1.write(json.dumps(recList))
            d1.close()
            if errList:
                print("Hatalar Var",adres,"dosyayı kontrol ediniz")
                print(*errList,sep="\n")



    def logTarihUret(self):
        from datetime import datetime
        simdi = datetime.now()
        return "_".join(list(map(str,[simdi.year,simdi.month,simdi.day,simdi.hour])))


nesne1 = CheckLogJson("Dokumanlar/OrnekUygulama/json_mock_data.json")
nesne1.checkLog()
