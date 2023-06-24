

best_Nubmer_spec = [0,0]
prime_deviation = []
for i in range(0,10):


    New_Num = int(input())
    
    # detect all prime division of input number
    all_prime_deviation = []
    for j in range(2,New_Num+1):

        if New_Num%j==0:
            indicator = 0
            for div_ind in all_prime_deviation:
                if j%div_ind==0:
                     indicator += 1
                     break
            if indicator==0:
                all_prime_deviation.append(j)
    
           

    if best_Nubmer_spec[1]<len(all_prime_deviation):
        best_Nubmer_spec[1]=len(all_prime_deviation)
        best_Nubmer_spec[0]=New_Num
        prime_deviation = all_prime_deviation
    elif best_Nubmer_spec[1] == len(all_prime_deviation):
        if best_Nubmer_spec[0]<New_Num:
            best_Nubmer_spec[0]=New_Num
            best_Nubmer_spec[1]=len(all_prime_deviation)
            prime_deviation = all_prime_deviation
    
print(best_Nubmer_spec)
print(prime_deviation)   

                
    
