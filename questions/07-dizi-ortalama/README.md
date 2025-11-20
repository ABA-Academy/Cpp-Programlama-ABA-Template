# Soru 7: Dizi Ortalaması

## Zorluk: ⭐⭐ Orta

## Açıklama

Kullanıcıdan N adet sayı alın, bu sayıları bir dizide saklayın ve ortalamasını hesaplayıp yazdırın.

## İstenenler

1. İlk satırda kaç adet sayı girileceğini alın (N)
2. Sonraki N satırda sayıları alın ve bir dizide saklayın
3. Sayıların ortalamasını hesaplayın
4. Ortalamayı ondalıklı olarak yazdırın (2 basamak)

## Örnekler

### Örnek 1
**Girdi:**
```
5
10
20
30
40
50
```
**Çıktı:** `30.00`

### Örnek 2
**Girdi:**
```
3
5
10
15
```
**Çıktı:** `10.00`

### Örnek 3
**Girdi:**
```
4
1
2
3
4
```
**Çıktı:** `2.50`

## İpuçları

- Dizi tanımlayın: `int dizi[100];`
- Döngü ile sayıları diziye ekleyin
- Toplamı hesaplayın
- Ortalama = Toplam / Adet
- `cout << fixed << setprecision(2)` ile 2 basamak yazdırın
- `#include <iomanip>` eklemeyi unutmayın

## Puanlama

- ✅ Tüm test durumları: 100 puan
