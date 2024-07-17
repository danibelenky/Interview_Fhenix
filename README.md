# Encrypted Database Exercise

### To run the solution:
in two separate terminals run:
    
    python server.py
And

    python client.py

in the client's terminal you'll be prompted with a request to put/get information form the DataBase. The messages 
received from the server will be printed into the terminal.
(I printed the encrypted message that was returned from the server, as well as the decrypted message (so the client decrypts the messages automatically))


### Explanations:

I chose to implement the task using python's sockets since they are an easy and quick solution for communication between
a client and server applications.

I chose the cryptography library and specifically the Fernet method for its easy and quick integration.
Moreover, from further research I discovered that the Fernet method requires the same key to be sed for encryption and decryption,
this enforces (obvious) demand that the server will not be able to decrypt the message sent by the client (and it remains confidential).
So, I believe it was a good choice for the implementation of the task.

In my implementation I allowed a client to overwrite (update) a key. But it's an easy fix to block that option if needed.
