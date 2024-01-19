import qrcode

def generate_qr_code(link, output_file='qrcode.jpg'):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file in JPG format
    img.save(output_file, format='JPEG')

if __name__ == "__main__":
    link = input("Enter the link for the QR code: ")
    output_file = input("Enter the output file name (default is 'qrcode.jpg'): ") or 'qrcode.jpg'
    
    generate_qr_code(link, output_file)
    print(f"QR code generated and saved as {output_file}")