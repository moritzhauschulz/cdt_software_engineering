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
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]], None),
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

def test_data_type():
    """Tests the case where data is wrong type – TypeError should be raised"""
    from inflammation.inflammation.models import patient_normalise
    test_input = np.array(([]))

    with pytest.raises(AssertionError):
        norm_data = patient_normalise(test_input)

def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])

class TestPatient:

    def setup_class(self):
        from inflammation.inflammation.models import Patient

        self.patient = Patient(0, np.array([0,2,4]))


    def test_patient_max(self):
        """test basic functionality of patient class"""
    
        npt.assert_array_equal(self.patient.data_max(),np.array(4))

    def test_patient_min(self):
        """test basic functionality of patient class"""

        npt.assert_array_equal(self.patient.data_min(),np.array(0))

    def test_patient_mean(self):
        """test basic functionality of patient class"""

        npt.assert_array_equal(self.patient.data_mean(),np.array(2))

from inflammation.inflammation.models import Trial

@pytest.fixture()
def trial_1(request):
    test = request.param
    return Trial(test, 1)

class TestTrial:
    @pytest.mark.parametrize(
    "trial_1, expected, expect_raises",
    [
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], None),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]], None),
        ([[-1, 1, 1], [1, 1, 1], [1, 1, 1]],[[-1, 1, 1], [1, 1, 1], [1, 1, 1]], ValueError),
    ],
    indirect=["trial_1"])
    
    def test_patient_normalise_class(self, trial_1, expected, expect_raises):
        if expect_raises:
            with pytest.raises(expect_raises):
                normalized_data = trial_1.patient_normalise()
        else:
            npt.assert_array_almost_equal(trial_1.patient_normalise(), expected)
        
