def avg(marks):
    assert len(marks) != 0,"The List is empty."
    return sum(marks)/len(marks)
marks1=[20,46,78,90,34]
print("The average of marks1:",avg(marks1))
marks2=[10,30,38,67,89]
print("The Average of marks2:",avg(marks2))