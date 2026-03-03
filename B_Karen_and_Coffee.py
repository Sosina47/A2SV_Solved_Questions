n, k, q = map(int, input().split())
recipes = []
for i in range(n):
    recipes.append(list(map(int, input().split())))

questions = []
for i in range(q):
    question = list(map(int, input().split()))
    questions.append(question)
     
prefix = [0] * (200000 + 1)
for left, right in recipes:
    prefix[left - 1] += 1
    prefix[right] -= 1

cur_sum = 0
for i in range(len(prefix)):
    cur_sum += prefix[i] 
    prefix[i] = 1 if cur_sum >= k else 0

for i in range(1, len(prefix)):
    prefix[i] += prefix[i - 1]
prefix.append(0)

for left, right in questions:
    print(prefix[right - 1] - prefix[left - 2])    
    
