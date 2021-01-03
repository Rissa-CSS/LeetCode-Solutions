class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        '''
        # Lists for current numer and reverse number
        self.ans = []
        self.rev =[]
        
        # Loops through the string and places it in a list
        
        for i in str(x):
            self.ans.append(i)
        #copies the list
        self.rev = self.ans[:]
        # reverses list
        self.ans.reverse()
        #checks if the the two lists are equal
        if self.ans==self.rev:
            return True
        '''
        #checks if str x and the reverse string are equal
        if str(x) == str(x)[::-1]:
            return True

        
