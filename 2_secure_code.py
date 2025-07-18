from cryptography.fernet import Fernet
#Generate key and save it securely (Stimulate loading a secure)
key = Fernet.generate_key()
cipher = Fernet (key)
ssn = input ("Enter your SSN: ")
enc_ssn = cipher.encrypt (ssn.encode())
with open ("userdata_encrypted.txt", "wb")as f:
    f.write (enc_ssn)
print ("Encrypted user data saved.")
