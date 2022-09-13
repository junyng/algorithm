def solution(dartResult):
    bonus = {
        "S": 1, 
        "D": 2, 
        "T": 3
    }
    
    options = {
        "*": 2, 
        "#": -1
    }
    
    results = []
    
    index = 0
    
    while index < len(dartResult):
        result = 0
        number = int(dartResult[index])
        
        if index+1 < len(dartResult):
            if dartResult[index+1] == '0':
                number = 10
                index += 1
            
            result = pow(number, bonus[dartResult[index+1]])
            index += 2
            
            if index < len(dartResult) and dartResult[index] in options:
                result = result * options[dartResult[index]]
                
                if results and dartResult[index] == "*":
                    results[-1] *= 2
                
                index += 1
        
        results.append(result)
        
    return sum(results)
