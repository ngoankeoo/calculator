Web application Calculator 
1. Install requirement 
```
pip install -r requirement.txt
```
2. Run 
```
python3 main.py
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