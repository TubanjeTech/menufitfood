from models import Restaurants

restaurants = Restaurants.query.all()
for restaurant in restaurants:
    print(restaurant.restaurant_profile_image)
