import unittest

"""
@author: Mohammad Mahjoub
@date: May, 25, 2018
This class is going to calculate how many years will it take to generate passive for a given income from renting apts.
"""
import math


class Calculator:
    def __init__(self, passive_income_desired_yearly,
                 yearly_savings,
                 starting_year,
                 price_of_one_apt,
                 price_of_renting_one_apt):
        
        if isinstance (starting_year, int):
            self._passive_income_desired_yearly = passive_income_desired_yearly
            self._yearly_savings = yearly_savings
            self._starting_year = starting_year
            self._years_needed = starting_year
            self._price_of_one_apt = price_of_one_apt
            self._price_of_renting_one_apt = price_of_renting_one_apt
            self._answer = dict ()
            self._calculate ()
        else:
            raise TypeError ("Make sure that the year input is an integer")
    
    """
    @:arg This method has no arguments
    """
    
    def _calculate(self):
        apt_number_owned = 0
        income_reached = 0
        while self._passive_income_desired_yearly >= (apt_number_owned * self._price_of_renting_one_apt):
            frac, whole = math.modf ((self._yearly_savings + income_reached) / self._price_of_one_apt)
            if whole > 0:
                income_reached += self._yearly_savings
                income_reached -= whole * self._price_of_one_apt  # pay for many apartment
                apt_number_owned += whole  # own the apt.
                income_reached += (apt_number_owned * self._price_of_renting_one_apt)
            else:
                income_reached += self._yearly_savings
                income_reached += (apt_number_owned * self._price_of_renting_one_apt)
            
            self._answer[self._starting_year] = [apt_number_owned, round (income_reached)]
            self._starting_year += 1
    
    def get_years_needed(self):
        return self._starting_year - self._years_needed
    
    def get_results(self):
        return self._answer
    
    def get_apartments_needed(self):
        key = max (self._answer, key=int)  # get the greatest key in the self._answer dictionary.
        value = self._answer[key]  # get the value of the greatest key in the self._answer dictionary.
        number_of_apartments = value[0]  # get the greatest
        return number_of_apartments
    
    def get_net_worth(self):
        return self.get_apartments_needed () * self._price_of_one_apt
    
    def print_results(self):
        print ("")
        print ("The passive income desired yearly is ${0}, "
               "the yearly investments is ${1}, "
               "the price of every apt is ${2}, "
               "the price for renting every apt is ${3},"
               " the net worth is ${4}".format (self._passive_income_desired_yearly,
                                                self._yearly_savings,
                                                self._price_of_one_apt,
                                                self._price_of_renting_one_apt,
                                                self.get_net_worth ()))
        for k, v in self._answer.items ():
            print ("Year number: {0}, Apt number owned {1} Passive Income ${2}"
                   .format (k, v[0], round (v[1])))
        print ("You can reach a passive income of ${0}, but it will take: {1} years"
               .format (self._passive_income_desired_yearly, self._starting_year - self._years_needed))
        print ("You have to invest ${0} every year ".format (self._yearly_savings))
        print ("")


