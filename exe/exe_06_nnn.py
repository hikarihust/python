# Input     : Nhập vào số tự nhiên n (0 < n < 10)
# Output    : In ra tổng của n + nn + nnn
# Ví dụ     : Nhập 5, in ra tổng 5 + 55 + 555 = 615

try:

      myNumber     = int(input("Nhập vào số tự nhiên n (0 < n < 10): "))

      if(myNumber > 0 and myNumber < 10):
            n1    = int( "%s" % myNumber )
            n2    = int( "%s%s" % (myNumber, myNumber))
            n3    = int( "%s%s%s" % (myNumber, myNumber, myNumber) )
            print ("{n1} + {n2} + {n3} = {result}".format(n1 = n1, n2 = n2, n3 = n3, result = n1 + n2 + n3))
      else :
            print ("Giá trị nhập vào không hợp lệ")
except ValueError:

      print ("Giá trị nhập vào phải là số tự nhiên")
