def merge_sort(arr):
    """
    병합 정렬 알고리즘을 사용하여 주어진 리스트를 정렬합니다. (분할 정복)
    Args:
        arr (list): 정렬할 숫자 리스트
    Returns:
        list: 정렬된 새 리스트
    """
    # ------------------
    # 정복 (Conquer) - Base Case
    # ------------------
    # 리스트의 원소가 1개 이하면 이미 정렬된 상태이므로 그대로 반환합니다.
    # 의사코드의 if (l + 1 == r) return A[l]; 에 해당합니다.
    if len(arr) <= 1:
        return arr

    # ------------------
    # 분할 (Divide)
    # ------------------
    # 리스트를 중앙을 기준으로 두 개의 작은 리스트로 분할합니다.
    # 의사코드의 int m = l + (r - l) / 2; 에 해당합니다.
    mid = len(arr) // 2
    # 파이썬 list슬라이스에서 end값은 포합되지 않는다.
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 각 부분을 재귀적으로 정렬합니다.
    # 의사코드의 sol1 <- sort(l, m); sol2 <- sort(m, r); 에 해당합니다.
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # ------------------
    # 결합 (Combine)
    # ------------------
    # 정렬된 두 부분을 다시 하나로 병합하여 반환합니다.
    # 의사코드의 return merge(sol1, sol2); 에 해당합니다.
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    정렬된 두 리스트(left, right)를 하나의 정렬된 리스트로 병합합니다.
    Args:
        left (list): 정렬된 왼쪽 부분 리스트
        right (list): 정렬된 오른쪽 부분 리스트
    Returns:
        list: 병합 후 정렬된 새 리스트
    """
    merged_list = []
    i, j = 0, 0  # left, right 리스트를 가리킬 포인터

    # 두 리스트 중 하나가 끝날 때까지 반복합니다.
    while i < len(left) and j < len(right):
        # 두 리스트의 현재 원소를 비교하여 더 작은 값을 결과 리스트에 추가합니다.
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    # 위 반복문이 끝난 후, 아직 원소가 남아있는 리스트의 나머지 부분을
    # 결과 리스트 뒤에 그대로 붙여줍니다. (이미 정렬되어 있으므로)
    if i < len(left):
        merged_list.extend(left[i:])
    if j < len(right):
        merged_list.extend(right[j:])

    return merged_list

# --- 실행 예시 ---
if __name__ == "__main__":
    # 슬라이드 6의 예시 데이터
    my_list = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original list: {my_list}")

    sorted_list = merge_sort(my_list)
    print(f"Sorted list:   {sorted_list}")

    # 다른 예시
    my_list_2 = [5, 2, 8, 1, 9, 4]
    print(f"\nOriginal list: {my_list_2}")
    sorted_list_2 = merge_sort(my_list_2)
    print(f"Sorted list:   {sorted_list_2}")


# T(n) = T(n/3) + T(2n/3) + O(n)의 total combine cost를 구하면 nlogn이 나오잖아 그리고 높이는
# log3n이 나오고 leaf node의 갯수는 2의 log3n승 맞지?