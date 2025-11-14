

MySet = {
    "name" : ["vivian", "Marcel" , "sequeira" ,"sequeira"],
    "talent" : ["nothing" , "but something" , "Sleeping"],
    "Name" : ["Vivian" , "Marcel" , "sequeira"]
}


unique = {uniq for unq in MySet.values() for uniq in unq}

print(unique)