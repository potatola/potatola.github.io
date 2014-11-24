if [ $# == 0 ]; then
    echo "don't forget the commit description"
    exit 0
fi
git add .
git commit -m "$1"
git push origin source