wget -O ./index.html  --post-data="feed=https://www.sme.sk/rss-title" https://webpub.herokuapp.com/
curl -T ./index.html  -u webpubjecoolnet:Abcde123 endora.endora.cz/webpub.jecool.net/ -V
