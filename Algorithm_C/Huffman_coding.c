// #include <stdio.h>
// #include <stdlib.h>
// #include <string.h>

// // --- 1. 자료구조 정의 ---

// // Python의 (심볼, 빈도수) 딕셔너리를 대체할 구조체
// typedef struct
// {
//     char symbol;   // 문자 (심볼)
//     int frequency; // 빈도수
// } SymbolFreq;

// // 최소 힙(Min-Heap)에 저장될 노드 구조체
// typedef struct
// {
//     int frequency; // 노드의 가중치 (빈도수 합)
//     int index;     // 노드의 인덱스 (리프 노드 또는 내부 노드)
// } MinHeapNode;

// // 허프만 트리의 간선(edge) 정보를 저장할 구조체
// // Python 코드의 self.edges 리스트 역할을 합니다.
// typedef struct
// {
//     int parent_index; // 부모 노드의 인덱스
//     int bit;          // 부모로 가는 경로의 비트 (0 또는 1)
// } HuffmanEdge;

// // --- 2. 최소 힙(Min-Heap) 구현 ---
// // 허프만 트리 생성을 위해 우선순위 큐로 사용됩니다.

// // 힙의 두 노드를 교환하는 함수
// void swapMinHeapNode(MinHeapNode *a, MinHeapNode *b)
// {
//     MinHeapNode temp = *a;
//     *a = *b;
//     *b = temp;
// }

// // 최소 힙 속성을 유지하기 위한 함수 (Heapify)
// void minHeapify(MinHeapNode heap[], int size, int i)
// {
//     int smallest = i;
//     int left = 2 * i + 1;
//     int right = 2 * i + 2;

//     if (left < size && heap[left].frequency < heap[smallest].frequency)
//         smallest = left;

//     if (right < size && heap[right].frequency < heap[smallest].frequency)
//         smallest = right;

//     if (smallest != i)
//     {
//         swapMinHeapNode(&heap[i], &heap[smallest]);
//         minHeapify(heap, size, smallest);
//     }
// }

// // 힙에서 최소 빈도수를 가진 노드를 추출하는 함수
// MinHeapNode extractMin(MinHeapNode heap[], int *size)
// {
//     MinHeapNode temp = heap[0];
//     heap[0] = heap[*size - 1];
//     (*size)--;
//     minHeapify(heap, *size, 0);
//     return temp;
// }

// // 힙에 새로운 노드를 삽입하는 함수
// void insertMinHeap(MinHeapNode heap[], int *size, MinHeapNode newNode)
// {
//     (*size)++;
//     int i = *size - 1;
//     heap[i] = newNode;

//     // 부모 노드와 비교하며 힙 속성을 만족할 때까지 위로 이동
//     while (i != 0 && heap[(i - 1) / 2].frequency > heap[i].frequency)
//     {
//         swapMinHeapNode(&heap[i], &heap[(i - 1) / 2]);
//         i = (i - 1) / 2;
//     }
// }

// // --- 3. 허프만 인코더 구현 ---

// // 허프만 트리를 생성하는 메인 함수
// HuffmanEdge *buildHuffmanTree(SymbolFreq freq_pairs[], int num_symbols)
// {
//     // 총 노드의 개수: (리프 노드 수) + (내부 노드 수) = n + (n-1) = 2n-1
//     // 리프 노드 인덱스 0~n-1 부모노드 인덱스 시작값 n~2n-2
//     int total_nodes = 2 * num_symbols - 1;

//     // 간선 정보를 저장할 배열을 동적으로 할당합니다.
//     HuffmanEdge *edges = (HuffmanEdge *)malloc(total_nodes * sizeof(HuffmanEdge));

//     // 최소 힙으로 사용할 노드 배열을 생성합니다.
//     MinHeapNode *frontier = (MinHeapNode *)malloc(num_symbols * sizeof(MinHeapNode));
//     int heap_size = 0;

//     // 초기 리프 노드들을 최소 힙에 삽입합니다.
//     for (int i = 0; i < num_symbols; ++i)
//     {
//         MinHeapNode node = {freq_pairs[i].frequency, i};
//         insertMinHeap(frontier, &heap_size, node);
//     }

//     // 다음 내부 노드에 할당될 인덱스 (리프 노드 다음부터 시작)
//     int next_node_index = num_symbols;

