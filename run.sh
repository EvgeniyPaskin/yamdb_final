rm -f /code/pytest.ini
rm -rf /code/tests

cp pytest.ini /code/pytest.ini
cp -a tests/ /code/tests

cd /code
pip3 install -r requirements.txt
pytest --tb=line 1>&2
