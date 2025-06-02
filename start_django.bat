@echo off
echo --------------------------------------
echo   Spoustim Django projekt...
echo --------------------------------------

REM Aktivace virtualniho prostredi (pokud mas slozku venv)
call venv\Scripts\activate

echo --------------------------------------
echo   Delam migrace...
echo --------------------------------------
python manage.py makemigrations
python manage.py migrate

echo --------------------------------------
echo   Spoustim server...
echo --------------------------------------
python manage.py runserver

pause

