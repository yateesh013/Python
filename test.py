def max_of_number(my_list,n):
    m=[]

    if(len(set(my_list))<n):
        return ValueError("error")
    
    for i in range(n):
        lar=0
        for j in range(len(my_list)):
            if my_list[j]>lar and my_list[j] not in m :
                lar=my_list[j]
        m.append(lar)            
              
    return lar            
                            