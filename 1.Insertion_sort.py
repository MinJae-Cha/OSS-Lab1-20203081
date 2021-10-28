import random # random 메소드 사용을 위해 import

a = random.sample(range(1, 10), 5) # 1<= x < 11의 난수 5개 리스트로 생성
print(a)# 정렬 전 리스트

for i in range(1, len(a)): # 리스트의 크기만큼 반복
    for j in range(i, 0, -1): # j 인덱스의 값이 줄어드면서 삽입할 위치를 찾을 때까지 반복
        if a[j] < a[j-1]: # 현재 인덱스가 앞의 원소보다 작다면
            a[j], a[j-1] = a[j-1], a[j] # swap해서 값 뒤로 밀어내기
        else : break # 불필요한 반복을 피하기 위해 break
print('\n')
print(a)# 정렬 후 리스트 출력

#출력
