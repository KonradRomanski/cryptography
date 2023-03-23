from prime import Prime
from rsa import RSA


def main():
    # rsa = RSA(31, 19)
    # print(rsa)
    # print(rsa.encrypt(8))
    # print(rsa.decrypt(312))

    # rsa.set_public_key((5, 589))
    # print(rsa.get_public_key())
    #
    # rsa.set_private_key((5, 589))
    # print(rsa.get_private_key())

    prime = Prime(1111, 9999)
    prime2 = Prime(4444, 9999)
    p = prime.get_prime()
    q = prime2.get_prime()
    p, q = 55837, 36011
    # p, q = 31, 19
    # print(f"p: {p}, q: {q}")

    rsa = RSA(p, q)
    print(rsa)
    message = 123456789
    encrypted = rsa.encrypt(message)
    print("public key:", rsa.get_public_key())
    print("private key:", rsa.get_private_key())
    print(f"message: {message}")
    print(f"encrypted: {encrypted}")
    print(f"decrypted: {rsa.decrypt(encrypted)}")


if __name__ == '__main__':
    main()
