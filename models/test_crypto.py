from crypto import Crypto
import pytest
def test_crypto_success():
    assert Crypto.enc_pass('hello') == '499.8485.4519.0519.0533.4'