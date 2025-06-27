#!/usr/bin/env python3

import socket

# Function to calculate whether passed in number is a power of two (found here: https://stackoverflow.com/questions/57025836/how-to-check-if-a-given-number-is-a-power-of-two)
def powOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0

def main():
    HOST = '192.168.100.20' # Server IP address
    PORT = 65432 # Server port

    # Creating binding host and port numbers to server and listening for communication
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Server listening on", HOST, PORT) # Prints that the server is listening on the specified host and port numbers
        
        conn, addr = s.accept() # Accepts connection from client
        with conn:
            print('Connected by', addr) # Prints that a connection has been made from a certain address
            data = conn.recv(1024) # Receives message from client
            if data:
                numbers = data.decode().split(',') # Decodes message and splits numbers up
                results = ["TRUE" if powOfTwo(int(num)) else "FALSE" for num in numbers] # Stores results from powOfTwo function (true or false)
                conn.sendall(','.join(results).encode()) # Encodes results and send results to client
        
    print("Server shutting down.") # Prints that the server is shutting down

# Found here: https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    main()
