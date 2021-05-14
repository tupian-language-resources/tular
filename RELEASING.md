# Releasing https://tular.clld.org

0. Checkout appropriate releases of the constituent databases:
   ```shell
   git -C ../tu(led|det) tag
   git -C ../tu(led|det) checkout <tag>
   ```
1. Recreate the database:
   ```shell
   clld initdb development.ini --cldf ../tuled/cldf/cldf-metadata.json --glottolog ../../glottolog/glottolog
   ```
2. Run the tests:
   ```shell
   pytest
   ```
3. Commit and push all changes in tupian-language-resources/tular and reset db repos
   to master|main.
4. Deploy

