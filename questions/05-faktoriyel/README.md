# Soru 5: Faktöriyel Hesaplama

## Zorluk: ⭐⭐ Orta

## Açıklama

Kullanıcıdan bir pozitif tam sayı N alın ve N! (N faktöriyel) değerini hesaplayıp yazdırın.

**Faktöriyel Nedir?**
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 0! = 1 (tanım gereği)

## İstenenler

1. Kullanıcıdan pozitif bir tam sayı N alın (0 ≤ N ≤ 20)
2. N faktöriyel değerini hesaplayın
3. Sonucu yazdırın

## Örnekler

### Örnek 1
**Girdi:** `5`
**Çıktı:** `120`

### Örnek 2
**Girdi:** `0`
**Çıktı:** `1`

### Örnek 3
**Girdi:** `3`
**Çıktı:** `6`

### Örnek 4
**Girdi:** `10`
**Çıktı:** `3628800`

## İpuçları

- Bir değişken ile başlayın: `long long sonuc = 1;`
- `for` veya `while` döngüsü kullanın
- Her adımda sonucu mevcut sayı ile çarpın
- Büyük sayılar için `long long` kullanın

## Puanlama

- ✅ Tüm test durumları: 100 puan
