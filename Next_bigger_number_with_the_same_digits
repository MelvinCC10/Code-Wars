"""

12 ==> 21
513 ==> 531
2017 ==> 2071

"""

def next_bigger(n):
    
    n =str(n)
    s = [int(i) for i in reversed(n)]
    #s.sort(reverse=True)
    
    ans = -1
    for i, num in enumerate(s):
        if i != 0:
            
            if num < s[i-1]:
              temp_list = s[0:i]
              temp_list2 = []
              for k, j in enumerate(temp_list):
                if num < j:
                  temp_list2.append(j)
                
              index = s.index(min(temp_list2))

              s[i] = s[index]
              s[index] = num
              if i>1:
                a = s[0:i]
                a.sort(reverse=True)
                s[0:i] = a

              s = [str(i) for i in reversed(s)]
              ans= ""
              ans = int(ans.join(s))

              break
      
    return ans
