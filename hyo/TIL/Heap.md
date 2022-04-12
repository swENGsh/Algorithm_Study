# Heap

- 완전 이진 트리 구조
- 최댓값 또는 최솟값을 찾아내는 연산을 빠르게 하기 위해서 고안됨.
- 시간복잡도 : O(log₂N)
- A가 B의 부모노드라면, A의 키 값과 B의 키 값 사이에 대소관계가 성립됨.

----

### 종류

- max heap(최대 힙) 
  - 키 값이 가장 큰 노드를 찾기 위한 완전 이진 트리(1 ~ N까지 빈 정점 없이 채워짐.)
  - {부모노드의 키 값 > 자식노드의 키 값}
  - 루트 노드 : `키 값이 가장 큰 노드`
- min heap(최소 힙)
  - 키 값이 가장 작은 노드를 찾기 위한 완전 이진 트리
  - {부모노드의 키 값 < 자식노드의 키 값}
  - 루트 노드 : `키 값이 가장 작은 노드`

----

### 최대 힙

![img](Heap.assets/99D670495B7174821D.jpeg)

#### 노드 추가

```
가장 마지막 노트에 자리를 하나 만들고 해당 노드에 값을 대입한 다음 부모 노드와 값을 비교하며 자리를 바꿔 나간다. (root node까지)
```

- 코드예시

```python
tree = [0, 20, 15, 19, 4, 13, 11]
last = len(tree)-1
add = 23
def enq(n):
    global last
    last += 1
    tree.append(n)	# 완전이진트리 유지
    c = last		# 새로 추가 된 정점을 자식으로
    p = c//2		# 완전이진트리에서의 부모 정점 번호
    while tree[p] < tree[c] and p != 0 and c != 0:
        tree[p],tree[c] = tree[c], tree[p]
        c = p
        p = c//2
    return tree
print(enq(add))
```

```
>> [0, 23, 15, 20, 4, 13, 11, 19]
```

#### 노드 삭제

```
root node를 저장해놓고, 가장 마지막 노드와 swap(자리를 바꿔줌.)
가장 마지막 값 pop(삭제(최댓값))
부모노드와 자식노드를 비교하면서 계속 swap해준다.
```

- 코드예시

```python
tree = [0, 23, 15, 19, 4, 13, 10]
last = len(tree) - 1
def deq():
    global last
    tmp = tree[1]			# 루트의 key 값
    tree[1] = tree[last]	# 마지막 정점의 키를 루트에 복사
    tree.pop()				# 마지막 정점의 키 버리기
    last -= 1				# 마지막 정점 삭제
    p = 1; c = p * 2		# 왼쪽 자식 노드 번호
    while c <= last:		# 왼쪽 자식이 있으면
        if c+1 <= last and tree[c] < tree[c+1]:	# 오른쪽 자식이 있고, 더 크면 오른쪽 자식 선택
            c += 1
        if tree[p] < tree[c]:		# 부모 키 값보다 자식 키 값이 더 크면
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p * 2
        else:
            break
    return tmp

print(deq(), end=' ')
print(tree)
```

```
>> 23 [0, 19, 15, 10, 4, 13]
```

----

### 최소 힙

![img](Heap.assets/99A1DE4D5B71748D1B.jpeg)

==> 최대힙과 방법은 같다.

----

# heapq 모듈

: 최소 힙을 지원하는 모듈로 직접 최소 힙을 구현하지 않아도 된다.

```
부모 노드의 인덱스를 1이라고 할 떄, 자식 노드의 인덱스는
- 부모 노드 인덱스 = 자식 인덱스 // 2
- 왼쪽 자식 노드 인덱스 = 부모 노드 인덱스 * 2
- 오른쪽 자식 노드 인덱스 = 부모 노드 인덱스 * 2 - 1
```

----

### 힙 함수

```
- heapq.heappush(heap, item) : item을 heap에 추가
- heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & return. (비어있으면 IndexError)
- heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함.
```

----

#### 1) 힙 데이터 추가

```python
import heapq

heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 7)
heapq.heappush(heap, 4)
heapq.heappush(heap, 6)

print(heap)
```

```
>> [2, 4, 6, 10, 7, 8]
```

만약, 이미 생성해 둔 리스트가 있다면

```python
import heapq

lst = [10, 2, 8, 7, 4, 6]
heapq.heapify(lst)

print(lst)
```

```
>> [2, 4, 6, 7, 10, 8]
```

==> 데이터를 일일이 추가한 것과 기존의 리스트를 가지고 힙으로 변형시킨 값이 다른 것을 볼 수 있다.

힙큐의 내부적 로직으로 인해 리스트를 순차적으로 진행하지 않음. 

but, heap은 최대, 최소값만 가장 앞에 나오면 되므로 문제가 되지 않음.

heapify() 는  <mark>시간복잡도가 O(N)</mark>

----

#### 2) 힙 데이터 삭제

```python
import heapq

heap = [2, 10, 8, 7]

result = heapq.heappop(heap)

print(result)
print(heap)
```

```
>> 2
>> [7, 10, 8]
```

만약 삭제하지 않고 데이터를 가지고 오고 싶다면,

```python
import heapq

heap = [2, 10, 8, 7]

result = heap[0]

print(result)
print(heap)
```

```
>> 2
>> [2, 10, 8, 7]
```

----

#### 3) 최대 힙 구현하기

```python
import heapq

max_heap = [1,3,5,7,9]

reverse_sign = lambda x: x*-1
max_heap2 = list(map(reverse_sign, max_heap))
heapq.heapify(max_heap2)
max_heap2 = list(map(reverse_sign, max_heap2))

print(max_heap2)
```

```
>> [9, 7, 5, 1, 3]
```

----

> 참고: lambda 함수

```
lambda 매개변수 : 표현식
```

> 참고: map 함수

```
map(함수, 리스트)
```

----

