# Design

>	The website backend is designed using Django with 3 applications: person, event, authenticator.

## 1. Person
1. Models: Necessary fields for user information
	*	Username: username is unique for entire database.
	*	Email: email is unique for entire database.
	*	Salt: for hashing password.
	* 	Password: only hashed password is stored.
	*	Role: member/admin. Default is member.
2. Views: operations on person
	*	like: the current user likes the event with given id.
	*	comment: the current user posts a comment in the event with given id.	
	* 	participate: the current user participate in the event with given id.
	*	getAllLikes: returns list of events liked by the current user.
	*	getAllComments: returns list of comments commented by the current user.
	*	getAllParticipation: returns list of events participated by the current user.

## 2. Event:
1. Models: Fields for an event
	1. Event: 
		*	Title: 
		* 	Description:
		*	Location: 
		*	StartDateTime: 
		*	EndDateTime:
		*	CreatedTime:
		*	Photo:
		*	Channel: one event can have multiple channels
	2. Channel:
		* 	Name:
	3. Like: links user to an event for a like
	4. Comment: links user to an event for a comment
		*	Content: content of the comment
	5. Participation: links user to an event for a participation

>	Event and Channel model is added to admin site so that administrator can create events and channels.

2. Views: operations on event
	* 	getAllEvents: returns list of all events created. Events are displayed by page of 5.
	*	getEvents: filters events by title, location, start date time, end date time or channels. Events are displayed by page of 5.
	*	getAllLikes: returns list of users who like the event with given id.
	*	getAllComments: returns lists of comments on the event with given id.
	*	getAllParticipations: returns lists of users who participate in the event with given id.	

## 3. Authenticator:

>	Authenticates login, signup, logout and session

1. Models: auth contains informations about the current session of user.
	*	Code: is a random string representing the current session of user.
	*	User_id: refers to the current user.
	*	CreatedTime:
	* 	ExpiredTime: is set to 1 day from created time.

2. Views:
	*	SignUp: validates sign up form and creates new user.
	*	Login: validates login form, username, password. Creates new authenticator corresponding to new session and sets cookies for this authenticator.
	* 	Logout: deletes the current authenticator in cookies

## 4. Miscellaneous:
1. Middleware: AuthMiddleware is used to authenticate current session through checking cookies and assigning current user to new header.
2. Utilities: mainly contains functions to hash password, display and create response.
3. Forms: models of login, sign up, search event, comment forms.
4. Urls:
	*	Root URL: http://127.0.0.1:8000
	*	All forms are under /form/
	* 	Authenticator is under /auth/
	*	List of events is under /event/
	*	User page is under /user/

# Setup new server

1. Install Python, Django, mySQL, nginx, uwsgi.
2. Go to project directory which is EntryTask/. nginx_config file is stored here. 
3. Run command: "uwsgi --socket :8001 --module EntryTask.wsgi" to start server.

# Test performance

1.	Tool: Apache Jmeter
2.	Config:
	*	Test go to login page and perform login action.
	*	Ramp-Up period: 1 second
3.	Results:
	1. 200 threads:
		1.	Go to login page:
			*	Success: 200
			*	Latest: 22.000s
			*	Average: 8.975s
			*	Deviation: 8.549s
		2.	Perform login action:
			*	Success: 200
			*	Latest: 6.294s
			*	Average: 5.485s
			*	Deviation: 2.564s
	2. 300 threads:
		1.	Go to login page:
			*	Success: 300
			*	Latest: 31.322s
			*	Average: 15.359s
			*	Deviation: 12.692s
		2.	Perform login action:
			*	Success: 300
			*	Latest: 12.258s
			*	Average: 6.334s
			*	Deviation: 3.886s
	3. 350 threads:
		1.	Go to login page:
			*	Success: 313
			*	Latest: 60.000s
			*	Average: 20.760s
			*	Deviation: 18.387s
		2.	Perform login action:
			*	Success: 313
			*	Latest: 13.538s
			*	Average: 7.900s
			*	Deviation: 5.198s
	4. 400 threads:
		1.	Go to login page:
			*	Success: 356
			*	Latest: 60.000s
			*	Average: 21.925s
			*	Deviation: 19.320s
		2.	Perform login action:
			*	Success: 356
			*	Latest: 6.624s
			*	Average: 6.988s
			*	Deviation: 6.221s

>	Server fails to support up to 350 concurrent logins per second.
