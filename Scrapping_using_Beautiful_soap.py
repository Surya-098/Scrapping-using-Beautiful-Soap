import requests
from bs4 import BeautifulSoup


class Scrap:
    url = "https://www.flipkart.com/kitchen-cookware-serveware/lunch-boxes-bottles-and-flasks/water-bottles/pr?sid=upp%2Cf2k%2C0zz&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTExOSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sInRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIldhdGVyIEJvdHRsZXMiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJoZXJvUGlkIjp7InNpbmdsZVZhbHVlQXR0cmlidXRlIjp7ImtleSI6Imhlcm9QaWQiLCJpbmZlcmVuY2VUeXBlIjoiUElEIiwidmFsdWUiOiJCT1RGUUZZSkZKUjlaUEdaIiwidmFsdWVUeXBlIjoiU0lOR0xFX1ZBTFVFRCJ9fX19fQ%3D%3D&fm=neo%2Fmerchandising&iid=M_3ad240fe-038d-40ee-afae-27d8b0ba2f2f_4.9SO6PU1JKLWT&ssid=huh0bgh4ao0000001656749216375&otracker=hp_omu_Top%2BOffers_1_4.dealCard.OMU_9SO6PU1JKLWT_3&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Top%2BOffers_NA_dealCard_cc_1_NA_view-all_3&cid=9SO6PU1JKLWT"


    data = requests.get(url)

    soup = BeautifulSoup(data.content, 'lxml')

    def website(self):
        return self.soup.prettify()

    def product_name(self):
        product_name = self.soup.find('div', class_='_4rR01T')
        print(product_name)
        return product_name.text
