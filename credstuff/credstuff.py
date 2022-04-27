
# with open('''usernames.txt''', 'r') as users_f:
#     with open('''passwords.txt''', 'r') as pass_f:
#         user = users_f.readline()
#         pwd = pass_f.readline()
#         if user == "cultiris":
#             print(user+":"+pwd)
#         users_f.close()
#         pass_f.close()

with open("usernames.txt") as f:
    f.read()