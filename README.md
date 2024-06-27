# Asset management API for a school project

## Usage
1. Clone the repository
2. Make sure you have docker installed and that the docker daemon is running (start docker desktop, if you're running linux i assume i don't have to explain)
3. create a mysql.env file, here's a sample file
  ```
  MYSQL_ROOT_PASSWORD=my_password
  MYSQL_DATABASE=asset_management
  MYSQL_USER=asset_server
  MYSQL_PASSWORD=letmein1
  ```
5. run ```docker-compose up --build```
6. profit

## Testing
you can run the test_endpoints.py script to test all of the APIs endpoints
