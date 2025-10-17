"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import numpy.testing as npt
import pytest 

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from inflammation.inflammation.models import daily_mean

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_max_zeros():
    """Test the max function for all zeros"""
    from inflammation.inflammation.models import daily_max

    test_input = test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    #check using the compare arrays function
    npt.assert_array_equal(daily_max(test_input), test_result)

def test_daily_max_integers():
    """Test the max function for all integers"""
    from inflammation.inflammation.models import daily_max

    test_input = test_input = np.array([[100, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([100, 0])

    #check using the compare arrays function
    npt.assert_array_equal(daily_max(test_input), test_result)

def test_daily_max_neg_integers():
    """Test the max function for all integers"""
    from inflammation.inflammation.models import daily_max

    test_input = test_input = np.array([[-100, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    #check using the compare arrays function
    npt.assert_array_equal(daily_max(test_input), test_result)


@pytest.mark.parametrize(
    "test, expected, expect_raises",
    [
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], None),
        ([[0, float('inf'), 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], None),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]], None),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]], None),
        ([[-1, 1, 1], [1, 1, 1], [1, 1, 1]],[[-1, 1, 1], [1, 1, 1], [1, 1, 1]], ValueError),
    ])
def test_patient_normalise(test, expected, expect_raises):
    """Test normalisation works for arrays of one and positive integers.
       Assumption that test accuracy of two decimal places is sufficient."""
    from inflammation.inflammation.models import patient_normalise
    if expect_raises:
        with pytest.raises(ValueError):
            patient_normalise(np.array(test))
    else:
        npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)

def test_data_empty():
    """Tests the case where darta is empty – assertion error should be raised"""
    from inflammation.inflammation.models import patient_normalise
    test_input = np.array(([]))

    with pytest.raises(AssertionError):
        norm_data = patient_normalise(test_input)

