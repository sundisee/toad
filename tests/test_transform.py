import unittest
import numpy as np
import pandas as pd

from toad.transform import WOETransformer, Combiner

np.random.seed(1)

feature = np.random.randint(10, size = 500)
target = np.random.randint(2, size = 500)


class TestTransform(unittest.TestCase):
    def setUp(self):
        pass

    def test_woe_transformer(self):
        f = WOETransformer().fit_transform(feature, target)
        self.assertEqual(f[451], -0.17061154127869285)

    def test_combiner(self):
        f = Combiner().fit_transform(feature, target, method = 'chi')
        self.assertEqual(f[451], 3)
