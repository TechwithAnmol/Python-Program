test_list = [1,2,3,4,5,6,7,8,9,10]
res = [test_list[i + 1] - test_list[i] for i in range(len(test_list)-1)] 
print(res)
