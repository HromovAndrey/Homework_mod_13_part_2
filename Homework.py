# Завдання 1
# Створіть два окремих "мікросервіси" (дві окремі
# програми). Одна програма створює та експортує дані у
# форматі JSON, а інша програма завантажує та обробляє ці
# дані. Це може бути, наприклад, система, яка створює та
# обробляє замовлення.
import json

def add_order():
    order = {
        "номер": "ЗМ0001",
        "товар": "Книга",
        "кількість": 2,
        "ціна": 150
    }
    return order

def export_data(filename):
    order = add_order()
    with open(filename, 'w') as file:
        json.dump(order, file)

if __name__ == "__main__":
    export_data("замовлення.json")
    print("Дані про замовлення було експортовано у файл 'замовлення.json'.")

#import json

def download_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def process_order(order):
    number = order["номер"]
    goods = order["товар"]
    quantity = order["кількість"]
    price = order["ціна"]


    total_cost  = quantity * price
    return number, goods, quantity, price, total_cost

if __name__ == "__main__":
    order = download_data("замовлення.json")
    number, goods, quantity, price, total_cost = process_order(order)
    print("Інформація про замовлення:")
    print("Номер:", number)
    print("Товар:", goods)
    print("Кількість:", quantity)
    print("Ціна за одиницю:", price)
    print("Загальна вартість:", total_cost)
