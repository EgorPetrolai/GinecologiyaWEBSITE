from bs4 import BeautifulSoup
with open('data.txt', 'r', encoding='utf-8') as file:
    # Читаем содержимое файла и разделяем его по запятым
    data = file.read().split(',')
html_code = """
<table>
    <tbody>
        <tr>
            <td colspan="2" width="623">
                <h5 style="text-align: center;"><a href="{0}"></a></h5>
                <h5 style="text-align: center;"><a href="{1}"></a></h5>
                <h5 style="text-align: center;"><a href="{2}"></a></h5>
                <h5 style="text-align: center;"><a href="{3}"></a></h5>
                <h5 style="text-align: center;"><a href="{4}">0</a></h5>
            </td>
        </tr>
        <tr>
            <td width="311">
                <h5 style="text-align: center;"><a href="{5}"></a></h5>
                <h5 style="text-align: center;"><a href="{6}"></a></h5>
                <h5 style="text-align: center;"><a href="{7}"></a></h5>
                <h5 style="text-align: center;"><a href="{8}"></a></h5>
                <h5 style="text-align: center;"><a href="{9}"></a></h5>
            </td>
            <td width="312">
                <h5 style="text-align: center;"><a href="{10}"></a></h5>
                <h5 style="text-align: center;"><a href="{12}"></a></h5>
                <h5 style="text-align: center;"><a href="{13}"></a></h5>
                <h5 style="text-align: center;"><a href="{14}"></a></h5>
                <h5 style="text-align: center;"><a href="{15}"></a></h5>
            </td>
        </tr>
        <tr>
            <td style="text-align: center;" width="311">
                <h5 style="text-align: center;"><a href="{16}"></a></h5>
                <h5 style="text-align: center;"><a href="{17}"></a></h5>
                <h5 style="text-align: center;"><a href="{18}"></a></h5>
                <h5 style="text-align: center;"><a href="{19}"></a></h5>
                <h5 style="text-align: center;"><a href="{20}"></a></h5>
            </td>
            <td width="312">
                <h5 style="text-align: center;"><a href="{21}"></a></h5>
                <h5 style="text-align: center;"><a href="{22}"></a></h5>
                <h5 style="text-align: center;"><a href="{23}"></a></h5>
                <h5 style="text-align: center;"><a href="{24}"></a></h5>
                <h5 style="text-align: center;"><a href="{25}"></a></h5>
            </td>
        </tr>
    </tbody>
</table>
"""
print(len(data))
if len(data) < 25:
    # Вычисляем, сколько пустых элементов нужно добавить
    empty_elements_to_add = 25 - len(data)

    # Добавляем пустые элементы
    data.extend([""] * empty_elements_to_add)
print(len(data))
print(type(data))
formatted_html = html_code.format(*data)

print(formatted_html)
