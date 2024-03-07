#zip - обединява две или повече итеруеми структори в една

username = ("Stoyan", "Stela", "Misha")
password = ["123", "abc", "1a2s3d"]
date_login = ["1/1/2024", "1/2/2024", "1/3/2024",]

user = list(zip(username, password))
for i in user:
	print(i)
print()

dict_user = dict(zip(username, password))

for key, value in dict_user.items():
	print(key + " : " + value)
print()

user_info = zip(username, password, date_login)
for i in user_info:
	print(i)
	
input()