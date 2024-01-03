git add *
git commit -m "changes"
git push
cd ..
jupyter-book build --all ADbook/ 
cd ADbook
ghp-import -n -p -f _build/html
