    History of creating task 1.1
    
    git clone https://github.com/nikyta384/DevOps_online_Dnipro_2022Q1Q2
    mkdir task1.1
    touch readme.txt
    git add .
    git commit -m "Init commit"
    git checkout -b develop
    touch index.html
    git add .
    git commit -a -m "Empty index.html file"
    git branch -b images
    git checkout -b images
    mkdir images
    git add .
    git commit -m "Images"
    nano index.html 
    git commit -a -m "Added Images"
    git checkout -b styles
    mkdir styles
    touch style.css
    nano style.css 
    git add .
    git commit -a -m "Style"
    nano style.css 
    nano index.html 
    git checkout images
    git commit -a -m "Added styles"
    git checkout images
    nano index.html 
    git add .
    git commit -a -m "Fixed file Index.html"
    git checkout develop
    git merge images
    git merge styles
    nano index.html
    git add .
    git commit -a -m "Conflict resolved"
    git checkout master
    git merge develop
    git log --help
    git log 
    git push origin --all
    git reflog >>task1.1_GIT.txt
    git add task1.1_GIT.txt 
    git commit -a -m "new task1.1_GIT.txt file"
    git push 
