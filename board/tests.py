from test_plus.test import TestCase


class BoardTest(TestCase):
    def test_get_board_list(self):
        board_list_url = self.reverse("board:list")
        self.get_check_200(board_list_url)

