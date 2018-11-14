import math

DEFAULT_BIT_NUMBER = 8

class BinaryNumber():
    '''
    Creates a signed binary number
    '''


    def __init__(self, decimal_number=None, binary_number=None, bits=DEFAULT_BIT_NUMBER):
        '''(self, int, list[1|0], int) -> None
        Creates a binary number [number] which contains [bits] number of 
        bits (not including sign bit)

        Requirements:
        decimal_number - must fit within [bits] bits
        binary_number - Must be a list of 1's and 0's and be within [bits] bits
        bits - Must be > 0 
        '''
        self._num_of_bits = bits
        self.bin_num = [0]
        if decimal_number is not None:
            # Parse the decimal number into its binary equivalent
            #self.bin_num = self.convert_to_binary(decimal_number)
            self.convert_to_binary(decimal_number)
            self.sign_extend(self._num_of_bits)

        elif binary_number is not None:
            # The number is already in binary form
            _num_of_bits = len(binary_number) - 1 
            self.bin_num = binary_number

    def convert_to_binary(self, n):
        '''(self, int) 
        Given a number convert that number to a signed binary number, 
        by representing it as a list of 1's and 0's

        Requirements:
        n - valid integer
        '''
        is_neg = False
        if n < 0:
            is_neg = True
            n = n * (-1)
        cur_pos = math.floor(math.log(n, 2))
        while (cur_pos >= 0):
            #print("pos: " + str(cur_pos) + ", num: " + str(n))
            if ((n / (2 ** cur_pos)) >= 1):
                self.bin_num.append(1)
                n = n - 2 ** cur_pos
            else:
                self.bin_num.append(0)
            cur_pos -= 1
            
            #print(str(self.bin_num))
        if is_neg:
            self.bin_num = self.compliment().bin_num

    def compliment(self):
        temp = self.bin_num[:]
        for i in range (0, len(self.bin_num), 1):
            temp[i] = (self.bin_num[i] + 1) % 2
        add_one = BinaryNumber(binary_number=temp) + BinaryNumber(1)
        return add_one

    def get_int(self):
        num = self.bin_num
        if self.bin_num[0] == 1:
            num = self.compliment().bin_num
        
        int_num = 0
        power = 0
        for i in range (len(num) - 1, -1, -1):
            int_num += num[i] * (2 ** power)
            power += 1
        
        if self.bin_num[0] == 1:
            int_num = int_num * -1
        return int_num
        


    def __add__(self, other):
        '''(self, Object) -> BinaryNumber
        Will add the current number with [other] in a binary fashion
        '''
        # If the other number is an integer, first convert it to a binary
        if type(other) == int:
            other = BinaryNumber(other)
        # If the other number is anything but a BinaryNumber raise an error
        elif not isinstance(other, BinaryNumber):
            return None
        
        x = self
        y = other
        
        if (len(x) > len(y)):
            y = y.get_sign_extend(len(x))
        else:
            x = x.get_sign_extend(len(y))
        result = []
        #print ("-----------------")
        #print x
        #print y
        carry = 0
        for i in range (len(x), -1, -1):
            #print ('index: ' + str(i) )
            sum = x[i] + y[i] + carry
            #print(' sum: ' + str(sum))
            if (sum == 1 or sum == 3):
                result += [1]
            else:
                result += [0]
            if (sum == 2 or sum == 3):
                carry = 1
            else:
                carry = 0
            
        result.reverse()
        #print result
        return BinaryNumber(binary_number=result)
        
    def sign_extend(self, length):
        if length < len(self.bin_num):
            return None
        extension = [ self.bin_num[0] ] * (length - len(self.bin_num) + 1)
        self.bin_num =  extension + self.bin_num
    
    def get_sign_extend(self, length):
        if length < len(self.bin_num):
            return BinaryNumber(binary_number=self.bin_num)
        extension = [ self.bin_num[0] ] * (length - len(self.bin_num) + 1)
        return BinaryNumber(binary_number = extension + self.bin_num)
    
    def __len__(self):
        '''(self) -> int
        Return the length of this binary number excluding the sign bit
        '''
        return self._num_of_bits

    def __getitem__(self, i):
        return self.bin_num[i]

    def __str__(self):
        if self.bin_num == None:
            return ("None")
        num = ''
        for bit in self.bin_num:
            num += str(bit)
        return (num)


