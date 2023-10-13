from sqlalchemy.orm import Session


class BaseMethod:
    """
    Базовый класс для работы с методами доступа к данным.
    
    Предоставляет базовые методы для работы с данными в базе данных
    через SQLAlchemy.

    Атрибуты:
    - session (Session): сессия для работы с базой данных.
    - model: класс модели SQLAlchemy для работы с определенной таблицей.
    """

    def __init__(self, session: Session, model):
        """
        Инициализирует объект BaseMethod.

        Параметры:
        - session (Session): сессия для работы с базой данных.
        - model: класс модели SQLAlchemy для работы с определенной таблицей.
        """
        self.session = session
        self.model = model

    def get(self, id: int):
        """
        Получает объект по его ID.

        Параметры:
        - id (int): ID объекта.

        Возвращает:
        - Объект модели или None, если объект не найден.
        """
        return self.session.query(self.model).filter(self.model.id == id).first()

    def find(self, **kwargs):
        """
        Ищет объекты, соответствующие переданным параметрам.

        Параметры:
        - **kwargs: параметры для фильтрации.

        Возвращает:
        - Список объектов, соответствующих критериям.
        """
        return self.session.query(self.model).filter_by(**kwargs).all()

    def get_all(self):
        """
        Получает все объекты данной модели.

        Возвращает:
        - Список всех объектов модели.
        """
        return self.session.query(self.model).all()

    def save(self, entity):
        """
        Сохраняет или обновляет объект в базе данных.

        Параметры:
        - entity: объект модели для сохранения или обновления.
        """
        self.session.add(entity)
        self.session.commit()

    def delete(self, entity):
        """
        Удаляет объект из базы данных.

        Параметры:
        - entity: объект модели для удаления.
        """
        self.session.delete(entity)
        self.session.commit()
