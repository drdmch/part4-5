
import re

name = r"[A-Za-zА-Яа-яІіЇїЄєҐґ0-9'’_-]{1,20}"
quantity = r"[0-9]+\.[0-9]{4}"
price = r"[0-9]+\.[0-9]{2}"
position = r"[1-9][0-9]*"
cost = r"[+-]?(?:[0-9]+(?:\.[0-9]+)?|\.[0-9]+)"
invoice = r"[A-Za-z0-9]{11}"
sep = r"[ \t]*[;:?][ \t]*"

pattern = re.compile(
    rf"(?P<name>{name}){sep}"
    rf"(?P<quantity>{quantity}){sep}"
    rf"(?P<price>{price}){sep}"
    rf"(?P<position>{position}){sep}"
    rf"(?P<cost>{cost}){sep}"
    rf"(?P<invoice>{invoice})"
)

with open("input.txt", "r", encoding="utf-8") as source, \
     open("output.txt", "w", encoding="utf-8") as result:

    for number, line in enumerate(source, 1):
        line = line.rstrip("\r\n")

        if not pattern.fullmatch(line):
            print(f"Рядок {number}: некоректний запис")
            continue

        converted = pattern.sub(r"\g<cost>;\g<invoice>", line)

        result.write(converted + "\n")

print("Готово! Результат записано у output.txt")
