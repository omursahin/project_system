[![Django CI](https://github.com/omursahin/project_system/actions/workflows/django.yml/badge.svg)](https://github.com/omursahin/project_system/actions/workflows/django.yml)


# Proje Yönetim Sistemi
___
## Başlangıç
Proje Yönetim Sistemi, Python 3.9 ile yazılmış bir web uygulamasıdır. Proje Yönetim Sistemi, Django 4.1.7 ve Django Rest Framework 3.14.0 sürümlerini kullanmaktadır.

Migration işlemleri için ilk olarak:

`python manage.py makemigrations` yazarak migration dosyalarını oluşturun.

Daha sonra:

`python manage.py migrate` yazarak migration işlemlerini gerçekleştirin.

Proje Yönetim Sistemi'ni çalıştırmak için:

`python manage.py runserver` yazarak çalıştırabilirsiniz.


___
## Yazım Standartları

**Girintileme**:
* 4 boşluk kullanılmalı, tab karakteri yerine boşluk kullanılmalıdır.

**Satır Uzunluğu:** 

* Maksimum satır uzunluğu 79 karakter olmalıdır.
* Eğer bir satır 79 karakterden daha uzun olmak zorunda kalırsa, o satır birden fazla satıra bölünmelidir.

**İçe Aktarma İfadeleri (import statements)**:

* İçe aktarma ifadeleri şu sıraya göre gruplandırılmalıdır: standart kütüphane içe aktarmaları, ilgili üçüncü taraf içe aktarmaları, yerel uygulama/kütüphane özgü içe aktarmaları.
* Her grup içe aktarması arasında boş bir satır bırakılmalıdır.

**Adlandırma Kuralları:**

* Modül isimleri tamamen küçük harf olmalıdır.
* Sınıf isimleri CamelCase şeklinde olmalıdır.
* Fonksiyon ve değişken isimleri alt çizgi ile ayrılmış küçük harflerden oluşmalıdır.

**Dize Tırnakları:**

* Dizeler tek tırnak içinde olmalıdır.
* Dizeler birden fazla satıra yayılmışsa, her satırın başında ve sonunda bir tırnak olmalıdır.

**Fonksiyon Argümanları:**

* Fonksiyon argümanları virgülden sonra bir boşlukla ayrılmalıdır.

**Boş Satırlar:**

* Mantıksal kod bölümlerini ayırmak için az sayıda boş satır kullanılmalıdır.

**Yorumlar:**

* Yorumlar Docstring formatında yazılmalıdır.
* Yorumlar kodun üzerinde yazılmalıdır.

DocString yazım standartları şöyledir:
* Docstringler üç çift tırnak işareti """ ile başlar ve biter.
* Docstring'in ilk satırı, kodunuzun görevini açıklayan bir açıklama içermelidir.
* İkinci satır boş bırakılmalıdır.
* Docstring'in geri kalanı, fonksiyonun parametrelerini, döndürdüğü değerleri ve herhangi bir özel işlevselliği açıklayan ek bilgiler içermelidir.
* Docstring'ler, rahat okunurluk için paragraflara ayrılabilir.
* Docstringlerde kod örnekleri ve başka belgeler de olabilir.

Örnek Docstring:

```python
def add_numbers(a, b):
    """
    Bu fonksiyon, iki sayıyı toplar.

    :param a: Toplama işlemi için ilk sayı.
    :type a: int
    :param b: Toplama işlemi için ikinci sayı.
    :type b: int
    :return: İki sayının toplamı.
    :rtype: int
    """
    return a + b
```

**Django özel kuralları:**

* Django'nun dahili fonksiyonunu kullanarak geçerli tarih ve saati alın, standart kütüphane datetime modülünü kullanmayın.
* Mümkün olduğunda, Django'nun dahili şablon etiketleri ve filtrelerini kullanın.

**Django Rest Framework kuralları:**

* Giriş ve çıkış verilerini işlemek için Django Rest Framework'un serileştirici sınıflarını kullanın.
API isteklerini ve cevaplarını yönetmek için Django Rest Framework'un görünümlerini ve görünüm setlerini kullanın.
Kimlik doğrulama ve yetkilendirme işlemlerini yönetmek için Django Rest Framework'un kimlik doğrulama ve izin sınıflarını kullanın.

Yazım standartlarını kontrol etmek için Flake8 kullanılmaktadır. 
Flake8 kuralları için [buraya](http://flake8.pycqa.org/en/latest/user/error-codes.html) bakabilirsiniz.

Örnek flake 8 komutu:
`flake8 --exclude migrations,pycache,manage.py,settings.py,env,venv .`

Testleri çalıştırmak ve kapsama miktarını hesaplamak için:
`coverage run --source='.' manage.py test`

HTML formatında kapsam raporu oluşturmak için:
`coverage html`

___

**Kullanıcı Hesapları**

* omur@test.com:123456
* ogrenci1@erciyes.edu.tr:Password@2023
* ogrenci2@erciyes.edu.tr:Password@2023