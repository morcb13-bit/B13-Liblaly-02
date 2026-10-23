"""表紙の数の盤（1〜60）を足し算だけで作る。
フィボナッチ：前の二つを足す。素数：p から p ずつ足して印をつける。幸運数：残った列を k 番目ごとに数えて抜く。
割り算・剰余は使わない。"""
N = 60

# フィボナッチ：1, 1 から前の二つを足す
fib = set()
a, b = 1, 1
while a <= N:
    fib.add(a)
    a, b = b, a + b

# 素数：2 から始めて、まだ印のない数 p について p+p, p+p+p, … に印をつける
marked = [False] * (N + 1)
primes = []
p = 2
while p <= N:
    if not marked[p]:
        primes.append(p)
        q = p + p
        while q <= N:
            marked[q] = True
            q += p
    p += 1

# 幸運数：奇数の列から、k 番目ごとに数えて抜く（k は残った列の次の数）
seq = []
x = 1
while x <= N:
    seq.append(x)
    x += 2
i = 1
while i < len(seq) and seq[i] <= len(seq):
    k = seq[i]
    out, count = [], 0
    for v in seq:
        count += 1
        if count == k:
            count = 0          # k 番目は抜く
        else:
            out.append(v)
    seq = out
    i += 1
lucky = seq

print("フィボナッチ:", sorted(fib))
print("素数　　　　:", primes)
print("幸運数　　　:", lucky)
both = [n for n in primes if n in set(lucky)]
print("素数でも幸運数でもある:", both)
print("三つともに入る:", [n for n in both if n in fib])
