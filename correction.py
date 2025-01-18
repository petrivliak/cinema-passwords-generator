import pandas as pd # импортируем библиотеку

def delete_columns_from_csv(original_file, corrected_file, columns_to_delete): # задаем функцию, которая удалит лишние столбцы. в скобках переменные, необходимые для работы функции. original_file - исходная база данных, corrected_file - исправленный файл, columns_to_delete - наименования столбцов, которые нужно удалить
    df = pd.read_csv('HollywoodMovies.csv')   # сначала читаем csv файл

    df.drop(columns=columns_to_delete, inplace=True)  # команда drop(), присущая библиотеке pandas, которая удаляет указанные столбцы
    df.to_csv('HollywoodMovies2.csv', index=False)     # сохранение измененных данных в новый csv файл

if __name__ == "__main__": # основная программа
    original_file = '.../ТКД/Tasks3/HollywoodMovies.csv' # путь к исходному файлу
    corrected_file = '.../ТКД/Tasks3/HollywoodMovies2.csv'  # путь к новому файлу
    columns_to_delete = ['RottenTomatoes', 'AudienceScore', 'TheatersOpenWeek', 'OpeningWeekend', 'BOAvgOpenWeekend', 'DomesticGross', 'WorldGross', 'ForeignGross', 'Budget', 'Profitability', 'OpenProfit', 'Year']  # список наименований столбцов, которые нужно удалить

    delete_columns_from_csv('HollywoodMovies.csv', 'HollywoodMovies2.csv', columns_to_delete) # работа функции и необходимые для этого данные
    print("Столбцы удалены и данные сохранены в", corrected_file)