import pandas as pd

# Загрузка данных из файла с явным указанием кодировки
file_path = 'ТЕГИ.CSV'
df = pd.read_csv(file_path, encoding='utf-8')

# Проверка наличия столбца 'Метки' в DataFrame
if 'Метки' not in df.columns:
    raise ValueError("Столбец 'Метки' не найден в DataFrame. Пожалуйста, убедитесь в правильности названия столбца.")

# Разделение меток и подсчет встречаемости
label_counts = {}
for labels in df['Метки'].dropna():
    label_list = [label.strip() for label in labels.split(' ')]
    for label in label_list:
        if label and label[0].isupper():
            label_counts[label] = label_counts.get(label, 0) + 1

# Создание выходного файла для 2012-2019 годов
years_2012_2019 = range(2012, 2020)
subset = df[df['Год'].isin(years_2012_2019)]
label_counts_2012_2019 = {}
for labels in subset['Метки'].dropna():
    label_list = [label.strip() for label in labels.split(' ')]
    for label in label_list:
        if label and label[0].isupper():
            label_counts_2012_2019[label] = label_counts_2012_2019.get(label, 0) + 1

result_2012_2019 = pd.DataFrame(list(label_counts_2012_2019.items()), columns=['Метка', 'Встречаемость'])
result_2012_2019.to_csv('output_2012_2019.csv', index=False)

# Создание выходного файла для 2020-2022 годов
years_2020_2022 = range(2020, 2023)
subset = df[df['Год'].isin(years_2020_2022)]
label_counts_2020_2022 = {}
for labels in subset['Метки'].dropna():
    label_list = [label.strip() for label in labels.split(' ')]
    for label in label_list:
        if label and label[0].isupper():
            label_counts_2020_2022[label] = label_counts_2020_2022.get(label, 0) + 1

result_2020_2022 = pd.DataFrame(list(label_counts_2020_2022.items()), columns=['Метка', 'Встречаемость'])
result_2020_2022.to_csv('output_2020_2022.csv', index=False)

# Создание выходного файла для 2023 года
subset_2023 = df[df['Год'] == 2023]
label_counts_2023 = {}
for labels in subset_2023['Метки'].dropna():
    label_list = [label.strip() for label in labels.split(' ')]
    for label in label_list:
        if label and label[0].isupper():
            label_counts_2023[label] = label_counts_2023.get(label, 0) + 1

result_2023 = pd.DataFrame(list(label_counts_2023.items()), columns=['Метка', 'Встречаемость'])
result_2023.to_csv('output_2023.csv', index=False)
