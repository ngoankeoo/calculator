Web application Calculator 
1. Install requirement 
```
pip install -r requirements.txt
```
2. Run 
```
python3 wsgi.py
```

3. Push heroku
```
heroku login
heroku create ngoankeoo-calculator
heroku buildpacks:set heroku/python
git push heroku master
// Check log
heroku logs --tail
```
4. Link web app
    
    https://ngoankeoo-calculator.herokuapp.com/
