import student_class as st
student_id = '892495683'
student_name = 'Ryan Do'
student_classification = 'freshman'
student_dob = '02/13/2000'

student1 = st.Student(student_id, student_name,student_dob, student_classification)

student1.calc_age()

student1.register()

print(student1.return_age())
print(student1.return_registration())
