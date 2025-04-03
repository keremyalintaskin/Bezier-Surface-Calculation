# Bezier Yüzeyi Hesaplama

## Açıklama
Kontrol noktaları ve parametre değerleri kullanarak Bézier yüzeyindeki noktaları hesaplamak için Python tabanlı bir uygulamadır. Bu proje, Bézier yüzeyindeki 3D noktaları hesaplamayı ve iki yüzey noktası arasındaki farkları (delta değerlerini) nasıl hesaplayacağınızı gösterir. 3D modelleme ve grafik uygulamalarına genişletilebilir.

## Özellikler
- Verilen kontrol noktaları ve u, w parametreleri için Bézier yüzeyi noktalarını hesaplar.
- İki yüzey noktası arasındaki farkları (delta) hesaplar.
- Bézier yüzeyi hesaplamalarında Bernstein polinomlarının kullanımını gösterir.

## Gereksinimler
- Python 3.x
- NumPy kütüphanesi

## Çalıştırma
1. Depoyu yerel makinenize klonlayın.
2. Gerekli bağımlılıkları yüklemek için şu komutu çalıştırın:
```pip install numpy```

3. `bezier_surface.py` dosyasını çalıştırarak sonuçları görün.

## Örnek
Kod, Bézier yüzeyindeki iki noktayı (`P1` ve `P2`) hesaplar ve ardından x, y ve z koordinatlarındaki farkları hesaplar.


