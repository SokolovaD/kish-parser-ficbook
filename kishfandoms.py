import csv
from collections import Counter

def process_column(input_csv_path, output_csv_path, output_count_csv_path):
    with open(input_csv_path, 'r', encoding='utf-8') as infile, open(output_csv_path, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['Processed_Column']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        processed_column = []

        for row in reader:
            original_value = row.get('Pairings', '')  # Замените 'Your_Column_Name' на фактическое имя вашего столбца
            processed_value = process_string(original_value)
            row['Processed_Column'] = processed_value
            writer.writerow(row)
            processed_column.append(processed_value)

        # Сохраняем элементы листа и их частоты в новый файл
        save_processed_count(processed_column, output_count_csv_path)

def process_string(input_string):
    if '/' in input_string:
        # Если есть слэш, обрабатываем строку
        parts = input_string.rsplit('/', 1)
        if ',' in parts[1]:
            # Если есть запятая после последнего слэша, удаляем все, что идет после нее (включая запятую)
            parts[1] = parts[1].split(',', 1)[0]
        return '/'.join(parts)
    else:
        # Если нет слэша, заменяем на пустую строку
        return ''

def save_processed_count(processed_column, output_count_csv_path):
    # Создаем лист с элементами, разделенными по запятой
    processed_string = ', '.join(processed_column)
    processed_elements = processed_string.split(', ')

    # Создаем Counter для подсчета частоты элементов
    processed_counter = Counter(processed_elements)

    # Сохраняем уникальные элементы и их частоты в новый файл
    with open(output_count_csv_path, 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['Processed_Element', 'Frequency']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for element, frequency in processed_counter.items():
            writer.writerow({'Processed_Element': element, 'Frequency': frequency})

# Пример использования
input_file_path = 'Парсинг КиШа - ПЕЙРИНГИ 3.csv'
output_file_path = 'Парсинг КиШа - ПЕЙРИНГИ 3 output.csv'
output_count_file_path = 'Парсинг КиШа - ПЕЙРИНГИ 3 output_count.csv'

process_column(input_file_path, output_file_path, output_count_file_path)



