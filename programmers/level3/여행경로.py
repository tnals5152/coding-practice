from collections import deque
import copy
def solution(tickets):
    answer = []
    """
    tickets_dict = {
        "ICN": ["JFK", ...], #start1: [destination1, ...],
    }
    """
    tickets_dict = dict()
    que = deque()
    total_count = len(tickets) + 1
    
    
    for ticket in tickets:
        if not tickets_dict.get(ticket[0]):
            tickets_dict[ticket[0]] = [ticket[1]]
        else:
            tickets_dict[ticket[0]].append(ticket[1])
    
    
    for i, ticket in enumerate(tickets_dict["ICN"]):
        if tickets_dict.get(ticket):#다음이 없으면 끝 -> 마지막이므로 넣지 않음
            copy_dict = copy.deepcopy(tickets_dict)
            if len(copy_dict["ICN"]) > 1:
                del copy_dict["ICN"][i]
            else:
                del copy_dict["ICN"]
            que.append((["ICN", ticket], copy_dict, 2))

    
    while que:
        visited, not_visited_dict, count = que.popleft()
        if count >= total_count:
            answer.append(visited)
            continue
        
        now = visited[-1]
        
        for i, ticket in enumerate(not_visited_dict[now]):
            if not_visited_dict.get(ticket):
                copy_dict = copy.deepcopy(not_visited_dict)
                if len(copy_dict[now]) > 1:
                    del copy_dict[now][i]
                else:
                    del copy_dict[now]
                que.append((visited + [ticket], copy_dict, count + 1))
            else:#마지막일 경우
                if count == total_count - 1:
                # if len(not_visited_dict.keys()) <= 1:
                    que.append((visited + [ticket], dict(), count + 1))
    

    return sorted(answer)[0]
