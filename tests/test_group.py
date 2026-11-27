import pandas as pd
import pytest

import quakewatch as qw


@pytest.mark.parametrize(
    "depth_km, expected_class",
    [
        (10.0, "shallow"),
        (69.9, "shallow"),
        (70.0, "intermediate"),
        (299.9, "intermediate"),
        (300.0, "deep"),
    ],
)
def test_depth_class_thresholds_member1(depth_km, expected_class):
    result = qw.depth_class(pd.Series([depth_km]))
    assert result[0] == expected_class
