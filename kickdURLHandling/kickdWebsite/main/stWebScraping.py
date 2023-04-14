from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys

def webScraper(data):
    url = "https://www.myst25.com/andef/index.php?data="
    if not data and len(sys.argv) <= 1:
        print("No argument was provided for data to check it's authenticity")
        return 0
    if data:
        url = "https://www.myst25.com/andef/index.php?data=" + data
    else:
        url = "https://www.myst25.com/andef/index.php?data=" + sys.argv[1]
    print(url)
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")


    small_elements = soup.findAll('small')


    authenticity_element = small_elements[1]
    authenticity = authenticity_element.text.strip()
    print(authenticity)
    is_authentic = False
    is_valid = False

    if "GENUINE" in authenticity:
        s_authentic = True
        return 0
    if "URL Invalid" in authenticity:
        print("Is the URL valid (is the data entered associated with a real chip): False")
        return 1
    
    print("Is the data authentic (Unique Tap Code valid): " + str(is_authentic))

    if not is_authentic:
        return 2
    else:
        return 3

if __name__ == '__main__':
    webScraper()