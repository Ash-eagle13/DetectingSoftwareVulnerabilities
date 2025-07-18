#Store sensitive data without encryption
ssn = input ("Enter your SSN: ")
with open ("userdata.txt", "w") as f:
    f.write (f"SSN: {ssn}\n")
print ("user data saved. ")