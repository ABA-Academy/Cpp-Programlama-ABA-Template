# Soru 9: Asal Sayı Kontrolü

## Zorluk: ⭐⭐⭐ İleri

## Açıklama

Kullanıcıdan bir pozitif tam sayı alın ve bu sayının asal olup olmadığını kontrol edin.

**Asal Sayı Nedir?**
- 1'den büyük ve sadece 1 ve kendisi ile bölünebilen sayılardır
- Örnekler: 2, 3, 5, 7, 11, 13, 17, 19, 23...
- 1 asal sayı değildir

## İstenenler

1. Kullanıcıdan pozitif bir tam sayı alın
2. Sayının asal olup olmadığını kontrol edin
3. Asal ise "Asal", değilse "Asal Degil" yazdırın

## Örnekler

### Örnek 1
**Girdi:** `7`
**Çıktı:** `Asal`

### Örnek 2
**Girdi:** `10`
**Çıktı:** `Asal Degil`

### Örnek 3
**Girdi:** `1`
**Çıktı:** `Asal Degil`

### Örnek 4
**Girdi:** `2`
**Çıktı:** `Asal`

## İpuçları

- 1 ve 2 için özel kontrol yapın
- 2'den n-1'e kadar döngü ile bölenleri kontrol edin
- Eğer bir bölen bulursanız, asal değildir
- Optimizasyon: sqrt(n)'e kadar kontrol etmek yeterli
- `#include <cmath>` ile sqrt kullanabilirsiniz

## Algoritma

```
Eğer n <= 1 ise: Asal Degil
Eğer n == 2 ise: Asal
2'den sqrt(n)'e kadar:
    Eğer n % i == 0 ise: Asal Degil
Asal
```

## Puanlama

- ✅ Tüm test durumları: 100 puan
