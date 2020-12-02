# Vidly
Is a proof of concept video rental website.
It is hosted on Heroku. Due a free tier limitation, only 1 person can view it at a time.
Website: https://aqueous-meadow-77455.herokuapp.com/

# SECRET_KEY
`SECRET_KEY` is located in two places:
1. `SECRET_KEY`is stored in [vidly > vidly > config.txt]. However, the file is never referenced, and is there just for reminder purposes. This is a personal preference.
2. `SECRET_KEY`is stored as a environment variable due to Heroku's preference.

##### To Store and Environment Variable

A short refresher on how to make an environment variable.

In the terminal in the virtual environment
```bash
(env) $ heroku config:set SECRET_KEY="YOUR_SECRET_KEY_VALUE"   
```

and then within your settings.py file

[vidly > vidly > settings.py]

```python
...
SECRET_KEY = os.getenv('SECRET_KEY')
...
```
