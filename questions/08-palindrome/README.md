# Soru 8: Palindrome Kontrolü

## Zorluk: ⭐⭐⭐ İleri

## Açıklama

Kullanıcıdan bir kelime alın ve bu kelimenin palindrome (tersten okunuşu da aynı) olup olmadığını kontrol edin.

**Palindrome Nedir?**
- "kayak" → tersten de "kayak" (palindrome)
- "ada" → tersten de "ada" (palindrome)
- "merhaba" → tersten "abahrem" (palindrome değil)

## İstenenler

1. Kullanıcıdan bir kelime alın (boşluksuz)
2. Kelimenin palindrome olup olmadığını kontrol edin
3. Palindrome ise "Palindrome", değilse "Palindrome Degil" yazdırın

## Örnekler

### Örnek 1
**Girdi:** `kayak`
**Çıktı:** `Palindrome`

### Örnek 2
**Girdi:** `merhaba`
**Çıktı:** `Palindrome Degil`

### Örnek 3
**Girdi:** `ada`
**Çıktı:** `Palindrome`

### Örnek 4
**Girdi:** `a`
**Çıktı:** `Palindrome`

## İpuçları

- String kullanın: `string kelime;`
- İki yöntem:
  1. **Yöntem 1**: Baştan ve sondan karşılaştırın
  2. **Yöntem 2**: String'i ters çevirin ve karşılaştırın
- `kelime.length()` ile uzunluğu alın
- `kelime[i]` ile karakterlere erişin

## Puanlama

- ✅ Tüm test durumları: 100 puan
