spam=['apples', 'bananas', 'tofu', 'cats']

def comma(lis):
    for i in range(len(lis)-1):
        print(lis[i],end=', ')
    print("and "+lis[-1])
        
comma(spam)