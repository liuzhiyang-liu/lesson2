# -*- coding: UTF-8 -*-
import random

ques_answer = '1_with_answer.txt'
ques_no_answer = '2_no_answer.txt'

f1 = open(ques_answer,'w')
f2 = open(ques_no_answer,'w')

for row in range(1,21):
    for col in range(1,6):
        a = random.randint(1,99)
        b = random.randint(1,99)
        op = (random.randint(1,10000)) % 4

        if op == 0:
            c=a + b
            op_xxx ='+'
            problem = '%2d %s %2d =\t\t' % (a,op_xxx,b)
            anwser = '%2d %s %2d = %5d\t\t' % (a,op_xxx,b,c)
        elif op==1:
            c=a - b
            op_xxx ='-'
            problem = '%2d %s %2d =\t\t' % (a,op_xxx,b)
            anwser = '%2d %s %2d = %5d\t\t' % (a,op_xxx,b,c)
        elif op==2:
            c=a * b
            op_xxx ='x'
            problem = '%2d %s %2d =\t\t' % (a,op_xxx,b)
            anwser = '%2d %s %2d = %5d\t\t' % (a,op_xxx,b,c)
        elif op==3:
            c=a / b
            op_xxx ='/'
            problem = '%2d %s %2d =\t\t' % (a,op_xxx,b)
            anwser = '%2d %s %2d = %5.2f\t\t' % (a,op_xxx,b,c)


        #data='a+b=c '
        f1.write(anwser)
        f2.write(problem)
    f1.write('\n')
    f2.write('\n')

f1.close()
f2.close()
