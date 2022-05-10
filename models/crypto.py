class Crypto:
    def enc_pass(password):
        enc_pass=""
        password.split()
        for letters in password:
            enc_pass+=str(((ord(letters)*24)^3)/5)
        return enc_pass