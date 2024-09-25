
echo ""
echo "Execute main script:"
echo "========================================================================="
python3 main.py --protocol http --hostname google.com --uri /fr --threshold 1
echo "========================================================================="
echo ""
echo ""
echo "Execute tests:"
echo "========================================================================="
python3 tests/test_format_url.py
echo "========================================================================="
echo "END"
