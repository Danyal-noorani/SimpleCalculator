#Functions_list
import colorama as cm
import pyfiglet as pf
Banner = pf.figlet_format("Python   Programs", font="slant", width = 2000)
print(Banner)
funcs = []
def Question_1():
    Name = input(cm.Fore.RED +"Name and Nationality" +cm.Fore.RESET+" \nEnter Name --> ")
    Nationality = input("Enter Nationality --> ")
    print(Name ," is " ,Nationality)
funcs.append(Question_1)

def Question_2():
    Num = input(cm.Fore.RED +"Square and Cube"+cm.Fore.RESET+"\nEnter a Number --> ")
    Num = float(Num)
    square = Num**2
    square = '{:,.2f}'.format(square)
    cube = Num**3
    cube = '{:,.2f}'.format(cube)
    print("Square = ",square)
    print("Cube = ",cube)
funcs.append(Question_2)
def Question_3():
    length = input(cm.Fore.RED +"Ar of Triangle"+cm.Fore.RESET+"\nEnter Length of triangle in cm --> ")
    length = float(length)
    breadth = input("Enter Breadth of triangle in cm --> ")
    breadth = float(breadth)
    ar_of_triangle = (length*breadth)/2
    ar_of_triangle = '{:,.2f}'.format(ar_of_triangle)
    print("Area of triangle is = ", ar_of_triangle,'sq.cm')
funcs.append(Question_3)

def Question_4():
    print(cm.Fore.RED +"3 number Total and AVG"+cm.Fore.RESET)
    num1 = input("Enter 1st Number --> ")
    num2 = input("Enter 2st Number --> ")
    num3 = input("Enter 3st Number --> ")
    added = float(num1)+float(num2)+float(num3)
    Avg = added / 3
    added ='{:,.2f}'.format(added)
    Avg = '{:,.2f}'.format(Avg)
    print("Sum = ", added)
    print("AVG = ",Avg)
funcs.append(Question_4)

def Question_5():
    inch = input(cm.Fore.RED +"Inch to cm"+cm.Fore.RESET+"\nEnter length in inch --> ")
    cms  = float(inch) *2.54
    cms = '{:,.2f}'.format(cms)
    print(cms,"cm")
funcs.append(Question_5)
def Question_6():
    radius = input(cm.Fore.RED +"Surface area and volume of spherer"+cm.Fore.RESET+"\nEnter Radius in cm --> ")
    radius = float(radius)
    Area = (4*22*radius*radius)/7
    Area =  '{:,.3f}'.format(Area)
    Volume =(4*22*radius*radius*radius)/(3*7)
    Volume ='{:,.3f}'.format(Volume)
    print("Surface Area = " , Area)
    print("Volume = ", Volume)
funcs.append(Question_6)
def Question_7():
    Gallon = input(cm.Fore.RED +"Gallon to Cubic Foot"+cm.Fore.RESET+"\nEnter Gallons --> ")
    cubic_foot = float(Gallon)/7.481
    cubic_foot = '{:,.3f}'.format(cubic_foot)
    print(cubic_foot," Cubic Foot")
funcs.append(Question_7)
def Question_8():
    minutes = input(cm.Fore.RED +"Minutes to Hrs"+cm.Fore.RESET+"\nEnter time in minutes --> ")
    minutes = int(minutes)
    Hrs = minutes//60
    mins = minutes % 60
    print("Time is ",Hrs,":",mins)
funcs.append(Question_8)

def Question_9():
    fils = input(cm.Fore.RED +"Fils to Dhs"+cm.Fore.RESET+"\nEnter amount of fils --> ")
    fils = int(fils)
    Dhs = fils//100
    fil = fils%100
    print("Amount is ",Dhs,"Dhm ",fil,"fils")
funcs.append(Question_9)
def Question_10():
    salary = float(input(cm.Fore.RED +"Salary Calculation"+cm.Fore.RESET+"\nInput Salary --> "))
    allowance = (12*salary)/100
    deduction = (10*salary)/100
    net_salary = salary+allowance-deduction
    deduction = '{:,.2f}'.format(deduction)
    allowance = '{:,.2f}'.format(allowance)
    net_salary = '{:,.3f}'.format(net_salary)

    print("     Pay Slip")
    print("-"*50)
    print(f"{'Basic Salary'}{':':>7}{str(salary):>16}")
    print(f"{'Allowance'}{':':>10}{str(allowance):>16}")
    print(f"{'Deduction'}{':':>10}{str(deduction):>16}")
    print("-"*50)
    print(f"{'Net'}{':' + str(net_salary):>12}")
funcs.append(Question_10)

def Question_11():
    meter = float(input(cm.Fore.RED +"Meter to Km"+cm.Fore.RESET+"\nEnter length in meter --> "))
    km = meter//1000
    m = meter%1000
    m = '{:,.2f}'.format(m)
    print(km,"kilometers and ",m," meters")
funcs.append(Question_11)

def Question_12():
    digits = input(cm.Fore.RED +"Digits Add"+cm.Fore.RESET+"\nEnter a number --> ")
    #digits = "1234"
    #convert them into induvidual number
    list_of_digits = []
    i = 0
    while i < len(digits):
        list_of_digits.append(digits[i])
        i+=1
    # Adding
    b = 0
    num=0
    while b < len(list_of_digits):
        num += int(list_of_digits[b])
        b+=1


    print('Addition of the numbers is --> ',num)
funcs.append(Question_12)

def Question_13():
    #input
    sec = int(input(cm.Fore.RED +"Seconds to time"+cm.Fore.RESET+"\nEnter Time in Seconds --> "))
    #convert to Minutes
    minute = sec//60
    secs = sec%60
    #convert to Hrs
    hr = minute//60
    minutes = minute%60
    #Out
    print(sec,'Seconds = ',hr,'Hrs :', minutes,'Mins :',secs,'Sec')
funcs.append(Question_13)

def Question_selecter():
    qno = int(input("Enter Question Number --> "))

    funcs[qno-1]()
    Question_selecter()
