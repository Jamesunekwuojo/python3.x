writeText = "Exampletext"
# writing into file, if file is not present it's being  created
saveFile = open('example.txt', 'w')

saveFile.write(writeText);
saveFile.close();
