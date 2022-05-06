import pytest
from company import Company

def test__init__():
    with pytest.raises(TypeError):
        assert Company(name=99)
    # test_company = Company('Amazon')
    # assert test_company.name == 'Amazon'

