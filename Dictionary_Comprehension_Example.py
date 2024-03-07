#Създаване на речници с по-лесен синтаксис:
#dictionaru = [ключ : израз за ключа и стойностите въху елементите]
#dictionaru = [ключ : израз за ключа и стойностите въху елементите, if условие]
#dictionaru = [ключ : (if/elsе условие)израз за ключа и стойностите въху елементите]

cities_in_F = {"New Yourk":32, "Boston":75, "Los Angelis":100, "Chikago":55}

cities_in_C = {key: round((value-32)*(5/9)) for key, value in cities_in_F.items()}
print(cities_in_C)

city_weather = {"New Yourk" : "snow", "Boston" : "sunny", "Los Angelis" : "sunny", "Chikago" : "cloud"}

sunny_dictionary = {key: value for key, value in city_weather.items() if value=="sunny"}
print(sunny_dictionary)

citi_desc	= {key: ("Hot" if value > 20  else "Cold") for key, value in cities_in_C.items()}
print(citi_desc)

def isHot(value):

	if value >= 70:
		return "Hot"
	elif 69 >= value <= 40:
		return "Warm"
	else:
		return "Cold"

city_desc_function = {key: isHot(value) for (key, value) in cities_in_F.items()}
print(city_desc_function)
