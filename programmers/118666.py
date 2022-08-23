def solution(survey, choices):
    types = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(survey)):
        if choices[i] < 4:
            types[survey[i][0]] += abs(4 - choices[i])
        else:
            types[survey[i][1]] += abs(4 - choices[i])
            
    result = ''
    result += 'R' if types['R'] >= types['T'] else 'T'
    result += 'C' if types['C'] >= types['F'] else 'F'
    result += 'J' if types['J'] >= types['M'] else 'M'
    result += 'A' if types['A'] >= types['N'] else 'N'
    
    return result
