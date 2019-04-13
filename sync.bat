git add *
git commit -m"update heruku project URL"
git push 
git push heroku master
heroku ps:scale web=1
heroku logs