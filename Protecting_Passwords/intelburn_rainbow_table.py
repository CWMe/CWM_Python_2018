#This was created by intelburn for a Code With Me challenge
#Import HashLib for the MD5 hashing capability
import hashlib
#open the dictionary file
with open("plaintext_passwords.txt", "r") as candidates:
    #Open the file for the future rainbow table
    with open("rainbow_table.txt", "w") as rainbow:
        #Loop through the lines in dictionary
        for line in candidates.readlines():
            #This line does multiple things in one line the next comments will go into the what the line is doing
            #First rainbow.write will write the contents of the argument into the file
            #hashlib.md5 will calculate the contents on the argument
            #line.rstrip() will remove the trailing newline
            #.encode() will encode the line for hashlib.md5
            #.hexdigest returns the human readable version of the hash
            #Then append a , and the content of the line from the plaintext
            rainbow.write(hashlib.md5(line.rstrip().encode()).hexdigest()+","+line)
