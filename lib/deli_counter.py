katz_deli = [3, 4, 5]

def line (katz_deli, number) : 
    i=1
    for customer in katz_deli:
        if number == customer:
            print(f"You are number {i} in the queue")
        else:
            i+=1

def take_a_number (katz_deli, name) :
    num = len(katz_deli) + 1
    new_num=katz_deli[num-2]+1
    katz_deli.append(new_num)
    if num == 1:
        print("The line is currently empty.")
    else:
        print(f"Welcome, {name}. You are number {num} in line")

take_a_number(katz_deli, "Fi")
take_a_number(katz_deli, "Mack")

def now_serving (katz_deli):
    num = katz_deli[0]
    print(f"Now serving {num}")
    del katz_deli[0]

now_serving(katz_deli)
now_serving(katz_deli)
now_serving(katz_deli)