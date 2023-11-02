
import math

MIN_CLASSES = 2
MAX_STUDENTS_PER_CLASS = 30


def class_allocation(num_students):

    # number of classes is num_students/30 or at least 2
    num_classes = max(MIN_CLASSES, math.ceil(num_students / MAX_STUDENTS_PER_CLASS))

    result = {}

    students_per_class = num_students // num_classes
    remainder_students = num_students % num_classes

    print(f"Proposed Allocation: {num_classes} classes")

    for _class in range(1, num_classes + 1):
        students_this_class = students_per_class
        if remainder_students > 0:
            students_this_class += 1
            remainder_students -= 1
        result[f"Class {_class}"] = students_this_class

    print(result)


class_allocation(31)
class_allocation(59)
class_allocation(87)

# more tests
class_allocation(123)
class_allocation(124)
class_allocation(125)
class_allocation(126)
class_allocation(2)
