def solution(string):
    ret = ""
    for c in string:
        ret = c + ret;
    return ret

print(solution('world'))