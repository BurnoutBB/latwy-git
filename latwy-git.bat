@echo off
mode con cols=35 lines=15
title Japierdole
:poczatek
cls
echo ===================================
echo.
tree | findstr /v "Folder PATH listing Volume serial number"
echo.
echo ===================================
echo.
set /p p="wybierz repozytorium: "
cls
cd %p%
cd
cls
:czynnosc
cls
echo ===================================
echo.
echo    1 = Pull
echo    2 = Push
echo    3 = Commit
echo    4 = Add
echo    5 = Branch
echo    6 = Klonuj
echo.
echo    7 = Powrut
echo.
echo ===================================
echo.
set /p c="Wybierz czynnosc: "
if %c% == 1 goto pull
if %c% == 2 goto push
if %c% == 3 goto commit
if %c% == 4 goto add
if %c% == 5 goto branch
if %c% == 6 goto klonuj
if %c% == 7 goto wruc
:pull
cls
git pull 
goto czynnosc
:push
cls
git push
goto czynnosc
:commit
cls
set /p m="Commit: "
git commit -m "%m%" -a
goto czynnosc
:add
cls
git add .
goto czynnosc
:wruc
cls
cd ..
goto poczatek
:klonuj
cls
set /p l="Link do repozytorium: "
cd ..
git clone %l%
goto poczatek
:branch
cls
echo ===================================
echo.
echo    1 = dev
echo    2 = main
echo    3 = beta
echo.
echo ===================================
set /p b="Wybierz branch: "
if %b% == 1 goto dev
if %b% == 2 goto main
if %b% == 3 goto beta
:dev
git checkout dev
goto czynnosc
:main 
git checkout main
goto czynnosc
:beta 
git checkout beta
goto czynnosc

