import sys

def LCS(str1, str2):
    """
    두 문자열의 최장 공통 부분 수열 길이를 계산하는 함수입니다.
    Args :
        str1 -> 첫번째 문자열
        str2 -> 두번쨰 문자열
    Return:
        int: LCS길이
    """
    len1 = len(str1)
    len2 = len(str2)

    dp = [[0] * (len2+1) for _ in range(len1+1)]

    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if(str1[i-1] == str2[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[len1][len2]
if __name__ == "__main__":
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()

    result = LCS(str1, str2)

    print(result)


