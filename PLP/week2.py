# list_1= [1 ,2 , 3, 4 ,5]
# # print(list_1[4])
# list_1 [0] = 44
# # print(list_1)
# list_1.insert(len(list_1),44)
# # print(list_1)
# list_1.append(66)
# # print(list_1)
# for item in list_1:
#     # print(item)

# prime_numbers = [2, 3, 5]  # Converting to a list
# print("List 1:", prime_numbers)

# even_numbers = [4, 6, 8]  # Converting to a list
# print("List 2:", even_numbers)

# prime_numbers.extend(even_numbers)  # Using extend() with a list
# print("List 1 after extending:", prime_numbers)

# # Converting back to a tuple if needed
# prime_numbers = tuple(prime_numbers)
# print("Tuple 1 after extending:", prime_numbers)

# numbers = [number*number for number in range (1,10)]
# print(numbers)

# capital_cities ={"Kenya" : "Nairobi " , "Tanzania" : "Dodoma" , "Uganda" :"Kampala"}
# print ("Intial capital cities:", capital_cities)
# capital_cities["Rwanda"] = "Kigali"
# print("Update capital cities:", capital_cities)
# del capital_cities["Tanzania"]
# print("updated capital_cities" , capital_cities)
# print(capital_cities['Tanzania'])

name = "Frank"
age = 22
country = "Kenya"
print(f"My name is {name}, I am {age} and I'm from {country}")