//     // 힙에 노드가 하나만 남을 때까지(루트 노드) 반복합니다.
//     while (heap_size > 1)
//     {
//         // 가장 작은 가중치를 가진 두 노드를 꺼냅니다.
//         MinHeapNode child1 = extractMin(frontier, &heap_size);
//         MinHeapNode child2 = extractMin(frontier, &heap_size);

//         // 새 부모 노드를 생성합니다.
//         int parent_index = next_node_index++;
//         MinHeapNode parent_node = {child1.frequency + child2.frequency, parent_index};

//         // 두 자식 노드의 edge 정보를 기록합니다. (부모 인덱스, 비트)
//         // Python의 False -> C의 0, True -> 1
//         edges[child1.index].parent_index = parent_index;
//         edges[child1.index].bit = 0; // 왼쪽 자식은 0

//         edges[child2.index].parent_index = parent_index;
//         edges[child2.index].bit = 1; // 오른쪽 자식은 1

//         // 새 부모 노드를 다시 힙에 추가합니다.
//         insertMinHeap(frontier, &heap_size, parent_node);
//     }

//     free(frontier); // 힙 메모리 해제
//     return edges;   // 생성된 트리(간선 정보) 반환
// }

// // 특정 심볼의 허프만 코드를 찾아 출력하는 함수
// void getHuffmanCode(char symbol, SymbolFreq freq_pairs[], int num_symbols, HuffmanEdge edges[])
// {
//     int symbol_index = -1;
//     // 입력된 심볼에 해당하는 인덱스를 찾습니다.
//     for (int i = 0; i < num_symbols; ++i)
//     {
//         if (freq_pairs[i].symbol == symbol)
//         {
//             symbol_index = i;
//             break;
//         }
//     }

//     if (symbol_index == -1)
//     {
//         printf("'%c'는(은) 사전에 없는 심볼입니다.\n", symbol);
//         return;
//     }

//     // 코드를 역순으로 저장할 배열
//     int code_reverse[100]; // 코드 최대 길이를 100으로 가정
//     int code_len = 0;

//     int current_node = symbol_index;
//     int root_node = 2 * num_symbols - 2;

//     // 리프 노드에서 루트 노드로 올라가면서 비트를 기록합니다.
//     while (current_node != root_node)
//     {
//         code_reverse[code_len++] = edges[current_node].bit;
//         current_node = edges[current_node].parent_index;
//     }

//     // 역순으로 저장된 코드를 올바른 순서로 출력합니다.
//     printf("심볼 '%c' : ", symbol);
//     for (int i = code_len - 1; i >= 0; --i)
//     {
//         printf("%d", code_reverse[i]);
//     }
//     printf("\n");
// }

// // --- 4. 메인 함수 (실행 예제) ---
// int main()
// {
//     // Python의 딕셔너리 대신 구조체 배열을 사용합니다.
//     SymbolFreq frequencies[] = {
//         {'a', 45}, {'b', 13}, {'c', 12}, {'d', 16}, {'e', 9}, {'f', 5}};
//     // 심볼의 총 개수를 계산합니다.
//     int num_symbols = sizeof(frequencies) / sizeof(frequencies[0]);

//     // 허프만 트리를 생성하고 간선 정보를 받습니다.
//     HuffmanEdge *huffman_edges = buildHuffmanTree(frequencies, num_symbols);

//     printf("--- 허프만 인코딩 테이블 ---\n");
//     // 모든 심볼에 대해 허프만 코드를 찾아 출력합니다.
//     for (int i = 0; i < num_symbols; ++i)
//     {
//         getHuffmanCode(frequencies[i].symbol, frequencies, num_symbols, huffman_edges);
//     }

//     printf("\n--- 특정 심볼 조회 ---\n");
//     getHuffmanCode('c', frequencies, num_symbols, huffman_edges);

//     // 동적으로 할당된 메모리를 반드시 해제해야 합니다.
//     free(huffman_edges);

//     return 0;
// }

#include <stdio.h>
#include <stdlib.h>

// --- 1. 자료구조 정의 ---

// 최소 힙(Min-Heap)에 저장될 노드 구조체
// Python 코드의 frontier 리스트에 저장되는 (weight, index) 튜플에 해당합니다.
typedef struct
{
    double probability; // 노드의 가중치 (확률 또는 확률의 합)
    int index;          // 노드의 인덱스 (0 ~ n-1: 리프 노드, n ~ 2n-2: 내부 노드)
} MinHeapNode;

