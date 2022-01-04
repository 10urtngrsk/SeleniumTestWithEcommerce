from operator import itemgetter
#User list, you can add valid or invalid users or passwords
users = [
    {"name":"valid_user","email":"your_email_here","password":"your_password_here"},
    {"name":"invalid_user","email":"admin@hepsiburada.com","password":"hepsiburada"},
    {"name":"invalid_user_2","email":"onurtengirsek@gmail.com","password":"password123"}
]
#returns the wanted user
def get_username(name):
    try:
        return next(user for user in users if user["name"] == name)
    except:
        print("\n  User %s is not defined, enter a valid user.\n" %name)