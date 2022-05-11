import hashlib
class Crypto:
    def enc_pass(password):
        enc_password=str(hashlib.sha256(password.encode()).hexdigest())
        return enc_password