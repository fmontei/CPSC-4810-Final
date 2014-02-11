class BinaryDivide:
    global c
    global ACC
    global MQ
    global total
    global MDR
    global two
    global c_two

    #Generic constructor
    #Calls two functions upon instantiation b/c they only need to be called once
    def __init__(self, MQ, MDR):
        self.total = MQ
        self.MDR  = MDR
        self.two = ""
        self.c_two = ""
        self.format()
        self.two_complement()

    #Takes the dividend in binary form and symbolically puts its first 8 bits
    #into the ACC, and the last 8 bits into the MQ 'register'
    def format(self):
        self.c   = "0"
        self.ACC = self.total[0:8]
        self.MQ  = self.total[8:len(self.total)]

    #Shifts each bit left one place
    #Total holds each 8-bit value from ACC and MQ into 1 string
    def shift_left(self):
        self.c   = self.total[0]
        self.ACC = self.total[1:9]
        self.MQ  = self.total[9:len(self.total)] + "."

    #Calculates the two's complement of the carry ('c') and the divisor ('MDR')
    def two_complement(self):
        if self.c == "0":
            self.c_two = "1"
        else:
            self.c_two = "0"
            
        for i in self.MDR:
            if i == "0":
                self.two += "1"
            else:
                self.two += "0"
    
        self.two = add(self.two, "00000001")

#Converts a number into its base-2 equivalent
def binary(n, bits):
    BASE = 2
    result = ""
    remainder = None

    #Algorithm for converting base-10 to base-2
    while n != 0:
        remainder = n % 2
        #'//' performs integer division rather than floating-point division
        n = n // 2
        result += str(remainder)

    #Adds additional zeros specified by the bits parameter
    for i in range(int(bits - len(result))):
        result += "0"

    #Returns the resultant string in reverse order
    return result[::-1]

#Adds two binary numbers together; assumes that they have the SAME length
def add(num1, num2):
    result = ""
    carry = 0

    #Adds the strings together in reverse order, beginning with leftmost digit
    for i in range(len(num1) - 1, -1, -1):
        a = num1[i]
        b = num2[i]

        if int(a) + int(b) + carry == 0:
            result += "0"
            carry = 0
        elif int(a) + int(b) + carry == 1:
            result += "1"
            carry = 0
        elif int(a) + int(b) + carry == 2:
            result += "0"
            carry = 1
        elif int(a) + int(b) + carry == 3:
            result += "1"
            carry = 1
            
    result = result[::-1]
    return result

#Executes algorithm specified by project rubric
def compute(D):
    print("\n(step 0: ( MDR != 0 ) and ( MDR > ACC ) so no exceptions)")
    MDR_original = D.MDR

    for i in range(1, 9):
        print("---------------------------------------------------")
        print("step %i:   %s %s %s" % (i, D.c, D.ACC, D.MQ))
        print("       <<            shift left")

        D.shift_left()
        print("         ", D.c, D.ACC, D.MQ)
 
        print("        -", D.c, D.MDR, end = "")
        print("         (add %s %s)" % (D.c_two, D.two))
        print("          ----------")

        #Combines the values from each 'register' into a single string
        #to facilitate addition by the add function
        temp1 = D.c + D.ACC + D.MQ[0:len(D.MQ) - 1]
        temp2 = D.c_two + D.two + "0000000"
        result = add(temp1, temp2)
        #Reinitializes each 'register' from the resultant string
        D.c   = result[0]
        D.ACC = result[1:9]
        D.MQ  = result[9:len(result)] 

        #If the number is negative (begins with '1'), undo subtraction
        if D.c == "1":
            #Replaces truncated MQ's '.' with '0'
            D.MQ += "0"
            print("         ", D.c, D.ACC, D.MQ)
            print("                            ^"
                  "  set to 0 since subtract unsucessful")
            D.c = "0"
            print("       + ", D.c, D.MDR,
                  "          restoring add")
            print("          ----------")
            
            temp1 = D.c_two + D.ACC + D.MQ
            temp2 = D.c + D.MDR + "00000000"
            result = add(temp1, temp2)
            D.c   = result[0]
            D.ACC = result[1:9]
            D.MQ  = result[9:len(result)]

            print("         ", D.c, D.ACC, D.MQ)
        else:
            #Replaces truncated MQ's '.' with '1'
            D.MQ += "1"
            print("         ", D.c, D.ACC, D.MQ)
            print("                            ^"
                  "  set to 1 since subtract sucessful")
            
        D.total = D.ACC + D.MQ

    return (D.ACC, D.MQ)
    print("---------------------------------------------------")

#Prints results formatted as specified by project rubric
def print_results(MQd, MDRd, MQ, MDR, result):
    print("\n check:       binary            decimal")
    print("          %8s     %8s" % (MQ, MQd))
    print("          /       %8s      /%6s" % (MDR, MDRd))
    print("          ----------------      -------")
    print("        ", result[0], result[1], "         ",
          MQd // MDRd, "R", MQd % MDRd) 

#Program's main driver    
def main():
    MQd = int(input("enter dividend: "))
    while MQd not in range(0, 65536):
        MQd = int(input("enter dividend in range 0 - 65535, inclusive: "))
        
    MDRd = int(input("enter divisor: "))
    while MDRd not in range(0, 256):
        MDRd = int(input("enter divisor in range 0 - 255, inclusive: "))

    MQ  = binary(MQd, 16)
    MDR = binary(MDRd, 8)
    D = BinaryDivide(MQ, MDR)
    
    print("c set to", D.c)
    print("acc:mq set to dividend =", MQd, "decimal and", MQ, "binary")
    print("mdr set to divisor =", MDRd, "decimal and", MDR, "binary")
        
    result = compute(D)
    print_results(MQd, MDRd, MQ, MDR, result)

main()
