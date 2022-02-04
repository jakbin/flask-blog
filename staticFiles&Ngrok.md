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

## You can use ngrok in this flask app ,

just uncomment this two lines :- 

1. line no. 5 from flask_ngrok_st import run_with_ngrok (first it will download ngrok on currnet directory)
2. line no. 19 run_with_ngrok(app) (and remove all arguments from app.run() )