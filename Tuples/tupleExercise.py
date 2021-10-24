# exercise:create a tuple with five items  
countriesTup = ("USA", "Canada", "Russia", "China", "UK")

# print the tuple items
print(countriesTup)

# add two more items to your tuple
countriesTup = countriesTup + ("Italy", "France")
print("Adding more countries to the Tuple: ", countriesTup)

# sort in asceding and descending order 
countriesAsc = sorted(countriesTup)
print(countriesAsc)

countriesDesc = sorted(countriesTup, reverse=True)
print(countriesDesc)

# Iterate over your tuple print the tems

for i in countriesAsc:
    print("Countries Asc: ",i)

for i in countriesDesc:
    print("Countries Desc: ", i)