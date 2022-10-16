from task_1 import filter_list
from task_2 import first_non_repeating_letter
from task_3 import digital_root
from task_4 import count_pairs
from task_5 import sort_names
from task_6 import next_bigger
from task_7 import int_to_ip


def test_1_1():
    assert filter_list([1, 2, 'a', 'b']) == [1, 2]


def test_1_2():
    assert filter_list([1, 'a', 'b', 0, 15]) == [1, 0, 15]


def test_1_3():
    assert filter_list([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123]


def test_2_1():
    assert first_non_repeating_letter("stress") == "t"


def test_2_2():
    assert first_non_repeating_letter("sTreSS") == "T"


def test_2_3():
    assert first_non_repeating_letter("snnaakkees") == ""


def test_3_1():
    assert digital_root(16) == 7


def test_3_2():
    assert digital_root(942) == 6


def test_3_3():
    assert digital_root(132189) == 6


def test_3_4():
    assert digital_root(493193) == 2


def test_3_5():
    assert digital_root(0) == 0


def test_4_1():
    assert count_pairs([1, 3, 6, 2, 2, 0, 4, 5], 5) == 4


def test_4_2():
    assert count_pairs([1, -1, 1, -1, 1], 0) == 6


def test_4_3():
    assert count_pairs([-4, -4, -4], -8) == 3


def test_5_1():
    assert sort_names(
        "Fred:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill") == "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"


def test_5_2():
    assert sort_names(
        "Fred:Corwill;Wilfred:Corwill;Fred:Corwill") == "(CORWILL, FRED)(CORWILL, FRED)(CORWILL, WILFRED)"


def test_6_1():
    assert next_bigger(12) == 21


def test_6_2():
    assert next_bigger(513) == 531


def test_6_3():
    assert next_bigger(2017) == 2071


def test_6_4():
    assert next_bigger(9) == -1


def test_6_5():
    assert next_bigger(111) == -1


def test_6_6():
    assert next_bigger(531) == -1


def test_7_1():
    assert int_to_ip(2149583361) == "128.32.10.1"


def test_7_2():
    assert int_to_ip(32) == "0.0.0.32"


def test_7_3():
    assert int_to_ip(0) == "0.0.0.0"