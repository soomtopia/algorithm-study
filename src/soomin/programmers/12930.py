
# 이상한 문자 만들기 
def solution(s):
    answer = []
    i = 0
    for token in s:
        if token == ' ':
            i = 0
            answer += token
        else:
            if i % 2 == 0:
                answer.append(token.upper())
            else:
                answer.append(token.lower())
            i += 1
    return "".join(answer)
# 테스트 1 〉	통과 (0.05ms, 10.6MB)
# 테스트 2 〉	통과 (0.04ms, 10.7MB)
# 테스트 3 〉	통과 (0.04ms, 10.6MB)
# 테스트 4 〉	통과 (0.06ms, 10.7MB)
# 테스트 5 〉	통과 (0.07ms, 10.7MB)
# 테스트 6 〉	통과 (0.04ms, 10.6MB)
# 테스트 7 〉	통과 (0.04ms, 10.7MB)
# 테스트 8 〉	통과 (0.06ms, 10.7MB)
# 테스트 9 〉	통과 (0.05ms, 10.7MB)
# 테스트 10 〉	통과 (0.09ms, 10.7MB)
# 테스트 11 〉	통과 (0.06ms, 10.6MB)
# 테스트 12 〉	통과 (0.06ms, 10.7MB)
# 테스트 13 〉	통과 (0.07ms, 10.7MB)
# 테스트 14 〉	통과 (0.04ms, 10.6MB)
# 테스트 15 〉	통과 (0.05ms, 10.6MB)
# 테스트 16 〉	통과 (0.06ms, 10.7MB)