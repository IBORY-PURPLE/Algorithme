#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int index; // 작업 번호 (1-based)
    int T;     // 작업 소요 시간
    int S;     // 벌금 (per day)
} Job;

// 비교 함수: S/T 비율이 높은 순서대로 정렬
int compare(const void *a, const void *b)
{
    Job *j1 = (Job *)a;
    Job *j2 = (Job *)b;

    // 두 작업의 S/T 비교 (실수 대신 교차곱 사용)
    long long lhs = (long long)j1->S * j2->T;
    long long rhs = (long long)j2->S * j1->T;

    if (lhs > rhs)
        return -1; // j1 먼저 (S/T 더 큼)
    else if (lhs < rhs)
        return 1; // j2 먼저
    else
    {
        // 비율이 같다면 인덱스가 작은 순으로
        if (j1->index < j2->index)
            return -1;
        else if (j1->index > j2->index)
            return 1;
        else
            return 0;
    }
}

int main()
{
    int N;
    scanf("%d", &N);

    Job jobs[1000];

    for (int i = 0; i < N; i++)
    {
        scanf("%d %d", &jobs[i].T, &jobs[i].S);
        jobs[i].index = i + 1; // 작업 번호 저장
    }

    // Smith’s rule 정렬
    qsort(jobs, N, sizeof(Job), compare);

    // 출력
    for (int i = 0; i < N; i++)
    {
        printf("%d", jobs[i].index);
        if (i != N - 1)
            printf(" ");
    }
    printf("\n");

    return 0;
}
    