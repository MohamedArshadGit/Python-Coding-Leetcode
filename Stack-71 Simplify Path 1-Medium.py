'''71. Simplify Path

Medium

Given a string path, which is an absolute path (starting with a slash '/') to a file or directory
 in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to
 the directory up a level, and any multiple consecutive slashes
  (i.e. '//') are treated as a single slash '/'.
   For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

    The path starts with a single slash '/'.
    Any two directories are separated by a single slash '/'.
    The path does not end with a trailing '/'.
    The path only contains the directories on the path from the root directory
     to the target file or directory (i.e., no period '.' or double period '..')

Return the simplified canonical path.

Example 1:

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Constraints:

    1 <= path.length <= 3000
    path consists of English letters, digits, period '.', slash '/' or '_'.
    path is a valid absolute Unix path.

'''

def simplyPath(path):
    stack=[]
    curr=""
    for c in path+"/": # if we add + '/' it will add / at the end of the string
        # it will be helpful for this sum while
        # running in loop it will help to append the remaining values in the curr
        if c=="/": # if / comes if something in curr we will try to append in stack if nothing there we will skip
            if curr=="..": # !!!!important part of this sum if .. comes means pop the last string of the stack
                if stack:
                    stack.pop()
            elif (curr !="" and curr!="."): #and curr!="_":  other than empty space and . it will append- what in curr
                stack.append(curr)
            curr="" #here we reset curr important
        else:
            curr=curr+c # add all the characters in one place and store it in curr
    print(stack)
    return "/"+"/".join(stack) #this is important  "/" + "/".join(stack) takes a list of elements in stack and creates a string where each element is separated by a "/" character, with a "/" at the beginning of the string.

path = "/home//foo/"
a=simplyPath(path)
print(a)

path = "/home/"
a=simplyPath(path)
print(a)

path = "/../"
a=simplyPath(path)
print(a)