class TestCalculate(unittest.TestCase):
    
    def setUp(self):
        self._calculator_obj_one = Calculator(150000, 70000, 2019, 80000, 6666)
        self._calculator_obj_two = Calculator(150000, 80000, 2019, 80000, 6666)
        self._calculator_obj_three = Calculator(150000, 90000, 2019, 80000, 6666)
        self._calculator_data_one = {2019: [0, 70000],
                                 2020: [1.0, 66666],
                                 2021: [2.0, 69998],
                                 2022: [3.0, 79996],
                                 2023: [4.0, 96660],
                                 2024: [6.0, 46656],
                                 2025: [7.0, 83318],
                                 2026: [8.0, 126646],
                                 2027: [10.0, 103306],
                                 2028: [12.0, 93298],
                                 2029: [14.0, 96622],
                                 2030: [16.0, 113278],
                                 2031: [18.0, 143266],
                                 2032: [20.0, 186586],
                                 2033: [23.0, 169904]}
        
        self._calculator_data_two = {2019: [1.0, 6666],
                                 2020: [2.0, 19998],
                                 2021: [3.0, 39996],
                                 2022: [4.0, 66660],
                                 2023: [5.0, 99990],
                                 2024: [7.0, 66652],
                                 2025: [8.0, 119980],
                                 2026: [10.0, 106640],
                                 2027: [12.0, 106632],
                                 2028: [14.0, 119956],
                                 2029: [16.0, 146612],
                                 2030: [18.0, 186600],
                                 2031: [21.0, 166586],
                                 2032: [24.0, 166570]}
        
        self._calculator_data_three = {2019: [1.0, 16666],
                                 2020: [2.0, 39998],
                                 2021: [3.0, 69996],
                                 2022: [4.0, 106660],
                                 2023: [6.0, 76656],
                                 2024: [8.0, 59984],
                                 2025: [9.0, 129978],
                                 2026: [11.0, 133304],
                                 2027: [13.0, 149962],
                                 2028: [15.0, 179952],
                                 2029: [18.0, 149940],
                                 2030: [20.0, 213260],
                                 2031: [23.0, 216578]}
        
    def test_calculate_easy_first(self):
        """Year number: 2019, Apt number owned 0 Passive Income $70000
            Year number: 2020, Apt number owned 1.0 Passive Income $66666
            Year number: 2021, Apt number owned 2.0 Passive Income $69998
            Year number: 2022, Apt number owned 3.0 Passive Income $79996
            Year number: 2023, Apt number owned 4.0 Passive Income $96660
            Year number: 2024, Apt number owned 6.0 Passive Income $46656
            Year number: 2025, Apt number owned 7.0 Passive Income $83318
            Year number: 2026, Apt number owned 8.0 Passive Income $126646
            Year number: 2027, Apt number owned 10.0 Passive Income $103306
            Year number: 2028, Apt number owned 12.0 Passive Income $93298
            Year number: 2029, Apt number owned 14.0 Passive Income $96622
            Year number: 2030, Apt number owned 16.0 Passive Income $113278
            Year number: 2031, Apt number owned 18.0 Passive Income $143266
            Year number: 2032, Apt number owned 20.0 Passive Income $186586
            Year number: 2033, Apt number owned 23.0 Passive Income $169904
            You can reach a passive income of $150000, but it will take: 15 years
        """

        for k in self._calculator_obj_one.get_results().keys():
            self.assertEqual(self._calculator_obj_one.get_results().get(k), self._calculator_data_one.get(k))

    def test_calculate_easy_second(self):
        """Year number: 2019, Apt number owned 1.0 Passive Income $6666
            Year number: 2020, Apt number owned 2.0 Passive Income $19998
            Year number: 2021, Apt number owned 3.0 Passive Income $39996
            Year number: 2022, Apt number owned 4.0 Passive Income $66660
            Year number: 2023, Apt number owned 5.0 Passive Income $99990
            Year number: 2024, Apt number owned 7.0 Passive Income $66652
            Year number: 2025, Apt number owned 8.0 Passive Income $119980
            Year number: 2026, Apt number owned 10.0 Passive Income $106640
            Year number: 2027, Apt number owned 12.0 Passive Income $106632
            Year number: 2028, Apt number owned 14.0 Passive Income $119956
            Year number: 2029, Apt number owned 16.0 Passive Income $146612
            Year number: 2030, Apt number owned 18.0 Passive Income $186600
            Year number: 2031, Apt number owned 21.0 Passive Income $166586
            Year number: 2032, Apt number owned 24.0 Passive Income $166570
            You can reach a passive income of $150000, but it will take: 14 years
        """

        for k in self._calculator_obj_two.get_results().keys():
            self.assertEqual(self._calculator_obj_two.get_results().get(k), self._calculator_data_two.get(k))

    def test_calculate_easy_third(self):
        """Year number: 2019, Apt number owned 1.0 Passive Income $16666
            Year number: 2020, Apt number owned 2.0 Passive Income $39998
            Year number: 2021, Apt number owned 3.0 Passive Income $69996
            Year number: 2022, Apt number owned 4.0 Passive Income $106660
            Year number: 2023, Apt number owned 6.0 Passive Income $76656
            Year number: 2024, Apt number owned 8.0 Passive Income $59984
            Year number: 2025, Apt number owned 9.0 Passive Income $129978
            Year number: 2026, Apt number owned 11.0 Passive Income $133304
            Year number: 2027, Apt number owned 13.0 Passive Income $149962
            Year number: 2028, Apt number owned 15.0 Passive Income $179952
            Year number: 2029, Apt number owned 18.0 Passive Income $149940
            Year number: 2030, Apt number owned 20.0 Passive Income $213260
            Year number: 2031, Apt number owned 23.0 Passive Income $216578
            You can reach a passive income of $150000, but it will take: 13 years
		"""
        
        for k in self._calculator_obj_three.get_results().keys():
            self.assertEqual(self._calculator_obj_three.get_results().get(k), self._calculator_data_three.get(k))

    def test_calculate_medium_first(self):
        with self.assertRaises(TypeError):
            Calculator("111111", "111111", "111111", "111111", "111111")
    
    def test_calculate_medium_second(self):
        with self.assertRaises(TypeError):
            Calculator(150000, 70000, 2019.123, 80000,  80000)
    
    def test_calculate_medium_third(self):
        with self.assertRaises(TypeError):
            Calculator(150000, "29217", 2019, 80000, True)
    
    def test_calculate_hard_first(self):
        with self.assertRaises(TypeError):
            Calculator(None, None, None, None, None)
    
    def test_calculate_hard_second(self):
        with self.assertRaises(TypeError):
            Calculator(111111, None, None, None, None)
    
    def test_calculate_hard_third(self):
        with self.assertRaises(TypeError):
            Calculator(111111, 293.28, 183029, 102938, Exception)
    
     
