# Kelime Benzerliği Web Uygulaması

Bu uygulama, Türkçe kelimelerin benzerliklerini bulmak için FastText modelini kullanan basit bir web arayüzü sunar. Girilen kelimeye en çok benzeyen 10 kelimeyi ve benzerlik oranlarını gösterir.

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/[kullanıcı-adınız]/kelime-benzerligi.git
cd kelime-benzerligi
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

3. FastText modelini indirin:
- [cc.tr.300.bin](https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.tr.300.bin.gz) dosyasını indirin
- İndirdiğiniz dosyayı açın ve `cc.tr.300.bin` dosyasını proje klasörüne koyun

## Çalıştırma

Uygulamayı başlatmak için:
```bash
python app.py
```

Tarayıcınızda `http://localhost:5000` adresine giderek uygulamayı kullanmaya başlayabilirsiniz.

## Kullanım

1. Arama kutusuna bir Türkçe kelime girin
2. "Ara" butonuna tıklayın veya Enter tuşuna basın
3. Benzer kelimeler ve benzerlik oranları listelenecektir

## Not

- Uygulama ilk açılışta modeli yükleyecektir, bu işlem birkaç dakika sürebilir
- Sadece Türkçe kelimeler desteklenmektedir
- Kelime sözlükte bulunamazsa uygun bir hata mesajı gösterilecektir 