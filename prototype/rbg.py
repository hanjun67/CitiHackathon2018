# This script is to generate random number of entries
import random
import xlsxwriter


# Predefined variable
length = 100
property_id = []
price = []
pricePerSqFt = []
tenure = []
location = []
size = []
type = []
amenities = []

# Using random to instill randomize the number
for i in range(length):
	price.append(random.randint(100000,5000000))
	size.append(random.randint(645, 39000))
	pricePerSqFt.append(price[i]/size[i])
	tenure.append(random.randint(0,1))
	location.append((random.uniform(1.26828, 1.46828),random.uniform(104.6444, 104.024719)))
	type.append(random.randint(0,8))
	amenities.append(random.randint(0,7))
	
# To map the randomize number with the property type and tenure type
tenure2 = []
type2 = []
tenureType = [99, 'Free Hold']
propertyType = ['Executive Condo', '3 Room Flat', '4 Room Flat', '5 Room Flat', 'Bungalow', 'Shophouse', 'Terrace','Private Condo', 'Mansion']
for i in range(length):
	tenure2.append(tenureType[tenure[i]])
	type2.append(propertyType[type[i]])

# To map the randomize number to the amenities
amenities2 = [None] * length
amenitiesType = ['Gym', 'Pool', 'Park', 'MRT', 'Bus Stop', 'Market', 'Playground', 'Mall']
for i in range(length):
	# Sample out the set from amenities.
	a = random.sample(set(amenitiesType), amenities[i]+1)
	for j in a:
		if amenities2[i] == None:
			amenities2[i] = j
		else:
			amenities2[i] = amenities2[i] + ', ' + j 


# Write the Random Generated Data into the xlsx
workbook = xlsxwriter.Workbook('RGB.xlsx')
worksheet = workbook.add_worksheet()

row = 0

for i in range(length):
	worksheet.write(row, 0, i+1)
	worksheet.write(row, 1, price[i])
	worksheet.write(row, 2, pricePerSqFt[i])
	worksheet.write(row, 3, tenure2[i])
	worksheet.write(row, 4, '('+str(location[i][0])+','+str(location[i][1])+')')
	worksheet.write(row, 5, size[i])
	worksheet.write(row, 6, type2[i])
	worksheet.write(row, 7, amenities2[i])
	row += 1
	


workbook.close()
