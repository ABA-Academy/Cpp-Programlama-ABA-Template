# 🎓 C++ Programlama - Otomatik Test Sistemi Demo

## ✨ Ne Hazırlandı?

10 adet örnek C++ sorusu ile **tamamen çalışır** bir template sistemi oluşturuldu!

### 📊 Demo Sorular

| # | Soru | Zorluk | Konu |
|---|------|--------|------|
| 01 | Hello World | ⭐ | Basit çıktı |
| 02 | İki Sayının Toplamı | ⭐ | Girdi/Çıktı |
| 03 | Çift/Tek Kontrolü | ⭐ | If-Else |
| 04 | 1'den N'e Sayılar | ⭐⭐ | For döngüsü |
| 05 | Faktöriyel | ⭐⭐ | While döngüsü |
| 06 | En Büyük Sayı | ⭐⭐ | Döngü + Karşılaştırma |
| 07 | Dizi Ortalaması | ⭐⭐ | Diziler |
| 08 | Palindrome | ⭐⭐⭐ | String işlemleri |
| 09 | Asal Sayı | ⭐⭐⭐ | Algoritmalar |
| 10 | Fibonacci | ⭐⭐⭐ | Fonksiyonlar |

---

## 🗂️ Proje Yapısı

```
Cpp-Programlama-ABA-Template/
│
├── questions/                    # 10 demo soru
│   ├── 01-hello-world/
│   │   ├── README.md            # Soru açıklaması
│   │   ├── main.cpp             # Başlangıç template
│   │   └── .github/workflows/test.yml  # Otomatik testler
│   ├── 02-iki-sayi-toplami/
│   ├── 03-cift-tek-kontrol/
│   ├── ...
│   └── 10-fibonacci/
│
├── generate_question.py          # 500 soru için generator
├── example_questions.json        # JSON format örneği
├── USAGE_GUIDE.md               # Detaylı kullanım kılavuzu
├── QUESTIONS_INDEX.md           # Soru listesi
│
├── .devcontainer/               # Codespaces ayarları
│   ├── devcontainer.json
│   └── setup.sh
│
└── README.md                    # Öğrenci talimatları
```

---

## 🚀 Hızlı Başlangıç

### 1️⃣ Demo Soruyu Test Edin

Herhangi bir soruyu test etmek için:

```bash
cd questions/01-hello-world
cat README.md          # Soruyu okuyun
cat main.cpp           # Template'i görün
cat .github/workflows/test.yml  # Testleri inceleyin
```

### 2️⃣ Yeni Soru Oluşturun

**Otomatik yöntem (ÖNERİLEN):**

```bash
# JSON dosyanızı hazırlayın
python3 generate_question.py example_questions.json
```

**Manuel yöntem:**

```bash
# Mevcut soruyu kopyalayın
cp -r questions/01-hello-world questions/11-yeni-soru

# Dosyaları düzenleyin
nano questions/11-yeni-soru/README.md
nano questions/11-yeni-soru/.github/workflows/test.yml
```

### 3️⃣ GitHub Classroom'a Ekleyin

Her soru için ayrı repository oluşturun:

```bash
cd questions/01-hello-world

# Dosyaları root'a kopyala
cp README.md ../../
cp main.cpp ../../
cp -r .github ../../
cp -r ../../.devcontainer ./

# Git repository oluştur
git init
git add .
git commit -m "Soru 1: Hello World"

# GitHub'a push et
gh repo create cpp-q01-hello-world --public --source=. --push
```

Sonra GitHub Classroom'da bu repo'yu template olarak seçin.

---

## 📚 500 Soru İçin Yol Haritası

### Adım 1: Kategori Planlaması

