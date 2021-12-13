"""
File `data/students.csv` stores information about students in CSV format.
This file contains the student’s names, age and average mark.

1. Implement a function get_top_performers which receives file path and
returns names of top performer students.
Example:
def get_top_performers(file_path, number_of_top_students=5):
    pass

print(get_top_performers("students.csv"))

Result:
['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia',
'Joseph Head']

2. Implement a function write_students_age_desc which receives the file path
with students info and writes CSV student information to the new file in
descending order of age.
Example:
def write_students_age_desc(file_path, output_file):
    pass

Content of the resulting file:
student name,age,average mark
Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27
"""


from csv import reader, writer


def get_top_performers(file_path, number_of_top_students=5):
    """
    Receives file path and returns names of top performer students.
    :param file_path: system path to the csv file
    :param number_of_top_students: int, default=5
    :return: list of students
    """
    performing = []
    top_students = []

    with open(file_path, 'r') as students:
        csv_reader = reader(students)
        header = next(csv_reader)
        performing = [line for line in csv_reader]
        
    performing_sorted = list(sorted(performing, \
                            key=lambda item: item[2], \
                            reverse=True))
    
    top_students = [student[0] for student in \
                    performing_sorted[:number_of_top_students]]

    return top_students

#print(get_top_performers('students.csv'))


def write_students_age_desc(file_path, output_file):
    """
    Receives the file path with students info and 
    writes CSV student information to the new file in descending order of age.
    :param file_path: system path to the csv file
    :param output_file: system path to the csv file
    :return: None
    """
    students_list = []
    with open(file_path, 'r') as students:
        csv_reader = reader(students)
        header = next(csv_reader)
        students_list = [[s[0],s[1],s[2].strip()] for s in csv_reader]

    students_list = list(sorted(students_list,  key=lambda item: item[1], \
                                        reverse=True))
    
    with open(output_file, 'a', newline='') as students:
        csv_writer = writer(students)
        for info in students_list:
            csv_writer.writerow(info)
