def pred(a, m, t):
    if a[m] > t:
        return 0
    return 1

def main():
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    
    target = nums[n - 1]
    l, r = -1, n
    
    while (r - l) != 1:
        m = (l + r) // 2
        if pred(nums, m, target) == 0:
            l = m
        else:
            r = m
    
    print(nums[l + 1])

if __name__ == "__main__":
    main()