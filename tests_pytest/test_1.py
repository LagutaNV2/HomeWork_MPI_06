import pytest

from collection import get_durations_dict, get_courses_min, get_courses_max, get_same_name_list


@pytest.mark.parametrize('courses_list, expected',
                         ([
                           [{'title': 'Java-разработчик с нуля', 'mentors': ['Филипп Воронов', 'Анна Юшина', 'Сергей Сердюк', 'Павел Дерендяев'], 'duration': 14},
                            {'title': 'Fullstack-разработчик на Python', 'mentors': ['Евгений Шмаргунов', 'Кирилл Табельский', 'Владимир Чебукин', 'Елена Никитина'], 'duration': 20},
                            {'title': 'Python-разработчик с нуля', 'mentors': ['Евгений Шмаргунов', 'Олег Булыгин', 'Елена Никитина', 'Роман Гордиенко'], 'duration': 12},
                            {'title': 'Frontend-разработчик с нуля', 'mentors': ['Владимир Чебукин', 'Михаил Ларченко'], 'duration': 20},]
                          , {12: [2], 14: [0], 20: [1, 3]}],)
                         )
def test_get_durations_dict(courses_list, expected):
    result = get_durations_dict(courses_list)
    assert expected == result
    
    
@pytest.mark.parametrize('minis, courses_list, expected',
                       ([
                            [2],  [{'title': 'Java-разработчик с нуля', 'mentors': ['Филипп Воронов', 'Анна Юшина', 'Сергей Сердюк', 'Павел Дерендяев'], 'duration': 14},
                            {'title': 'Fullstack-разработчик на Python', 'mentors': ['Евгений Шмаргунов', 'Кирилл Табельский', 'Владимир Чебукин', 'Елена Никитина'], 'duration': 20},
                            {'title': 'Python-разработчик с нуля', 'mentors': ['Евгений Шмаргунов', 'Олег Булыгин', 'Елена Никитина', 'Роман Гордиенко'], 'duration': 12},
                            {'title': 'Frontend-разработчик с нуля', 'mentors': ['Владимир Чебукин', 'Михаил Ларченко'], 'duration': 20},],
                            ['Python-разработчик с нуля']],)
                         )
def test_get_list_min(minis, courses_list, expected):
    result = get_courses_min(minis, courses_list)
    assert expected == result
    
@pytest.mark.parametrize('maxes, courses_list, expected',
                       ([
                            [1, 3],
                            [{'title': 'Java-разработчик с нуля', 'mentors': ['Филипп Воронов', 'Анна Юшина', 'Сергей Сердюк', 'Павел Дерендяев'], 'duration': 14},
                            {'title': 'Fullstack-разработчик на Python', 'mentors': ['Евгений Шмаргунов', 'Кирилл Табельский', 'Владимир Чебукин', 'Елена Никитина'], 'duration': 20},
                            {'title': 'Python-разработчик с нуля', 'mentors': ['Евгений Шмаргунов', 'Олег Булыгин', 'Елена Никитина', 'Роман Гордиенко'], 'duration': 12},
                            {'title': 'Frontend-разработчик с нуля', 'mentors': ['Владимир Чебукин', 'Михаил Ларченко'], 'duration': 20},],
                            ['Fullstack-разработчик на Python', 'Frontend-разработчик с нуля']],)
                         )
def test_get_list_max(maxes, courses_list, expected):
    result = get_courses_max(maxes, courses_list)
    assert expected == result

@pytest.mark.parametrize('course, unique_names, expected',
                       (
                               [
                            {'title': 'Java-разработчик с нуля', 'mentors': ['Филипп Воронов', 'Анна Юшина', 'Сергей Сердюк', 'Павел Дерендяев'], 'duration': 14},
                            ['Анна', 'Павел', 'Сергей', 'Филипп'],
                                []
                               ],
                                [
                            {'title': 'Fullstack-разработчик на Python', 'mentors': ['Евгений Шмаргунов', 'Кирилл Табельский', 'Владимир Чебукин', 'Елена Никитина', 'Евгений Шек'],'duration': 20},
                            ['Владимир', 'Евгений', 'Елена', 'Кирилл'],
                                ['Евгений Шмаргунов', 'Евгений Шек']
                               ],
                                [
                            {'title': 'Python-разработчик с нуля', 'mentors': ['Евгений Шмаргунов', 'Олег Булыгин', 'Елена Никитина', 'Александр Ульянцев', 'Александр Бардин', 'Роман Гордиенко'], 'duration': 12},
                            ['Александр', 'Евгений', 'Елена', 'Олег', 'Роман'],
                                ['Александр Ульянцев', 'Александр Бардин']
                               ],
                               [
                                   {'title': 'Frontend-разработчик с нуля', 'mentors': ['Владимир Чебукин', 'Михаил Ларченко'], 'duration': 20},
                                   ['Владимир', 'Михаил'],
                                   []
                               ],
                         )
                    )
def test_get_same_name_list(course, unique_names, expected):
    result = get_same_name_list(course, unique_names)
    assert expected == result
