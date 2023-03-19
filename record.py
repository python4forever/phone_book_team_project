def format_data(all_data, sep):
    separated_data = ''
    for i in all_data:
        separated_data += sep.join(i.values())
    return separated_data

def write_data(all_data, src):
    with open(src, 'w', encoding='utf-8') as file:
        file.write(format_data(all_data), '||')