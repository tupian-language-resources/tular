# Releasing https://tular.clld.org

```shell
git clone https://github.com/tupian-language-resources/tular
cd tular
pip install -e .[test]
unzip tular.sql.zip
createdb tular
psql -d tular -f tular.sql
pytest
pip freeze > requirements.txt
```
