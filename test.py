import csv


filename = 'results.csv'
with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    second_field_values = []

    for row in reader:
        if len(row) > 1:
            second_field_values.append(row[1])

max_value = max(second_field_values)

print("Максимальное значение во втором поле:", max_value)
