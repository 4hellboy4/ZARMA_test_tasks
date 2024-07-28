import csv
import json


class Item:
    def __init__(self, name:str, sales:list[tuple[str, str]]):
        self.name = name
        self.sales = sales


def json_parser(data: dict[str, Item]) -> None:
    with open('data/info.json', 'r', encoding='utf-8') as file:
        sales = json.load(file)
        for sale in sales:
            data[str(sale['product_id'])].sales.append((str(sale['sale_id']), str(sale['amount'])))
        file.close()


def csv_parser() -> dict[str, Item]:
    data = {}
    with open('data/info.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            product_id, product_name = row
            data[product_id] = Item(product_name, [])
        file.close()
    return data


def display_data_row_by_row(data: dict[str, Item]) -> None:
    with open('data/res2.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['product_id', 'name', 'sale_id', 'amount'])
        for k in data.keys():
            if len(data[k].sales) == 0:
                writer.writerow([k, data[k].name, "NO SALES", ""])
                continue
            for sale in data[k].sales:
                writer.writerow([k, data[k].name, sale[0], sale[1]])
        file.close()


def merge_data() -> None:
    data: dict[str, Item] = csv_parser()
    json_parser(data)
    for k in data.keys():
        print(f'{k}: {data[k].name}, {data[k].sales}')
    display_data_row_by_row(data)


def main() -> None:
    merge_data()


if __name__ == '__main__':
    main()
