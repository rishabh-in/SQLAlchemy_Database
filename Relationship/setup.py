from basic import db,Student,Subject,Class_room


## ------- Creating objects--------------##

## creating students objects ---------##

db.create_all()

stud1=Student("Rishabh")
stud2=Student("Rishav")

db.session.add_all([stud1,stud2])
db.session.commit()

print(Student.query.all())

rishabh=Student.query.filter_by(name="Rishabh").first()
print(rishabh)          ## Here I have not decided which class to choose

## creating class rooms ##

class1=Class_room("Science",stud1.id)

## Subjects for stud1 ##

subject1=Subject("Maths",stud1.id)
subject2=Subject("Language1",stud1.id)


## add to database

db.session.add_all([class1,subject1,subject2])
db.session.commit()

rishabh=Student.query.filter_by(name="Rishabh").first()
print(rishabh)