## gptswap

gptswap, OpenAI API'sini kullanarak bir programlama dilini başka bir dille dönüştüren bir yazılımdır. Bu proje, OpenAI API'sini kullanarak doğal dil işleme konusunda becerilerinizi geliştirebileceğiniz bir ortam sunar.

## Kullanım

Projenin kullanımı oldukça basittir. Öncelikle, OpenAI API anahtarınızı OPENAI_API_KEY ortam değişkeninde tanımlayın veya .env dosyasına kaydedin. Daha sonra, aşağıdaki komutu kullanarak gptswap'i çalıştırın:

```python
python gptswap.py -i <kaynak_dosya> -o <hedef_dosya>
```

Burada <kaynak_dosya>, dönüştürmek istediğiniz kaynak kodunun dosya yolu ve adıdır. <hedef_dosya> kaynak kodunun dönüştürülmüş hali için kaydedilecek dosya yolu ve adıdır.

## Gereksinimler

gptswap'in çalışması için aşağıdaki gereksinimlere ihtiyacınız vardır:

-   Python 3.x
-   dotenv kütüphanesi
-   requests kütüphanesi

Bu gereksinimleri yüklemek için aşağıdaki komutları kullanabilirsiniz:

```bash
pip install -r requirements.txt
```

## Notlar

-   gptswap, OpenAI API'sini kullanır. Bu nedenle, proje kullanmak için OpenAI API anahtarınızın olması gereklidir.
-   gptswap, şu anda sadece gpt-3.5-turbo modeli ile çalışmaktadır.
-   Kaynak kodu içindeki geri tırnak (`) karakteri ve Markdown biçimlendirmesi gptswap tarafından desteklenmemektedir.