// 허프만 트리의 간선(edge) 정보를 저장할 구조체
// Python 코드의 self.edges 리스트 역할을 합니다.
typedef struct
{
    int parent_index; // 부모 노드의 인덱스
    int bit;          // 부모로 가는 경로의 비트 (0 또는 1)
} HuffmanEdge;

// --- 2. 최소 힙(Min-Heap) 구현 ---
// 허프만 트리 생성을 위해 우선순위 큐로 사용됩니다.

// 힙의 두 노드를 교환하는 함수
void swapMinHeapNode(MinHeapNode *a, MinHeapNode *b)
{
    MinHeapNode temp = *a;
    *a = *b;
    *b = temp;
}

// 최소 힙 속성을 유지하기 위한 함수 (Heapify)
// i를 루트로 하는 서브트리가 힙 속성을 만족하도록 조정합니다.
void minHeapify(MinHeapNode heap[], int size, int i)
{
    int smallest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    // 왼쪽 자식이 현재 노드보다 작으면 smallest를 왼쪽 자식 인덱스로 변경
    if (left < size && heap[left].probability < heap[smallest].probability)
        smallest = left;

    // 오른쪽 자식이 현재 smallest 노드보다 작으면 smallest를 오른쪽 자식 인덱스로 변경
    if (right < size && heap[right].probability < heap[smallest].probability)
        smallest = right;

    // smallest가 원래 노드가 아니라면, 두 노드를 교환하고 재귀적으로 호출
    if (smallest != i)
    {
        swapMinHeapNode(&heap[i], &heap[smallest]);
        minHeapify(heap, size, smallest);
    }
}

// 힙에서 최소 확률을 가진 노드를 추출하는 함수
MinHeapNode extractMin(MinHeapNode heap[], int *size)
{
    MinHeapNode temp = heap[0]; // 루트 노드가 최소값
    heap[0] = heap[*size - 1];  // 마지막 노드를 루트로 가져옴
    (*size)--;                  // 힙 크기 감소
    minHeapify(heap, *size, 0); // 루트에서부터 힙 속성을 복원
    return temp;
}

// 힙에 새로운 노드를 삽입하는 함수
void insertMinHeap(MinHeapNode heap[], int *size, MinHeapNode newNode)
{
    (*size)++;
    int i = *size - 1;
    heap[i] = newNode;

    // 부모 노드와 비교하며 힙 속성을 만족할 때까지 위로 이동
    while (i != 0 && heap[(i - 1) / 2].probability > heap[i].probability)
    {
        swapMinHeapNode(&heap[i], &heap[(i - 1) / 2]);
        i = (i - 1) / 2;
    }
}

// --- 3. 허프만 인코더 구현 ---

