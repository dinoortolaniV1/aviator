import requests
from bs4 import BeautifulSoup


class AviatorMultiplier:
    def __init__(self):
        self.url = "https://www.bahsegel821.com/tr/game/aviator-spribe/play-for-fun"

    def get_multipliers(self):
        # HTTP GET isteği gönder
        response = requests.get(self.url)

        # Yanıtın durum kodunu kontrol et
        if response.status_code == 200:
            # HTML içeriğini ayrıştır
            soup = BeautifulSoup(response.content, "html.parser")

            # "app-bubble-multiplier" taglarını bul
            bubble_multiplier_tags = soup.find_all("app-bubble-multiplier")

            # Tüm "app-bubble-multiplier" taglarının içindeki metni bir listeye ekle
            multipliers = [
                bubble_multiplier_tag.text.strip() for bubble_multiplier_tag in bubble_multiplier_tags
            ]

            return multipliers
        else:
            # Web sitesine erişim sağlanamadı
            raise Exception("Web sitesine erişim sağlanamadı. Durum kodu:", response.status_code)

    def calculate_average(self, multipliers):
        # Metni integer dizisine dönüştür
        integer_multipliers = [int(multiplier) for multiplier in multipliers]

        # Dizideki sayıların ortalamasını hesapla
        average = sum(integer_multipliers) / len(integer_multipliers)

        return average

    def run(self):
        # Sayfadaki ilk 10 `app-bubble-multiplier` etiketinin içindeki metni çek
        multipliers = self.get_multipliers()

        # Dizideki sayıların ortalamasını hesapla
        average = self.calculate_average(multipliers)

        # Ortalamayı ekrana yazdır
        print("Ortalama:", average)


if __name__ == "__main__":
    # Eklentiyi başlat
    AviatorMultiplier().run()
