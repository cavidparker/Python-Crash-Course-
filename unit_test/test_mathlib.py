
###### How to to RUN unit test #########
### python -m pytest
## py.test
## py.test -v

import mathlib
import pytest
import sys


@pytest.mark.skip(reason="I don't want to run this test at this moment")
def test_calc_total():
    total = mathlib.cal_total(4,5)
    assert total == 9

def test_calc_mul():
    total = mathlib.cal_multipy(4,5)
    assert total == 20    