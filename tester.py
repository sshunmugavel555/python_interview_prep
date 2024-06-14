def sayFullName(fn,ln='',mn=''):
    """ Compute a full name from the first,last and middle names and return the full name """
    if mn and ln:
        return fn.title()+' '+mn.title()+' '+ln.title()
    else:
        if ln:
            return fn.title()+' '+ln.title()
        else:
            return fn.title()
    

# while True:
#     fn=input("Enter your first name / Q to quit ")
#     ln=input("Enter your last name / Q to quit ")
#     if fn=='Q' or ln=='Q':
#         break
#     else:
#         fullName=sayFullName(fn,ln)
#         print(fullName)