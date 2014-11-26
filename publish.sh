if [ $# == 0 ]; then
    echo "don't forget the commit description"
    exit 0
fi
pelican content -s pelicanconf.py
ghp-import -b master -m "$1" output
git push origin master:master -f