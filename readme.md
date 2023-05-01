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

---

## gptswap

gptswap is a software that converts a programming language to another language using the OpenAI API. This project provides an environment where you can improve your natural language processing skills using the OpenAI API.

# Usage

Using gptswap is quite simple. First, define your OpenAI API key in the OPENAI_API_KEY environment variable or save it to the .env file. Then, run gptswap using the following command:

```python
gptswap.py -i <source_file> -o <target_file>
```

Here, <source_file> is the file path and name of the source code you want to convert. <target_file> is the file path and name where the converted source code will be saved.

## Requirements

You need the following requirements to run gptswap:

-   Python 3.x
-   dotenv library
-   requests library

You can install these requirements using the following command:

```bash
pip install -r requirements.txt
```

## Notes

-   gptswap uses the OpenAI API. Therefore, you need an OpenAI API key to use the project.
-   gptswap currently works with only the gpt-3.5-turbo model.
-   The backtick (`) character and Markdown formatting in the source code are not supported by gptswap.
