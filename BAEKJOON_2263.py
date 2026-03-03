n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
arr = []

k = n
index = 0

pos = [0] * (n + 1)
for i in range(n):
    pos[inorder[i]] = i

def solve(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = postorder[post_end]
    print(root, end=' ')

    root_index = pos[root]
    left_size = root_index - in_start

    solve(in_start,
          root_index - 1,
          post_start,
          post_start + left_size - 1)

    solve(root_index + 1,
          in_end,
          post_start + left_size,
          post_end - 1)

solve(0, n-1, 0, n-1)