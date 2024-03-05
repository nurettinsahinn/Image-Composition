# Resim Üstüne Resim Ekleme Programı

Bu program, birinci resmin üstüne ikinci resmi ekleyerek yeni bir görüntü oluşturur. Birinci resim, ikinci resmi kaplayacak bir arka plan olarak kullanılırken, ikinci resim üstte görünecek ön planı oluşturur.

## Nasıl Kullanılır

1. Programı çalıştırmak için Python yüklü olmalıdır.
2. İlk resmi `img2` olarak adlandırılan dosya ile ikinci resmi `img1` olarak adlandırılan dosya ile değiştirin.
3. Resimlerin boyutlarını ve pozisyonlarını ayarlamak için gerekirse `scale_percent`, `x_offset` ve `y_offset` değişkenlerini düzenleyin.
4. Programı çalıştırın ve sonucu gözlemleyin.

## Önemli Notlar

- İlk resmin boyutları ve pozisyonu, ikinci resmin üzerine yerleştirilme şeklini belirler. Bu nedenle, resimlerin boyutları ve konumları dikkatlice ayarlanmalıdır.
- Opsiyonel olarak, beyaz renkli pikselleri farklı bir renkle maskeleyebilirsiniz. Bu işlem için `white_mask` değişkenini güncelleyin.

## Kullanılan Teknolojiler

- Python
- OpenCV (cv2)
- NumPy
