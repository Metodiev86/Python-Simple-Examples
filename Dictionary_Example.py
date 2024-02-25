#"Dictionary" е структора от данни, която е променлива, неподредена (неиндексирана),
# от уникални двойки "Ключ : Стойност". Изключително бързи защото използват хеширане.
# Позволяват бързо достъпване по стойност.

def bar() :
    n = 0
    while n<81:
        print("-", end="")
        n+=1
    print()


capitals = {"Japan" :  "Tokio",
            "China" : "Pekin",
            "Bulgaria" : "Sofia"}

print(capitals)

#Отпечатването на дадена стойност от речника, става като подаваме нейния ключ, като индекс.
print(capitals["Bulgaria"])
bar()
#Методът 'get()' е по безопасен за използване от индексатора, защото е ако дадена стойност за ключ не присъства,
#ще върне стойност "None", а няма да даде грешка
print(capitals.get("Germany"))
print(type(capitals.get("Germany")))
print(type(capitals.get("Japan")))
bar()
#Методът 'keys()', връща всички ключове, в речника
print(capitals.keys())
bar()
#Методът 'values()', връща всички стойности, в речника
print(capitals.values())

#Методът 'items()', връща всички двойки ключ : стойност, в речника
print(capitals.items())
bar()
#Промяната на речник се извършва с метода 'update()'.
# Първо проверява дали има такъв ключ за да промени стойноста му
# и ако няма създава нова двойка "ключ : стойност"
capitals.update({"Bulgaria" : "Plovdiv"})
capitals.update({"Македония" : "Скопие"})
bar()
for key, value in capitals.items():
    print(key, value)
#Методът 'pop()', изважда дадена двойки ключ : стойност, в речника, по нейния ключ
capitals.pop("China")

bar()
for key, value in capitals.items():
    print(key, value)

bar()

