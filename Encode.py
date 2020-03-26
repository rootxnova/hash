from hashlib import*
fname = input('Enter File Name : ')
with open(fname,mode='r')as f:
    for line in f:
        line=line.strip()
        hashing = md5(line.encode()).hexdigest()
        print('MD5 = ',hashing)
        
ending = input('Press Enter To End Script')
