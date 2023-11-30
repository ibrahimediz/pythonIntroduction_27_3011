adres = "Dokumanlar/OrnekUygulama/json_mock_data.json"
liste = ['insert_date', 'update_date', 'id', 'first_name', 'last_name', 'email', 'gender', 'salary', 'currency_code']
#######################
def tarihKontrol(rowNum,key,data,sep="."):
    liste = data.split(sep)
    if len(liste) == 3:
        gun = liste[0] if int(liste[0]) in range (1,32) else "--"
        ay = liste[1] if int(liste[1]) in range (1,13) else "--"
        yil = liste[2] if len(liste[2]) == 4 and liste[2].isdigit() else "--"
        sonuc = sep.join([gun,ay,yil])
        if sonuc.count("--") != 0:
            raise Exception(f"{rowNum};{key};{sonuc}")
        else:
            return sonuc
def logTarihUret():
    from datetime import datetime
    simdi = datetime.now()
    return "_".join(list(map(str,[simdi.year,simdi.month,simdi.day,simdi.hour])))
#####################
if __name__ == "__main__":
    import json
    veri = json.load(open(adres))
    for i in range(len(veri)):
            rec = veri[i]
            for item in ['insert_date', 'update_date']:
                try:
                    tarihKontrol(i,item,rec.get(item),".")
                except Exception as hata:
                    adres = f"log_{logTarihUret()}.csv"
                    print(hata,file=open(adres,"a+")) 





