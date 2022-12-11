import json

#def load_candidates() - загружает данные из файла candidates.json
def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)

#проверяем работу функции def load_candidates()
#print(load_candidates())
#вернет список ключей файла json


#def get_all() - покажет всех кандидатов
def get_all():
    return load_candidates()


#def get_candidate_by_pk - вернет кандидата по pk
def get_candidate_by_pk(pk):
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate
    return


#def get_candidate_by_skill - вернет кандидата по навыку (перебираем список навыков)
#split(', ') - делаем список из строки skills и делим, чтобы искать именно в списке
# и по запросу не получать лишних результатов
# lower() - т.к. в skills есть разный регистр
def get_candidate_by_skill(skill):
    candidates = []
    for candidate in load_candidates():
        if skill.lower() in candidate['skills'].lower().split(', '):
            candidates.append(candidate)
    return candidates
