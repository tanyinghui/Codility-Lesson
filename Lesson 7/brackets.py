check = {
    '(': ')',
    '{': '}',
    '[': ']'
    }

def solution(S):
    if len(S) == 0:
        return 1
    pairs = []
    for e in S:
        if e in check.values():
            if pairs and check[pairs[-1]] == e:
                pairs.pop()
            else:
                return 0
        else:
            pairs.append(e)
    return 1 if not pairs else 0