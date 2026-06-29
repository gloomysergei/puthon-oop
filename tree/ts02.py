import os
import sys
sys.path.append(os.path.abspath('/usr/src/app/'))

class BinaryTreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        
def sorted_array_to_BST(nums):
    if not nums:
        return None
    
    mid = len(nums) // 2
    root = BinaryTreeNode(nums[mid])
    root.left = sorted_array_to_BST(nums[:mid])
    root.right = sorted_array_to_BST(nums[mid+1:])
    
    return root

lst = [1,2,3,4,5,6,7,8,9]
result = sorted_array_to_BST(lst)
print(result)