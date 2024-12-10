# car_retail_system.py

cars = []


def add_car(car):
    global cars
    if not isinstance(car, dict) or 'id' not in car or 'price' not in car:
        raise ValueError("Invalid car object")
    cars.append(car)


def remove_car_by_id(car_id):
    global cars
    initial_length = len(cars)
    cars = [car for car in cars if car['id'] != car_id]
    if len(cars) == initial_length:
        raise ValueError("Car not found")


def get_car_by_id(car_id):
    for car in cars:
        if car['id'] == car_id:
            return car
    return None


def calculate_inventory_value():
    return sum(car['price'] for car in cars)


def get_all_cars():
    return cars


def update_car_price(car_id, new_price):
    for car in cars:
        if car['id'] == car_id:
            car['price'] = new_price
            return
    raise ValueError("Car not found")


def clear_inventory():
    global cars
    cars = []


def count_cars():
    return len(cars)


def filter_cars_by_make(make):
    return [car for car in cars if car['make'] == make]


def filter_cars_by_price_range(min_price, max_price):
    return [car for car in cars if min_price <= car['price'] <= max_price]


def find_oldest_car():
    if not cars:
        return None
    return min(cars, key=lambda car: car['year'])


def find_newest_car():
    if not cars:
        return None
    return max(cars, key=lambda car: car['year'])


def sort_cars_by_price(ascending=True):
    return sorted(cars, key=lambda car: car['price'], reverse=not ascending)


def sort_cars_by_year(ascending=True):
    return sorted(cars, key=lambda car: car['year'], reverse=not ascending)


def get_total_number_of_makes():
    return len(set(car['make'] for car in cars))


def get_cars_by_year(year):
    return [car for car in cars if car['year'] == year]


def calculate_average_car_price():
    if not cars:
        return 0
    return calculate_inventory_value() / len(cars)


def find_most_expensive_car():
    if not cars:
        return None
    return max(cars, key=lambda car: car['price'])


def find_least_expensive_car():
    if not cars:
        return None
    return min(cars, key=lambda car: car['price'])


def get_car_summary(car_id):
    car = get_car_by_id(car_id)
    if not car:
        raise ValueError("Car not found")
    return f"{car['make']} {car['model']} ({car['year']}): ${car['price']}"


def add_discount_to_all_cars(discount_percentage):
    for car in cars:
        car['price'] -= car['price'] * (discount_percentage / 100)


def get_makes_inventory():
    makes_inventory = {}
    for car in cars:
        make = car['make']
        if make not in makes_inventory:
            makes_inventory[make] = 0
        makes_inventory[make] += 1
    return makes_inventory


def find_cars_within_budget(budget):
    return [car for car in cars if car['price'] <= budget]


def is_inventory_empty():
    return len(cars) == 0


def get_inventory_snapshot():
    return [{"id": car['id'], "make": car['make'], "price": car['price']} for car in cars]


# Additional 20 Functions to Extend the System

def find_cars_by_model(model):
    return [car for car in cars if car['model'] == model]


def find_cars_by_make_and_year(make, year):
    return [car for car in cars if car['make'] == make and car['year'] == year]


def get_cheapest_car():
    if not cars:
        return None
    return min(cars, key=lambda car: car['price'])


def get_most_recent_car():
    if not cars:
        return None
    return max(cars, key=lambda car: car['year'])


def update_car_make(car_id, new_make):
    for car in cars:
        if car['id'] == car_id:
            car['make'] = new_make
            return
    raise ValueError("Car not found")


def update_car_model(car_id, new_model):
    for car in cars:
        if car['id'] == car_id:
            car['model'] = new_model
            return
    raise ValueError("Car not found")


def update_car_year(car_id, new_year):
    for car in cars:
        if car['id'] == car_id:
            car['year'] = new_year
            return
    raise ValueError("Car not found")


def update_car_details(car_id, new_details):
    for car in cars:
        if car['id'] == car_id:
            car.update(new_details)
            return
    raise ValueError("Car not found")


def average_price_of_make(make):
    cars_of_make = [car['price'] for car in cars if car['make'] == make]
    if not cars_of_make:
        return 0
    return sum(cars_of_make) / len(cars_of_make)


def total_value_of_make(make):
    return sum(car['price'] for car in cars if car['make'] == make)


def get_makes_list():
    return list(set(car['make'] for car in cars))


def get_models_by_make(make):
    return list(set(car['model'] for car in cars if car['make'] == make))


def count_cars_by_make(make):
    return sum(1 for car in cars if car['make'] == make)


def count_cars_by_model(model):
    return sum(1 for car in cars if car['model'] == model)


def get_max_price_car_by_make(make):
    cars_of_make = [car for car in cars if car['make'] == make]
    if not cars_of_make:
        return None
    return max(cars_of_make, key=lambda car: car['price'])


def get_min_price_car_by_make(make):
    cars_of_make = [car for car in cars if car['make'] == make]
    if not cars_of_make:
        return None
    return min(cars_of_make, key=lambda car: car['price'])


def get_price_distribution():
    distribution = {}
    for car in cars:
        price = car['price']
        if price not in distribution:
            distribution[price] = 0
        distribution[price] += 1
    return distribution


def filter_cars_by_age_range(min_age, max_age):
    current_year = 2024
    return [car for car in cars if min_age <= current_year - car['year'] <= max_age]


def get_car_age(car_id):
    car = get_car_by_id(car_id)
    if car:
        return 2024 - car['year']
    return None


def get_inventory_statistics():
    total_value = calculate_inventory_value()
    total_cars = count_cars()
    return {"total_value": total_value, "total_cars": total_cars, "average_price": total_value / total_cars if total_cars > 0 else 0}




