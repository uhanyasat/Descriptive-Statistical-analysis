# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 07:51:41 2021

@author: Sathish
"""
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        ele=" "+ele
        str1 += ele  
    
    # return string  
    return str1 
def Curved_grade(lines,Grade,Grade_A,Grade_B,Grade_C,Grade_D):
    for i in lines:
        if Grade_A <= lines[i]:
            Grade.append('A')
        elif lines[i]<Grade_A and lines[i]>=Grade_B :
            Grade.append('B')
        elif lines[i]<Grade_B and lines[i]>=Grade_C :
            Grade.append('C')
        elif lines[i]<Grade_C and lines[i]>=Grade_D :
            Grade.append('D')
        elif lines[i]<Grade_D:
            print(Grade_D,lines[i])
            Grade.append('F')
    return Grade

def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele== x):
            count = count + 1
            print
    return count

def main():
   bc = ["\n"]
   with open("scores.txt") as file_in:
    lines = []
    for line in file_in:
        for i in bc :
            line = line.replace(i, '')
            line=int(line)
        lines.append(line)
   # print(lines)
    #print(type(lines[1]))
    No_of_scores=len(lines)
    
    Min=min(lines)
    
    Max=max(lines)
    
    mean = sum(lines) / len(lines)
    
    variance = sum([((x - mean) ** 2) for x in lines]) / len(lines)
    std = variance ** 0.5
    print('**************************************')
    print('Count:',No_of_scores)
    print('Average:',mean)
    print('Standard Deviation:',std)
    print('Maximum',Max)
    print('Minimum:',Min)
    print('**************************************')
    print("Curve Grade - Cut off Points(to 1 decimal place)")
    Grade_A=mean+1.5*std
    print('A:',round(Grade_A,1))
    Grade_B=mean+0.5*std
    print('B:',round(Grade_B,1))
    Grade_C=mean-0.5*std
    print('C:',round(Grade_C,1))
    Grade_D=mean-1.5*std
    print('D:',round(Grade_D,1))
    print('**************************************')
    Grade=[]
    for i in range(len(lines)):
        if (Grade_A <= lines[i]):
            Grade.append('A')
        elif lines[i] < Grade_A and lines[i] >= Grade_B :
            Grade.append('B')
        elif lines[i] < Grade_B and lines[i] >= Grade_C :
            Grade.append('C')
        elif lines[i] < Grade_C and lines[i] >= Grade_D :
            Grade.append('D')
            #print(Grade_C,lines[i])
        elif lines[i]<Grade_D:
            #print(Grade_D,lines[i])
            Grade.append('F')
    #print(Grade)
    print('**************************************')
    print("GRADE DISTRIBUTION AFTER CURVING GRADES USING CUT-OFF POINTS FROMABOVE:")
 
    print('{}:{} {}:{} {}:{} {}:{}  {}:{} '.format('A', countX(Grade, 'A'),
                    'B', countX(Grade, 'B'),'C', countX(Grade, 'C'),'D', 
                    countX(Grade, 'D'),'F', countX(Grade, 'F')))
    print('**************************************')
    with open('Scores-and-Letter-Grades.txt', 'w') as f:
        for i in range(len(lines)):
            strr=str(lines[i])+':'+Grade[i]
            f.write(strr)
            f.write('\n')

    
if __name__=="__main__":
	main()			 # call main function
