# Turimas "audi" dict.

# Parašykite funkciją "show_object_values", kuri kaip argumentą priims objektą
# ir grąžins visus jo "values" list'e.

audi = {
    "make": 'audi',
    "model": 'A6',
    "year": 2005,
    "color": 'white',
}


def show_object_values(x):
    values_list = []
    for item, value in x.items():
        values_list.append(value)
    print(values_list)


show_object_values(audi)

# ats: ['audi', 'A6', 2005, 'white']
