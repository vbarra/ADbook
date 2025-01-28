git config http.postBuffer 524288000
git add *
git commit -m "changes"
git push
jupyter-book build  --all . 
ghp-import -n -p -f _build/html
