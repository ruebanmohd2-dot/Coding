countrycode = {"india": "0091", "australia": "0025", "nepal": "00977"}
print("countrycode for india:")
print(countrycode.get("india", "not found"))

print("Country Code for Japan:")
print(countrycode.get("Japan", "Not found"))
