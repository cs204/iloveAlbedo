s = input("Верблюжий стиль: ")
snake_case  =""
for c in s:
    if c.isupper():
        snake_case = snake_case + "_" + c.lower()
    else:
        snake_case = snake_case + c

print(snake_case)