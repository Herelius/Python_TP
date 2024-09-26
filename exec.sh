
PYTHON_EXEC=python
PROTOCOL=http
HOSTNAME=google.com
URI=/fr
THRESHOLD=10

echo Exec params:
echo ===========================================================================================
echo PROTOCOL = $PROTOCOL
echo HOSTNAME = $HOSTNAME
echo URI = $URI
echo THRESHOLD = $THRESHOLD
echo ===========================================================================================
echo 
echo 
echo Execute main script:
echo ===========================================================================================
$PYTHON_EXEC main.py --protocol $PROTOCOL --hostname $HOSTNAME --uri $URI --threshold $THRESHOLD
echo ===========================================================================================
echo ""
echo ""
echo Execute tests:
echo ===========================================================================================
$PYTHON_EXEC tests/test_format_url.py
echo ===========================================================================================
echo END
