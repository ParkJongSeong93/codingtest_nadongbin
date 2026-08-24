import heapq

n = int(input())

cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

answer = 0
while cards:
    if len(cards) == 1:
        break
    
    card_sum = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, card_sum)
    answer += card_sum

print(answer)