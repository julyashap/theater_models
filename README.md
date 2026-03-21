# theater_models

## Задание
Cпроектировать pydantic-модели для театра: зритель, актер, постановка и представление

## Запуск
```python -m venv venv```

```source venv/bin/activate```

```pip install requirements.txt```

```python main.py```

## Созданные модели

### Модель зрителя [Viewer](models/viewer.py)

#### Обязательные поля
* id - уникальный идентификатор
* name - имя зрителя
* surname - фамилия зрителя
* email_address - email-адрес
* ticket_number - номер билета

#### Необязательные поля (дефолт)
* phone_number - номер телефона (None)

#### Конфигурация
```str_strip_whitespace=True```

### Модель актера [Actor](models/actor.py)

#### Обязательные поля
* id - уникальный идентификатор
* name - имя актера
* surname - фамилия актера
* passport_number - номер паспорта (исключается из сериализации)
* skills - навыки и их уровни

#### Конфигурация
```str_strip_whitespace=True```

### Модель постановки [Production](models/production.py)

#### Обязательные поля
* id - уникальный идентификатор
* name - название постановки
* genre - театральный жанр

#### Связь с другими моделями
* actors - список актеров (объектов Actor)

#### Необязательные поля (дефолт)
* description - описание постановки (None)
* age_rating - возрастное ограничение (0)
* duration - продолжительность (1 час)
* has_intermission - есть ли антракт (да)

#### Конфигурация
```str_strip_whitespace=True```

### Модель представление [Performance](models/performance.py)

#### Обязательные поля
* id - уникальный идентификатор
* start_datetime - дата и время начала представления
* theater_name - название театра, в котором будет проводиться представление
* count_tickets - количество билетов всего

#### Связь с другими моделями
* viewers - список зрителей (объектов Viewer)
* production - постановка (объект Production)

#### Необязательные поля (дефолт)
* is_premiere - является ли премьерой (нет)

#### Вычисляемые поля
* avaliable_tickets - количество оставшихся билетов

#### Конфигурация
```str_strip_whitespace=True```