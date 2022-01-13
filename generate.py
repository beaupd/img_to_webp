from PIL import Image
# from PIL import features
import os
# import sys

# print(features.check_module('webp'))

# IMAGE_OLD = '/Users/beaudekker/Desktop/etc/dutchwebs/channeldock/images/amazon-logo.png'
# IMAGE_NEW = '/Users/beaudekker/Desktop/etc/dutchwebs/channeldock/images/amazon-logo.webp'

# im = Image.open(IMAGE_OLD)
# im.save(IMAGE_NEW, format="WebP", lossless=True)


# def progress(count, total, status=''):
#     bar_len = 60
#     filled_len = int(round(bar_len * count / float(total)))

#     percents = round(100.0 * count / float(total), 1)
#     bar = '=' * filled_len + '-' * (bar_len - filled_len)

#     sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
#     sys.stdout.flush()


media_files = []

path = r'/Users/beaudekker/Desktop/etc/dutchwebs/channeldock/images/'

for root, directories, files in os.walk(path):
    for file in files:
        if(file.endswith(".png") or file.endswith(".jpg")):
            media_files.append(os.path.join(root, file))

total = len(media_files)
for i, media in enumerate(media_files):
    IMAGE_OLD = media
    temp = media.replace(".jpg", ".webp")
    IMAGE_NEW = temp.replace(".png", ".webp")

    im = Image.open(IMAGE_OLD)
    im.save(IMAGE_NEW, format="WebP", lossless=True)
    print("Saved new gen format at: \n", IMAGE_NEW, "\n")

print("done saved ", total, " total files")
