def range_bitwise_and(M, N):
    shift = 0
    while M < N:
        M >>= 1
        N >>= 1
        shift += 1
    return M << shift


if __name__ == "__main__":
    M, N = map(int, input("Enter M and N: ").split())
    print(range_bitwise_and(M, N))
