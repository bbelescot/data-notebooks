from utils import *
import pytest
from pandas.testing import assert_frame_equal


def test_jugement_majoritaire_computations():
    assert_frame_equal(
        jugement_majoritaire_computations(
            {"Proposition 1": {"A": 51, "B": 49}, "Proposition 2": {"A": 33, "B": 67}}
        ),
        pd.DataFrame(
            {
                "JUGEMENT MAJORITAIRE": {"Proposition 1": "A", "Proposition 2": "B"},
                "B": {"Proposition 1": 0.49, "Proposition 2": 0.67},
                "A": {"Proposition 1": 0.51, "Proposition 2": 0.33},
            }
        ),
    )
