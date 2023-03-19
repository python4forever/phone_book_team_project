

def format_data(all_data, src):
    with open(src, 'a', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=';', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(all_data)
