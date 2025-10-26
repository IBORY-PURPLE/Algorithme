//  --- 2. 접미사(Suffix) 방식 코드 (우리의 구현) ---
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// int max(int a, int b) { return (a > b) ? a : b; }

void lcs_suffix(char *X, char *Y)
{
    int m = strlen(X);
    int n = strlen(Y);
    int table[m + 1][n + 1];

    // [차이점 1] 기본 사례: 마지막 행과 마지막 열을 0으로 초기화
    // 빈 접미사와의 LCS 길이는 0이기 때문
    for (int j = 0; j <= n; j++)
        table[m][j] = 0;
    for (int i = 0; i <= m; i++)
        table[i][n] = 0;

    // [차이점 2] 반복문 방향: m-1부터 0, n-1부터 0까지 역방향으로 진행
    for (int i = m - 1; i >= 0; i--)
    {
        for (int j = n - 1; j >= 0; j--)
        {

            // [차이점 3] 문자 비교: X[i], Y[j] 비교 (현재 접미사의 시작 문자)
            if (X[i] == Y[j])
            {
                // 대각선 오른쪽 아래(다음 접미사) 값 + 1
                table[i][j] = 1 + table[i + 1][j + 1];
            }
            else
            {
                // 아래쪽 값과 오른쪽 값 중 더 큰 값
                table[i][j] = max(table[i + 1][j], table[i][j + 1]);
            }
        }
    }

    // [차이점 4] 최종 결과: 테이블의 가장 왼쪽 위에 저장됨
    printf("[접미사 방식] LCS의 길이는 %d 입니다.\n", table[0][0]);
}