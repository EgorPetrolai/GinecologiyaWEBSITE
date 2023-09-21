import requests
from bs4 import BeautifulSoup
with open('data.txt', 'r', encoding='utf-8') as file:
    # Читаем содержимое файла и разделяем его по запятым
    google_sheet_links = file.read().split(', ') # Список ссылок на Google Таблицы

    # Создаем пустой список для названий таблиц
    table_names = []

    # Проходим по каждой ссылке и извлекаем название таблицы
    for link in google_sheet_links:
        response = requests.get(link)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            table_name_element = soup.find('title')

            if table_name_element:
                table_name = table_name_element.text.strip()
                table_names.append(table_name)
            else:
                table_names.append('Название не найдено')
        else:
            table_names.append('Ошибка при доступе к таблице')

    only_date = [item.split('-')[0].strip() for item in table_names]
    only_date_name = [item.split('-')[1].strip() for item in table_names]



insert_html_template1 = '''<h5 style="text-align: center;"><a href="'''
insert_html_template2 = '''">'''
insert_html_template3 = '''</a></h5>'''

result = []

for one, two in zip(google_sheet_links, only_date):
    template = insert_html_template1 + one + insert_html_template2 + two + insert_html_template3
    result.append(template)

final_html = '\n'.join(result)

list_final_html = final_html.split('\n')


if only_date_name[0] == 'понедельник.xlsx':
    check = 5
elif only_date_name[0] == 'вторник.xlsx':
    check = 4
elif only_date_name[0] == 'среда.xlsx':
    check = 3
elif only_date_name[0] == 'четверг.xlsx':
    check = 2
elif only_date_name[0] == 'пятница.xlsx':
    check = 1

first_week = ''
count = 0
while count < len(list_final_html) and count != check:
    first_week = first_week + list_final_html[count] + '\n'
    count += 1
print(count)
second_week = ''
while count < len(list_final_html) and count <= check + 4:
    second_week = second_week + list_final_html[count] + '\n'
    count += 1
print(count)
third_week = ''
while count < len(list_final_html) and count <= check + 9:
    third_week = third_week + list_final_html[count] + '\n'
    count += 1
print(count)
fourth_week = ''
while count < len(list_final_html) and count <= check + 14:
    fourth_week = fourth_week + list_final_html[count] + '\n'
    count += 1

fifth_week = ''
while count < len(list_final_html) and count <= check + 19:
    fifth_week = fifth_week + list_final_html[count] + '\n'
    count += 1

print(first_week)
print(second_week)
print(third_week)
print(fourth_week)
print(fifth_week)
print(count)

html1 = """
    <table hidden>
        <tbody>
            <tr>
                <td colspan="2" width="623">"""
html2 = """</td>
        </tr>
        <tr>
            <td width="311">"""
html3 = """</td>
            <td width="312">"""
html4 = """</td>
        </tr>
        <tr>
            <td style="text-align: center;" width="311">"""
html5 = """</td>
            <td width="312"> """
html6 = """</td>
        </tr>
    </tbody>
</table>"""
resultHtml = html1 + '\n' + first_week + html2 + '\n' + second_week + html3 + '\n' + third_week + html4 + '\n' + fourth_week +html5 + '\n' + fifth_week + html6

print(resultHtml)
with open("resultHTML.txt", "w") as file:
    file.write(resultHtml)