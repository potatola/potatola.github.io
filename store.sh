git pull
read -p "input comment:" comment
git add -A .
git commit -m "$comment"
git push origin source
