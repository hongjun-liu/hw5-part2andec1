import unittest
import hw5_cards_ec1

class TestHand(unittest.TestCase):

    def  test_q1(self):
        Deck1 = hw5_cards_ec.Deck()
        q1 = hw5_cards_ec.Hand(Deck1.cards)
        self.assertIsInstance(q1, hw5_cards_ec.Hand)
        self.assertEqual(q1.init_card, Deck1.cards)
        return type(q1), hw5_cards_ec.Hand

    def  testAddAndRemove(self):
        Deck2 = hw5_cards_ec.Deck()
        cardlist =Deck2.cards.copy()
        card = cardlist.pop(-1)
        q2 = hw5_cards_ec.Hand(Deck2.cards)
        cardlist2=q2.init_card.copy()
        num1 = len(q2.init_card)
        q2.remove_card(card)
        cardlist1 = q2.init_card.copy()
        num2 = len(q2.init_card)
        q2.add_card(card)
        num3 = len(q2.init_card)
        diff1 = num1-num2
        diff2 = num3-num2
        self.assertEqual(cardlist1, cardlist)
        self.assertEqual(cardlist2, q2.init_card)
        self.assertEqual(diff1, 1)
        self.assertEqual(diff2, 1)
        return diff1, 1, diff2, 1

    def  test_q3(self):
        Deck4 = hw5_cards_ec.Deck()
        cardlist = Deck4.cards.copy()
        cardlist1 = Deck4.cards.copy()
        cardlist2 = Deck4.cards.copy()
        card = cardlist.pop(-1)
        cardlist1.append(card)
        q3 = hw5_cards_ec.Hand(cardlist2)
        num1 = len(q3.init_card)
        num3 = len(Deck4.cards)
        q3.draw(Deck4)
        num2 = len(q3.init_card)
        num4 = len(Deck4.cards)
        diff1 = num2-num1
        diff2 = num3-num4
        self.assertEqual(cardlist, Deck4.cards)
        self.assertEqual(q3.init_card, cardlist1)
        self.assertEqual(diff1, 1)
        self.assertEqual(diff2, 1)
        return diff1, 1, diff2, 1

if __name__=="__main__":
    unittest.main()
