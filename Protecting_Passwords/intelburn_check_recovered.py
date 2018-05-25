#This was created by intelburn for a Code With Me challenge
#Open the file with all of the recovered hashes
with open("recovered_password_hashes.txt", "r") as hashes:
    #Open the csv formatted rainbow table
    with open("rainbow_table.txt", "r") as rainbow:
        #create a dict for all of the hashes and paintext passwords
        solutions={}
        #loop through the lines in the rainbow table
        for line in rainbow.readlines():
            #make an array of the line with the hash in position 0 and the plaintext in position 1
            #remove any trailing newlines
            entry=line.rstrip().split(",")
            #add the array to the dict
            solutions[entry[0]]=entry[1]
        #loop through the lines in the recovered passwords
        for line in hashes.readlines():
            #Remove the trailing newline from the recovered password hash
            password=line.rstrip()
            #check if the recovered hash is in the rainbow table
            if password in solutions:
                #print the hash and plaintext
                print(password+" "+solutions[password])
            #No match found
            else:
                #print that there is no match
                print("Hash {0} not in table".format(password))
