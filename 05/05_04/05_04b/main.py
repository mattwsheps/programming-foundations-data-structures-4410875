from collections import deque

def generate_binary(n):
  if n <= 0:
    return
  
  queue = deque()
  queue.append(1)

  for i in range(n):
    binary = queue.popleft()
    print(binary)
    queue.append(binary * 10)
    queue.append(binary * 10 + 1)


generate_binary(12)