// 허프만 트리를 생성하는 메인 함수
HuffmanEdge *buildHuffmanTree(const double probabilities[], int num_symbols)
{
    // 총 노드의 개수는 (리프 노드 수) + (내부 노드 수) = n + (n-1) = 2n-1 입니다.
    int total_nodes = 2 * num_symbols - 1;
    // 이 노드들의 간선 정보를 저장할 배열을 동적으로 할당합니다.
    // 2n-2로 만들어도 된다. -> 엣지 리스트는 각 노드들의 부모에 대한 정보를 넣기 때문에
    // 마지막 루트노드의 인덱스인 2n-2에서는 부모가 없어서 저장할 필요가 없기 때문이다.
    HuffmanEdge *edges = (HuffmanEdge *)malloc(total_nodes * sizeof(HuffmanEdge));

    // 최소 힙으로 사용할 노드 배열을 생성합니다.
    MinHeapNode *frontier = (MinHeapNode *)malloc(num_symbols * sizeof(MinHeapNode));
    int heap_size = 0; // 현재 힙에 들어있는 노드의 개수

    // 초기 리프 노드들을 최소 힙에 삽입합니다.
    // 리프 노드들을 최소 힙에 넣음으로써 트리 구조의 리프라고 정의한 것이기 때문에
    // 따로 위치를 저장할 필요없음 그저 리프의 부모노드 인덱스를 알기만 하면 됨.
    for (int i = 0; i < num_symbols; ++i)
    {
        MinHeapNode node = {probabilities[i], i};
        insertMinHeap(frontier, &heap_size, node);
    }

    // 다음 내부 노드에 할당될 인덱스 (리프 노드 인덱스 다음부터 시작)
    int next_node_index = num_symbols;

    // 힙에 노드가 하나만 남을 때까지(루트 노드) 반복합니다.
    while (heap_size > 1)
    {
        // 가장 작은 확률을 가진 두 노드를 힙에서 꺼냅니다.
        MinHeapNode child1 = extractMin(frontier, &heap_size);
        MinHeapNode child2 = extractMin(frontier, &heap_size);

        // 부모 인덱스 n 대입후에 ++연산 진행한다.
        int parent_index = next_node_index++;
        // 부모 노드의 확률은 두 자식 노드 확률의 합입니다.
        MinHeapNode parent_node = {child1.probability + child2.probability, parent_index};

        // 두 자식 노드의 edge 정보를 기록합니다. (부모 인덱스, 비트)
        // Python의 False는 C의 0, True는 1에 해당합니다.
        edges[child1.index].parent_index = parent_index;
        edges[child1.index].bit = 0; // 첫 번째(더 작은) 자식은 왼쪽(0)

        edges[child2.index].parent_index = parent_index;
        edges[child2.index].bit = 1; // 두 번째 자식은 오른쪽(1)

        // 생성된 새 부모 노드를 다시 힙에 추가합니다.
        insertMinHeap(frontier, &heap_size, parent_node);
    }

    free(frontier); // 힙 생성에 사용된 메모리를 해제합니다.
    return edges;   // 완성된 트리(간선 정보)의 포인터를 반환합니다.
}

// 특정 심볼(인덱스)의 허프만 코드를 찾아 출력하는 함수
void printHuffmanCode(int symbol_index, int num_symbols, const HuffmanEdge edges[])
{
    // 코드를 역순으로 저장할 임시 배열 (경로가 길지 않으므로 100 정도면 충분)
    int code_reverse[100];
    int code_len = 0;

    int current_node = symbol_index;
    // 루트 노드의 인덱스는 항상 마지막으로 생성된 노드인 2n-2 입니다.
    int root_node = 2 * num_symbols - 2;

    // 심볼이 하나만 있는 예외적인 경우
    if (num_symbols == 1)
    {
        printf("심볼 %d (확률: ...): 0\n", symbol_index);
        return;
    }

    // 현재 노드가 루트 노드가 될 때까지 부모를 따라 올라갑니다.
    while (current_node != root_node)
    {
        // 경로의 비트를 역순 코드 배열에 저장합니다.
        code_reverse[code_len++] = edges[current_node].bit;
        // 현재 노드를 부모 노드로 이동시킵니다.
        current_node = edges[current_node].parent_index;
    }

    // 심볼 정보와 함께 코드를 출력합니다.
    printf("심볼 %d ", symbol_index);
    // 역순으로 저장된 코드를 올바른 순서(루트->리프)로 출력합니다.
    for (int i = code_len - 1; i >= 0; --i)
    {
        printf("%d", code_reverse[i]);
    }
    printf("\n");
}

// --- 4. 메인 함수 (실행 예제) ---
int main()
{
    // Python 예제와 동일한 확률 리스트
    double probabilities[] = {0.3, 0.28, 0.12, 0.1, 0.2};
    // 심볼의 총 개수를 계산합니다.
    int num_symbols = sizeof(probabilities) / sizeof(probabilities[0]);

    // 허프만 트리를 생성하고 간선 정보를 받습니다.
    HuffmanEdge *huffman_edges = buildHuffmanTree(probabilities, num_symbols);

    printf("--- 허프만 인코딩 테이블 ---\n");
    // 모든 심볼(인덱스 0부터 n-1)에 대해 허프만 코드를 찾아 출력합니다.
    for (int i = 0; i < num_symbols; ++i)
    {
        // 확률 정보도 함께 출력하기 위해 probabilities 배열을 참조합니다.
        printf("(확률: %.2f) ", probabilities[i]);
        printHuffmanCode(i, num_symbols, huffman_edges);
    }

    // 동적으로 할당된 메모리를 반드시 해제해야 합니다.
    free(huffman_edges);

    return 0;
}