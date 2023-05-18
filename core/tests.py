# def make_pretty(func):
#     # define the inner function 
#     def inner():
#         # add some additional behavior to decorated function
#         print("I got decorated")

#         # call original function
#         func()
#     # return the inner function
#     return inner

# # define ordinary function
# def ordinary():
#     print("I am ordinary")
    
# # decorate the ordinary function
# decorated_func = make_pretty(ordinary)

# # call the decorated function
# decorated_func()






# def make_pretty(func):

#     def inner():
#         print("I got decorated")
#         func()
#     return inner

# @make_pretty
# def ordinary():
#     print("I am ordinary")

# ordinary()  

# def add_one(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result + 1
#     return wrapper

# @add_one
# def add(a, b):
#     return a + b

# # def add(*args):
    
# #     result = a+b
        
# print(add(2,3))


# print(add(2,3))


final = [
    {'num_comments': 5, 'title': 'B'},
    {'num_comments': 10, 'title': 'C'},
    {'num_comments': 3, 'title': ''},
    {'num_comments': None, 'title': 'D'},
    {'num_comments': 10, 'title': 'E'},
    {'num_comments': 8, 'title': None}
]

sorted = sorted(final,key = lambda x: (-x['num_comments'] if x['num_comments'] is not None else 0,x['title'] or '' ))
print(sorted)