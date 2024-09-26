@echo off

set PYTHON_EXEC=python
set PROTOCOL=http
set HOSTNAME=google.com
set URI=/fr
set THRESHOLD=10

echo Exec params:
echo ===========================================================================
echo PROTOCOL = %PROTOCOL%
echo HOSTNAME = %HOSTNAME%
echo URI = %URI%
echo THRESHOLD = %THRESHOLD%
echo ===========================================================================
echo.
echo.
echo Executing main script:
echo ===========================================================================
%PYTHON_EXEC% main.py --protocol %PROTOCOL% --hostname %HOSTNAME% --uri %URI% --threshold %THRESHOLD%
echo ===========================================================================
echo.
echo.
echo Executing tests:
echo ===========================================================================
%PYTHON_EXEC% tests\test_format_url.py
echo ===========================================================================
echo.
echo END