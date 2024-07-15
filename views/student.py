from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from models.student import Student, db
import random
from datetime import datetime

student = Blueprint('student', __name__)


@student.route('/students', methods=['GET'])
def get_students():
    if request.method == 'GET':
        all_students = Student.query.all()

        students = []
        all_student_set = set(all_students)

        for stud in all_student_set:
            students.append(Student.to_dict(stud))
        # print(students)

        return render_template('students.html', students=students, current_user=current_user)


@student.route('/students/new', methods=['GET', 'POST'])
@login_required
def add_student():
    if request.method == 'GET':
        return render_template('add_student.html', data=request.form, current_user=current_user)
    elif request.method == 'POST':
        stud_id = random.randint(1, 9999999)
        first_name = request.form.get('first_name')
        first_name = first_name.strip()

        last_name = request.form.get('last_name')
        last_name = last_name.strip()

        department = request.form.get('department')
        department = department.strip()

        DOB = request.form.get('DOB')
        DOB = DOB.strip()

        if not first_name or not last_name or not DOB or not department:
            flash('Some fields are missing', 'error')
            return render_template('add_student.html', data=request.form, current_user=current_user)
        else:
            try:
                # print(request.form)
                new_student = Student(first_name=first_name,
                                      last_name=last_name,
                                      student_id=stud_id,
                                      department=department,
                                      DOB=DOB)

                db.session.add(new_student)
                db.session.commit()
                flash('successfully added student', 'success')
                return redirect(url_for('views.student.get_students'))
            except Exception as exc:
                print(exc)
                message = 'could not add student'
                flash(message, 'error')
                return render_template('add_student.html',
                                    data=request.form,
                                    current_user=current_user)



@student.route('/students/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update_student(id):
    try:
        print('stud id: ', id)
        if request.method == 'GET':
            student = Student.query.filter_by(student_id=id).first()
            if not student:
                flash('student could nto be found', 'error')
                return render_template('edit.html', current_user=current_user, student=student)
            else:
                return render_template('edit.html', current_user=current_user, student=student)
        if request.method == 'POST':
            method = request.form.get('_method')
            print('method: ', method)
            if method and method == 'UPDATE':
                first_name = request.form.get('first_name')
                first_name = first_name.strip()

                last_name = request.form.get('last_name')
                last_name = last_name.strip()

                student_id = request.form.get('student_id')
                student_id = student_id.strip()

                department = request.form.get('department')
                department = department.strip()

                DOB = request.form.get('DOB')
                DOB = DOB.strip()

                if not first_name or not last_name or not student_id or not department or not DOB:
                    flash('some fields are empty, could not update student', 'error')
                    return render_template('students.html', current_user=current_user)
                else:
                    updated_student = Student.query.filter_by(student_id=student_id).update(
                        {'first_name': first_name,
                        'last_name': last_name,
                        'student_id': student_id,
                        'department': department,
                        'DOB': DOB,
                        'updated_at': datetime.now()},
                        synchronize_session='fetch'
                    )
                    db.session.commit()
                    if updated_student:
                        flash('student updated successfully', 'success')
                        return redirect(url_for('views.student.get_students'), 302)
            else:
                flash('something went wrong, could not perform operation', 'error')
                return redirect(url_for('views.student.get_students'), 302)
    except Exception as exc:
        print(exc)
        flash('something went wrong, could not perform operation', 'error')
        return redirect(url_for('views.student.get_students'), 302)





@student.route('/students/<int:id>/delete', methods=['POST'])
@login_required
def delete_student(id):
     if request.method == 'POST':
          method = request.form.get('_method')
          if method and method == 'DELETE':
            try:
                stud_to_delete = Student.query.filter_by(student_id=id).first()
                if not stud_to_delete:
                        message = 'could not delete Student, student not found'
                        flash(message, 'error')
                        return render_template('students.html', current_user=current_user)
                else:
                    db.session.delete(stud_to_delete)
                    db.session.commit()
                    flash(f'student with id {id} deleted successfuly', 'success')
                    return redirect(url_for('views.student.get_students'))
            except Exception as exc:
                print(exc)
                message = 'could not delete Student'
                flash(message, 'error')
                return render_template('students.html', current_user=current_user)
