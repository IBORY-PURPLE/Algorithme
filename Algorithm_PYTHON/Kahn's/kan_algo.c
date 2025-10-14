#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// --- 상수 및 전역 변수 정의 ---
#define NUM_VERTICES 6 // 정점의 개수 (A, B, C, D, E, F)

// 정점 이름을 인덱스로, 인덱스를 이름으로 변환하기 위한 배열
// A=0, B=1, C=2, D=3, E=4, F=5
const char *vertex_names[NUM_VERTICES] = {"A", "B", "C", "D", "E", "F"};

// --- 자료구조 정의 ---

// 1. 그래프의 인접 리스트를 위한 노드 구조체
typedef struct AdjListNode
{
    int dest;                 // 목적지 정점의 인덱스
    struct AdjListNode *next; // 다음 이웃 노드를 가리키는 포인터
} AdjListNode;

// 2. 그래프 구조체
typedef struct Graph
{
    int numVertices;        // 그래프의 정점 수
    AdjListNode **adjLists; // 각 정점의 인접 리스트 (헤드 포인터 배열)
} Graph;

// 3. 큐(Queue) 구조체
typedef struct Queue
{
    int items[NUM_VERTICES];
    int front;
    int rear;
} Queue;

// --- 헬퍼 함수 (그래프 및 큐 생성/관리) ---

// 새로운 인접 리스트 노드를 생성하는 함수
AdjListNode *createAdjListNode(int dest)
{
    AdjListNode *newNode = (AdjListNode *)malloc(sizeof(AdjListNode));
    newNode->dest = dest;
    newNode->next = NULL;
    return newNode;
}

// 그래프를 생성하고 초기화하는 함수
Graph *createGraph(int vertices)
{
    Graph *graph = (Graph *)malloc(sizeof(Graph));
    graph->numVertices = vertices;
    graph->adjLists = (AdjListNode **)malloc(vertices * sizeof(AdjListNode *));

    for (int i = 0; i < vertices; i++)
    {
        graph->adjLists[i] = NULL;
    }
    return graph;
}

// 그래프에 간선(edge)을 추가하는 함수 (src -> dest)
void addEdge(Graph *graph, int src, int dest)
{
    // 새로운 노드를 src의 인접 리스트 맨 앞에 추가
    AdjListNode *newNode = createAdjListNode(dest);
    newNode->next = graph->adjLists[src];
    graph->adjLists[src] = newNode;
}

// 큐를 생성하고 초기화하는 함수
Queue *createQueue()
{
    Queue *q = (Queue *)malloc(sizeof(Queue));
    q->front = -1;
    q->rear = -1;
    return q;
}

// 큐가 비어있는지 확인하는 함수
bool isEmpty(Queue *q)
{
    return q->rear == -1;
}

// 큐에 원소를 추가하는 함수 (enqueue)
void enqueue(Queue *q, int value)
{
    if (q->rear == NUM_VERTICES - 1)
    {
        printf("Queue is full!\n");
    }
    else
    {
        if (q->front == -1)
        {
            q->front = 0;
        }
        q->rear++;
        q->items[q->rear] = value;
    }
}

// 큐에서 원소를 제거하고 반환하는 함수 (dequeue)
int dequeue(Queue *q)
{
    int item;
    if (isEmpty(q))
    {
        printf("Queue is empty!\n");
        item = -1;
    }
    else
    {
        item = q->items[q->front];
        q->front++;
        if (q->front > q->rear)
        {
            // 큐가 비워졌으므로 초기 상태로 리셋
            q->front = q->rear = -1;
        }
    }
    return item;
}

// --- 칸의 알고리즘 (핵심 로직) ---

void kahnTopologicalSort(Graph *graph)
{
    // 1. 모든 정점의 진입 차수(in-degree) 계산
    int in_degree[NUM_VERTICES] = {0};

    for (int u = 0; u < graph->numVertices; u++)
    {
        AdjListNode *temp = graph->adjLists[u];
        while (temp)
        {
            in_degree[temp->dest]++; // u -> dest 간선이 있으므로 dest의 진입 차수 증가
            temp = temp->next;
        }
    }

    // 2. 진입 차수가 0인 모든 정점을 큐에 추가
    Queue *q = createQueue();
    for (int i = 0; i < graph->numVertices; i++)
    {
        if (in_degree[i] == 0)
        {
            enqueue(q, i);
        }
    }

    // 위상 정렬 결과를 저장할 배열
    int topological_order[NUM_VERTICES];
    int count = 0; // 위상 정렬된 정점의 수를 세는 카운터

    // 3. 메인 루프: 큐가 빌 때까지 반복
    while (!isEmpty(q))
    {
        // 큐에서 정점을 하나 꺼내 결과 배열에 추가
        int u = dequeue(q);
        topological_order[count++] = u;

        // 현재 정점 u와 연결된 모든 이웃 정점들의 진입 차수를 1 감소
        AdjListNode *temp = graph->adjLists[u];
        while (temp)
        {
            in_degree[temp->dest]--;

            // 만약 이웃 정점의 진입 차수가 0이 되었다면 큐에 추가
            if (in_degree[temp->dest] == 0)
            {
                enqueue(q, temp->dest);
            }
            temp = temp->next;
        }
    }

    // 4. 사이클(Cycle) 확인 및 결과 출력
    if (count < graph->numVertices)
    {
        printf("그래프에 사이클이 존재하여 위상 정렬을 완료할 수 없습니다.\n");
    }
    else
    {
        printf("위상 정렬 결과: ");
        for (int i = 0; i < count; i++)
        {
            printf("%s ", vertex_names[topological_order[i]]);
        }
        printf("\n");
    }

    // 동적 할당된 메모리 해제
    free(q);
}

// --- main 함수 (프로그램 시작점) ---

int main()
{
    Graph *graph = createGraph(NUM_VERTICES);

    // 슬라이드 24의 예시 그래프 생성
    // A=0, B=1, C=2, D=3, E=4, F=5
    addEdge(graph, 0, 1); // A -> B
    addEdge(graph, 0, 2); // A -> C
    addEdge(graph, 1, 3); // B -> D
    addEdge(graph, 2, 3); // C -> D
    addEdge(graph, 2, 4); // C -> E
    addEdge(graph, 3, 5); // D -> F
    addEdge(graph, 4, 5); // E -> F

    printf("슬라이드 예시 그래프 G의 위상 정렬:\n");
    kahnTopologicalSort(graph);

    printf("\n----------------------------------------\n\n");

    // 사이클이 있는 그래프 예시
    Graph *graph_cycle = createGraph(3);
    // A=0, B=1, C=2
    addEdge(graph_cycle, 0, 1); // A -> B
    addEdge(graph_cycle, 1, 2); // B -> C
    addEdge(graph_cycle, 2, 0); // C -> A (사이클)

    printf("사이클이 있는 그래프 G_cycle의 위상 정렬:\n");
    // 임시로 전역 배열을 사용하여 이름 출력
    const char *cycle_names[] = {"A", "B", "C"};
    // kahnTopologicalSort 함수는 NUM_VERTICES를 전역으로 사용하므로,
    // 이 예제에서는 직접 사이클 확인 로직만 보여주는 것이 더 적합합니다.
    // 여기서는 간단한 출력을 위해 그냥 실행합니다. (실제로는 함수 수정 필요)
    kahnTopologicalSort(graph_cycle);

    // 메모리 해제 (더 완전한 해제를 위해서는 각 노드도 해제해야 함)
    free(graph->adjLists);
    free(graph);
    free(graph_cycle->adjLists);
    free(graph_cycle);

    return 0;
}