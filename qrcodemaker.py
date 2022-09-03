# Script to write and read QR Codes

import qrcode
import cv2
import os


# Function to generate the QR code
def write_qr():
    # Receiving the data to transform into QR Code
    link = input("Enter link to generated QR Code: ")
    # Storing the QR code file name
    save_name = input("Enter file name to save QR Code: ")
    # Creating the QR code
    img = qrcode.make(link)
    type(img)
    img.save(save_name + ".png")
    print(save_name + " is saved")


# Function to read the contents of a QR code
def read_qr():
    # Receiving the file name
    file_name = input("Enter QR Code file name: ")
    # Receiving the file type
    file_type = input("Enter QR Code file type: ")
    d = cv2.QRCodeDetector()

    # Checking if the file exists
    if os.path.isfile(file_name + "." + file_type):
        # Transforming the QR code into text
        val, _, _ = d.detectAndDecode(cv2.imread(file_name + "." + file_type))
        print("Decoded text is: ", val)
    else:
        print("Wrong file entered")


# Main menu function
def main():
    while True:
        # Showing the main menu
        print("----MENU-----")
        print("1. Generate QR")
        print("2. Read QR")
        print("3. Exit")
        # Collecting user choice
        response = input("Choice: ")

        # Checking user selection. If selection is invalid program loops until a valid selection is inputted
        if response == "1":
            write_qr()
        elif response == "2":
            read_qr()
        elif response == "3":
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
