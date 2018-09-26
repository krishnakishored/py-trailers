#https://www.programiz.com/python-programming/list
## Functions on lists


# https://www.hackerrank.com/challenges/list-comprehensions/problem

def hr_listcomprehension(x,y,z,n):
    return [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c!=n]

# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

def hr_second_max(mylist):
   temp = mylist.copy()
   temp.remove(max(mylist))
   return max(temp)




if __name__ == '__main__':
    # x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input())

    # x, y, z, n = (int(input()) for _ in range(4))

    # print(hr_listcomprehension(2,2,2,2))
    print(hr_listcomprehension(1,1,1,2))
    print(hr_second_max([1,3,4,56,77,100]))

    n = int(input())
    arr = map(int, input().split())
    temp = set(arr)
    # temp = list(arr) # doesn't work for repeated numbers
    # max1 = max(temp)
    temp.remove(max(temp))
    print(max(temp))