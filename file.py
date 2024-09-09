
# <-----WRITE TO A FILE------->
writeText = "Exampletext"
# writing into file, if file is not present it's being  created
saveFile = open('example.txt', 'w')

saveFile.write(writeText)
saveFile.close()

# Writing into a file will overide any data or text that has being previously stored or present in the file
# Appending will not overide the current text present rather it will  update the file with the current data 


# <------APPPENDING TO A FILE------>

appendText = " is a file created using python functions"
saveFile = open('example.txt', 'a' )#'a' after the filename is the major difference between this and when writing afresh into a file"
saveFile.write(appendText)
saveFile.close()

# <-----READING TO A FILE-------->
readMe = open('example.txt', 'r').read()

print(readMe)