Önerilen dağılım (USAGE_GUIDE.md'de detaylı):
- 50 Temel Sözdizimi
- 50 Değişkenler
- 50 Koşullu İfadeler
- 60 Döngüler
- 50 Diziler
- 40 String İşlemleri
- 50 Fonksiyonlar
- 30 Pointer'lar
- 40 Struct/Class
- 40 Algoritmalar
- 20 Dosya İşlemleri
- 20 Veri Yapıları

**TOPLAM: 500 Soru**

### Adım 2: JSON Hazırlama

`example_questions.json` dosyasını referans alarak 500 sorunuzu tanımlayın.

**Örnek JSON formatı:**

```json
{
  "slug": "carpim-tablosu",
  "title": "Çarpım Tablosu",
  "difficulty": "⭐⭐ Orta",
  "description": "...",
  "requirements": "...",
  "examples": "...",
  "hints": "...",
  "test_steps": "..."
}
```

### Adım 3: Otomatik Üretim

```bash
python3 generate_question.py all_500_questions.json
```

### Adım 4: Toplu Repository Oluşturma

`USAGE_GUIDE.md` dosyasındaki `create_all_assignments.sh` scriptini kullanın.

---

## 💡 Özellikler

### ✅ Otomatik Test Sistemi
- GitHub Actions ile her commit'te otomatik test
- Öğrenciler anında geri bildirim alır
- Detaylı hata mesajları

### ✅ Codespaces Desteği
- Öğrenciler tarayıcıdan kod yazabilir
- Kurulum gerektirmez
- Herkeste aynı ortam

### ✅ Tek Komut Sistemi
```bash
gonder  # Kod gönder, test et, sonuçları gör
```

### ✅ Türkçe Dokümantasyon
- Tüm açıklamalar Türkçe
- Öğrencilere özel basit talimatlar
- Her soru için detaylı örnekler

### ✅ Ölçeklenebilir Yapı
- 10 sorudan 1000 soruya kolayca geçiş
- Otomatik generator scripti
- JSON tabanlı soru tanımlama

---

## 📖 Dokümantasyon

- **USAGE_GUIDE.md** - Detaylı kullanım kılavuzu
- **QUESTIONS_INDEX.md** - Tüm soruların listesi
- **questions/XX-*/README.md** - Her soru için özel açıklama

---

## 🔍 Örnek Bir Soruyu İnceleyin

### Soru 2: İki Sayının Toplamı

**README.md:**
- Açıklama
- İstenenler
- 4 örnek senaryo
- İpuçları

**main.cpp:**
```cpp
#include <iostream>
using namespace std;

int main() {
    // İpuçları ile başlangıç template'i
    return 0;
}
```

**test.yml:**
- 4 farklı test senaryosu
- Pozitif, negatif, sıfır, büyük sayılar
- Detaylı hata mesajları

---

## 🎯 Sonraki Adımlar

### Kısa Vadede:
1. ✅ 10 demo soru hazır
2. ✅ Generator script hazır
3. ✅ Dokümantasyon tamamlandı
4. ⏳ İlk soruyu GitHub Classroom'a ekleyin
5. ⏳ Öğrencilerle test edin

### Uzun Vadede (500 soru için):
1. ⏳ Konu kategorilerini netleştirin
2. ⏳ 500 soruyu JSON formatında hazırlayın
3. ⏳ Generator ile tüm soruları oluşturun
4. ⏳ Toplu repo oluşturma scriptini çalıştırın
5. ⏳ GitHub Classroom'da assignment'ları oluşturun

---

## ❓ Sorularınız mı Var?

- 📖 `USAGE_GUIDE.md` dosyasını okuyun
- 🔍 Demo soruları inceleyin
- 💬 Soru sorun, birlikte çözelim!

---

## 🎉 Özet

**Hazır olan:**
- ✅ 10 çeşitli zorlukta soru
- ✅ Otomatik test sistemi
- ✅ Codespaces yapılandırması
- ✅ Soru generator scripti
- ✅ Kapsamlı dokümantasyon
- ✅ Öğrenci kullanım kılavuzu

**Yapılacak (500 soru için):**
- JSON dosyası hazırlama
- Generator'u çalıştırma
- GitHub Classroom setup

**Süre tahmini:** 500 soru için JSON hazırlığı ~ 2-3 gün (yoğun çalışma ile)

---

Hazır! 🚀 Ne dersiniz? Detayları konuşalım!
