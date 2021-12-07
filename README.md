# Vincit Rising Star

This repo includes and API endpoint for wanted functionality.

To use the API you first need to download dependencies, all 2 of them.

They have been managed with python dependency software poetry.

Install poetry with pip install poetry.

Then in root folder run poetry install

Now run the application by going to the src folder and entering poetry run flask run

## Endpoints

All three endpoints require from and to as UNIX timestamps and coingecko

To get the decreasing number of days endpoint is: longest_decreasing.

Returns the number of days

To get info the buy endpoint is bying_info

Returns the days in UNIX timestamp form

And to get maximum total volume endpoint is maximum_volume
Total volume is returned in euros and the day in UNIX timestamp