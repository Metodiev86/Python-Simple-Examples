from sqlalchemy import or_, not_, and_
from sqlalchemy.orm import sessionmaker 
from Fresh_DB_Map import my_engine, Region, Client, Product, Category

#Създаваме сесия която я насочваме да работи с нашата база данни
Session = sessionmaker(bind=my_engine)

#Създаваме обект session
session = Session()

#Създаваме нoв обект, отговарящ за таблицата Region
# region = Region(Name = "София")

#Добавяме към сесията новосъздадения обект
# session.add(region)

#Запазваме промените в базата данни
# session.commit()

#Правим заявка, която връща като списък всички елементи от таблицата Region
# regions = session.query(Region).all()

#Опечатваме елементите върнати от заявката
# for region in regions:
#     print(str(region.ID) + " " + region.Name)

#Првим различен вид на филтрация
# region = session.query(Region).filter_by(ID=9).one_or_none()

#Изтриваме подаден елемент
# session.delete(region)
# session.commit()


#Правим подреба на елементите във възходящ ред по подаден критерий
region_alfabetical = session.query(Region).order_by(Region.Name).all()

for item in region_alfabetical:
    print(str(item.ID) + " " + item.Name)

print("-" * 50)

#Правим подреба във низходящ ред по зададен критерий
region_alfabetical_desc = session.query(Region).order_by(Region.Name.desc()).all()

for item in region_alfabetical_desc:
    print(str(item.ID) + " " + item.Name)

clients_filter = session.query(Client).filter(Client.Discount > 15).all()

for item in clients_filter:
    print(item.Name + " - " + str(item.Discount) + "%")

products_where = session.query(Product).where(Product.Currency >3.00).all()

for product in products_where:
    print(f"{product.Name} - {product.Currency:0.2f}")

products_logical_filter = (
    session.query(Product).
        where(
            or_(
                not_(Product.Categories_ID ==5),
                    and_(Product.Currency < 6.00)
                )
            )
        )

for product in products_logical_filter:
    print(f"{product.Name} - {product.Currency:0.2f}")
