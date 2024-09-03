from datetime import datetime

yob=int(input("what is your yob? "))
current_year=datetime.now().year
age=current_year-yob
print( "you are"+ " "+ str(age )+' '+ 'old' )

name=input('what is your name? ')
print('My name is' + name)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('kagendo')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
