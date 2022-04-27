import codecs

users_f = open('credstuff/usernames.txt', 'r')
pass_f = open('credstuff/passwords.txt', 'r')
while True:
    user = users_f.readline()
    pwd = pass_f.readline()
    if user == "cultiris\n":
        break

print(user.replace("\n","")+":"+pwd)
users_f.close()
pass_f.close()

print(codecs.decode(pwd, "rot_13"))