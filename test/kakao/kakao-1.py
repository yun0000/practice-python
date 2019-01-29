record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    answer = []
    slicedRecord = []
    idAndName = {}
    for i in range(len(record)):
        eachList = record[i].split(" ")
        if eachList[0] == "Enter" or eachList[0] == "Change":
            idAndName[eachList[1]] = eachList[2]    
        slicedRecord.append(eachList)

    for i in range(len(record)):
        eachList = record[i].split(" ")
        if eachList[0] == "Enter":
            answer.append(idAndName[slicedRecord[i][1]]+"님이 들어왔습니다.")                                 
                                  
        elif eachList[0] == "Leave":
            answer.append(idAndName[slicedRecord[i][1]]+"님이 나갔습니다.")                                
    return answer

print(solution(record))

#다른 답안 참고하기
