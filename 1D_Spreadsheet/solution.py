def do_operation(idx, grp):
    operation, arg_1, arg_2 = grp
    idx_error = False



    if '$' in arg_1 and isinstance(lst[int(arg_1[1:])], int):
        arg_1 = lst[int(arg_1[1:])]
    elif '$' in arg_1 and not isinstance(lst[int(arg_1[1:])], int):
        idx_error = True
      
    if '$' in arg_2 and isinstance(lst[int(arg_2[1:])], int):
        arg_2 = lst[int(arg_2[1:])]
    elif '$' in arg_2 and not isinstance(lst[int(arg_2[1:])], int):
        idx_error = True


    if not idx_error:
        if operation == 'ADD':
            lst[idx] = (int(arg_1) + int(arg_2))
        elif operation == 'SUB':
            lst[idx] = (int(arg_1) - int(arg_2))
        elif operation == 'VALUE':
            lst[idx] = (int(arg_1))
        elif operation == 'MULT':
            lst[idx] = (int(arg_1) * int(arg_2))




if __name__ == "__main__":
    n = int(input())
    lst = [input().split() for i in range(n)]
    # ipt = ['VALUE 3 _','ADD $0 4']
    # lst = [ipt[i].split() for i in range(n)]
    

    while True:
        intcount = 0

        for i in range(len(lst)):

            if not isinstance(lst[i], int):
                do_operation(i,lst[i])
     
            else:
                intcount += 1
        
        if intcount == n:
            break

    for i in lst:
        print(i)