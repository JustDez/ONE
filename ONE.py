#Python coding Questions

#Question 1
def hello_name(user_name):
    print(user_name)
hello_name("Dez")


#Question 2
def first_odds(d):
    return [x for x in range(0, d) if x%2 != 0]
print(first_odds(100))


#Question 3
def max_num_in_list(a_list):
    max = a_list[ 0 ]
    for b in a_list:
        if b > max:
            max = b
    return max
print(max_num_in_list([5,8,12,32,45,68,72]))
#

#Question 4
def is_leap_year(a_year):
    if a_year % 400 == 0:
        return True
    if a_year % 100 == 0:
        return False
    if a_year % 4 == 0:
        return True
    else:
        return False
print(is_leap_year(2016))
print(is_leap_year(2023))

#Question 5 
def is_consecutive(a_list):
    total = 2
    while total > 1:
        test = a_list.pop(0)
        if test == a_list[0] - 1:
            total = len(a_list)
        else:
            return False
            break
    return True
check = [2,6,4,12,11]

works = is_consecutive(check)
print(works)
