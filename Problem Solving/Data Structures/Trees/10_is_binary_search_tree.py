#https://www.hackerrank.com/challenges/is-binary-search-tree/problem

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_node(root,min_value,max_value):
    if(root!=None):
        if(root.data<=min_value or root.data>=max_value):
            return False
        else:
            return check_node(root.left,min_value,root.data) and                                                      check_node(root.right,root.data,max_value)
    else:
        return True
    
def check_binary_search_tree_(root):
    return check_node(root,-1,10001)
        
