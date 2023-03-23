import random


class Shamir:
    def findshares(self, s, n, t, p):
        shares, rs = [], []
        for i in range(t - 1):
            rs.append(random.randint(1, 100000))
        for i in range(n):
            sum_ = 0
            for j in range(t - 1):
                sum_ += rs[j] * (i + 1) ** (j + 1)
            sum_ += s
            sum_ = sum_ % p
            shares.append((i + 1, sum_))
        return shares

    def reconstruct(self, shares, prime):
        sum_ = 0
        for share in shares:
            li, mi = [], []
            l = 1
            for i in shares:
                if i != share:
                    li.append(i[0])
                    mi.append(share[0] - i[0])
            for i in range(len(mi)):
                li[i] /= mi[i]
                l *= li[i]
            sum_ += share[1] * l
        print("Reconstructed:", sum_ % prime)


def main():
    s = 1851  # secret
    n = 7  # number of shares
    t = 3  # needed shares
    p = 9999991  # prime
    p = Shamir().findshares(s, n, t, p)
    print("Shares:", p)
    q = p[:t]
    print("Used shares:", q)
    Shamir().reconstruct(q, 9999991)


if __name__ == '__main__':
    main()
