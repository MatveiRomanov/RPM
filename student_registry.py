class StudentRegistry:
    students = []

    @staticmethod
    def add_student(name):
        StudentRegistry.students.append(name)

    @staticmethod
    def get_student_count():
        return len(StudentRegistry.students)

    @staticmethod
    def get_all_students():
        return StudentRegistry.students.copy()

    @classmethod
    def clear_registry(cls):
        cls.students.clear()