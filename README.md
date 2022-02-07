# A Blogging website using Flask Python

 [![Deploy](https://github.com/jakbin/flask-blog/actions/workflows/deploy.yml/badge.svg)](https://github.com/jakbin/flask-blog/actions/workflows/deploy.yml)
 ![GitHub Contributors](https://img.shields.io/github/contributors/jakbin/flask-blog)
 ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/jakbin/flask-blog)
 ![GitHub last commit](https://img.shields.io/github/last-commit/jakbin/flask-blog)

## we use sqlite database for better devlopment support

note:- heroku does not detect changes in sqlite after restart. You need to use any other database.

## Admin Page :-

Admin page at **/dashboard** 

username : - admin

password :- admin

(**You must change it before deploy on server**)

## Change password :-

**For changing Admin Dashboard password run change_pass.py**

Open config.json and change configuration according to your mind.

### Available ophtions in config.josn:-

* 1. Mysql database Path
* 2. Sqlite3 database Path
* 3. Facebook Url
* 4. Twitter Url
* 5. Github Url
* 6. Blog Name
* 7. Gmail id 
* 8. Gmail Pass
* 9. **Number of Post per page on home page** (Importent)
* 10. Post Writer name (i will remove it after some time)
* 11. Image Upload Path

note:- After changing configuration in josn file restart server manually

## Todo-List

- [x] Secure Login 
- [x] Secure File Upload 
- [x] UI Improvements 
- [x] About Page Improvements
- [ ] Uploaded Images Viewer
- [ ] Post View counter 
- [x] Improve Search Functionality
- [ ] Blueprint (Not yet)

[Static FIles & ngrok](staticFiles&Ngrok.md)
