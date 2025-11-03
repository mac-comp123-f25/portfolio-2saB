"""
Contains a simulation of the Petrie Multiplier that is based on classes.
"""

import random
import math


class Employee:
    """
    For this simulation, we only focus on the gender of an employee, and on
    whether this employee is likely to make negative statements
    towards the other gender.
    """

    def __init__(self, gender: str, will_comment):
        """
        Takes in the employee's gender and whether they comment, and it
        saves those values to instance variables. It also initializes the
        variable that holds the comments received by this employee to zero.
        """

        self.gender = gender
        self.will_comment = will_comment
        self.comments_received = 0


    def __str__(self):
        """
        Produces a printable string format for this employee.
        """
        return (self.gender.rjust(5)
                + ": "
                + str(self.comments_received)
                + " sexist comments received")

    def set_commenter_status(self, will_comment):
        self.will_comment = will_comment

    def receive_sexist_comment(self):
        self.comments_received += 1

    def get_gender(self):
        return self.gender

    def get_commenter_status(self):
        return self.will_comment

    def get_comments_received(self):
        return self.comments_received


def print_employee_list(lst):
    """
    Given a list of employees, this method will print the details of each employee
    by using the print() method
    """
    for employee in lst:
        print(employee)


def create_employees(total_num):
    """
    Takes in the number of employees to make, builds and returns a list that contains
    that many employees. It ensures that ~80% are men and the rest women.
    """

    employees = []

    # Calculate number of men (80%) and women (remaining)
    num_men = math.floor(total_num * 0.8)
    num_women = total_num - num_men

    # male employees
    for employee in range(num_men):
        employees.append(Employee("Man", False))

    # female employees
    for employee in range(num_women):
        employees.append(Employee("Woman", False))

    return employees



def create_commenters(lst):
    """
    Given a list of employees, make 20% of each gender be sexist employees. This
    method should not return anything.
    """

    for employee in lst:

        if random.random() < 0.2:            # generates a random value between 0 and 1
            employee.set_commenter_status(True)                        # 20% chance the employee becomes a commenter


def generate_comments(lst):
    """
    Given a list of employees, have each sexist employee give one sexist comment to
    another employee of the opposite gender, chosen randomly. This method should
    not return anything
    """

    # Split employees by gender
    men = [emp for emp in lst if emp.get_gender() == "Man"]
    women = [emp for emp in lst if emp.get_gender() == "Woman"]

    for man in men:
        if man.get_commenter_status():
            recipient = random.choice(women)           #chooses a random woman
            recipient.receive_sexist_comment()

    for woman in women:
        if woman.get_commenter_status():                     #chooses a random man
            recipient = random.choice(men)
            recipient.receive_sexist_comment()


def average_comments(lst):
    """
    Returns a tuple that represents the average amount of comments received for men and women
    respectively. Return statement will be in the form (<avg_for_men>, <avg_for_women>)
    """

    men_comments = []
    women_comments = []

    for employee in lst:
        if employee.get_gender() == "Man":
            men_comments.append(employee.get_comments_received())
        else:
            women_comments.append(employee.get_comments_received())

    men_avg = sum(men_comments) / len(men_comments) if men_comments else 0           #avoiding dividing by 0 just in case to avoid errors
    women_avg = sum(women_comments) / len(women_comments) if women_comments else 0

    return (men_avg, women_avg)



def main():
    """
    Print out information about the average comments
    received by men and women after a simulation has been run
    """
    num_employees_to_generate = 100
    num_comment_rounds = 50

    employee_list = create_employees(num_employees_to_generate)
    create_commenters(employee_list)
    for rounds in range(num_comment_rounds):
        generate_comments(employee_list)

    (men_avg, women_avg) = average_comments(employee_list)
    print("  Men received on average ",   men_avg, "sexist comments")
    print("Women received on average ", women_avg, "sexist comments")


if __name__ == "__main__":
    "<----- Test code for print_employee_list ----->"
    lst = [Employee('Man', True),
           Employee('Man', False),
           Employee('Woman', True),
           Employee('Woman', False)]
    print_employee_list(lst)

    "<----- Test code for create_employees ----->"
    employees = create_employees(10)
    print_employee_list(employees)

    "<----- Test code for create_commenters ----->"
    create_commenters(employees)
    print_employee_list(employees)

    "<----- Test code for generate_comments ----->"
    generate_comments(employees)
    print_employee_list(employees)

    "<----- Test code for average_comments ----->"
    print(average_comments(employees))

    "<----- Run the simulation ----->"
    main()  # <-- KEEP THIS, Uncomment it after implementing all the functions
