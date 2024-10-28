student_scores={
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62
}

student_garde={
}

for value in student_scores:
    student_garde.update({value:"Outstanding" if (student_scores[value]>=91) else "Exeeds Expectaton" if (student_scores[value]>=81)else "Acceptable" 
    if (student_scores[value]>=71) else "Fail"} )

print(student_garde)
