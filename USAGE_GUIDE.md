# C++ Programlama Template Kullanım Kılavuzu

## 📚 İçindekiler
1. [Genel Bakış](#genel-bakış)
2. [Demo Sorular](#demo-sorular)
3. [500 Soru İçin Hazırlık](#500-soru-için-hazırlık)
4. [Soru Oluşturma](#soru-oluşturma)
5. [GitHub Classroom Kullanımı](#github-classroom-kullanımı)
6. [Öğrenci Kullanımı](#öğrenci-kullanımı)

---

## Genel Bakış

Bu template sistemi ile C++ programlama ödevleri oluşturabilir ve otomatik test edebilirsiniz.

### Özellikler
- ✅ Otomatik test sistemi (GitHub Actions)
- ✅ Codespaces desteği (öğrenciler browser'dan kod yazabilir)
- ✅ Tek komutla gönderme (`gonder`)
- ✅ Anında geri bildirim
- ✅ Türkçe dokümantasyon

---

## Demo Sorular

`questions/` klasöründe 10 örnek soru bulunmaktadır:

1. **Hello World** - Basit çıktı (Başlangıç)
2. **İki Sayının Toplamı** - Girdi/Çıktı (Başlangıç)
3. **Çift/Tek Kontrolü** - If-Else (Başlangıç)
4. **1'den N'e Sayılar** - For Döngüsü (Orta)
5. **Faktöriyel** - While Döngüsü (Orta)
6. **En Büyük Sayı** - Döngü + Karşılaştırma (Orta)
7. **Dizi Ortalaması** - Diziler (Orta)
8. **Palindrome** - String İşlemleri (İleri)
9. **Asal Sayı** - Algoritmalar (İleri)
10. **Fibonacci** - Fonksiyonlar (İleri)

### Demo Soruları Test Etme

Herhangi bir soruyu test etmek için:

```bash
cd questions/01-hello-world
# Dosyaları root'a kopyala ve test et
cp -r .github ../../
cp main.cpp ../../
cp README.md ../../
```

---

## 500 Soru İçin Hazırlık

### Adım 1: Soru Kategorileri Belirleyin

Öneri dağılım:

| Kategori | Soru Sayısı | Zorluk |
|----------|-------------|--------|
| Temel Sözdizimi | 50 | ⭐ |
| Değişkenler ve Operatörler | 50 | ⭐ |
| Koşullu İfadeler | 50 | ⭐⭐ |
| Döngüler | 60 | ⭐⭐ |
| Diziler | 50 | ⭐⭐ |
| String İşlemleri | 40 | ⭐⭐ |
| Fonksiyonlar | 50 | ⭐⭐⭐ |
| Pointer'lar | 30 | ⭐⭐⭐ |
| Struct/Class | 40 | ⭐⭐⭐ |
| Algoritmalar | 40 | ⭐⭐⭐ |
| Dosya İşlemleri | 20 | ⭐⭐⭐ |
| Veri Yapıları | 20 | ⭐⭐⭐ |

**Toplam: 500 Soru**

### Adım 2: JSON Şablonu Hazırlayın

`example_questions.json` dosyasını referans alarak 500 sorunuzu tanımlayın:

```json
[
  {
    "slug": "soru-url-friendly-adi",
    "title": "Soru Başlığı",
    "difficulty": "⭐⭐ Orta",
    "description": "Soru açıklaması...",
    "requirements": "İstenenler listesi...",
    "examples": "Örnek girdi/çıktılar...",
    "hints": "İpuçları...",
    "hint_comment": "main.cpp'deki yorum satırı",
    "test_steps": "GitHub Actions test adımları..."
  }
]
```

### Adım 3: Soruları Otomatik Oluşturun

```bash
# 500 soruyu içeren JSON dosyanız varsa:
python3 generate_question.py all_500_questions.json

# Belirli aralıktaki soruları oluşturmak için JSON'u düzenleyin
```

---

## Soru Oluşturma

### Manuel Oluşturma

Her soru klasörü şu yapıda olmalı:

```
questions/
  XXX-soru-adi/
    README.md              # Soru açıklaması
    main.cpp               # Başlangıç template'i
    .github/
      workflows/
        test.yml           # Otomatik test konfigürasyonu
```

### Otomatik Oluşturma

1. JSON dosyanızı hazırlayın
2. `generate_question.py` scriptini çalıştırın
3. Oluşturulan dosyaları inceleyin ve düzenleyin

---

## GitHub Classroom Kullanımı

### Her Soru için Ayrı Assignment Oluşturma

1. **Template Repository Oluşturun**
   ```bash
   # Her soru için ayrı repo
   cp -r questions/01-hello-world /tmp/cpp-q01-hello-world
   cd /tmp/cpp-q01-hello-world

   # Root'a taşı
   mv README.md ../../
   mv main.cpp ../../
   mv .github ../../

   # Git init
   git init
   git add .
   git commit -m "Initial commit"

   # GitHub'a push
   gh repo create cpp-q01-hello-world --public --source=. --push
   ```

2. **GitHub Classroom'da Assignment Oluşturun**
   - GitHub Classroom → New Assignment
   - Template repository olarak yeni oluşturduğunuz repo'yu seçin
   - Assignment link'ini öğrencilerle paylaşın

3. **Toplu Oluşturma için Script**

```bash
#!/bin/bash
# create_all_assignments.sh

for i in {1..500}; do
  question_dir=$(ls questions/ | sed -n "${i}p")

  # Repository oluştur
  cd questions/$question_dir

  # Dosyaları hazırla
  cp -r .github ../../../temp_repo/
  cp main.cpp ../../../temp_repo/
  cp README.md ../../../temp_repo/
  cp ../../../.devcontainer ../../../temp_repo/ -r

  # Git işlemleri
  cd ../../../temp_repo
  git init
  git add .
  git commit -m "Soru $i"

  # GitHub'a push
  repo_name="cpp-soru-$(printf "%03d" $i)-$question_dir"
  gh repo create $repo_name --public --source=. --push

  # Temizle
  rm -rf .git .github main.cpp README.md

  cd ..
done
```

---

## Öğrenci Kullanımı

### Öğrenciler için talimatlar:

1. **Codespace Açma**
   - Assignment linkine tıkla
   - Accept assignment
   - Repository sayfasında: Code → Codespaces → Create codespace

2. **Kod Yazma**
   - `main.cpp` dosyasını aç
   - Kodu yaz

3. **Test Etme ve Gönderme**
   ```bash
   gonder
   ```

4. **Sonuçları Görme**
   - Otomatik testler çalışır
   - Terminal'de sonuçlar gösterilir
   - Repository → Actions sekmesinden detayları görebilir

---

## Sık Sorulan Sorular

### Öğretmen Soruları

**S: 500 soru çok fazla manuel iş değil mi?**
A: `generate_question.py` scripti ile JSON'dan otomatik üretebilirsiniz.

**S: Her soru için ayrı repo mu olmalı?**
A: Evet, GitHub Classroom her assignment için ayrı repo oluşturur.

**S: Testleri nasıl özelleştirebilirim?**
A: `.github/workflows/test.yml` dosyasını düzenleyin.

**S: Öğrenci puanlarını nasıl görebilirim?**
A: GitHub Classroom dashboard'undan veya Actions sekmesinden.

### Öğrenci Soruları

**S: Yerel bilgisayarımda çalıştırabilir miyim?**
A: Evet, ancak Codespaces kullanmanız önerilir.

**S: Kaç kere gönderebilirim?**
A: Sınırsız! Her `gonder` komutu yeni bir test çalıştırır.

**S: Test neden başarısız oldu?**
A: Terminal'deki hata mesajını okuyun veya Actions sekmesinden detaylara bakın.

---

## İleri Seviye Özellikler

### Özel Test Senaryoları

Test dosyalarında özel kontroller ekleyebilirsiniz:

```yaml
- name: Bellek Kontrolü
  run: |
    valgrind --leak-check=full ./program

- name: Performans Testi
  run: |
    time ./program < large_input.txt

- name: Kod Kalitesi
  run: |
    cppcheck main.cpp
```

### Otomatik Puanlama

```yaml
- name: Puanlama
  run: |
    score=0
    # Test 1
    if [ test1_passed ]; then score=$((score + 25)); fi
    # Test 2
    if [ test2_passed ]; then score=$((score + 25)); fi
    # Test 3
    if [ test3_passed ]; then score=$((score + 25)); fi
    # Test 4
    if [ test4_passed ]; then score=$((score + 25)); fi

    echo "PUAN: $score/100"
```

---

## Destek

Sorunlarla karşılaşırsanız:
- GitHub Issues açın
- Dokümantasyonu kontrol edin
- Demo sorulara bakın

---

## Lisans

MIT License - Eğitim amaçlı kullanım için özgür.
