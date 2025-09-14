#include <stdio.h>

#define N 3 // 부분집합을 만들 집합의 원소 개수

int subset[N]; // 현재 부분집합을 저장하는 배열

// 부분집합 출력 함수
void print_subset(int size)
{
    printf("{ ");
    for (int i = 0; i < size; i++)
    {
        printf("%d ", subset[i]);
    }
    printf("}\n");
}

// 재귀 탐색 함수
void search(int k, int idx)
{
    if (k > N)
    {
        // 종료 조건: 1 ~ N까지 포함 여부를 다 정했을 때
        print_subset(idx);
    }
    else
    {
        // 1. k를 포함하는 경우
        subset[idx] = k;
        search(k + 1, idx + 1);

        // 2. k를 포함하지 않는 경우
        search(k + 1, idx);
    }
}

int main()
{
    search(1, 0); // 1부터 시작, 현재 subset 크기 0
    return 0;
}
