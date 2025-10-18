import heapq

class HuffmanEncoder:
    """
    확률(빈도) 리스트를 기반으로 허프만 코드를 생성하고 조회하는 클래스입니다.

    이 클래스는 리스트를 사용하여 트리 구조를 효율적으로 저장합니다.
    - 심볼(문자)은 0부터 시작하는 정수 인덱스로 가정합니다.
    - self.edges[i]는 (부모 노드 인덱스, 비트) 튜플을 저장하여
      자식 노드 i에서 부모로의 경로를 나타냅니다.
    """

    def __init__(self, probabilities):
        """
        주어진 확률(probabilities)로 허프만 트리를 생성합니다.

        Args:
            probabilities (list or numpy array): 각 심볼의 확률(또는 빈도수) 리스트.
        """
        num_symbols = len(probabilities)
        if num_symbols < 2:
            raise ValueError("허프만 코딩을 위해서는 최소 2개 이상의 심볼이 필요합니다.")

        # 트리의 총 노드 개수는 (리프 노드 + 내부 노드) = n + (n-1) = 2n-1 입니다.
        # 리스트의 길이가 2n-1 이므로 인덱스는 0~ 2n-2
        # 노드는 0부터 2n-2까지 인덱싱됩니다.
        # 0 ~ n-1 : 리프 노드 , n ~ 2n-2 : 내부노드
        self.edges = [None] * (2 * num_symbols - 1)
        self.probabilities = probabilities

        # 우선순위 큐(최소 힙)를 초기화합니다.
        # (가중치, 노드 인덱스) 튜플을 저장합니다.
        frontier = [(weight, index) for index, weight in enumerate(probabilities)]
        heapq.heapify(frontier)

        # 다음 내부 노드에 할당할 인덱스 (리프 노드 인덱스 다음부터 시작)
        next_node = num_symbols

        # 큐에 루트 노드 하나만 남을 때까지 반복
        while len(frontier) > 1:
            # 가장 작은 가중치를 가진 두 노드를 꺼냅니다.
            weight1, child1 = heapq.heappop(frontier)
            weight2, child2 = heapq.heappop(frontier)

            # 자식 노드의 edges 항목에 부모(next_node)와 비트(0, 1)를 기록합니다.
            # False는 0 (왼쪽), True는 1 (오른쪽)을 의미합니다.
            self.edges[child1] = (next_node, False)
            self.edges[child2] = (next_node, True)

            # 두 가중치를 합산하여 새로운 부모 노드를 큐에 추가합니다.
            new_weight = weight1 + weight2
            heapq.heappush(frontier, (new_weight, next_node))

            # 다음 내부 노드의 인덱스를 1 증가시킵니다.
            next_node += 1

    def __len__(self):
        """인코더에 있는 심볼의 개수를 반환합니다."""
        return len(self.probabilities)

    def __getitem__(self, symbol):
        """
        주어진 'symbol'에 대한 허프만 코드 단어를 반환합니다.

        Args:
            symbol (int): 0부터 len(self)-1 사이의 심볼 인덱스.

        Returns:
            list: 심볼에 대한 코드 단어 (예: [0, 1, 1]).
        """
        assert 0 <= symbol < len(self), "심볼이 범위를 벗어났습니다."

        codeword_reverse = []
        node = symbol

        # 루트 노드는 마지막으로 생성된 노드입니다.
        # 총 노드 수가 2n-1이므로 마지막 노드 인덱스는 2n-2입니다.
        root_node = 2 * len(self) - 2

        # 리프 노드(symbol)에서 시작하여 루트 노드에 도달할 때까지 위로 올라갑니다.
        while node != root_node:
            # self.edges에서 부모 노드와 비트를 가져옵니다.
            parent, bit = self.edges[node]
            codeword_reverse.append(bit)
            node = parent

        # 경로가 '리프 -> 루트' 순이므로 뒤집어서 '루트 -> 리프' 순서로 만듭니다.
        # bool 값을 int(0, 1)로 변환하여 반환합니다.
        return [int(b) for b in reversed(codeword_reverse)]

