def visit_country(test_list):
    i = 0
    while i < len(test_list):
        for value in test_list[i].values():
            if value[1] != 'Россия':
                test_list.pop(i)
                i -= 1
        i += 1
    return test_list


def geo_id(id_dict):
    a = set()
    values = id_dict.values()
    for value in values:
        for i in value:
            a.add(i)
    return a


def search_terms_generator(queries):
    helper = {}
    for query in queries:
        word = query.split()
        if len(word) in helper.keys():
            helper[len(word)] += 1
        else:
            helper.update({len(word): 1})

    for key, value in helper.items():
        per = round((value / len(queries)) * 100, 2)
        yield f'Количество поисковых запросов из {str(key)} слов: {str(per)}%, кол-во {str(value)}'


def check_generator(query):
    check_list = []
    for item in search_terms_generator(query):
        check_list.append(item)
    return check_list