import time
import string
import random
import multiprocessing as mp


# creating random email adresses
domains     = ['gmail.com', 'gmx.de', 'web.de', 'outlook.de', 't-online.de', 'aol.com']
recipients  = [''.join(random.choice(string.ascii_lowercase) for i in range(7)) + '@'
               + random.choice(domains) for i in range(10)]

# function that fakes sending mail by waiting 0.5 seconds
def send_mail(i):
    time.sleep(0.5)
    print('email was sent to ' + i)

#for i in recipients:
#    send_mail(i)

# sending mails to every recipient by using multiprocessing
if __name__ == '__main__':
    mp.freeze_support()
    pool = mp.Pool(mp.cpu_count())
    pool.map(send_mail, [i for i in recipients])
    pool.close()
