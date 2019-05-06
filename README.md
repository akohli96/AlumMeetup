# AlumMeetup


##  Django app to allow alumni to connect

### Tech
Built with Django and Postgres. Skeleten CSS and some custom CSS is used for the frontend.

### Usage
#### Build and Run it
Docker is the best way to run this, just try it :smile:
```bash
git clone https://github.com/akohli96/AlumMeetup.git
cd AlumMeetup
docker-compose build --no-cache && docker-compose up
```
### Using it
You should have a Django app.
Try logging in at http://127.0.0.1:8000/meetup/login/
The yml loads some test data already. 
Feel free to login with test and test to move around the app.

### Features
#### Features include
1. Ability to search based on school and year of graduation.
2. Sending invites to events.
3. Modification to the profile of the user.
4. Displaying results based on location (no maps)
5. Seeing event detail in detail
6. Seeing notification of event in inbox.
7. Admin panel
8. Login and logout

#### Improvements
##### Code
1. Layered architecture : Although I tried to stick to breaking things apart there were areas where too much logic was put in rest layer and some services were crossing bounderies.
2. Speeding up joins : Event and Notification contain many to many relations and as such built in Django features can be used to speed up the querying.
3. Using caches and queues : Caches can be used for storing results of nearby alums in order to prevent making calls to a database. Scheduling events should return a status url when event invites are being scheduled for large groups of people in order to make it an async process. Large groups although a nebulous term can be determined with load testing.
4. Splitting application up : A frontend framework can be used with DRF and authentication and authorization can be handled with a JWT token.
5. User interface : The user interface is critical to user experience and currently is simple.

##### Features
1. Integration with school specific technology using social login: Something like https://documentation.its.umich.edu/api-directory would be handy.
2. User notification on unread invites: Currently, the user has to go to their inbox to check the invites.
3. Maps and cities : There can be a map on invite page with info on top locations that can be used to determine meetup location and integration with packages like django-cities too. I did start out by using postgis but prioritized other features.
4. Advanced meetup/scheduling system with calender integration : This would help in scheduling events that works for everyones schedule.
