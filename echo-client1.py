#!/usr/bin/env python3

import socket

def main():
    HOST = '192.168.100.20'  # Server IP address
    PORT = 65432 # Server port

    # Connecting to server using server IP address and port number
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        

        numbers = [] # Creating a list to store numbers provided by the user
        print("Enter up to 4 numbers (press Enter after each number, or leave empty to stop program)")
        
        # For loop executes 4 times
        for _ in range(4):
            num = input("Enter a number: ").strip() # Stores user entered number as string and strips anything extra (eg. space)
            
            # Breaks loop if no number entered
            if not num:
                break 
            
             # Ensures only digits are entered (Found here: https://www.w3schools.com/python/ref_string_isdigit.asp)
            if not num.isdigit():
                print("Invalid input. Please enter only integers.")
                return

            # Stores number in numbers list
            numbers.append(num)
        
        # Adding user entered numbers to message, encoding message and then sending the message to the server
        message = ','.join(numbers) # Found here: https://www.w3schools.com/python/ref_string_join.asp
        s.sendall(message.encode())
        
        response = s.recv(1024) # Stores message receive from server
        print("Server response:", response.decode()) # Decode message from server and prints out

# Found here: https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    main()
