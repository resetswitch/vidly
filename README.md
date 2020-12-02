# Vidly
Is a proof of concept video rental website.
It is a Django (python based) website hosted on Heroku. Due a free tier limitation, only 1 person can view it at a time.

Website: https://aqueous-meadow-77455.herokuapp.com/

### Features

- Customized Layout (HTML)
- Shared Template Across Website (Header Banner)
- URL paramters (ex. '.../movies/1' where 1 is the ID of a movie)
- Exception Handling (ex. http://127.0.0.1:8001/movies/10 is a 404 error)
- Referencing URLs (ex. [The Terminator](https://aqueous-meadow-77455.herokuapp.com/movies/1))
- Django Admin

### Pictures

Hover cursor to see captions
<p>
  <img src=https://github.com/resetswitch/Images_for_Projects/blob/main/Vidly/Vidly_1.png width=400 title="Vidly Homepage">
  <img src=https://github.com/resetswitch/Images_for_Projects/blob/main/Vidly/Vidly_2.png width=400 title="Vidly Movies Database">
  <img src=https://github.com/resetswitch/Images_for_Projects/blob/main/Vidly/Vidly_3.png width=400 title="Vidly Movie Details">
  <img src=https://github.com/resetswitch/Images_for_Projects/blob/main/Vidly/Vidly_admin.gif width=400 title="Vidly Admin">
</p>



### Django SECRET_KEY
`SECRET_KEY` is located in two places:
1. `SECRET_KEY`is stored in [vidly > vidly > config.txt]. However, the file is never referenced, and is there just for reminder purposes. This is a personal preference.
2. `SECRET_KEY`is stored as a environment variable due to Heroku's preference.

##### To Store and Environment Variable

A short refresher on how to make an environment variable.

In the terminal while inside the project virtual environment
```bash
(venv) $ heroku config:set SECRET_KEY="YOUR_SECRET_KEY_VALUE"   
```

and then within your settings.py file

[vidly > vidly > settings.py]

```python
...
SECRET_KEY = os.getenv('SECRET_KEY')
...
```
