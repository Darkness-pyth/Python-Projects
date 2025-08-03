import qrcode

upi_id = input("Enter Your UPI ID: ")

qr_code_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name'

Pay_qr = qrcode.make(qr_code_url)

Pay_qr.save('Pay_qr.png')

Pay_qr.show()