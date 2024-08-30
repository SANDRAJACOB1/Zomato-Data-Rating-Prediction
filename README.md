**Zomato Restaurant Rating Prediction**

This project aims to predict restaurant ratings using Zomato's dataset. By leveraging machine learning techniques, the goal is to develop a model that can accurately forecast a restaurant's rating based on various features such as country code, price range, and other relevant factors.


**Project Structure**

Zomatodata/: Contains the dataset used for the analysis.

Project_SANDRA JACOB_ZomatoData.ipynb/: Source code for data preprocessing, feature engineering, model training, and prediction.

app.py/: Saved models and checkpoints.

README.md: Project documentation.



**DATA DESCRIPTION**

The dataset provided to us contains 9551 rows, and 19 different independent features. We aim to predict the rating of restuarants. This is clearly a Regression probelm and we will train the Regression models to predict the desired outputs. Mentioned below are the details of the features provided to us, which we will be feeding to our model to train it.

RestaurantID: Unique identifier for each restaurant.

RestaurantName: The name of the restaurant.

CountryCode: Country code where the restaurant is located.

City: The city where the restaurant is located.

Address: The specific address of the restaurant.

Locality: Locality or district within the city.

LocalityVerbose: A more detailed description of the locality.

Longitude: Longitude coordinate of the restaurant's location.

Latitude: Latitude coordinate of the restaurant's location.

Cuisines: Types of cuisines served at the restaurant.

Currency: Currency used in pricing.

Has_Table_booking: Indicates whether the restaurant offers table booking (Yes/No).

Has_Online_delivery: Indicates whether the restaurant offers online delivery (Yes/No).

Is_delivering_now: Indicates whether the restaurant is currently delivering orders (Yes/No).

Switch_to_order_menu: Indicates whether there's an option to switch to the ordering menu (Yes/No).

Price_range: Range indicating the price level of the restaurant.

Votes: Number of votes or reviews received by the restaurant.

Average_Cost_for_two: Average cost for two people to dine at the restaurant.

Rating: Rating of the restaurant.
