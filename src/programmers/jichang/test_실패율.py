# 실패율 https://programmers.co.kr/learn/courses/30/lessons/42889
def failure_rate(N, stages):
    """스테이지의 수 N과 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 주어질 때, 실패율이 높은 스테이지부터
    내림차순으로 스테이지의 번호가 담겨있는 배열을 구한다.
    시간 복잡도:

    """
    stages_dict = {'total': 0}
    failure_rating = {}

    for index in stages:
        try:
            stages_dict[index] += 1
        except:
            stages_dict[index] = 1
        stages_dict['total'] += 1

    for index in range(1, N+1):
        try:
            failure_rating[index] = (stages_dict[index] / stages_dict['total'])
            stages_dict['total'] -= stages_dict[index]
        except:
            failure_rating[index] = 0

    answer = []
    
    for key in sorted(failure_rating.items(), key=lambda failure_rating: failure_rating[1], reverse=True):
        answer.append(key[0])
    return answer


def test_failure_rate():
    assert failure_rate(5, [2, 1, 2, 6, 2, 4, 3, 3]) == [3, 4, 2, 1, 5]
    assert failure_rate(4, [4, 4, 4, 4, 4]) == [4, 1, 2, 3]