from database import SessionLocal, init_db
from methods import BaseMethod
from models.position import Position
from models.employee import Employee
from models.time_track import TimeTrack
from models.equipment import Equipment
from models.employee_equipment import EmployeeEquipment

# Инициализация базы данных (создание таблиц)
init_db()

# Создание сессии для работы с базой данных
session = SessionLocal()

# Создание репозиториев для каждой сущности
employee_repository = BaseMethod(session, Employee)
position_repository = BaseMethod(session, Position)
time_track_repository = BaseMethod(session, TimeTrack)
equipment_repository = BaseMethod(session, Equipment)
employee_equipment_repository = BaseMethod(session, EmployeeEquipment)

# Добавление новых должностей
developer_position = Position(position_name="Developer", salary=5000.0)
manager_position = Position(position_name="Manager", salary=5500.0)
position_repository.save(developer_position)
position_repository.save(manager_position)

# Добавление новых сотрудников
john_employee = Employee(first_name="John", last_name="Doe", position_id=1)
jane_employee = Employee(first_name="Jane", last_name="Smith", position_id=1)
bob_employee = Employee(first_name="Bob", last_name="Brown", position_id=2)
employee_repository.save(john_employee)
employee_repository.save(jane_employee)
employee_repository.save(bob_employee)

# Добавление записей о рабочем времени
time_track_repository.save(TimeTrack(employee_id=1, worked_hours=8))
time_track_repository.save(TimeTrack(employee_id=2, worked_hours=7))
time_track_repository.save(TimeTrack(employee_id=3, worked_hours=6))

# Добавление нового оборудования
laptop_equipment = Equipment(equipment_name="Laptop")
phone_equipment = Equipment(equipment_name="Smartphone")
equipment_repository.save(laptop_equipment)
equipment_repository.save(phone_equipment)

# Добавление записей о выдаче оборудования сотрудникам
employee_equipment_repository.save(EmployeeEquipment(employee_id=1, equipment_id=1))
employee_equipment_repository.save(EmployeeEquipment(employee_id=2, equipment_id=2))
employee_equipment_repository.save(EmployeeEquipment(employee_id=3, equipment_id=2))

# Вывод всех сотрудников с дополнительной информацией
all_employees = employee_repository.get_all()
for emp in all_employees:
    print(f"Сотрудник: {emp.first_name} {emp.last_name}")
    print(f"Должность: {emp.position.position_name}, Зарплата: {emp.position.salary}")
    
    # Вывод оборудования, выданного сотруднику
    equipment_assigned = [eq.equipment.equipment_name for eq in emp.equipments]
    if equipment_assigned:
        print(f"Оборудование: {', '.join(equipment_assigned)}")
    else:
        print("Оборудование: не выдано")
    
    # Вывод отработанных часов
    total_hours = sum([tt.worked_hours for tt in emp.time_tracks])
    print(f"Всего отработано часов: {total_hours}")
    
    print("-" * 50)  # Разделитель для удобства чтения вывода


# Закрытие сессии после завершения работы
session.close()
