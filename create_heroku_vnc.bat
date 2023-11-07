@REM git clone https://github.com/melodic456/chrome-novnc.git
@REM cd chrome-novnc
rmdir /s /q .git
git init
git add .
git commit -m "Initial commit"
heroku create shaf-chrome-3 --region eu
heroku stack:set container
git push heroku master
