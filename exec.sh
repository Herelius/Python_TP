
PYTHON_EXEC=python
PROTOCOL=https
MY_HOSTNAME=github.com
MY_URI=Herelius
THRESHOLD=10

echo Exec params:
echo ===========================================================================================
echo PROTOCOL = $PROTOCOL
echo HOSTNAME = $MY_HOSTNAME
echo URI = $MY_URI
echo THRESHOLD = $THRESHOLD
echo ===========================================================================================
echo 
echo 
echo Execute main script:
echo ===========================================================================================
$PYTHON_EXEC main.py --protocol $PROTOCOL --hostname $MY_HOSTNAME --uri $MY_URI --threshold $THRESHOLD
echo ===========================================================================================
echo 
echo 
echo Execute tests:
echo ===========================================================================================
$PYTHON_EXEC tests/test_format_url.py
echo ===========================================================================================
echo END
