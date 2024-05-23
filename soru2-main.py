import pandas as pd
import matplotlib.pyplot as plt
# Gerekli olan kütüphaneleri ekliyoruz.
# Pandas kütüphanesini ile veri setimizi python kodunda kullanılacak şekilde içe aktarılıyor.
# Matplotlib kütüphanesi ile verilerin grafik ile görselleştirilmesi sağlanıyor.


# data_fd değişkenine veri setini atıyoruz.
data_fd = pd.read_csv('kc_house_data.csv')


# Değişkenlere özelliklerimizi aktarıyoruz.
x1 = data_fd['bedrooms'].values
x2 = data_fd['bathrooms'].values
x3 = data_fd['sqft_living'].values
x4 = data_fd['sqft_lot'].values
x5 = data_fd['waterfront'].values
x6 = data_fd['view'].values
x7 = data_fd['condition'].values
x8 = data_fd['grade'].values
x9 = data_fd['sqft_above'].values
x10 = data_fd['sqft_basement'].values
x11 = data_fd['yr_built'].values
x12 = data_fd['yr_renovated'].values
x13 = data_fd['lat'].values
x14 = data_fd['long'].values
x15 = data_fd['sqft_living15'].values
x16 = data_fd['sqft_lot15'].values
y = data_fd['price'].values


# Buluncak olan teta değişkenlerini tanımlıyoruz ve 0 değerini atıyoruz.
teta0 = 0.0
teta1 = 0.0
teta2 = 0.0
teta3 = 0.0
teta4 = 0.0
teta5 = 0.0
teta6 = 0.0
teta7 = 0.0
teta8 = 0.0
teta9 = 0.0
teta10 = 0.0
teta11 = 0.0
teta12 = 0.0
teta13 = 0.0
teta14 = 0.0
teta15 = 0.0
teta16 = 0.0


# Algoritmanın hızını belirleyen alfa değişkenini oluşturup 0.0000001 değeri atanıyor.
alfa = 0.000001
# Veri setindeki veri sayısı çekilip ornekSayisi değişkenine atanıyor.
ornekSayisi = len(x1)

# Çizdirilen grafikteki değerleri oluşturduğumuz dizi_cost ve dizi_item dizilerinden alıyoruz.
dizi_cost = []
dizi_item = []


# Gradient Descent algoritmasındaki toplam sembolünün bulunduğu kısmı ayırıp for döngüsü içerisinde
# toplam methodu içerisinde hesaplayp return ile döndürüyoruz.
def toplam(t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16):
    topla = 0.0
    for i in range(0, ornekSayisi, 1):
        topla += (t0 + t1 * x1[i] + t2 * x2[i] + t3 * x3[i] + t4 * x4[i] + t5 * x5[i] + t6 * x6[i] + t7 * x7[i] + t8 *
                  x8[i] + t9 * x9[i] +
                  t10 * x10[i] + t11 * x11[i] + t12 * x12[i] + t13 * x13[i] + t14 * x14[i] + t15 * x15[i] + t16 * x16[
                      i] - y[i])

        return topla

# Maliyet değerimizin bulunduğu değişkeni tanımlayıp varsayılan olarak 1.0 değeri atanıyor.
# Burada maliyet değişkenine 1.0 değerini atamamızın sebebi 0 olduğunda döngünün içine girmemesidir.
maliyet = 1.0


# Aşağıda hipotezin doğruluğunu test etmek için hipotez metodu oluşturuldu.
# Bulunan tetalar ile hipotez formulü oluşturulup x değerlerine veri setinden
# veriler çekilerek test edildi ve gerçek değer ile karşılaştırılması yapıldı ve ekrana yazdırıldı.
def hipotez(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, y):
    h = teta0 + teta1 * x1[0] + teta2 * x2[0] + teta3 * x3[0] + teta4 * x4[0] + teta5 * x5[0] + teta6 * x6[0] + teta7 * \
        x7[0] + teta8 * x8[0] + teta9 * x9[0] + teta10 * x10[0] + teta11 * x11[0] + teta12 * x12[0] + teta13 * x13[
            0] + teta14 * x14[0] + teta15 * x15[0] + teta16 * x16[0]
    print("Tahmin edilen değer {} , Gerçek Değer {}".format(h, y[0]))
    return h


