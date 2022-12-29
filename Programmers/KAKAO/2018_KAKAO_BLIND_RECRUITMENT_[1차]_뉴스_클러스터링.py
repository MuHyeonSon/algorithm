def solution(str1, str2):
    # 대문자 소문자 차이 무시 처리
    str1 = str1.lower() 
    str2 = str2.lower()
    
    str1_list = [str1[i] + str1[i+1] for i in range(len(str1)-1) if str1[i].isalpha() and str1[i+1].isalpha()]
    str2_list = [str2[i] + str2[i+1] for i in range(len(str2)-1) if str2[i].isalpha() and str2[i+1].isalpha()]
    
    
    # 교집합의 원소의 수와 합집합 원소의 수 구하기
    share = 0
    sum_of_set = 0
    """
    if len(str1_list) > len(str2_list):
        for x in range(len(str2_list)):
            if str2_list[x] in str1_list :
                share += min(str1_list.count(str2_list[x]),str2_list.count(str2_list[x]))
                sum_of_set += max(str1_list.count(str2_list[x]),str2_list.count(str2_list[x]))
                for item in str1_list:
                    if item == str2_list[x]: 
                        str1_list.remove(str2_list[x])
        sum_of_set += len(str1_list)                
    else :
        for x in range(len(str1_list)):
            if str1_list[x] in str2_list :
                share += min(str2_list.count(str1_list[x]),str1_list.count(str1_list[x]))
                sum_of_set += max(str2_list.count(str1_list[x]),str1_list.count(str1_list[x]))
                for item in str2_list:
                    if item == str1_list[x]: 
                        str2_list.remove(str1_list[x])
        sum_of_set += len(str2_list)  
        
    """
        
            

    
    #sum_of_set = len(set(str1_list + str2_list))
    
    # A혹은 B 둘 중 하나라도 공집합이라면 결과는 1
    if share == 0 or sum_of_set == 0:
        return 1 * 65536
    
    answer = share/sum_of_set
    answer = int(answer*65536)
    return answer 
    #return [share,sum_of_set]
    #return str1_list + str2_list


##### 공백혹은 특수문자 처리가 똑바로 안된 것 같음.


# 느낀점
"""

"""
