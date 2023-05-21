import time
hosts_file  = r"/Users/vudinhquang/Documents/quang/python/2.Xay-dung-cac-ung-dung-voi-python/2.ung-dung-chan-truy-cap-trang-web/test.txt"


while True:
    with open(hosts_file,'a') as file:
        file.write("Hello\n")
                    
    time.sleep(5)
