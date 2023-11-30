from paket import modul1 as md1,paketFonksiyon as pf
print(md1.modulFonk(2,3))
print(md1.modulFonk.__name__)
print(pf(2,4))
print(pf.__name__)
########################################################
import paket
print(paket.paketFonksiyon(2,4))
print(paket.modul1.modulFonk(2,3))
print(paket.paketFonksiyon.__name__)
print(paket.modul1.modulFonk.__name__)
########################################################

print("Ana",__name__) # Ana __main__



