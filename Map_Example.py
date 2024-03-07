#Map() - функцията се прилага въху всеки итеруем елемент (list, tuple и т.н.)
#
#map(function, iterable) - приема два аргумента, функция и итериращ елемент

store = [("Дънки", 40.00),
         ("Риза", 35.00),
         ("Яке", 50.00),
         ("Чорапи", 5.00),
        ]

to_dolars = lambda data: (data[0], data[1]*0.55)

store_dolars = list(map(to_dolars, store))

for i in store_dolars:
  print(f"{i}")
print()
store_dolars = [('Дънки', 22.0),
                ('Риза', 19.25),
                ('Яке', 27.500000000000004),
                ('Чорапи', 2.75),
              ]
to_lv = lambda data: (data[0], data[1]/0.55)

store_lv = list(map(to_lv, store))

for i in store_lv:
  print(i)
