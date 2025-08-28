from json import dumps, loads, dump, load

json_string = '{"name": "Джон", "возраст": 30, "city": "New York", "kids": ["Mike", "Anna"], "pets": {"dog": "Rex", "cat": "Barsik"}, "wife": {"name": "Jane", "age": 28}}'  # json-строка
print(json_string, type(json_string))  # строка)

json_object = loads(json_string)  # преобразование строки в объект
print(json_object, type(json_object))  # словарь)

json_string = dumps(json_object, indent=4, ensure_ascii=False)  # преобразование объекта в строку
print(json_string, type(json_string))  # строка)

with open("data.json", "w", encoding="utf-8") as file:
    dump(json_object, file, indent=4, ensure_ascii=False)
    
with open("data.json", "r", encoding="utf-8") as file:
    json_object = load(file)
    print(json_object, type(json_object))    
    
   