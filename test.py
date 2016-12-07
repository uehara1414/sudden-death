import unittest
from sd import generator
from sd import parse
from msw import measure_sentence_width


class TestSentenceSize(unittest.TestCase):

    def test_alphabet(self):
        self.assertEqual(measure_sentence_width('die!'), 4)

    def test_alphabet_and_kana(self):
        self.assertEqual(measure_sentence_width('突然のDie!'), 10)

    def test_half_kana(self):
        self.assertEqual(measure_sentence_width('ﾅﾝﾃｺｯﾀｲ'), 7)

    def test_number(self):
        self.assertEqual(measure_sentence_width('114514'), 6)

    def test_long_sentence(self):
        self.assertEqual(measure_sentence_width('これが人類最大の威力の攻撃手段！！ これこそが！究極の攻撃魔法. explosion!!!'), 75)


class TestGenerator(unittest.TestCase):

    def test_generate_small_sudden_death(self):
        self.assertEqual(generator('死!'),
                         "＿人人人＿\n"
                         "＞　死!　＜\n"
                         "￣Y^Y^Y￣")

    def test_generate_short_English_sudden_death(self):
        self.assertEqual(generator('die!'),
                         "＿人人人人＿\n"
                         "＞　die!　＜\n"
                         "￣Y^Y^Y^Y￣")

    def test_generate_middle_sudden_death(self):
        self.assertEqual(generator('一般的突然の死！'),
                         "＿人人人人人人人人人人＿\n"
                         "＞　一般的突然の死！　＜\n"
                         "￣Y^Y^Y^Y^Y^Y^Y^Y^Y^Y￣")

    def test_generate_middle_English_sudden_death(self):
        self.assertEqual(generator('The Long Dark'),
                         "＿人人人人人人人人＿\n"
                         "＞　The Long Dark　＜\n"
                         "￣Y^Y^Y^Y^Y^Y^Y^Y￣")

    def test_generate_long_sudden_death(self):
        self.assertEqual(generator('これが人類最大の威力の攻撃手段！！ これこそが！究極の攻撃魔法. エクスプロォージョンッ！！！'),
                                   '＿人人人人人人人人人人人人人人人人人人人人人人人人人人人人人人人人人人人人人人人人人人人人人人人＿\n'
                                   '＞　これが人類最大の威力の攻撃手段！！ これこそが！究極の攻撃魔法. エクスプロォージョンッ！！！　＜\n'
                                   '￣Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y￣')


class TestParser(unittest.TestCase):

    def test_no_args(self):
        args = ''.split()
        parsed = parse(args)
        self.assertEqual(parsed.sentence, '')
        self.assertEqual(parsed.copy, False)

    def test_parse_only_a_word(self):
        args = 'word'.split()
        parsed = parse(args)
        self.assertEqual(parsed.sentence, 'word')
        self.assertEqual(parsed.copy, False)

    def test_parse_two_words(self):
        args = 'word1 word2'.split()
        parsed = parse(args)
        self.assertEqual(parsed.sentence, 'word1 word2')
        self.assertEqual(parsed.copy, False)

    def test_parse_words_with_c_option(self):
        args = 'word1 word2 -c'.split()
        parsed = parse(args)
        self.assertEqual(parsed.sentence, 'word1 word2')
        self.assertEqual(parsed.copy, True)

    def test_parse_words_with_q_option(self):
        args = 'word1 word2 -c'.split()
        parsed = parse(args)
        self.assertEqual(parsed.sentence, 'word1 word2')
        self.assertEqual(parsed.copy, True)
        self.assertEqual(parsed.quiet, False)

    def test_parse_words_with_c_and_q_options(self):
        args = 'word1 word2 -qc'.split()
        parsed = parse(args)
        self.assertEqual(parsed.sentence, 'word1 word2')
        self.assertEqual(parsed.copy, True)
        self.assertEqual(parsed.quiet, True)


if __name__ == '__main__':
    unittest.main()