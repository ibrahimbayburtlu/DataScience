import pyqrcode 


# String which represent the QR code 

link = "https://www.youtube.com/watch?v=fI-XfjQCDwM&t=113s"

url = pyqrcode.create(link)

url.svg("QR Codes/myyoutube.svg",scale=8)