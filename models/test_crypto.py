from crypto import Crypto
import pytest
def test_crypto_success():
    assert Crypto.enc_pass('Hello') == "185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969"