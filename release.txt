wget -O ./index.html  --post-data="rss_feed=https://www.sme.sk/rss-title&sort=Sort+feed+by+date" https://webpub.herokuapp.com/
curl -T ./index.html  -u webpubjecoolnet:Abcde123 ftp://endora.endora.cz