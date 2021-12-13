# A Blogging website using Flask Python

 ![GitHub Contributors](https://img.shields.io/github/contributors/jakbin/flask-blog)
 ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/jakbin/flask-blog)
 ![GitHub last commit](https://img.shields.io/github/last-commit/jakbin/flask-blog)


## we use sqlite database for better devlopment support

Admin page at **/dashboard** and default password is admin,admin(**You must change it before deploy on server**)


**For changing Admin Dashboard run change_pass.py**

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
* 9. **Number of Post** (Importent)
* 10. Post Writer name (i will remove it after some time)
* 11. Image Upload Path

### After changing configuration in josn file restart server manually 

## for local development download static files from here
[Static Files](https://drive.google.com/file/d/1aLLtI4DPhIZCpg6zLEXiUK5Trs8IH5Hy/view?usp=sharing)

## Static folder structure

```
static
|
└───css
|    └─── custom css files
|
└───img
|    └─── image file
|
└───jquery
|    └─── jquery files
|
└───js
|    └─── custom js files
|
└───vendor
     |
     └───bootstrap
     |   |
     |   └─── all bootstrap css and js files
     |
     └───fontawesome-free
         |
         └─── all fontawesome css
```

## Todo-List 

- [X] Secure Login 
- [X] Secure File Upload 
- [X] UI Improvements 
- [X] About Page Improvements
- [ ] Uploaded Images Viewer
- [ ] Post View counter 
- [ ] Improve Search Functionality
- [ ] Blueprint (Not yet)


## You can use ngrok in this flask app ,

just uncomment this two lines :- 
1. line no. 5 from flask_ngrok_st import run_with_ngrok (first it will download ngrok on currnet directory)
2. line no. 19 run_with_ngrok(app) (and remove all arguments from app.run() )