
flovor = ["mango" , "choco" , "tulsi" , "bannana"]

for i in flovor:
    if i == "mango":
        continue
    if i == "tulsi":
        break
    print(f"{i}")


print(f"the item is not available or the loop is came to an end")