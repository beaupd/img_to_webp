import bs4
from bs4 import BeautifulSoup

file_input = input("Input html file name: ")
filename = file_input if ".html" in file_input else file_input+".html"
print(filename)

with open(filename) as html_in:
    html = html_in.read()
    soup = bs4.BeautifulSoup(html, "html5lib")

imgs = soup.find_all("img")

for img in imgs:
    if ".jpg" not in str(img):
        if ".png" not in str(img):
            # print(".jpg" not in str(img))
            imgs.remove(img)

for img in imgs:
    # print(img["src"])
    temp = img["src"].replace(".jpg", "")
    src_base = temp.replace(".png", "")
    img.replace_with(BeautifulSoup(f"""
                    <picture>
                        <source srcset="{src_base}.webp" type="image/webp">
                        <source srcset="{src_base}.jpg" type="image/jpeg">
                        <img src="{src_base}.jpg">
                    </picture>
                    """, "html.parser"))

print(soup)
with open(f"{filename.replace('.html', '')}_new.html", "w") as file_out:
    file_out.write(str(soup.prettify()))

# print(soup)
