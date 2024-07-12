def printResult(scores,  total):
    n = len(scores)
    print(total)
    print(scores)
    print(total / n)

def main():
    scores = []
    n = int(input("학생 수를 입력하세요: "))
    
    total = 0
    
    for i in range(0, n):
        jumsu = int(input("[%d] 영어시험 성적: " % (i+1)))
        total += jumsu
        scores.append(jumsu)
    
    printResult(scores, total)

main()  
