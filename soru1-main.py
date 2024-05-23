import pandas as pd
import matplotlib.pyplot as plt
# Gerekli olan kütüphaneleri ekliyoruz.
# Pandas kütüphanesini ile veri setimizi python kodunda kullanılacak şekilde içe aktarılıyor.
# Matplotlib kütüphanesi ile verilerin grafik ile görselleştirilmesi sağlanıyor.


# data_fd değişkenine veri setini atıyoruz.
data_fd = pd.read_csv('kc_house_data.csv')


# x1 değişkenine veri setindeki 'sqft_living' sütunu atanıyor.
x1 = data_fd['sqft_living'].values
# x2 değişkenine veri setindeki 'sqft_lot' sütunu atanıyor.
x2 = data_fd['sqft_lot'].values
# y değişkenine 'price' sütunu atanıyor.
y = data_fd['price'].values


# Buluncak olan teta değişkenlerini tanımlıyoruz ve 0 değerini atıyoruz.
teta0 = 0
teta1 = 0
teta2 = 0


# Algoritmanın hızını belirleyen alfa değişkenini oluşturup 0.0000001 değeri atanıyor.
alfa = 0.000001
# Veri setindeki veri sayısı çekilip ornekSayisi değişkenine atanıyor.
ornekSayisi = len(x1)

# Çizdirilen grafikteki değerleri oluşturduğumuz dizi_cost ve dizi_item dizilerinden alıyoruz.
dizi_cost = []
dizi_item = []


# Gradient Descent algoritmasındaki toplam sembolünün bulunduğu kısmı ayırıp for döngüsü içerisinde
# toplam methodu içerisinde hesaplayp return ile döndürüyoruz.
def toplam(t0, t1, t2):
    topla = 0
    for i in range(0, ornekSayisi, 1):
        topla += (t0 + t1*x1[i] + t2*x2[i] - y[i])

        return topla

# Maliyet değerimizin bulunduğu değişkeni tanımlayıp varsayılan olarak 1.0 değeri atanıyor.
# Burada maliyet değişkenine 1.0 değerini atamamızın sebebi 0 olduğunda döngünün içine girmemesidir.
maliyet =1.0

# Aşağıda hipotezin doğruluğunu test etmek için hipotez metodu oluşturuldu.
# Bulunan tetalar ile hipotez formulü oluşturulup x değerlerine veri setinden
# veriler çekilerek test edildi ve gerçek değer ile karşılaştırılması yapıldı ve ekrana yazdırıldı.
def hipotez(x1, x2, y):
    h = teta0 + teta1 * x1[0] + teta2 * x2[0]
    print("Tahmin edilen değer {} , Gerçek Değer {}".format(h, y[0]))
    return h


# while döngüsü oluşturuldu.
# Durma değeri olarak belli bir aralık verildi.
# Elimizdeki özellik sayısı ile aynı sayıda çıktı alınabilmesi için 69. satırdaki mod yapısı oluşturuldu.
# Bu yapı ile index in alacağı değerler sınırlandırılarak özellik sayı kadar döndürülmesi sağlandı.
# Gradient Descent algoritması manuel olarak yazıldı ve hesaplandı.
# Her döngüde maliyet fonksiyou güncellendi.
# dizi_cost dizisinin içerisine eklendi.
# İterasyon sayısı içinde bir dizi oluşturuldu ve döngünün her dönüşünde eleman eklenmesi sağlandı.
# Veriler ekrana yazdırıldı.
i = 0
while(maliyet > 0.001 or maliyet < -0.001):
    index = i % ornekSayisi
    teta0 = (teta0 - alfa * (1.0 / ornekSayisi) * toplam(teta0, teta1, teta2))
    teta1 = (teta1 - alfa * (1.0 / ornekSayisi) * toplam(teta0, teta1, teta2) * x1[index])
    teta2 = (teta2 - alfa * (1.0 / ornekSayisi) * toplam(teta0, teta1, teta2) * x2[index])

    maliyet = (1 / (2 * ornekSayisi)) * pow(toplam(teta0, teta1, teta2), 2)

    dizi_cost.append(maliyet)

    dizi_item.append(i)
    i += 1
    print(i, teta0, teta1, teta2, maliyet)

# Hipotez metodu çağrılarak karşılaştırılma yapıldı.
hipotez(x1, x2, y)
# Grafik çizdirildi.
# Eksenlerin ve grafiğin başlıkları verildi.
plt.plot(dizi_item, dizi_cost)
plt.xlabel('Epoch Sayısı')
plt.ylabel('Maliyet Fonksiyonu')
plt.title('Epoch Sayısına Göre Maliyet Fonksiyonunun Değişimi')
plt.show()