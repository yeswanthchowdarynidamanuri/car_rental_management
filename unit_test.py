# unit_test.py

import unittest
from car_retail_system import *


class TestCarRetailSystem(unittest.TestCase):

    def setUp(self):
        clear_inventory()
        self.car1 = {'id': '1', 'make': 'Toyota', 'model': 'Camry', 'year': 2021, 'price': 25000}
        self.car2 = {'id': '2', 'make': 'Honda', 'model': 'Civic', 'year': 2019, 'price': 20000}
        self.car3 = {'id': '3', 'make': 'Toyota', 'model': 'Corolla', 'year': 2020, 'price': 22000}
        add_car(self.car1)
        add_car(self.car2)
        add_car(self.car3)

    def add_car(self):
        new_car = {'id': '4', 'make': 'Ford', 'model': 'Focus', 'year': 2022, 'price': 18000}
        add_car(new_car)
        self.assertEqual(len(cars), 4)
        self.assertEqual(cars[-1]['id'], '4')

    def remove_car_by_id(self):
        remove_car_by_id('1')
        self.assertEqual(len(cars), 2)
        self.assertIsNone(get_car_by_id('1'))
        with self.assertRaises(ValueError):
            remove_car_by_id('999')  # Nonexistent ID

    def test_get_car_by_id(self):
        car = get_car_by_id('2')
        self.assertIsNotNone(car)
        self.assertEqual(car['make'], 'Honda')
        self.assertIsNone(get_car_by_id('999'))

    def test_calculate_inventory_value(self):
        self.assertEqual(calculate_inventory_value(), 67000)

    def test_get_all_cars(self):
        all_cars = get_all_cars()
        self.assertEqual(len(all_cars), 3)

    def test_update_car_price(self):
        update_car_price('1', 28000)
        self.assertEqual(get_car_by_id('1')['price'], 28000)
        with self.assertRaises(ValueError):
            update_car_price('999', 15000)  # Nonexistent ID

    def test_clear_inventory(self):
        clear_inventory()
        self.assertEqual(len(cars), 0)

    def test_count_cars(self):
        self.assertEqual(count_cars(), 3)

    def test_filter_cars_by_make(self):
        toyota_cars = filter_cars_by_make('Toyota')
        self.assertEqual(len(toyota_cars), 2)

    def test_filter_cars_by_price_range(self):
        cars_in_range = filter_cars_by_price_range(20000, 25000)
        self.assertEqual(len(cars_in_range), 3)

    def test_find_oldest_car(self):
        oldest_car = find_oldest_car()
        self.assertEqual(oldest_car['id'], '2')

    def test_find_newest_car(self):
        newest_car = find_newest_car()
        self.assertEqual(newest_car['id'], '1')

    def test_sort_cars_by_price(self):
        sorted_cars = sort_cars_by_price()
        self.assertEqual(sorted_cars[0]['id'], '2')

    def test_sort_cars_by_year(self):
        sorted_cars = sort_cars_by_year(ascending=False)
        self.assertEqual(sorted_cars[0]['id'], '1')

    def test_get_total_number_of_makes(self):
        self.assertEqual(get_total_number_of_makes(), 2)

    def test_get_cars_by_year(self):
        cars_2020 = get_cars_by_year(2020)
        self.assertEqual(len(cars_2020), 1)
        self.assertEqual(cars_2020[0]['id'], '3')

    def calculate_average_car_price(self):
        avg_price = calculate_average_car_price()
        self.assertEqual(avg_price, 22333.33)

    def test_find_most_expensive_car(self):
        most_expensive = find_most_expensive_car()
        self.assertEqual(most_expensive['id'], '1')

    def test_find_least_expensive_car(self):
        least_expensive = find_least_expensive_car()
        self.assertEqual(least_expensive['id'], '2')

    def test_get_car_summary(self):
        summary = get_car_summary('1')
        self.assertEqual(summary, "Toyota Camry (2021): $25000")
        with self.assertRaises(ValueError):
            get_car_summary('999')  # Nonexistent ID

    def test_add_discount_to_all_cars(self):
        add_discount_to_all_cars(10)
        self.assertEqual(get_car_by_id('1')['price'], 22500)

    def test_get_makes_inventory(self):
        inventory = get_makes_inventory()
        self.assertEqual(inventory['Toyota'], 2)
        self.assertEqual(inventory['Honda'], 1)

    def test_find_cars_within_budget(self):
        budget_cars = find_cars_within_budget(22000)
        self.assertEqual(len(budget_cars), 2)

    def test_is_inventory_empty(self):
        self.assertFalse(is_inventory_empty())
        clear_inventory()
        self.assertTrue(is_inventory_empty())

    def test_get_inventory_snapshot(self):
        snapshot = get_inventory_snapshot()
        self.assertEqual(len(snapshot), 3)
        self.assertEqual(snapshot[0]['id'], '1')

    # Additional 20 Functions

    def test_find_cars_by_model(self):
        cars_by_model = find_cars_by_model('Camry')
        self.assertEqual(len(cars_by_model), 1)
        self.assertEqual(cars_by_model[0]['id'], '1')

    def test_find_cars_by_make_and_year(self):
        cars = find_cars_by_make_and_year('Toyota', 2021)
        self.assertEqual(len(cars), 1)
        self.assertEqual(cars[0]['id'], '1')

    def test_get_cheapest_car(self):
        cheapest_car = get_cheapest_car()
        self.assertEqual(cheapest_car['id'], '2')

    def test_get_most_recent_car(self):
        recent_car = get_most_recent_car()
        self.assertEqual(recent_car['id'], '1')

    def test_update_car_make(self):
        update_car_make('1', 'Nissan')
        self.assertEqual(get_car_by_id('1')['make'], 'Nissan')
        with self.assertRaises(ValueError):
            update_car_make('999', 'Hyundai')  # Nonexistent ID

    def test_update_car_model(self):
        update_car_model('1', 'Altima')
        self.assertEqual(get_car_by_id('1')['model'], 'Altima')
        with self.assertRaises(ValueError):
            update_car_model('999', 'Sonata')  # Nonexistent ID

    def test_update_car_year(self):
        update_car_year('1', 2023)
        self.assertEqual(get_car_by_id('1')['year'], 2023)
        with self.assertRaises(ValueError):
            update_car_year('999', 2025)  # Nonexistent ID

    def test_update_car_details(self):
        new_details = {'model': 'Fusion', 'price': 23000}
        update_car_details('1', new_details)
        self.assertEqual(get_car_by_id('1')['model'], 'Fusion')
        self.assertEqual(get_car_by_id('1')['price'], 23000)
        with self.assertRaises(ValueError):
            update_car_details('999', new_details)  # Nonexistent ID

    def test_average_price_of_make(self):
        avg_price = average_price_of_make('Toyota')
        self.assertEqual(avg_price, 23500)

    def test_total_value_of_make(self):
        total_value = total_value_of_make('Toyota')
        self.assertEqual(total_value, 47000)

    def test_get_makes_list(self):
        makes_list = get_makes_list()
        self.assertIn('Toyota', makes_list)
        self.assertIn('Honda', makes_list)

    def test_get_models_by_make(self):
        models = get_models_by_make('Toyota')
        self.assertIn('Camry', models)
        self.assertIn('Corolla', models)

    def test_count_cars_by_make(self):
        count = count_cars_by_make('Toyota')
        self.assertEqual(count, 2)

    def test_count_cars_by_model(self):
        count = count_cars_by_model('Camry')
        self.assertEqual(count, 1)

    def test_get_max_price_car_by_make(self):
        max_price_car = get_max_price_car_by_make('Toyota')
        self.assertEqual(max_price_car['id'], '1')

    def test_get_min_price_car_by_make(self):
        min_price_car = get_min_price_car_by_make('Toyota')
        self.assertEqual(min_price_car['id'], '3')

    def test_get_price_distribution(self):
        distribution = get_price_distribution()
        self.assertEqual(distribution[25000], 1)
        self.assertEqual(distribution[20000], 1)

    def test_filter_cars_by_age_range(self):
        cars_in_age_range = filter_cars_by_age_range(2, 5)
        self.assertEqual(len(cars_in_age_range), 3)

    def test_get_car_age(self):
        car_age = get_car_age('1')
        self.assertEqual(car_age, 3)

    def get_inventory_statistics(self):
        stats = get_inventory_statistics()
        self.assertEqual(stats['total_value'], 67000)
        self.assertEqual(stats['total_cars'], 3)
        self.assertEqual(stats['average_price'], 22333.33)


if __name__ == '__main__':
    unittest.main()








