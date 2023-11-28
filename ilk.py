import os
import shutil
liste = ["HakanOzden","HakanOzel","GamzeCelik","FurkanKeles","MerveSarpBoyar","OzgeCillik","SimgeAydin","IpekDolu"]
fileName = "01_05_Sozluk.ipynb"
for item in liste:
    if not os.path.exists(f"Egzersizler/{item}"):
        os.mkdir(f"Egzersizler/{item}")
    # open(f"Egzersizler/{item}/{fileName}","a+")
    kaynakadres = f"Egzersizler/SoruCevaplar/{fileName}" 
    hedefadres = f"Egzersizler/{item}/{fileName}"
    shutil.copy(kaynakadres,hedefadres)
# print("Merhaba")