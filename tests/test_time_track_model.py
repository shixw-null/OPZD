import sys
sys.path.append("D:/Документы/Учеба/Учеба_5к1с/ОПЗБД/SQLAlchemy")

import unittest
from models.time_track import TimeTrack
from models.employee import Employee
from methods import BaseMethod
from database import SessionLocal, init_db

class TestTimeTrackModel(unittest.TestCase):

    def setUp(self):
        init_db()
        self.session = SessionLocal()
        self.timetrack_method = BaseMethod(self.session, TimeTrack)

    def create_employee(self):
        employee = Employee(first_name="Иван", last_name="Иванов", phone="+79123456789")
        self.session.add(employee)
        self.session.commit()
        return employee

    def test_get_timetrack(self):
        employee = self.create_employee()
        timetrack = TimeTrack(employee_id=employee.id, worked_hours=8)
        self.timetrack_method.save(timetrack)
        retrieved_timetrack = self.timetrack_method.get(timetrack.id)
        self.assertEqual(retrieved_timetrack.worked_hours, 8)

    def test_find_timetrack_by_hours(self):
        employee = self.create_employee()
        timetrack = TimeTrack(employee_id=employee.id, worked_hours=5)
        self.timetrack_method.save(timetrack)
        found_timetracks = self.timetrack_method.find(worked_hours=5)
        self.assertEqual(len(found_timetracks), 1)
        self.assertEqual(found_timetracks[0].worked_hours, 5)

    def test_get_all_timetracks(self):
        employee = self.create_employee()
        timetracks = [TimeTrack(employee_id=employee.id, worked_hours=i) for i in range(3)]
        for timetrack in timetracks:
            self.timetrack_method.save(timetrack)
        all_timetracks = self.timetrack_method.get_all()
        self.assertEqual(len(all_timetracks), len(timetracks))

    def test_update_timetrack(self):
        employee = self.create_employee()
        timetrack = TimeTrack(employee_id=employee.id, worked_hours=4)
        self.timetrack_method.save(timetrack)
        timetrack.worked_hours = 7
        self.timetrack_method.save(timetrack)
        updated_timetrack = self.timetrack_method.get(timetrack.id)
        self.assertEqual(updated_timetrack.worked_hours, 7)

    def test_delete_timetrack(self):
        employee = self.create_employee()
        timetrack = TimeTrack(employee_id=employee.id, worked_hours=6)
        self.timetrack_method.save(timetrack)
        self.timetrack_method.delete(timetrack)
        deleted_timetrack = self.timetrack_method.get(timetrack.id)
        self.assertIsNone(deleted_timetrack)

    def tearDown(self):
        self.session.query(TimeTrack).delete()
        self.session.query(Employee).delete()
        self.session.commit()
        self.session.close()

if __name__ == '__main__':
    unittest.main()
