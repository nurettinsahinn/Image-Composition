
# resim üstüne resim ekleme programı*****

import cv2
import numpy as np

# Görüntüleri yükle
img2 = cv2.imread("ucak.jpeg")
img1 = cv2.imread("turkbayragii.jpg")

#  resmin boyutlarını al
height, width, _ = img1.shape

#  resmi küçült
scale_percent = 30  # Küçültme yüzdesi
new_width = int(width * scale_percent / 100)
new_height = int(height * scale_percent / 100)
img1_resized = cv2.resize(img1, (new_width, new_height))

# İlk görüntüyü arkaplanla birleştirerek ön planı oluştur
mask = np.zeros((img2.shape[0], img2.shape[1]), dtype=np.uint8)

# Beyaz renkli pikselleri maskele(opsiyoneldir kendi maskelemek istediğiniz renk dizisini giriniz!)
white_mask = cv2.inRange(img1_resized, np.array([240, 240, 240]), np.array([255, 255, 255]))

# Beyaz maskenin tam tersini al
mask_inv = cv2.bitwise_not(white_mask)

# Tusas resmini sol üst köşeye yerleştir
x_offset = 0
y_offset = 0
roi = img2[y_offset:y_offset+new_height, x_offset:x_offset+new_width]
img1_fg = cv2.bitwise_and(img1_resized, img1_resized, mask=mask_inv)
img2_bg = cv2.bitwise_and(roi, roi, mask=white_mask)

# Ön planı ve arka planı birleştir
dst = cv2.add(img1_fg, img2_bg)

# Yeni oluşturulan görüntüyü orijinal görüntüdeki ROI'ye yerleştir
img2[y_offset:y_offset+new_height, x_offset:x_offset+new_width] = dst

# Sonucu göster
cv2.imshow("resim", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
