tpl = ("zero", "one", "two", "three")        # 튜플(인덱스 기반)
lst = ["zero", "one", "two", "three"]       # 리스트(인덱스 기반)

dct = {0: "zero", 1: "one", 2: "two", 3: "three"}  # 딕셔너리(키 기반, 여기선 키를 인덱스처럼 씀)
dct2 = {"a": "apple", "b": "banana", "c": "cherry"} # 딕셔너리(문자 키)


# 튜플/리스트 enumerate로 인덱스+값 접근
for i, v in enumerate(tpl):
    print(f"index={i}, value={v}")

for i, v in enumerate(lst):
    print(f"index={i}, value={v}")

# dct key값을 순회해서 value에 접근하기
for k in dct:
    print(f"key={k}, value={dct[k]}")

# dct.items으로 key와 value한번에 접근
for k, v in dct.items():
    print(f"key={k}, value={v}")