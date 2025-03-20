import random
from datetime import datetime, timedelta

from connect import session
from models import Group, Teacher, Student, Subject, Grade

# Function to generate a random date within the last year
def random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + timedelta(days=random_number_of_days)

if __name__ == "__main__":
    # Create 3 groups
    group1 = Group(name="ІТ-11")
    group2 = Group(name="ІТ-12")
    group3 = Group(name="ІТ-13")
    
    session.add_all([group1, group2, group3])
    session.commit()
    
    # Create 5 teachers
    teacher1 = Teacher(first_name="Олександр", last_name="Шевченко", email="shevchenko@example.com")
    teacher2 = Teacher(first_name="Оксана", last_name="Ковальчук", email="kovalchuk@example.com")
    teacher3 = Teacher(first_name="Андрій", last_name="Бондаренко", email="bondarenko@example.com")
    teacher4 = Teacher(first_name="Наталія", last_name="Мельник", email="melnyk@example.com")
    teacher5 = Teacher(first_name="Тарас", last_name="Кравченко", email="kravchenko@example.com")
    
    session.add_all([teacher1, teacher2, teacher3, teacher4, teacher5])
    session.commit()
    
    # Create 8 subjects
    subject1 = Subject(name="Математика", teacher=teacher1)
    subject2 = Subject(name="Фізика", teacher=teacher2)
    subject3 = Subject(name="Інформатика", teacher=teacher3)
    subject4 = Subject(name="Історія України", teacher=teacher4)
    subject5 = Subject(name="Хімія", teacher=teacher5)
    subject6 = Subject(name="Біологія", teacher=teacher1)
    subject7 = Subject(name="Англійська мова", teacher=teacher2)
    subject8 = Subject(name="Програмування", teacher=teacher3)
    
    session.add_all([subject1, subject2, subject3, subject4, subject5, subject6, subject7, subject8])
    session.commit()
    
    # Create 40 students
    students = []
    first_names = ["Олександр", "Дмитро", "Максим", "Богдан", "Андрій", "Олексій", "Артем", "Ілля", 
                  "Кирило", "Михайло", "Назар", "Матвій", "Роман", "Єгор", "Арсен", "Іван", "Денис", 
                  "Євген", "Данило", "Тимофій", "Владислав", "Ігор", "Володимир", "Павло", "Руслан", 
                  "Марко", "Костянтин", "Тимур", "Олег", "Ярослав", "Антон", "Микола", "Гліб", "Віктор", 
                  "Тарас", "Вадим", "Степан", "Юрій", "Василь", "Віталій"]
    
    last_names = ["Шевченко", "Бондаренко", "Ковальчук", "Коваленко", "Бойко", "Ткаченко", "Кравченко", 
                  "Олійник", "Шевчук", "Поліщук", "Бондар", "Ткачук", "Мельник", "Кравчук", "Савченко", 
                  "Руденко", "Марченко", "Лисенко", "Мороз", "Данилюк", "Левченко", "Мазур", "Карпенко", 
                  "Коломієць", "Савчук", "Литвиненко", "Пономаренко", "Василенко", "Павленко", "Семенюк", 
                  "Дмитренко", "Гаврилюк", "Захарчук", "Романюк", "Гончаренко", "Кузьменко", "Панасюк", 
                  "Кулик", "Пилипенко", "Іваненко"]
    
    groups = [group1, group2, group3]
    
    for i in range(40):  # Create 40 students
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        email = f"{first_name.lower()}.{last_name.lower()}{i}@example.com"
        group = random.choice(groups)
        
        student = Student(first_name=first_name, last_name=last_name, email=email, group=group)
        students.append(student)
    
    session.add_all(students)
    session.commit()
    
    # Create grades for students
    subjects = [subject1, subject2, subject3, subject4, subject5, subject6, subject7, subject8]
    start_date = datetime.now() - timedelta(days=365)  # 1 year ago
    end_date = datetime.now()
    
    grades = []
    for student in students:
        # Each student receives between 12 and 20 grades
        num_grades = random.randint(12, 20)
        for _ in range(num_grades):
            subject = random.choice(subjects)
            grade_value = random.uniform(60.0, 100.0)  # Grades from 60 to 100
            grade_value = round(grade_value, 1)  # Round to 1 decimal place
            date_received = random_date(start_date, end_date)
            
            grade = Grade(student=student, subject=subject, grade=grade_value, date_received=date_received)
            grades.append(grade)
    
    session.add_all(grades)
    session.commit()
    
    print("База даних успішно заповнена!")
    print(f"Додано {len(groups)} груп")
    print(f"Додано {len([teacher1, teacher2, teacher3, teacher4, teacher5])} викладачів")
    print(f"Додано {len(subjects)} предметів")
    print(f"Додано {len(students)} студентів")
    print(f"Додано {len(grades)} оцінок")
    
    session.close() 