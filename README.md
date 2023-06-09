# Урок 10. Домашнее задание <br>

---

> **main.py** - файл запуска программы <br>

Сохраните данные ниже в JSON файл candidates.json.

- Содержание файла (раскрой меня!)
    
    ```python
    # candidates.json
    
    [
      {
        "pk": 1,
        "name": "Adela Hendricks",
        "picture": "https://picsum.photos/200",
        "position": "Go разработчик",
        "gender": "female",
        "age": 40,
        "skills": "go, python"
      },
      {
        "pk": 2,
        "name": "Sheri Torres",
        "picture": "https://picsum.photos/200",
        "position": "Delphi developer",
        "gender": "female",
        "age": 26,
        "skills": "Delphi, pascal, fortran, basic"
      },
      {
        "pk": 3,
        "name": "Burt Stein",
        "picture": "https://picsum.photos/200",
        "position": "Team lead",
        "gender": "male",
        "age": 33,
        "skills": "делегирование, пользоваться календарем, обсуждать важные вопросы"
      },
      {
        "pk": 4,
        "name": "Bauer Adkins",
        "picture": "https://picsum.photos/200",
        "position": "CTO",
        "gender": "male",
        "age": 37,
        "skills": "very important face"
      },
      {
        "pk": 5,
        "name": "Day Holloway",
        "picture": "https://picsum.photos/200",
        "position": "HR manager",
        "gender": "male",
        "age": 35,
        "skills": "LinkedIn, telegram, spam, spam, spam"
      },
      {
        "pk": 6,
        "name": "Austin Cochran",
        "picture": "https://picsum.photos/200",
        "position": "python-develop",
        "gender": "male",
        "age": 26,
        "skills": "python, html"
      },
      {
        "pk": 7,
        "name": "Sheree Love",
        "picture": "https://picsum.photos/200",
        "position": "Django developer",
        "gender": "female",
        "age": 33,
        "skills": "Python, Django, flask"
      }
    ]
    ```
    

Импортируйте данные в ваше приложение.

**Шаг 0**

Напишите функции, которые получали бы данные:

`load_candidates()`, которая загрузит данные из файла

`get_all()`, которая покажет всех кандидатов

`get_by_pk(pk)`, которая вернет кандидата по pk

`get_by_skill(skill_name)`, которая вернет кандидатов по навыку

**Шаг 1**

Создайте представление для роута `/` (главная страница).

Выведите список в таком формате (тег <pre> - преформатирование)

```bash
<pre>
  Имя кандидата - 
  Позиция кандидата
  Навыки через запятую

  Имя кандидата - 
  Позиция кандидата
  Навыки через запятую

  Имя кандидата - 
  Позиция кандидата
  Навыки через запятую
</pre>
```

**Шаг 2**

Создайте представление для роута `candidates/<x>`, 

Который бы выводил данные про кандидата так: 

```python
<img src="(ссылка на картинку)">

<pre>
  Имя кандидата - 
  Позиция кандидата
  Навыки через запятую
</pre>

```

Ссылку на картинку можно разместить в html-коде так же, как и любую другую переменную в тексте, с помощью f-строки, вот так:

```python
url = "http://mypictures.me/123"

f"<img src='({url})'>"
```

**Шаг 3**

Создайте представление `/skills/<x>` для поиска по навыкам.

Выведите тех кандидатов, в списке навыков у которых содержится `skill`.

Поиск по навыку не должен зависеть от регистра.

```python
<pre>
  Имя кандидата - 
  Позиция кандидата
  Навыки через запятую

  Имя кандидата - 
  Позиция кандидата
  Навыки через запятую

  Имя кандидата - 
  Позиция кандидата
  Навыки через запятую
<pre>
```