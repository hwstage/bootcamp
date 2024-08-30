arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# 주어진 문자열이 정수인지 아닌지 판단
def judge(x):
    # 주어진 문자열이 음수일 경우 -가 0번째 인덱스로 오기때문에 이를 체크
    if x[0] == '-':
        for i in x[1:]:
            if i not in arr:
                return False
    else:
        for i in x:
            if i not in arr:
                return False
    return True

def comma(x):
    if judge(x):
        # 주어진 숫자가 음수일 경우, -를 제외한 숫자에 콤마를 붙이고, -를 앞에 붙임
        if x[0] == '-':
            return '-' + comma(x[1:])
        else:
            # 콤마를 붙이는 부분으로, 문자열을 뒤집은 후 3번째 인덱스마다 ,를 삽입
            reversedx = x[::-1]
            parts = [reversedx[i:i+3] for i in range(0, len(reversedx), 3)]
        return ','.join(parts)[::-1]
    return "에러임"

def main():
    n = int(input())
    for i in range(n):
        m = input()
        print(f'결과 : {comma(m)}')

if __name__ == "__main__":
   print(main())
