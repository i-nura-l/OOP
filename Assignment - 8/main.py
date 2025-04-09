from employee import Employee
from employee_dao import EmployeeDAO

if __name__ == '__main__':
    dao = EmployeeDAO('employee_db.sqlite')

    # Create and insert a new employee
    new_employee = Employee(id=None, name='John Doe', position='Software Engineer', salary=75000.0, hire_date='2023-01-15')
    new_id = dao.insert(new_employee)
    print(f'Inserted Employee ID: {new_id}')

    # Get employee by ID
    employee = dao.get_by_id(new_id)
    print('Retrieved by ID:', employee)

    # Delete employee
    dao.delete(3)
    print(f'Employee with ID {new_id} deleted.')

    # Get all employees
    all_employees = dao.get_all()
    print('All Employees:')
    for emp in all_employees:
        print(emp)

    # Update employee
    if employee:
        employee.name = 'Jane Doe'
        employee.salary = 80000.0
        dao.update(employee)
        print('Updated Employee:', dao.get_by_id(employee.id))
