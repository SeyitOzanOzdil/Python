def komsulukMatrisi(dugumSayisi):

    komsulukListesi=[ [ 0 for i in range(dugumSayisi+1) ] for j in range(dugumSayisi+1) ]
    for i in range(dugumSayisi+1):
        for j in range(dugumSayisi+1):
            if i!=j:
                yolBilgisi = raw_input("V"+str(i)+" V"+str(j)+\
                              " Dogrudan Yol Var mı ?"+" E/H :")
                if yolBilgisi in "eE" and yolBilgisi!="":
                    agirlik = raw_input("Ağırlıgı varsa giriniz(Yoksa geciniz): ")
                    if agirlik=="":
                        continue   #komsulukListesi.append(("V"+str(i)+" V"+str(j),0))
                    else:
                        komsulukListesi[i][j] = int(agirlik)

    return komsulukListesi
    
    
