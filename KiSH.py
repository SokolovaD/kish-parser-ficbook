import csv

# Замените 'input.csv' на путь к вашему CSV файлу
input_file_path = 'KISHALL.csv'
output_file_path = 'output2.csv'

# Создаем новый CSV файл с дополнительными столбцами
with open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
    # Заголовки новых столбцов
    fieldnames = ['Type','Rating','Statues','Fandoms','Pairings','Data','Tags']

    # Создаем писателя CSV файла
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)

    # Записываем заголовки в новый файл
    writer.writeheader()

    # Читаем CSV файл
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        # Создаем читателя CSV файла
        reader = csv.reader(input_file)

        # Пропускаем заголовки
        next(reader, None)

        # Обрабатываем каждую строку входного файла
        for row in reader:
            # row в списке
            # print (row[0])
            # print(type(row[0]))
            print("***")
            line = row[0].split("\n")
            type = line[0]
            rating = line[1]
            statues = line[2]

            # идём по Line, находим флаг a с названием Фандомы - вытаскиваем их, флаг б с пейрингами, флаг с датой, флаг д с метками
            fandom = 0
            peiring = 0
            data = 0
            metki = 0

            for i in range(len(line)-1):
                if "Фэндом" in line[i]: fandom = i + 1
                if "Пэйринг" in line[i]: peiring = i + 1
                if "Дата" in line[i]: data = i + 1
                if "Метки" in line[i]: metki = i + 1
            if fandom != 0: fandomA = line[fandom]
            else: fandomA = ""
            if peiring != 0: peiringA = line[peiring]
            else: peiringA = ""
            if data != 0: dataA = line[data]
            else: dataA = ""
            if metki != 0: metkiA = line[metki]
            else: metkiA = ""

            # Записываем данные в новую строку
            new_row = {'Type': type, 'Rating': rating, 'Statues': statues, 'Fandoms': fandomA, 'Pairings': peiringA, 'Data': dataA, 'Tags': metkiA}

            # Записываем новую строку в новый файл
            writer.writerow(new_row)

print("Готово! Проверьте файл", output_file_path)