# --- 실행 예제 ---
if __name__ == "__main__":
    # 주어진 확률 값
    probabilities = [.3, .28, .12, .1, .2]

    # HuffmanEncoder 클래스의 인스턴스 생성
    huffman_encoder = HuffmanEncoder(probabilities)

    print(f"주어진 확률: {probabilities}\n")

    # 각 심볼에 대한 허프만 코드 출력
    for i in range(len(huffman_encoder)):
        code = huffman_encoder[i]
        # 리스트를 문자열로 변환하여 보기 좋게 출력
        code_str = "".join(map(str, code))
        print(f"심볼 {i} (확률: {probabilities[i]})의 허프만 코드: {code_str}")




"""
import heapq

class PracticalHuffmanEncoder:
    """
    (심볼, 빈도수) 딕셔너리를 기반으로 허프만 코드를 생성하는 현실적인 클래스.
    """
    def __init__(self, freq_dict):
        """
        주어진 (심볼, 빈도수) 딕셔너리로 허프만 트리를 생성합니다.

        Args:
            freq_dict (dict): {'심볼': 빈도수} 형태의 딕셔너리.
        """
        if not freq_dict or len(freq_dict) < 2:
            raise ValueError("허프만 코딩을 위해서는 최소 2개 이상의 심볼이 필요합니다.")

        # 1. 심볼과 인덱스를 매핑하는 테이블 생성
        self.symbols = sorted(freq_dict.keys(), key=lambda s: freq_dict[s])
        self.symbol_to_index = {symbol: i for i, symbol in enumerate(self.symbols)}

        # 원본 로직을 위해 빈도수 리스트를 추출
        probabilities = [freq_dict[symbol] for symbol in self.symbols]

        num_symbols = len(probabilities)
        self.edges = [None] * (2 * num_symbols - 1)

        # 이제부터 원본 코드의 로직과 거의 동일하게 진행
        frontier = [(weight, index) for index, weight in enumerate(probabilities)]
        heapq.heapify(frontier)

        next_node = num_symbols

        while len(frontier) > 1:
            weight1, child1_idx = heapq.heappop(frontier)
            weight2, child2_idx = heapq.heappop(frontier)

            self.edges[child1_idx] = (next_node, False)
            self.edges[child2_idx] = (next_node, True)

            new_weight = weight1 + weight2
            heapq.heappush(frontier, (new_weight, next_node))

            next_node += 1

    def get_code(self, symbol):
        """주어진 'symbol'에 대한 허프만 코드 단어를 반환합니다."""
        if symbol not in self.symbol_to_index:
            raise ValueError(f"'{symbol}'은(는) 사전에 없는 심볼입니다.")

        # 심볼을 내부 인덱스로 변환
        symbol_index = self.symbol_to_index[symbol]

        codeword_reverse = []
        node = symbol_index
        root_node = 2 * len(self.symbols) - 2

        if root_node < 0: # 심볼이 하나뿐인 엣지 케이스
            return [0]

        while node != root_node:
            parent, bit = self.edges[node]
            codeword_reverse.append(bit)
            node = parent

        return [int(b) for b in reversed(codeword_reverse)]

    def get_encoding_table(self):
        """모든 심볼에 대한 허프만 코드 테이블을 딕셔너리로 반환합니다."""
        return {symbol: self.get_code(symbol) for symbol in self.symbols}


# --- 실행 예제 ---
if __name__ == "__main__":
    # 실제 사용 예: (문자, 빈도수) 딕셔너리
    frequencies = {
        'a': 45,
        'b': 13,
        'c': 12,
        'd': 16,
        'e': 9,
        'f': 5
    }

    encoder = PracticalHuffmanEncoder(frequencies)

    # 전체 인코딩 테이블 출력
    encoding_table = encoder.get_encoding_table()

    print("--- 허프만 인코딩 테이블 ---")
    for symbol, code in encoding_table.items():
        code_str = "".join(map(str, code))
        print(f"심볼 '{symbol}' (빈도: {frequencies[symbol]}) : {code_str}")

    # 특정 심볼의 코드 직접 조회
    print("\n'c'의 코드:", "".join(map(str, encoder.get_code('c'))))
"""