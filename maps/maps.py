from typing import Union

class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.
        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """
        def get_list_rating(list_of_movies):
            list_reit = []
            if (list_of_movies.get('country').find(',') != -1
                and list_of_movies.get('rating_kinopoisk') != ''
                and float(list_of_movies.get('rating_kinopoisk')) != 0):
                list_reit = float(list_of_movies.get('rating_kinopoisk'))

            return list_reit

        list_reit = list(filter(None, map(get_list_rating, list_of_movies)))
        average_rating = sum(list_reit)/len(list_reit)

        return average_rating

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению
        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        def amount_letter(list_of_movies):
            list_of_movies = list_of_movies
            if list_of_movies.get('rating_kinopoisk') and float(list_of_movies.get('rating_kinopoisk')) >= rating:
                return list_of_movies.get('name').count('и')

        amount_letter = sum(list(filter(lambda y: y !=None, map(amount_letter, list_of_movies))))

        return amount_letter


