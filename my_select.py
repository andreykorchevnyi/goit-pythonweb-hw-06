from sqlalchemy import func, desc, select
from connect import session
from models import Student, Teacher, Group, Subject, Grade


def select_1():
    """
    Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    """
    result = session.query(
        Student.id,
        Student.first_name,
        Student.last_name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    
    return result


def select_2(subject_id):
    """
    Знайти студента із найвищим середнім балом з певного предмета.
    """
    result = session.query(
        Student.id,
        Student.first_name,
        Student.last_name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade).filter(Grade.subject_id == subject_id).group_by(Student.id).order_by(desc('avg_grade')).first()
    
    return result


def select_3(subject_id):
    """
    Знайти середній бал у групах з певного предмета.
    """
    result = session.query(
        Group.id,
        Group.name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).select_from(Group).join(Student).join(Grade).filter(Grade.subject_id == subject_id).group_by(Group.id).all()
    
    return result


def select_4():
    """
    Знайти середній бал на потоці (по всій таблиці оцінок).
    """
    result = session.query(
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).scalar()
    
    return result


def select_5(teacher_id):
    """
    Знайти які курси читає певний викладач.
    """
    result = session.query(
        Subject.id,
        Subject.name
    ).filter(Subject.teacher_id == teacher_id).all()
    
    return result


def select_6(group_id):
    """
    Знайти список студентів у певній групі.
    """
    result = session.query(
        Student.id,
        Student.first_name,
        Student.last_name
    ).filter(Student.group_id == group_id).all()
    
    return result


def select_7(group_id, subject_id):
    """
    Знайти оцінки студентів у окремій групі з певного предмета.
    """
    result = session.query(
        Student.id,
        Student.first_name,
        Student.last_name,
        Grade.grade,
        Grade.date_received
    ).join(Grade).filter(
        Student.group_id == group_id,
        Grade.subject_id == subject_id
    ).order_by(Student.last_name, Student.first_name).all()
    
    return result


def select_8(teacher_id):
    """
    Знайти середній бал, який ставить певний викладач зі своїх предметів.
    """
    result = session.query(
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Subject).filter(Subject.teacher_id == teacher_id).scalar()
    
    return result


def select_9(student_id):
    """
    Знайти список курсів, які відвідує певний студент.
    """
    result = session.query(
        Subject.id,
        Subject.name
    ).join(Grade).filter(Grade.student_id == student_id).group_by(Subject.id).all()
    
    return result


def select_10(student_id, teacher_id):
    """
    Список курсів, які певному студенту читає певний викладач.
     """
    result = session.query(
        Subject.id,
        Subject.name
    ).join(Grade).filter(
        Grade.student_id == student_id,
        Subject.teacher_id == teacher_id
    ).group_by(Subject.id).all()
    
    return result


if __name__ == "__main__":
    print("\n1. Студенти з найбільшим середнім балом:")
    for student in select_1():
        print(f"{student.first_name} {student.last_name}: {student.avg_grade}")
    
    subject = session.query(Subject).first()
    print(f"\n2. Студент з найвищим середнім балом з предмету '{subject.name}':")
    best_student = select_2(subject.id)
    if best_student:
        print(f"{best_student.first_name} {best_student.last_name}: {best_student.avg_grade}")
    
    print(f"\n3. Середній бал у групах з предмету '{subject.name}':")
    for group in select_3(subject.id):
        print(f"{group.name}: {group.avg_grade}")
    
    print("\n4. Середній бал на потоці:", select_4())
    
    teacher = session.query(Teacher).first()
    print(f"\n5. Курси, які читає викладач {teacher.first_name} {teacher.last_name}:")
    for course in select_5(teacher.id):
        print(f"- {course.name}")
    
    group = session.query(Group).first()
    print(f"\n6. Список студентів у групі {group.name}:")
    for student in select_6(group.id):
        print(f"- {student.first_name} {student.last_name}")
    
    print(f"\n7. Оцінки студентів у групі {group.name} з предмету '{subject.name}':")
    for record in select_7(group.id, subject.id):
        print(f"{record.first_name} {record.last_name}: {record.grade} ({record.date_received.strftime('%d.%m.%Y')})")
    
    print(f"\n8. Середній бал, який ставить викладач {teacher.first_name} {teacher.last_name}:", select_8(teacher.id))
    
    student = session.query(Student).first()
    print(f"\n9. Список курсів, які відвідує студент {student.first_name} {student.last_name}:")
    for course in select_9(student.id):
        print(f"- {course.name}")
    
    print(f"\n10. Список курсів, які студенту {student.first_name} {student.last_name} читає викладач {teacher.first_name} {teacher.last_name}:")
    for course in select_10(student.id, teacher.id):
        print(f"- {course.name}")
    
    session.close() 