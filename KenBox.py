from datetime import datetime

class KenBox:
    
    containedBox=None
    childrenCount=0
    
    def __init__(self,box=None):
        self.containedBox = box
        if (box is KenBox):
            self.childrenCount = box.childrenCount + 1
    
    def getChildBoxRecurse(self,box):
        if (box.containedBox is not None):
            return self.getChildBoxRecurse(box.containedBox) + 1
        return 0
    
    def getNumberOfChildBoxesRecursive(self):
        return self.getChildBoxRecurse(self)
    
    def getNumberOfChildBoxesIterative(self):
        i = 0
        child = self.containedBox
        while (child is not None):
            i += 1
            if (child.containedBox is not None):
                child = child.containedBox
            else:
                child = None
        return i

    def getNumberOfChildBoxesCounter(self):
        return childrenCount
