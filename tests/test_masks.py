from src.masks import get_mask_card_number, get_mask_account

def test_masks():
   card_number = "1234567891234567"

   masked = get_mask_card_number(card_number)
   cleaned_card = card_number.replace(" ", "")
   assert len(cleaned_card) == 16

   assert masked.startswith("1234 56")

   assert masked.endswith("4567")

   assert get_mask_card_number([]) == "Номер карты должен содержать 16 цифр"

   assert "*" in masked

   assert get_mask_card_number(card_number) == f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

def test_masks_account():
    mask_account = "12345678912345678912"
    masked = get_mask_account(mask_account)
    assert len(mask_account) == 20

    assert masked.startswith("")

    assert masked.endswith("**8912")

    assert get_mask_account([]) == "Номер счета должен содержать 20 цифр"

    assert "*" in masked

    assert get_mask_account(mask_account) == f"**{mask_account[-4:]}"

