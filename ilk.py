import os
import shutil
liste = ["HakanOzden","HakanOzel","GamzeCelik","FurkanKeles","MerveSarpBoyar","OzgeCillik","SimgeAydin","IpekDolu"]
fileName = "02_03_Donguler.ipynb"
for item in liste:
    if not os.path.exists(f"Egzersizler/{item}"):
        os.mkdir(f"Egzersizler/{item}")
    # open(f"Egzersizler/{item}/{fileName}","a+")
    kaynakadres = f"Egzersizler/SoruCevaplar/{fileName}"
    if not os.path.exists(kaynakadres):
        open(kaynakadres,"wb")
    hedefadres = f"Egzersizler/{item}/{fileName}"
    shutil.copy(kaynakadres,hedefadres)
# print("Merhaba")