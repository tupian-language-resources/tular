# Releasing https://tular.clld.org

1. Recreate the database:
   ```shell
   clld initdb development.ini --cldf ../tuled/cldf/cldf-metadata.json --glottolog ../../glottolog/glottolog
   ```
2. Run the tests:
   ```shell
   pytest
   ```
3. Commit and push all changes in tupian-language-resources/tular
4. Deploy

