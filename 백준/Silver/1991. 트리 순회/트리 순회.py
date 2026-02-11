import sys

input=sys.stdin.readline
n=int(input())
nodes={}
for _ in range(n):
    a,b,c=input().split()
    nodes[a]=[b,c]

def preorder(root):
    if root==".":
        return
    print(root,end="")
    preorder(nodes[root][0])
    preorder(nodes[root][1])

def inorder(root):
    if root==".":
        return
    inorder(nodes[root][0])
    print(root,end="")
    inorder(nodes[root][1])

def postorder(root):
    if root==".":
        return
    postorder(nodes[root][0])
    postorder(nodes[root][1])
    print(root,end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')