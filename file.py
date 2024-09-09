writeText = "Exampletext"
# writing into file, if file is not present it's being  created
saveFile = open('example.txt', 'w')

saveFile.write(writeText);
saveFile.close();

# Writing into a file will overide any data or text that has being previously stored or present in the file
# Appending will not overide the current text present rather it will  update the file with the current data 