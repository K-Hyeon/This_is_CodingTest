def solution(str1, str2):
    
    str1=str1.lower(); str2=str2.lower()

    str1_=[]
    for i in range(len(str1)):
        word=str1[i:i+2]
        if word.isalpha() and len(word)==2:
            str1_.append(word)
    str2_=[]        
    for i in range(len(str2)):
        word=str2[i:i+2]
        if word.isalpha() and len(word)==2:
            str2_.append(word)   
            
    if len(str2_)==0: 
        return int(65536)
    
    n=0
    for i in str1_:
        if i in str2_: 
            str2_.remove(i); n+=1

    return int(n/len(str1_+str2_)*65536)
