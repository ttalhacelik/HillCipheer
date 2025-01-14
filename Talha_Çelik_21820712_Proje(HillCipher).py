# https://bilgisayarkavramlari.com/2008/11/19/hill-sifrelemesi-hill-cipher/      Hill şifreleme algoritması için link

import random 
import numpy as np

class Hillcipher():

    """
        Class'ı kullanabilmek için öncelikle bir object oluşturulmalıdır. Eğer anahtar matrise sahip iseniz objeyi oluştururken input kısmına '1' i 
    tuşlayarak matrisinizi girebilirsiniz. Eğer matrisiniz yok ise '0' ı tuşlayarak yeni bir matris oluşturabilirsiniz. Daha sonra bu matrise erişmek
    isterseniz 'objeismi.key' yazarak anahtar matrise ulaşabilirsiniz. Şifreleme yapmak için hangi obje için şifrelemek yapacaksanız 
    'objeismi.encryption()' fonksiyonunu çağırıp mesajınızı girmeniz yeterli olacaktır. Eğer şifrelenen anahtar matrise sahip iseniz deşifrelemek için
    'objeismi.decryption()' fonksiyonunu çağırıp şifreli mesajı girmeniz yeterli olacaktır. Matrisi girerken yanlış girilmesi durumunda 'exit' keyword'ü
    anahtar matris girme işlemini başa saracaktır.

    """
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    kullanıcılar = []
    count = 0
    
    def blocklength():       # Kullanıcıdan şifre uzunluğunu bölecek şekilde bir blok uzunluğu isteniyor.
        while True: 
            try:
                block_len = int(input("Lütfen şifrenin blok uzunluğunu giriniz: "))    # Kullanıcı int değeri dışında bir değer girememesi için.
                if block_len > 1:    # Kullanıcı negatif bir sayı girdiğinde hata almamak için
                    break
                else:
                    print("Lütfen geçerli bir tuşlama yapınız! ")     # Kullanıcı 1'den büyük bir değer girmezse uyarı yapılıyor
            except:
                print("Lütfen geçerli bir tuşlama yapınız! ")         # Kullanıcı bir Int değeri girmezse uyarı yapılıyor 
        return block_len

    def keymaker():         # Kullanıcı anahtar matrise sahip değilse şifreleme yapmak için yeni bir anahtar matris üretiyor.
        
        """
            Burada ki fonksiyon yukarıda tanımladığım fonksiyonu çağırarak blok uzunluğunu "n" değişkeninin içine atıyor daha sonrasında nxn biçiminde
        boş bir matris oluşturuyor. Daha sonra bu matrisin içini doldurmak için algoritma tanımladım. Nested for döngüsüyle matrisin girdilerini 
        tarayarak her bir girdisini 0 ile 25 arasında sayılardan oluşturuyor daha sonrasında bu matrisin determinantını hesaplayarak 
        26 ile aralarında asal olupolmadığına bakıyor eğer aralarında asal ise döngüden çıkıyor.
        
        """
        
        global n
        n = Hillcipher.blocklength()    
        key = np.empty((n,n))       
        while True:
            for i in range(n):
                for j in range(n):     
                    key[i,j] = random.randint(0,25)  # Anahtar matrisin girdilerini 0 ve 25 üzerinde rastgele int sayılar olarak üretiyor. (Mod 26) 
            det_key = round(np.linalg.det(key))  
            if det_key % 2 != 0 and det_key % 13 != 0 : # Anahtar matrisinin tersi olup olmadığını kontrol ediyor
                break 
        return key 
       
    def keychecker():     # Kullanıcıdan matris girişi alınıyor ancak girilen matris tersinir olmayabilir o yüzden bunu kontrol ediyor.
        
        """
            Anahtar matrisimizin tersinir olabilmesi için gerek ve yeterli koşul anahtar matrisimizin determinantının mod 26 daki değerinin 26 ile 
        aralarında asal olması ve determinant değerinin 0'dan farklı olmasıdır. Eğer sadece determinantı 0'dan farklı matrislerin hepsini kabul edersek 
        26 ile aralarında asal olmayan sayıların mod 26 da çarpımsal tersleri olmayacağında tersinir matrisleri de tanımlı olmayacaktır.
        (Küçük bir ekleme mod 26'da determinantın 0'a denk olması demek determinantın 26'ya bölümünden 0 kalması demektir.)
        Aşağıdaki while True algoritması biraz karışık oldu ama kullanıcı yanlış tuşlama yaptığında algoritmayı başa sarabilmek için 'exit' 
        keyword'ünü kullanması yeterli.
        
        """
        
        global n
        while True:  # Kullanıcıdan alınan matrisi kontrol etme algoritması (Yukarıda ki algoritmayla aynı)
            n = Hillcipher.blocklength()
            key = np.empty((n,n))
            girdi = 0
            for i in range(n):
                if girdi == 'exit':
                    break
                for j in range(n):
                    if girdi == 'exit':
                        break
                    while True:     # Kullanıcıdan matris girişi alınıyor
                        try:
                            girdi = input(f"Lütfen anahtar matrisinizin {i+1}.satır {j+1}.sütunundaki elemanı giriniz: ")
                            if girdi == 'exit':
                                break
                            else:
                                key[i,j] = int(girdi) % 26
                                break
                        except:
                                print("Lütfen geçerli bir matris elemanı giriniz! ")
            det_key = round(np.linalg.det(key))
            if girdi != 'exit':
                if det_key % 2 != 0 and det_key % 13 != 0:  # Anahtar matrisin tersinirlik kontrolü
                    return key
                else:
                    print("Girdiğiniz matris mod 26 sisteminde tersinir değildir lütfen mod 26 sisteminde tersinir bir matris giriniz.")
        
    def keyfunc(): 
        
        """
            Bu fonksiyon yukarıda tanımladığım iki fonksiyonu koşullu olarak çağırıyor eğer kullanıcı anahtar matrise sahip ise terminalden "1"'i
        tuşlayarak tersinir anahtar matrisini giriyor eğer tersinir değilse yukarıdaki keychecker fonksiyonu bunu yakalayarak hata döndürüyor.
        Eğer kullanıcı matrise sahip değilse veya yeni bir matris istiyorsa "0"'ı tuşlayarak yeni bir matris çağırıyor keymaker() fonksiyonu ile
        yeni bir tersinir anahtar matrisi üretiliyor
        
        """
        
        while True:         
            try:
                keycall = input("Anahtar matrise sahipseniz \"1\"'i tuşlayın lütfen! Eğer yeni bir anahtar matris istiyorsanız \"0\"'ı tuşlayın ")
                if keycall == "1":
                    return np.array(Hillcipher.keychecker())      # Yukarıda ki matris kontrol fonksiyonu çağrılıyor
                elif keycall == "0":
                    return np.array(Hillcipher.keymaker())       # Yukarıda ki matris oluşturma fonksiyonu çağrılıyor
                else:
                    print("Lütfen geçerli bir tuşlama yapınız")
            except:
                print("Lütfen geçerli bir tuşlama yapınız")

    def reversingkey(key):   
        
        """
            Reversingkey fonksiyonu bizim için anahtar matrisimizin mod 26 da tersini bulacak ama burası biraz matematik bilgisi gerektiriyor.
        Python'da tanımlı olan np.linalg.inv() fonksiyonu 1/det(A) * cof(A) = inv(A) olarak tanımlanmıştır. Genel olarak matrisler ile 
        Q (Rasyonel Sayılar) Kümesi üzerinde çalıştığımız için doğru bir tanımlamadır ancak çalıştığımız kümeyi mod 26 olarak değiştirdiğimiz zaman 
        1/det(A) mod 26 da tanımlı olmuyor. Bu yüzden Python'daki bu fonksiyonu kullanarak mod 26'da tersinir bir matris elde edemiyoruz. Bunun yerine 
        formulün aslını kullanacağız det(A)^-1 * cof(A) = inv(A) burada iki şeye ihtiyacımız var det(A)^-1 ve cof(A) det(A)^-1 için aşağıdaki 
        fonksiyonda ters hesaplama algoritması kurdum. det(A)^-1 demek det(A) ile mod 26 'daki bir sayıyı çarptığımızda çıkan sonuç 26k+1 şeklinde 
        olması demektir.Örnek olarak det(A) = 9 olsun 9'un mod 26 daki tersi "3" elemanıdır 9 * 3 = 27 = 26*1 + 1 olarak yazılabilir. Son olarak cof(A) 
        kaldı bunun için np.linalg.inv() fonksiyonunu kullanacağım. yukardaki formülden biliyoruz ki det(A) * inv(A) = cof(A) buradan kolayca cof(A) yı 
        bulabiliyoruz daha sonrasında det(A)^-1 * cof(A) = inv(A) ile mod 26 daki anahtar matrisimizin tersini bulacağız.)
     
        """  
        
        cof_key = (np.linalg.det(key) * np.linalg.inv(key))  # Cof(A) bulma adımı (1/det(A)'yı karşıya çarpı olarak attım)
        det_key = round(np.linalg.det(key)) % 26                  # Det(A)'yı alıyor (Mod 26'da)                     
        tersinir_list = [1,3,5,7,9,11,15,17,19,21,23,25]                
        for i in tersinir_list:
            if (i * det_key) % 26 == 1:
                ters = i                                        # Det(A)^-1'i buluyor
                break
        reversed_key = (cof_key * ters) % 26                    # Det(A)^-1 ile Cof(A) yı çarparak matrisin tersini buluyor.
        for i in range(key.shape[0]):
            for j in range(key.shape[1]):
                reversed_key[i][j] = round(reversed_key[i][j])  # Round fonksiyonu kullanılmazsa burada yanlış sonuç alınıyor o yüzden önemli !!!
        return reversed_key
    
    def __init__(self,name):
        key =  Hillcipher.keyfunc()
        reversed_key = Hillcipher.reversingkey(key)
        self.name = name
        self.key = key
        self.yek = reversed_key   # yek ne alaka diye düşünürseniz key'in tersi yek :D
        self.n = n
        Hillcipher.kullanıcılar.append(name)
        Hillcipher.count += 1
    
    def plaintext(self):      # Kullanıcıdan mesaj metni alıp onu bir matrise çevirme işlemi yapıyor.
        
        """
            Burada kullanıcıdan alınan plaintext metnini bir listenin içerisine aktarıyorum daha sonra for ile bu listenin elemanlarını i'ye atarak
        bunların alphabet listesindeki indekslerini çağırıyorum. (Burada ki alphabet listenin indeksleri o harfin ingilizce alfabedeki sayısal değeri)
        Burada ki ilk yazdığım if koşulu verilen metinin blok uzunluğunun bir katı olup olmadığını kontrol ediyor. Eğer metin uzunluğu metin 
        uzunluğunu tam bölmüyorsa metini yeniden girilmesi isteniyor. Eğer istenilen uzunluktaysa kod else'e girerek plaintexti yukarda bahsettiğim
        gibi harflerin sayısal değerlerini alıp bunu bir matrise çeviriyor. Bu girdilerin matris olabilmesi için 2. for döngüsünü özellikle yazdım
        listeyi blok uzunluğunda slice olacak şekilde alıp listenin içerisine atıyor listenin girdileri liste olduğu için bunu bir matris olarak 
        görüyor. Örnek np.array([[1,2,3],[2,3,4],[3,4,5]]) olan liste 3x3 lük bir matris
        
        """
         
        while True:       # Int değeri dışında değer girilememesi için try except kullandım
            try:
                plaintext_matr = []           # Mesajın harflerinin alfabedeki sayısal karşılıklarını içine atmak için liste oluşturdum.
                plain_list = list(input(f"Lütfen {self.name} kullanıcısına göndermek istediğiniz mesajı giriniz: "))
                plain_leng = len(plain_list)
                if plain_leng % self.n != 0:    # Mesaj uzunluğu bloğu bölmek zorunda olduğu için bunu burada kontrol ediyorum
                    print(f"Lütfen şifreniz {self.n} sayısının bir katı olsun!\nGirilen şifre uzunluğu: {plain_leng}")
                else:              # For döngülerinin boşuna çalışmaması için else içerisinde yazmayı tercih ettim.
                    for i,j in enumerate(plain_list):      
                        plain_list[i] = Hillcipher.alphabet.index(j)     
                    for i in range(int(plain_leng/n)):                       
                        plaintext_matr.append(plain_list[i * self.n:self.n * (i + 1)]) 
                    break                                                 
            except:
                print("Lütfen sadece ingiliz alfabesindeki harfleri kullanınız!")
        return np.array(plaintext_matr)

    
    def ciphertext(self):        # Yukarıda ki algoritmaya benzer şekilde çalışıyor, deşifrelemek için yaptım burayı şifrelenmiş mesajı matrise  
        while True:              # çeviriyor bunu anahtar matrisin tersiyle çarparak açık mesajı bize geri döndürüyor.
            try:            # Yukarıda ki algoritmayla benzer olduğu için çok detaylı açıklamadım
                ciphertext_matr = []
                cipher_list = list(input(f"Lütfen {self.name} kullanıcısından gelen mesajı giriniz: "))
                cipher_leng = len(cipher_list)
                if cipher_leng % self.n != 0:
                    print(f"Lütfen şifreniz {self.n} sayısının bir katı olsun!") 
                    print(f"Girilen şifrenin uzunluğu : {cipher_leng}")
                for i,j in enumerate(cipher_list):
                    cipher_list[i] = Hillcipher.alphabet.index(j)
                for i in range(int(cipher_leng/self.n)):
                    ciphertext_matr.append(cipher_list[i * self.n:self.n * (i + 1)])
                if cipher_leng % self.n == 0:
                    break
            except:
                print("Lütfen sadece ingiliz alfabesindeki harfleri kullanınız!")
        return np.array(ciphertext_matr)

    def encryption(self):     # Girilen metini anahtar matris ile şifreliyor.
        cipher_matr = self.plaintext() @ self.key % 26
        cipher_list = []                 # Matrisi alfabedeki karakterlere dönüştürüp içine atacağım listeyi oluşturdum.
        cipher = ""                # Yukarıda ki listeyi tamamladıktan sonra string'e dönüştürmek için cipher adında boş bir string oluşturdum
        for i in range(cipher_matr.shape[0]):
            for j in range(cipher_matr.shape[1]):     # Yukarıda ki matris çarpımında elde edilen şifreyi taramak için nested for döngüleri
                cipher_list.append(Hillcipher.alphabet[round(cipher_matr[i,j])])  
                cipher = "".join(cipher_list)        # Üst satırda oluşturulan listeyi stringin içerisine aktarıyor.
        return print(f"Şifreniz: {cipher}")

    def decryption(self):   # Girilen şifrelenmiş mesajı anahtar matrisin tersi ile açık mesaj haline döndürüyor 
        plaintext_matr = (self.ciphertext() @ self.yek) % 26
        plaintext_list = []         # Matrisi alfabedeki karakterlere dönüştürüp içine atacağım listeyi oluşturdum.
        plaintext = ""           # Yukarıda ki listeyi tamamladıktan sonra string'e dönüştürmek için cipher adında boş bir string oluşturdum.
        for i in range(plaintext_matr.shape[0]):      
            for j in range(plaintext_matr.shape[1]):
                plaintext_list.append(Hillcipher.alphabet[int(plaintext_matr[i,j])])
                plaintext = "".join(plaintext_list)  # Üst satırda oluşturulan listeyi oluşturduğum boş stringin içerisine aktarıyor
        return print("Mesajınız: ", plaintext)
    


#############################################
# Test için aşağıdaki / """" \'leri siliniz #
#############################################

"""

talha = Hillcipher(name = "Talha")

print(talha.key)  # Talha objesi için oluşturulan matris.

arat = Hillcipher(name = "Mustafa Murat")  # Yukarıda talha obj sahip olduğu matrisi giriyorum.

talha.encryption()  # Talha'ya yollamak için mesaj şifreleniyor.

arat.decryption()  # Arat'tan gelen mesaj deşifreleniyor.

print(talha.kullanıcılar)  # Kimlerle mesajlaşabileceğinizin listesi.

print(talha.count)  # Kişilerin sayısı

"""
