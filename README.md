## Vista Testing Framework (VTF)
Version 1.009

#### Mirror a repository
Create an exact duplicate of vista test and mirror to https://github.com/VistaStaff/vtf:

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

