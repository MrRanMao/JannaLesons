# Janna Lessons


 1186  cd JannaLesons
 1187  python3 -m venv ./env
 1188  source ./env/bin/activate
 1189  pip3 install django
 1190  django-admin
 1191  django-admin startproject config
 1192  mv config config_rm
 1193  cd config_rm
 1194  ls -la
 1195  cp -r * ../
 1196  cd ..
 1197  ls -la
 1198  rm -rf ./config_rm
 1199  ls -la
 1200  ./manage.py
 1201  ./manage.py startapp Blog
 1202  ./manage.py migrate
 1203  ./manage.py createsuperuser 
 1204  ./manage.py runserver
 1205  ./manage.py makemigrations
 1206  ./manage.py migrate
 1207  ./manage.py runserver
 1208  ./manage.py shell
 1209  ./manage.py makemigrations
 1210  ./manage.py migrate
 1211  ./manage.py runserver
 1212  mkdir tmeplates
 1213  rm -rf tmeplates
 1214  mkdir templates
 1215  ./manage.py
 1216  python3
 1217  pip3 install telebot
 1218  pip3 install pytelegrambotapi
 1219  ./manage.py telegram_bot
 1220  ./manage.py runserver
 1221  ./manage.py telegram_bot
 1222  pip3 freeze > requirements.txt
 1223  pip3 install psycopg2-binary
 1224  pip3 freeze > requirements.txt