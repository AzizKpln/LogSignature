# LogSignature
<p align="center" width="100%">
    <img width="100%" src="https://i.ibb.co/pwDcWcg/Ekran-Al-nt-s.png">
</p>

## Kurulum

````
sudo apt update
sudo apt install git -y
sudo apt install python3 -y
git clone https://github.com/AzizKpln/LogSignature.git
````

## Çalıştırma ve Ayarlamalar
#### ilk olarak private key oluşturulur - parola ataması yapılmalıdır:
<p align="center" width="100%">
    <img width="100%" src="https://i.ibb.co/4F2GMMS/Ekran-Al-nt-s-3.png">
</p>

> openssl genpkey -algorithm RSA -out private_key.pem -aes256

#### Ardından public key oluşturulur:
<p align="center" width="100%">
    <img width="100%" src="https://i.ibb.co/XkSgXPT/Ekran-Al-nt-s-4.png">
</p>

> openssl rsa -pubout -in private_key.pem -out public_key.pem

#### Oluşturulan anahtarlar ssl klasörüne taşınır:
<p align="center" width="100%">
    <img width="100%" src="https://i.ibb.co/7GzpnCh/Ekran-Al-nt-s-5.png">
</p>

> cp private_key.pem public_key.pem ssl/

#### Main.py dosyası editlenir:
<p align="center" width="100%">
    <img width="100%" src="https://i.ibb.co/myJ6h9M/Ekran-Al-nt-s-1.png">
</p>

> En alt satırdaki 'ssl_pass_phrase' bölümü private key parolası ile değiştirilir

#### Main.py Dosyası Çalıştırılır.
<p align="center" width="100%">
    <img width="100%" src="https://i.ibb.co/8cP2J0X/Ekran-Al-nt-s-6.png">
</p>

* Log dosyalarının bulunduğu dizin girilir. Örneğin wazuh loglarını imzalayacaksak /var/ossec/logs/alerts/ şeklinde bir girdi vermeliyiz.
* Burada dikkat edilmesi gereken şey girilecek dizin /var/ossec/logs/alerts olarak değil /var/ossec/logs/alerts/ olarak girilmesidir.

<br>
<p align="center" width="100%">
    <img width="100%" src="https://i.ibb.co/DtRH1pQ/Ekran-Al-nt-s-7.png">
</p>

* Oluşturulan imzalar /var/log/LogSignatures dizini altında tarihe göre oluşturulmuş klasörler içerisinde bulunur.



#### Crontab Girilir:
<p align="center" width="100%">
    <img width="100%" src="https://i.ibb.co/KjY7z7C/Ekran-Al-nt-s-8.png">
</p>

* Yukarıdaki crontab de günlük olarak loglama yapılır. Bu kural kullanıcının kendi isteğine göre değiştirilebilir.
