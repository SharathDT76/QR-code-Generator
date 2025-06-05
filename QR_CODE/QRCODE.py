import qrcode
from PIL import Image
from pygments.styles.dracula import background
from qrcode.console_scripts import error_correction

qr = qrcode.QRCode(version = 1,error_correction =qrcode.constants.ERROR_CORRECT_H,box_size = 10,border = 4)
qr.add_data("https://www.youtube.com/@Shadow-135-i9k/videos")
qr.make(fit = True)
img = qr.make_image(fill_color = "black",back_color = "white")
img.save("My_Youtube.png")