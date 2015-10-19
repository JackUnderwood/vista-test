# vtf
Vista Testing Framework (VTF)

To mirror a repository - create an exact duplicate of vista_test and mirror to https://github.com/VistaStaff/vtf:

$ git clone --bare https://github.com/JackUnderwood/vista-test
 # Make a bare clone of the repository

$ cd vista-test.git
$ git push --mirror https://github.com/VistaStaff/vtf
 # Mirror-push to the new repository--the mirror repository

$ cd ..
$ rm -rf vista-test.git
 # Remove the temporary local repository


-- Merge that always creates a new commit object - avoids lossing information
$ git merge --no-ff myfeature
