#created by Matthew Walsh
#created for ICS3U 
#created on oct 2017
#nested loop alphabet lower and upper case

for uppercase in range(65,91):
    for lowercase in range(97,123):     
           print(str(unichr(uppercase)) + "  " + str(unichr(lowercase)))
