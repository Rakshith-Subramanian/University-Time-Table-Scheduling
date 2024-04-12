S_D=["Monday","Tuesday","Wednesday","Thursday","Friday"]


Total_Sub={1:[["UMA2176","UGE2176","UPH2176","UCY2176","UGE2177"],
                ["UGE2176","UMA2176","UCY2176","UGE2177","UPH2176"]],
          
           2:[["UCS2201","UCS2202","UMA2276","UEN2276","UEE2276"],
              ["UCS2202","UCS2201","UEN2276","UEE2276","UMA2276"]],
          
           3:[["UCS2303","UCS2302","UCS2301","UMA2377","UHS2351"],
              ["UCS2302","UCS2303","UMA2377","UHS2351","UCS2301"]],
          
           4:[["UCS2404","UCS2401","UCS2403","UCS2402","UMA2455"],
              ["UCS2401","UCS2404","UCS2402","UMA2455","UCS2403"]],
          
           5:[["UCS2501","UCS2502","UCS2504","UCS2503","UCS2520"],
              ["UCS2502","UCS2501","UCS2503","UCS2520","UCS2504"]],
          
           6:[["UCS2601","UCS2602","UCS2603","UCS2604","UCS2620"],
              ["UCS2602","UCS2601","UCS2604","UCS2620","UCS2603"]],
          
           7:[["UCS2701","UCS2703","UCS2702","UCS2720","UCS2730"],
              ["UCS2703","UCS2701","UCS2720","UCS2730","UCS2702"]],
          
           8:[["UCS2820","UCS2830","UCS2818","UCS2818","UCS2818"],
              ["UCS2830","UCS2820","UCS2818","UCS2818","UCS2818"]]}

Abbv={1:["UEN2176 Technical English","UMA2176 Matrices and Calculus","UPH2176 Engineering Physics ","UCY2176 Engineering Chemistry", "UGE2176 Problem Solving and Programming in Python","UGE2177 Engineering Graphics" ,"UGS2197 Physics and Chemistry Lab", "UGE2197 Programming in Python Lab"],

      
      2:["UCS2201 Fundamentals and Practice of Software Development (TCP)","UCS2202 Foundations of Data Science","UMA2276 Complex Functions and Laplace Transformations","UEN2276 Humanities Elective","UEE2276 Basic Electrical and Electronics","UGE2297 Design Thinking and Engineering Practices Lab","UCS2211 Programming in C Lab"],

      
      3:["UCS2303 Object Oriented Programming","UCS2302 Data Structures","UCS2301 Digital Principles and System Design","UMA2377 Discrete Mathematics","UHS2351 Universal Human Values II","UCS2311 Digital Design Lab","UCS2312 Data Structures Lab"],

      
      4:["UCS2404 Database Management Systems","UCS2401 Computer Organization and Architecture","UCS2403 Design and Analysis of Algorithms","UCS2402 Operating Systems","UMA2455 Probablity and Statistics","UCS2412 Operating Systems Lab","UCS2411 Database Lab"],
      
      5:["UCS2501 Computer Networks","UCS2502 Microprocessors, microcontrollers,and Interfacing","UCS2504 Foundations of Artificial Intelligence(TCP)","UCS2503 Software Engineering","UCS2520 Professional Elective-I","UCS2511 Networks Lab","UCS2512 Microprocessors Lab"],
      
      6:["UCS2601 Internet Programming","UCS2602 Software System Security","UCS2603 Theory of Computation","UCS2604 Principles of Machine Learning","UCS2620 Open Elective-II","","UCS2612 Machine Learning Lab"],

      
      7:["UCS2701 Distributed Systems","UCS2703 Software Architecture","UCS2702 Compiler Design (TCP)","UCS2720 Proffesional Elective-4","UCS2730 Proffesional Elective-3","UCS2717 Project Work Phase I","UCS2716 Industrial Training / Internship"],
      
      8:["UCS2830 Professional Elective-5","UCS2820 Proffesional Elective-6","UCS2818 Project Hour","UCS2818 Project Hour","UCS2818 Project Hour"]}







