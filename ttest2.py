
while True : 
    s = raw_input()

    f = open('/home/pi/test/qr_test/testfolder/test.txt','a')
    f.write(s)
    f.close()
