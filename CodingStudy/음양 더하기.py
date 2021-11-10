def solution(absolutes, signs): 
  answer = 0 
  for i in range(len(absolutes)): 
    minus = 1 
    if not signs[i]: 
      minus = -1 
      
    answer += minus * absolutes[i] 
    
  return answer
