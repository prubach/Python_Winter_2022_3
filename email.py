email1 = 'pawel.rubach@sgh.waw.pl'
email2 = 'pawel.rubach$sgh.waw.pl'
email3 = 'pawel.rubach@'
email4 = '@sgh.waw.pl'
email5 = 'pawel.rubach@.pl'
email6 = 'pawel@rubach@.pl'


def check_email(email):
    #TODO implement all checks here
    if email:
        return True
    else:
        return False


for em in [email1, email2, email3, email4, email5, email6]:
    print('{}: {}'.format(em, check_email(em)))

for i in range(len(email4)):
    print(email4[i])