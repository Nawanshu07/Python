print("Enter 1 for sick Leave Application")
print("Enter 2 for brother Leave Application")
print("Enter 3 for Urgent work Leave Application")

a = int(input("Enter a choice:"))
name = input("Enter your name:")
clas = input("Enter your class:")
school = input("Enter your school name:")

if(a == 1):
    content = f'''
    To
    The Principal
    {school}

    Subject: Application for Leave

    Respected Sir/Madam,

    I respectfully request you to kindly grant me leave as I am suffering from fever and unable to attend classes. I will complete all pending work after recovery.

    Therefore, I kindly request you to approve my leave application.

    Thanking you.

    Yours obediently,
    {name}
    {clas}
    '''

    print(content)
elif(a == 2):

    content = f'''
To
The Principal
{school}

Subject: Application for Leave

Respected Sir/Madam,

I respectfully request you to kindly grant me leave as I have to attend my brother's marriage ceremony. Therefore, I will be unable to attend classes.

I will complete all pending work after returning.

Therefore, I kindly request you to approve my leave application.

Thanking you.

Yours obediently,
{name}
{clas}
'''

    print(content)


elif(a == 3):

    content = f'''
To
The Principal
{school}

Subject: Application for Leave

Respected Sir/Madam,

I respectfully request you to kindly grant me leave due to some urgent work at home. Therefore, I will be unable to attend classes.

I will complete all pending work after returning.

Therefore, I kindly request you to approve my leave application.

Thanking you.

Yours obediently,
{name}
{clas}
'''

    print(content)

else:
    print("Invalid Choice")