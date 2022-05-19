from models.data import Data
import pytest 
def test_valid_init():
    data1=Data("Jan, 25", "12:00", "Access Data")
    assert data1.date=="Jan, 25"
    assert data1.time=="12:00"
    assert data1.action=="Access Data"

def test_invalid_init():
    with pytest.raises(TypeError):
        Data(12, "Valid", "Valid")
    with pytest.raises(TypeError):
        Data("Jan 25", 12, "Valid")
    with pytest.raises(TypeError):
        Data("Jan 25", "12:00", 5)
        
