/* --- 1. 접두사(Prefix) 방식 코드 (이미지 기반) ---
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int max(int a, int b) { return (a > b) ? a : b; }

void lcs_prefix(char *X, char *Y)
{
    int m = strlen(X);
    int n = strlen(Y);
    int table[m + 1][n + 1];

    // [차이점 1] 기본 사례: 첫 행과 첫 열을 0으로 초기화
    // 빈 접두사와의 LCS 길이는 0이기 때문
    for (int i = 0; i <= m; i++)
        table[i][0] = 0;
    for (int j = 0; j <= n; j++)
        table[0][j] = 0;

    // [차이점 2] 반복문 방향: 1부터 m, 1부터 n까지 정방향으로 진행
    for (int i = 1; i <= m; i++)
    {
        for (int j = 1; j <= n; j++)
        {

            // [차이점 3] 문자 비교: X[i-1], Y[j-1] 비교 (현재 접두사의 마지막 문자)
            if (X[i - 1] == Y[j - 1])
            {
                // 대각선 왼쪽 위(이전 접두사) 값 + 1
                table[i][j] = 1 + table[i - 1][j - 1];
            }
            else
            {
                // 위쪽 값과 왼쪽 값 중 더 큰 값
                table[i][j] = max(table[i - 1][j], table[i][j - 1]);
            }
        }
    }

    // [차이점 4] 최종 결과: 테이블의 가장 오른쪽 아래에 저장됨
    printf("[접두사 방식] LCS의 길이는 %d 입니다.\n", table[m][n]);
}

*/