def next_greater_element(vec):
    n = len(vec)
    ans = [-1] * n  # Initialize the answer list with -1
    stk = []  # Initialize an empty stack

    # Push the first element onto the stack
    stk.append(vec[0])
    
    for i in range(1, n):
        # Pop elements from the stack while the current element is greater
        while stk and stk[-1] <= vec[i]:
            stk.pop()
        # If the stack is not empty, the top element is the next greater element
        if stk:
            ans[i] = stk[-1]
        else:
            ans[i] = -1
        # Push the current element onto the stack
        stk.append(vec[i])

    return ans

# Example usage:
vec = [int(x) for x in input().split()]
result = next_greater_element(vec)
print(" ".join(map(str, result)))