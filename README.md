## Vista Testing Framework (VTF)

## Mirror a repository
Create an exact duplicate of vista_test and mirror to https://github.com/VistaStaff/vtf:

Make a bare clone of the repository
```
$ git clone --bare https://github.com/JackUnderwood/vista-test
```

Mirror-push to the new repository--the mirror repository
```
$ cd vista-test.git
$ git push --mirror https://github.com/VistaStaff/vtf
```

Remove the temporary local repository
```
$ cd ..
$ rm -rf vista-test.git
```


## Merge
Merge that always creates a new commit object - avoids lossing information
```
$ git merge --no-ff myfeature
```