def calculate():
    #A Dictionary to hold the  respective timetable and list with days
    S_TT={"Monday":[],"Tuesday":[],"Wednesday":[],"Thursday":[],"Friday":[]}

    #Lists to hold the subjects and the Hours of each one in priority order

    Sub_L=[]
    S_H=[7,7,6,6,6]
    Free=["Mentor","Library"]
    c=0
    F_H=4

    #Manually assigning lab hours
    def LabDay(sem1,sec1):
        if sem1==1:
            if sec1=='A':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UGS2197")
            elif sec1=='B':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UGS2197")
        if sem1==2:
            if sec1=='A':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UGE2297")
            elif sec1=='B':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UGE2297")
        if sem1==3:
            if sec1=='A':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2311")
            elif sec1=='B':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2311")
        if sem1==4:
            if sec1=='A':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2412")
            elif sec1=='B':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2412")
        if sem1==5:
            if sec1=='A':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2511")
            elif sec1=='B':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2511")
        if sem1==6:
            if sec1=='A':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2611")
            elif sec1=='B':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2611")
        if sem1==7:
            if sec1=='A':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2717")
            elif sec1=='B':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2717")
        if sem1==8:
            if sec1=='A':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2817")
            elif sec1=='B':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2817")
    
    
    def LabDay2(sem1,sec1):
        if sem1==1:
            if sec1=='A':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UGE2197")
            elif sec1=='B':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UGE2197")
        if sem1==2:
            if sec1=='A':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2211")
            elif sec1=='B':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2211")
        if sem1==3:
            if sec1=='A':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2312")
            elif sec1=='B':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2312")
        if sem1==4:
            if sec1=='A':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2411")
            elif sec1=='B':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2411")
        if sem1==5:
            if sec1=='A':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2512")
            elif sec1=='B':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2512")
        if sem1==6:
            if sec1=='A':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2612")
            elif sec1=='B':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2612")
        if sem1==7:
            if sec1=='A':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2716")
            elif sec1=='B':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2716")
        if sem1==8:
            if sec1=='A':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2816")
            elif sec1=='B':
                L1=input("Enter day on which lab will be conducted:")
                if L1 in S_TT.keys():
                    for i in range(0,3):
                        S_TT[L1].append("UCS2816")









    #Function used to find index of element with max hours in the hours list
    def max_index(list0):
        index= 0
        max_n= list0[0]
        for i in range(0, len(list0)):
            if list0[i] > max_n:
                max_n= list0[i]
                index = i
        return index

    #Function to check forenoon hours
    def FNC(Sub_List,s,S_DList,m,n):
        flag=0
        if Sub_List[m] in s[S_DList[n]]:
            return False
        else:
            return True

    #Collecting Inputs:
    global sem
    global sec
    sem=int(input("Enter Semester:"))
    sec=input("Enter Section(A/B):")

    if sec=='A':
        Sub_L=Total_Sub[sem][0]
        LabDay(sem,sec)
        LabDay(sem,sec)
    elif sec=='B':
        Sub_L=Total_Sub[sem][1]


    for j in range(5):
        k=max_index(S_H)
        for x in range(5):
            if FNC(Sub_L,S_TT,S_D,k,x) is True:
                S_TT[S_D[x]].append(Sub_L[k])
                S_H[k] =  S_H[k] - 1
                k=max_index(S_H)


    for i in range(5):
        for q in range(5):
            if Sub_L[i] not in S_TT[S_D[q]]:
                S_TT[S_D[q]].append(Sub_L[i])
                S_H[i]=S_H[i]-1

    if sec=='B':
        LabDay(sem,sec)
        LabDay(sem,sec)
          
    for i in range(3):
        for j in range(5):
            if len(S_TT[S_D[j]])<8:
               
                   w=max_index(S_H)
                   if S_H[w]>0:
                       if Sub_L[w] not in S_TT[S_D[j]][5:]:
                       
                           S_TT[S_D[j]].append(Sub_L[w])
                           S_H[w]-=1
                   elif S_H[w]==0 :
                   
                       S_TT[S_D[j]].append(Free[c])
                       c+=1
    if sec=='B':
        S_TT["Monday"][3],S_TT["Monday"][4]=S_TT["Monday"][4],S_TT["Monday"][3]
        S_TT["Wednesday"][3],S_TT["Wednesday"][4]=S_TT["Wednesday"][4],S_TT["Wednesday"][3]


    print()
    print("Semester-",sem," ","Section",sec)
    print("Day   ","  1st    ","   2nd     ","  3rd     ","  4th    ","   5th   ","    6th    ","   7th     ","  8th   ")   
    for i in S_D:
        print(i[0:3],":",end="    ")
        for j in S_TT[i]:
            print(j,end="    ")
        print()
    print()
    x=Abbv[sem]
    print("            Subject Code ","  Name")
    for i in x:
        a=i[0:7]
        b=i[8:]
        print("           ",a,"       ",b)
        
    print()
    print()
    print()
    return S_TT
           

Clg_TT={1:[0,0],2:[0,0],3:[0,0],4:[0,0],5:[0,0],6:[0,0],6:[0,0],7:[0,0],8:[0,0]}
for i in range(4):
    for i in range(2):
        print("_")
        L1=calculate()
        if sec=='A':
            x=0
        else:
            x=1
        Clg_TT[sem][x]=L1


print()
print()
total_fac={}
sub_fac={}#both will have same keys i.e the name of the faculties

fac=int(input("enter total number of faculties whose timetable is to be checked:"))
for i in range(fac):
    print("")
    print()
    print()
    name=input("enter the unique name of the faculty:")
    print()
    total_fac[name]={"Monday":[' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - '],"Tuesday":[' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - '],"Wednesday":[' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - '],"Thursday":[' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - '],"Friday":[' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ']}
    sub_fac[name]=[]
    
    numclass=int(input("enter total number of classes taken by above faculty: "))

    for j in range(numclass):
        print("")
        semester=int(input("enter semester(1-8) taken: "))
        section=input("enter section (A/B) ")
        
        if section=='A':
            newsection=0
        else:
            newsection=1
        clas=Clg_TT[semester][newsection]
        A=str(semester)+"-"+str(section)
        print()
        print("for ",A)
        print("please avoid choosing subject of same priority index")
        fac_sub_list=Abbv[semester]
        
        subject=input("enter subject code handled for the above class:")
        print()
        print()
        for sub in fac_sub_list:
            if sub[0:7]==subject:
                B=A+" "+str(subject)+str(" ")+str(sub[7:])
                
        sub_fac[name].append(B)
        for day in S_D:
            for period in range(8):
                if clas[day][period]==subject:
                    total_fac[name][day][period]=A
                    



for i in total_fac.keys():
    print()
    print()
    print("faculty = ",i)
    print()
    print("TT is")
    print()
    f_tt=total_fac[i]
    for day in S_D:
        print(day[0:3],":",end="    ")
        for val in f_tt[day]:
            print(val,end="    ")
        print()
    print()
    y=sub_fac[i]
    print("Class ","Subject Code","  Subject Name")
    for subject in y:
        print(subject[0:3],"  ",subject[4:11],"      ",subject[13:],end=" ")
        print()
    print()
    
    #i=staff name
    #f_tt holds individual staff tt
    #2-A UCS2202  Foundations of Data Science