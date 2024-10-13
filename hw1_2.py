# # 讀輸入整數類型。
N: int=int(input("Please input an integer (1 ≤ N ≤ 100000): "))

# 把整數轉到字符串並反轉，轉回整數。
R: int=int(str(N)[::-1])

# 輸出結果。
print(R)