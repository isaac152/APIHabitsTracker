# API habits Tracker v1

## About

I was trying to replicate an android habit tracker app. This is part the backend part of a full stack project. You can register/login, create/edit/delete habits and mark if you fulfill your work.

The db used was MongoDB.

I am working to make some kind of score.

## Endpoints

**[POST]** /user/register

**[POST]** /user/login

Just username and password in both cases.

**[POST]** /user/password

Must send a JSON with the actual and the new password

**[POST,PUT]** /user/username

Just the new user

**[POST]** /habits/

    {"name":"Programming",
    "description":"Programming cool stuff",
    "days":2}

"**days**" are the repetitions in the week.
Example: If you want to write every day this should be 7.

**[GET]** /habits/
Return all the habits from the user coded in Auth header.

**[DELETE]** /habits/[habit_id]

**[PUT]** /habits/[habit_id]

**[POST]** /habits/today/[habit_id]

    {"mark":True}

Else it will unmark today habit.

## How to use

Clone the repo and install the requirementes. Then change MONGO URI in the config file.

## TO DO

- [ ] Score in each habit
- [ ] Testing
- [ ] Add multiple dates in the same request
