'''---Ex10: Тест на короткую фразу---'''
class TestCheckPhrase:

    def test_check_phrase(self):
        phrase = input("Set a phrase: ")
        length = len(phrase)
        assert length != 0, f"Your phrase is empty :("
        assert length <= 15, f"Phrase is longer than 15 digits"
        #return length
        print("Your phrase is", length, "symbols length")