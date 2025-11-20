# Soru 10: Fibonacci Dizisi

## Zorluk: ⭐⭐⭐ İleri

## Açıklama

Kullanıcıdan bir sayı N alın ve Fibonacci dizisinin ilk N elemanını yazdırın.

**Fibonacci Dizisi Nedir?**
- Her sayı, kendinden önceki iki sayının toplamıdır
- Dizi: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2)

## İstenenler

1. Kullanıcıdan pozitif bir tam sayı N alın
2. Fibonacci dizisinin ilk N elemanını hesaplayın
3. Her elemanı boşlukla ayırarak tek satırda yazdırın

## Örnekler

### Örnek 1
**Girdi:** `7`
**Çıktı:** `0 1 1 2 3 5 8`

### Örnek 2
**Girdi:** `5`
**Çıktı:** `0 1 1 2 3`

### Örnek 3
**Girdi:** `1`
**Çıktı:** `0`

### Örnek 4
**Girdi:** `2`
**Çıktı:** `0 1`

## İpuçları

- İki değişken kullanın: `a = 0, b = 1`
- Döngü ile:
  - Mevcut değeri yazdırın
  - Yeni değer = a + b
  - a = b, b = yeni değer
- Alternatif: Dizi kullanarak hesaplayın

## Kod Şablonu

```cpp
int a = 0, b = 1;
for (int i = 0; i < n; i++) {
    cout << a << " ";
    int yeni = a + b;
    a = b;
    b = yeni;
}
```

## Puanlama

- ✅ Tüm test durumları: 100 puan
