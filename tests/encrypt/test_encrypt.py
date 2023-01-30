from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():

    assert encrypt_message("buapau", 3) == "uap_aub" 
    assert encrypt_message("buapau", 4) == "ua_paub"
    assert encrypt_message("buapau", 9) == "uapaub"

    with pytest.raises(TypeError):
        encrypt_message(3, "buapau")
