# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.__nestedList = nestedList
        self.__position = 0
        self.__lists = []
    
    def next(self) -> int:
        integer = self.__nestedList[self.__position].getInteger()
        self.__position += 1
        return integer
        
    
    def hasNext(self) -> bool:    
        while not self.__isComplete():
            currNode = self.__nestedList[self.__position]
            
            if currNode.isInteger():
                return True
            else:
                self.__position += 1
                self.__lists.append((self.__nestedList, self.__position))
                self.__position = 0
                self.__nestedList = currNode.getList()
            
        if self.__isComplete() and not self.__listEmpty():
            self.__nestedList, self.__position = self.__lists.pop()
            return self.hasNext()
                    
        return False
    
    def __listEmpty(self) -> bool:
        return len(self.__lists) == 0
    
    def __isComplete(self) -> bool:
        return self.__position >= len(self.__nestedList)
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())