read -p "input comment:" comment
git add -A .
git commit -m "$comment"
git pull
git push origin source
