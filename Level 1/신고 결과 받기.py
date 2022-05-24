def solution(id_list, report, k):
    report_dict = dict()
    answer = [0 for i in id_list]
    for i in report:
        repoter, report_p = i.split()
        report_dict[report_p] = report_dict.get(report_p, set()) | {repoter}
    for repoters in report_dict.values():
        if len(repoters) >= k:
            for repoter in repoters:
                answer[id_list.index(repoter)] += 1
    return answer

# URL : https://programmers.co.kr/learn/courses/30/lessons/92334
# 문제를 요약하면 report를 받아서 중복을 제거한 report의 수가 k 이상이면 신고한 신고자에게 처리 결과를 말해주면 됩니다.
# 일단 먼저 report에서 중복을 제거해야하며, 파이썬에서는 중복과 관련된 처리를 빠르게 할 수 있는 `set` 타입을 지원합니다.
# 해당 아래의 `6 Line`에서 처리하는 것을 확인할 수 있습니다.
# 또한 신고한 사람이 k 이상인지 확인하기 위해 `8 Line`에서 체크하는 것을 확인할 수 있습니다.
# 마지막으로 k 이상이라면 처리 결과를 말해야하기 때문에 `10 Line`에서 처리하는 것을 확인할 수 있습니다.