read -p "input comment:" comment
pelican content -s pelicanconf.py
ghp-import -b master -m "$comment" output
git push origin master:master -f
