# pip install qrcode module to use it  
import qrcode

upi_id = input("Enter Your UPI ID: ") # Take input from users for their Upi id


qr_code_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name' #Here we Define qr code url structure

Pay_qr = qrcode.make(qr_code_url) # Here We use qrcode module to make qrcode

Pay_qr.save('Pay_qr.png') # Here we save it in our computer as an image

Pay_qr.show() # Here we show the qr using pillow module