class TestGetYearsNeeded(unittest.TestCase):
    def setUp(self):
        self._calculator_obj_one = Calculator(150000, 70000, 2019, 80000, 6666)
        self._calculator_obj_two = Calculator(150000, 80000, 2019, 80000, 6666)
        self._calculator_obj_three = Calculator(150000, 90000, 2019, 80000, 6666)

    def test_years_needed_easy_first(self):
        self.assertEqual(self._calculator_obj_one.get_years_needed(), 15)

    def test_years_needed_easy_second(self):
        self.assertEqual(self._calculator_obj_two.get_years_needed(), 14)

    def test_years_needed_easy_third(self):
        self.assertEqual(self._calculator_obj_three.get_years_needed(), 13)

    def test_years_needed_medium_first(self):
        pass

    def test_years_needed_medium_second(self):
        pass

    def test_years_needed_medium_third(self):
        pass

    def test_years_needed_hard_first(self):
        pass

    def test_years_needed_hard_second(self):
        pass

    def test_years_needed_hard_third(self):
        pass


class TestGetApartmentsNeeded(unittest.TestCase):
    def setUp(self):
        self._calculator_obj_one = Calculator(150000, 70000, 2019, 80000, 6666)
        self._calculator_obj_two = Calculator(150000, 80000, 2019, 80000, 6666)
        self._calculator_obj_three = Calculator(150000, 90000, 2019, 80000, 6666)
        
    def test_apartments_needed_easy_first(self):
        self.assertEqual(self._calculator_obj_one.get_apartments_needed(), 23)

    def test_apartments_needed_easy_second(self):
        self.assertEqual(self._calculator_obj_two.get_apartments_needed(), 24)

    def test_apartments_needed_easy_third(self):
        self.assertEqual(self._calculator_obj_three.get_apartments_needed(), 23)
    
    def test_apartments_needed_medium_first(self):
        pass

    def test_apartments_needed_medium_second(self):
        pass

    def test_apartments_needed_medium_third(self):
        pass

    def test_apartments_needed_hard_first(self):
        pass

    def test_apartments_needed_hard_second(self):
        pass

    def test_apartments_needed_hard_third(self):
        pass


class TestGetNetWorth(unittest.TestCase):
    def setUp(self):
        self._calculator_obj_one = Calculator(150000, 70000, 2019, 80000, 6666)
        self._calculator_obj_two = Calculator(150000, 80000, 2019, 80000, 6666)
        self._calculator_obj_three = Calculator(150000, 90000, 2019, 80000, 6666)
        
    def test_net_worth_easy_first(self):
        self.assertEqual(self._calculator_obj_one.get_net_worth(), 1840000)

    def test_net_worth_easy_second(self):
        self.assertEqual(self._calculator_obj_two.get_net_worth(), 1920000)

    def test_net_worth_easy_third(self):
        self.assertEqual(self._calculator_obj_three.get_net_worth(), 1840000)
        
    def test_net_worth_medium_first(self):
        pass

    def test_net_worth_medium_second(self):
        pass

    def test_net_worth_medium_third(self):
        pass

    def test_net_worth_hard_first(self):
        pass

    def test_net_worth_hard_second(self):
        pass

    def test_net_worth_hard_third(self):
        pass
    
    
if __name__ == '__main__':
    unittest.main()
