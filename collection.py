def get_durations_dict(courses_list):
    '''Наводим порядок: упорядочиваем курсы по продолжительности'''
    durations_dict = {}
    for id, course in enumerate(courses_list):
        key = course["duration"]  # Получите значение из ключа duration
        if key not in durations_dict.keys():
            durations_dict[key] = [id]
        else:
            x = durations_dict[key]
            x.append(id)
            durations_dict[key] = x
    durations_dict = dict(sorted(durations_dict.items()))
    return durations_dict


def get_courses_min(minis, courses_list):
    'Самый короткий курс(ы)'
    courses_min = []
    for id_ in minis:
        courses_min.append(courses_list[id_][
                               "title"])
    return courses_min

def get_courses_max(maxes, courses_list):
    'Самый длинный курс(ы)'
    courses_max = []
    for id_ in maxes:
        courses_max.append(
            courses_list[id_]["title"])
    return courses_max


def get_same_name_list(course, unique_names):
    'Подсчитываем тёзок на каждом курсе'
    # global mentor
    same_name_list = []
    for unique_name in unique_names:
        if (','.join(course["mentors"])).count(unique_name) > 1:
            print('>1')
            for mentor in course["mentors"]:
                if unique_name in mentor:
                    same_name_list.append(mentor)
            
    return same_name_list


if __name__ == "__main__":
    courses = ["Java-разработчик с нуля",
               "Fullstack-разработчик на Python",
               "Python-разработчик с нуля",
               "Frontend-разработчик с нуля"
               ]
    mentors = [
        ["Филипп Воронов", "Анна Юшина", "Сергей Сердюк", "Павел Дерендяев",],
        ["Евгений Шмаргунов", "Кирилл Табельский", "Владимир Чебукин", "Елена Никитина", "Евгений Шек",],
        ["Евгений Шмаргунов", "Олег Булыгин", "Елена Никитина", "Александр Ульянцев", "Александр Бардин", "Роман Гордиенко",],
        ["Владимир Чебукин", "Михаил Ларченко",]
    ]
    durations = [14, 20, 12, 20]
    
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title":course, "mentors":mentor, "duration":duration}
        courses_list.append(course_dict)
    
    durations_dict = get_durations_dict(courses_list)
    
    # 1 Наводим порядок: упорядочиваем курсы по продолжительности
    print('-----------')
    for key_dur, id_cours in durations_dict.items():
        
        for id in id_cours:
            course = courses_list[id]
            name_cours = course["title"]
            print(f'{name_cours} - {key_dur} месяцев') # Получите значение из ключа duration
            
            
    # 2 Найдите cамый длинный и короткий курс(ы)
    print('-----------')
    
    min = min(durations)
    max = max(durations)
    
    maxes = []
    minis = []
    for id_dur, duration in enumerate(durations):
        if duration == max:
            maxes.append(id_dur)
        elif duration == min:
            minis.append(id_dur)
    
    courses_min = get_courses_min(minis, courses_list)
    courses_max = get_courses_max(maxes, courses_list)
    
    print(f'Самый короткий курс(ы): {", ".join(courses_min)} - {min} месяца(ев)')
    print(f'Самый длинный курс(ы): {", ".join(courses_max)} - {max} месяца(ев)')
    
    
    # 3 Подсчитываем тёзок на каждом курсе
    print('-----------')
    
    for course in courses_list:
        all_names_list = []
        for mentor in course["mentors"]:
            name = mentor.split()[0]
            all_names_list.append(name)
        
        unique_names = sorted(list(set(all_names_list)))
        
        # Организуйте цикл по всем именам на курсе из множества:
        print(f'{unique_names=}')
        print(f'{course=}')
        same_name_list = get_same_name_list(course, unique_names)
        print(f'{same_name_list}')
        
        if len(same_name_list):
            same_name_list.sort()
            print(f'На курсе {course["title"]} есть тёзки: {", ".join(same_name_list)}')
        