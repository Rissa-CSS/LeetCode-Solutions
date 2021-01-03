class Solution(object):
    def reverse(self,x):
        """
        :type x: int
        :rtype: int
        """
        # creates a list and string
        self.number =[]
        self.answer =""
        
        #Converts the number into a string and pushes each digit into the list
        for num in str(x):
            self.number.append(num)
        #Reverses thed list
        self.number.reverse()
        #Loops through the reversed list
        for i in range(len(self.number)):
            #Makes sure that the current element is a digit not a sign 
            #and adds it to the answer string
            if self.number[i].isdigit():
                self.answer+=self.number[i]
        #Ensures the answer is within the range -2^31 and 2^31 -1
        if (int(self.answer)<(pow(2,31)-1) and int(self.answer)>pow(-2,31)):
            #if the number is positive convert the string to an integer and return it
            if x>=0:
                return int(self.answer)    
            #if the number is negative multiply the answer by -1 and return it
            else:
                return int(self.answer) *-1
        #if the number is out of the range return 0
        else:
            return 0

def main():
    #Calls the function
    print(Solution.reverse(x))
