# baekjoon 25206
grade_dict = {"A+":	4.5,
"A0":	4.0,
"B+":	3.5,
"B0":	3.0,
"C+":	2.5,
"C0":	2.0,
"D+":	1.5,
"D0":	1.0,
"F":	0.0}

transcript = [input().split() for _ in range(20)]

point_sum = 0
sum = 0
for i in transcript:
  subject = i[0] 
  point = float(i[1])
  grade = i[2]
  if grade != "P":
    grade = float(grade_dict[i[2]] )
    point_sum += point
    sum  += grade * point
    final_grade = sum/point_sum

print(final_grade)
