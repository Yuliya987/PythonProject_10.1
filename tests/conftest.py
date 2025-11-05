@pytest.fixture

def valid_card_number():
    return "Maestro 7000792289606361"

@pytest.fixture
def valid_card_number():
    return "Visa Classic 1234567890123456"

def test_valid_card_number(valid_card_number): # правильный ввод с одним словом
   assert get_mask_card_number(valid_card_number) == "Maestro 7000 79** **** 6361"

def test_valid_card_number(valid_card_number): # правельный ввод с двумя словами
   assert get_mask_card_number(valid_card_number) == "Visa Classic 1234 56** **** 3456"

def test_masking_correct(): # правильная маска
   assert get_mask_card_number("Visa Classic 1234567890123456") == "Visa Classic 1234 56** **** 3456"

def test_card_number_is_missing():
    assert get_mask_card_number("Visa Classic") == "Некорректный номер карты"
