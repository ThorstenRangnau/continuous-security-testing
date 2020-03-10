FROM rvanbuijtenen/bdd-security
ENV URL=https:\/\/vulnerable-api:8080
CMD sed -E -i "s/<baseUrl>.+<\/baseUrl>/<baseUrl>$URL<\/baseUrl>/" config.xml && ./gradlew -Dcucumber.options="--tags ${TAGS} --tags ${TAGS_SKIP}"

