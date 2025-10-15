#include <stdio.h>
#include <stdlib.h> // malloc, free 함수를 사용하기 위해 필요

// 두 개의 정렬된 부분 배열을 병합하는 함수
// 왼쪽 부분 배열: arr[left...mid]
// 오른쪽 부분 배열: arr[mid+1...right]
void merge(int arr[], int left, int mid, int right)
{
    int i, j, k;
    int n1 = mid - left + 1; // 왼쪽 부분 배열의 크기
    int n2 = right - mid;    // 오른쪽 부분 배열의 크기

    // 임시 배열을 동적으로 할당합니다.
    int *L = (int *)malloc(n1 * sizeof(int));
    int *R = (int *)malloc(n2 * sizeof(int));

    // 데이터를 임시 배열 L[]과 R[]에 복사합니다.
    for (i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    // --- Python의 merge 함수 로직과 동일 ---
    i = 0;    // L[]의 초기 인덱스
    j = 0;    // R[]의 초기 인덱스
    k = left; // 병합될 주 배열(arr)의 초기 인덱스

    // 두 임시 배열의 원소를 비교하며 주 배열에 정렬하여 삽입합니다.
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // L[] 또는 R[]에 남아있는 원소들을 복사합니다.
    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }
    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }

    // 동적으로 할당한 메모리를 해제합니다.
    free(L);
    free(R);
}

// 주어진 배열 arr의 left부터 right까지를 병합 정렬하는 함수
void mergeSort(int arr[], int left, int right)
{
    // Base Case: 원소가 1개인 경우 (left >= right)
    if (left < right)
    {
        // 분할 (Divide)
        // 오버플로우를 방지하기 위해 (left+right)/2 대신 사용
        int mid = left + (right - left) / 2;

        // 정복 (Conquer)
        // 재귀적으로 두 부분으로 나누어 각각 정렬합니다.
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        // 결합 (Combine)
        // 정렬된 두 부분을 병합합니다.
        merge(arr, left, mid, right);
    }
}

// 배열을 출력하는 유틸리티 함수
void printArray(int A[], int size)
{
    for (int i = 0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}

// --- 실행 예시 (main 함수) ---
int main()
{
    // 슬라이드 6의 예시 데이터
    int my_list[] = {38, 27, 43, 3, 9, 82, 10};
    int arr_size = sizeof(my_list) / sizeof(my_list[0]);

    printf("Original list: ");
    printArray(my_list, arr_size);

    // 병합 정렬 호출 (시작 인덱스 0, 마지막 인덱스 arr_size - 1)
    mergeSort(my_list, 0, arr_size - 1);

    printf("Sorted list:   ");
    printArray(my_list, arr_size);

    printf("\n");

    // 다른 예시
    int my_list_2[] = {5, 2, 8, 1, 9, 4};
    int arr_size_2 = sizeof(my_list_2) / sizeof(my_list_2[0]);

    printf("Original list: ");
    printArray(my_list_2, arr_size_2);

    mergeSort(my_list_2, 0, arr_size_2 - 1);

    printf("Sorted list:   ");
    printArray(my_list_2, arr_size_2);

    return 0;
}
