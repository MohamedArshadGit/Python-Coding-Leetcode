def simplyPath(path):
    stack=[]
    curr=""
    for c in path+"/":
        if c=="/":
            if curr=="..":
                if stack:
                    stack.pop()
            elif (curr !="" and curr!="."): #and curr!="_":
                stack.append(curr)
            curr=""
        else:
            curr=curr+c
    return "/"+"/".join(stack)


path = "/home//foo/"
a=simplyPath(path)
print(a)

path = "/home/"
a=simplyPath(path)
print(a)

path = "/../"
a=simplyPath(path)
print(a)