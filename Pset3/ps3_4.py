def find_average(list_of_lists):
    results = []
    overall_total = 0
    count = 0
    
    for list in list_of_lists:
        if len(list) != 0: 
            total = 0
            for nums in list:
                overall_total += nums
                count += 1
                total += nums
            results.append(total/len(list))
        else:
            results.append(0)
    
    return(results, overall_total/count)

ans=find_average ([[3,4],[5,6,7],[-1,2,8]])
print(ans)

ans=find_average ([[13.13 ,1.1 ,1.1] ,[] ,[1 ,1 ,0.67]])
print(ans)