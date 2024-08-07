from lib.most_often import *

#testing that the class is initialised
def test__init__():
    most_often = MostOften(["test"])
    assert most_often.starting_list == ["test"]


#testing add new string to empty list
def test_add_new_string_empty_ls():
    most_often = MostOften([])
    most_often.add_new("hello")
    most_often.add_new("world")
    assert most_often.starting_list == ["hello", "world"]

#testing add different dat types (string, integer, list) 
# to empty list
def test_add_diff_types():
    most_often = MostOften([])
    most_often.add_new("hello")
    most_often.add_new(25)
    most_often.add_new(["hello", "world"])
    assert most_often.starting_list == ["hello", 25, ["hello", "world"]]

#testing a list with a winner
def test_winner():
    list = [1,2,3,4,5,5,5,5,6]
    test = MostOften(list)
    test.add_new(2)
    assert test.get_most_often() == 5
