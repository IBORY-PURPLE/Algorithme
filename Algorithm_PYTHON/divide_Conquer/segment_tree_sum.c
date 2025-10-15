#include <stdio.h> // 표준 입출력 헤더

#define MAX_N 100                           // 원본 배열 A의 최대 크기
int tree[4 * MAX_N];                        // 세그먼트 트리를 저장할 배열(여유분 4배)
int A[MAX_N] = {0, 5, 4, 2, 6, 9, 1, 4, 3}; // 1번 인덱스부터 사용: A[1..8]

// [l..r] 구간을 트리의 노드 i에 빌드하여 합을 tree[i]에 저장
int build(int l, int r, int i)
{ // l: 구간 왼쪽, r: 구간 오른쪽, i: 트리 노드 인덱스
    if (l == r)
    {                   // 리프(원소 하나)까지 내려온 경우
        tree[i] = A[l]; // 그 원소 값을 그대로 저장
        return tree[i]; // 상위로 합을 되돌려줌
    }

    int m = (l + r) / 2;                   // 중간 지점(좌/우로 분할)
    int sol1 = build(l, m, 2 * i);         // 왼쪽 자식(인덱스 2*i)에 [l..m] 빌드
    int sol2 = build(m + 1, r, 2 * i + 1); // 오른쪽 자식(2*i+1)에 [m+1..r] 빌드

    tree[i] = sol1 + sol2; // 현재 노드의 값 = 왼쪽 합 + 오른쪽 합
    return tree[i];        // 계산된 합을 상위로 반환
}

int main(void)
{
    int n = 8;      // 실제 사용할 원소 개수(A[1]..A[8])
    build(1, n, 1); // 루트 노드(1)부터 [1..n] 구간을 빌드

    // 트리 배열의 앞부분을 간단히 출력(루트~깊이 3 수준 확인용)
    for (int i = 1; i < 2 * n; i++)
    {                           // 관례적으로 1..(2n-1) 정도까지 보면 충분
        printf("%d ", tree[i]); // 각 노드에 저장된 구간 합
    }
    printf("\n");
    return 0; // 정상 종료
}
