# Dictionaries - the idea is to have keys and then values.
# All keys have to be unique, but their values are not immutable.

gradeDic = {'kelly':90, 'philipia':45, 'caleb':68}

print(gradeDic)


gradeDic['kelly'] = 45 # updating kelly

print(gradeDic)

del gradeDic['caleb'] #deleting  caleb

print(gradeDic) 

gradeDic = {"kelly": [40,45], 'philipia': [40,56]} # pairing values

print(gradeDic)
