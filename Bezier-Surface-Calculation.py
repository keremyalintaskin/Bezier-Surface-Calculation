import numpy as np
from math import comb  # Kombinasyon hesaplama fonksiyonunu içe aktarıyoruz

def bezier_yuzeyi(kontrol_noktalari, u, w):
    """
    Kontrol noktaları ve u, w parametreleri ile Bézier yüzeyinde bir nokta hesaplar.
    :param kontrol_noktalari: Her biri (x, y, z) şeklinde bir tuple olan 2D kontrol noktaları listesi.
    :param u: u-yönünde [0, 1] aralığında bir parametre.
    :param w: w-yönünde [0, 1] aralığında bir parametre.
    :return: Bézier yüzeyindeki bir noktayı temsil eden (x, y, z) şeklinde bir tuple.
    """
    m = len(kontrol_noktalari) - 1  # Satır sayısı - 1
    n = len(kontrol_noktalari[0]) - 1  # Sütun sayısı - 1

    def bernstein(t, i, n):
        """Bernstein polinomu değerini hesaplar."""
        return comb(n, i) * (t ** i) * ((1 - t) ** (n - i))

    nokta = np.array([0.0, 0.0, 0.0])
    for i in range(m + 1):
        for j in range(n + 1):
            b = bernstein(u, i, m) * bernstein(w, j, n)
            nokta += b * np.array(kontrol_noktalari[i][j])

    return tuple(nokta)

# 5x3 Bézier yüzeyi için kontrol noktalarını tanımlıyoruz
kontrol_noktalari = [
    [(0, 0, 0), (1, 0, 1), (2, 0, 2), (3, 0, 1), (4, 0, 0)],
    [(0, 1, 1), (1, 1, 2), (2, 1, 3), (3, 1, 2), (4, 1, 1)],
    [(0, 2, 2), (1, 2, 3), (2, 2, 4), (3, 2, 3), (4, 2, 2)]
]

# P1 ve P2 için parametreler
u1, w1 = 0.25, 0.65
u2, w2 = 1.0, 0.0

# P1 ve P2 noktalarını hesaplıyoruz
P1 = bezier_yuzeyi(kontrol_noktalari, u1, w1)
P2 = bezier_yuzeyi(kontrol_noktalari, u2, w2)

# Delta (fark) değerlerini hesaplıyoruz
delta_x = P2[0] - P1[0]
delta_y = P2[1] - P1[1]
delta_z = P2[2] - P1[2]

# Sonuçları ekrana yazdırıyoruz
print(f"P1 için x={P1[0]:.2f}; y={P1[1]:.2f}; z={P1[2]:.2f}")
print(f"P2 için x={P2[0]:.2f}; y={P2[1]:.2f}; z={P2[2]:.2f}")
print(f"Δ||delta x={delta_x:.2f}")
print(f"Δ||delta y={delta_y:.2f}")
print(f"Δ||delta z={delta_z:.2f}")