# while döngüsü oluşturuldu.
# Durma değeri olarak belli bir aralık verildi.
# Elimizdeki özellik sayısı ile aynı sayıda çıktı alınabilmesi için 101. satırdaki mod yapısı oluşturuldu.
# Bu yapı ile index in alacağı değerler sınırlandırılarak özellik sayı kadar döndürülmesi sağlandı.
# Gradient Descent algoritması manuel olarak yazıldı ve hesaplandı.
# Her döngüde maliyet fonksiyou güncellendi.
# dizi_cost dizisinin içerisine eklendi.
# İterasyon sayısı içinde bir dizi oluşturuldu ve döngünün her dönüşünde eleman eklenmesi sağlandı.
# Veriler ekrana yazdırıldı.
i = 0
while (maliyet > 0.001 or maliyet < -0.001):
    index = i % ornekSayisi

    teta0 = (teta0 - alfa * (1.0 / ornekSayisi) * toplam(teta0, teta1, teta2, teta3, teta4, teta5, teta6,
                                                         teta7, teta8, teta9, teta10, teta11, teta12, teta13,
                                                         teta14, teta15, teta16))
    teta1 = (teta1 - alfa * (1.0 / ornekSayisi) * toplam(teta0, teta1, teta2, teta3, teta4, teta5, teta6,
                                                         teta7, teta8, teta9, teta10, teta11, teta12, teta13,
                                                         teta14, teta15, teta16) * x1[index])
    teta2 = (teta2 - alfa * (1.0 / ornekSayisi) * toplam(teta0, teta1, teta2, teta3, teta4, teta5, teta6,
                                                         teta7, teta8, teta9, teta10, teta11, teta12, teta13,
                                                         teta14, teta15, teta16) * x2[index])
    teta3 = (teta3 - alfa * (1.0 / ornekSayisi) * toplam(teta0, teta1, teta2, teta3, teta4, teta5, teta6,
                                                         teta7, teta8, teta9, teta10, teta11, teta12, teta13,
                                                         teta14, teta15, teta16) * x3[index])
    teta4 = (teta4 - alfa * (1.0 / ornekSayisi) * toplam(teta0, teta1, teta2, teta3, teta4, teta5, teta6,
                                                         teta7, teta8, teta9, teta10, teta11, teta12, teta13,
                                                         teta14, teta15, teta16) * x4[index])
    teta5 = (teta5 - alfa * (1.0 / ornekSayisi) * toplam(teta0, teta1, teta2, teta3, teta4, teta5, teta6,
                                                         teta7, teta8, teta9, teta10, teta11, teta12, teta13,
                                                         teta14, teta15, teta16) * x5[index])
    teta6 = (teta6 - alfa * (1.0 / ornekSayisi) * toplam(teta0, teta1, teta2, teta3, teta4, teta5, teta6,
                                                         teta7, teta8, teta9, teta10, teta11, teta12, teta13,
                                                         teta14, teta15, teta16) * x6[index])
    teta7 = (teta7 - alfa * (1.0 / ornekSayisi) * toplam(teta0, teta1, teta2, teta3, teta4, teta5, teta6,
                                                         teta7, teta8, teta9, teta10, teta11, teta12, teta13,
                                                         teta14, teta15, teta16) * x7[index])
    teta8 = (teta8 - alfa * (1.0 / ornekSayisi) * toplam(teta0, teta1, teta2, teta3, teta4, teta5, teta6,
                                                         teta7, teta8, teta9, teta10, teta11, teta12, teta13,
                                                         teta14, teta15, teta16) * x8[index])
    teta9 = (teta9 - alfa * (1.0 / ornekSayisi) * toplam(teta0, teta1, teta2, teta3, teta4, teta5, teta6,
                                                         teta7, teta8, teta9, teta10, teta11, teta12, teta13,
                                                         teta14, teta15, teta16) * x9[index])
    teta10 = (teta10 - alfa * (1.0 / ornekSayisi) * toplam(teta0, teta1, teta2, teta3, teta4, teta5, teta6,
                                                           teta7, teta8, teta9, teta10, teta11, teta12, teta13,
                                                           teta14, teta15, teta16) * x10[index])
    teta11 = (teta11 - alfa * (1.0 / ornekSayisi) * toplam(teta0, teta1, teta2, teta3, teta4, teta5, teta6,
                                                           teta7, teta8, teta9, teta10, teta11, teta12, teta13,
                                                           teta14, teta15, teta16) * x11[index])
    teta12 = (teta12 - alfa * (1.0 / ornekSayisi) * toplam(teta0, teta1, teta2, teta3, teta4, teta5, teta6,
                                                           teta7, teta8, teta9, teta10, teta11, teta12, teta13,
                                                           teta14, teta15, teta16) * x12[index])
    teta13 = (teta13 - alfa * (1.0 / ornekSayisi) * toplam(teta0, teta1, teta2, teta3, teta4, teta5, teta6,
                                                           teta7, teta8, teta9, teta10, teta11, teta12, teta13,
                                                           teta14, teta15, teta16) * x13[index])
    teta14 = (teta14 - alfa * (1.0 / ornekSayisi) * toplam(teta0, teta1, teta2, teta3, teta4, teta5, teta6,
                                                           teta7, teta8, teta9, teta10, teta11, teta12, teta13,
                                                           teta14, teta15, teta16) * x14[index])
    teta15 = (teta15 - alfa * (1.0 / ornekSayisi) * toplam(teta0, teta1, teta2, teta3, teta4, teta5, teta6,
                                                           teta7, teta8, teta9, teta10, teta11, teta12, teta13,
                                                           teta14, teta15, teta16) * x15[index])
    teta16 = (teta16 - alfa * (1.0 / ornekSayisi) * toplam(teta0, teta1, teta2, teta3, teta4, teta5, teta6,
                                                           teta7, teta8, teta9, teta10, teta11, teta12, teta13,
                                                           teta14, teta15, teta16) * x16[index])

    maliyet = (1 / (2 * ornekSayisi)) * pow(
        toplam(teta0, teta1, teta2, teta3, teta4, teta5, teta6, teta7, teta8, teta9, teta10, teta11, teta12,
               teta13, teta14, teta15, teta16), 2)

    dizi_cost.append(maliyet)

    dizi_item.append(i)
    i += 1

    print(i, teta0, teta1, teta2, teta3, teta4, teta5, teta6, teta7, teta8, teta9, teta10, teta11, teta12, teta13,
          teta14, teta15, teta16, maliyet)


# Hipotez metodu çağrılarak karşılaştırılma yapıldı.
hipotez(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, y)
# Grafik çizdirildi.
# Eksenlerin ve grafiğin başlıkları verildi.
plt.plot(dizi_item, dizi_cost)
plt.xlabel('Epoch Sayısı')
plt.ylabel('Maliyet Fonksiyonu')
plt.title('Epoch Sayısına Göre Maliyet Fonksiyonunun Değişimi')
plt.show()
