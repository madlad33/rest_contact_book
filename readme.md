#Assignment
- Developed CRUD API for contact book
- Added basic authentication using JWT
- Added filters for searching
- Added pagination for 10 items per page
- Added basic unit tests
- Added caching for scalability

#Urls
##Users (for authentication)
- http://127.0.0.1:8000/user/create/ to create a new User
- http://127.0.0.1:8000/user/token/ to generate a new Token
- http://127.0.0.1:8000/user/me/ to get the info of current user

##Contact API Urls
- http://127.0.0.1:8000/api/create/ to create new contacts (POST)
- http://127.0.0.1:8000/api/all/ to get all the current contacts (GET)
- http://127.0.0.1:8000/api/detail/1/ to get the detail view of the contact with pk=1. This page contains both Update (PUT) and Delete (DELETE) methods.