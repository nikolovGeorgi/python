gnikolov@Georgis-MacBook-Pro UofS (master) $ touch fact.py
gnikolov@Georgis-MacBook-Pro UofS (master) $ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	./

nothing added to commit but untracked files present (use "git add" to track)
gnikolov@Georgis-MacBook-Pro UofS (master) $ cd ..
gnikolov@Georgis-MacBook-Pro python (master) $ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	UofS/

nothing added to commit but untracked files present (use "git add" to track)
gnikolov@Georgis-MacBook-Pro python (master) $ git add . UofS/
gnikolov@Georgis-MacBook-Pro python (master) $ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   UofS/fact.py

gnikolov@Georgis-MacBook-Pro python (master) $ git commit -m "Added factorial stub function."
[master 5104c13] Added factorial stub function.
 1 file changed, 10 insertions(+)
 create mode 100644 UofS/fact.py
gnikolov@Georgis-MacBook-Pro python (master) $ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   UofS/fact.py

no changes added to commit (use "git add" and/or "git commit -a")
gnikolov@Georgis-MacBook-Pro python (master) $ git add .
gnikolov@Georgis-MacBook-Pro python (master) $ git commit -m "Coded up a recursive implementation of factorial."
[master b054e22] Coded up a recursive implementation of factorial.
 1 file changed, 4 insertions(+), 1 deletion(-)
gnikolov@Georgis-MacBook-Pro python (master) $ git add fact.py
fatal: pathspec 'fact.py' did not match any files
gnikolov@Georgis-MacBook-Pro python (master) $ git status
On branch master
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   UofS/fact.py

no changes added to commit (use "git add" and/or "git commit -a")
gnikolov@Georgis-MacBook-Pro python (master) $ git add .
gnikolov@Georgis-MacBook-Pro python (master) $ git commit -m "Replaced the recursion in factorial() with a loop."
[master 0646df4] Replaced the recursion in factorial() with a loop.
 1 file changed, 4 insertions(+), 4 deletions(-)
gnikolov@Georgis-MacBook-Pro python (master) $ cd UofS/
gnikolov@Georgis-MacBook-Pro UofS (master) $ git diff HEAD~1 HEAD -- fact.py
diff --git a/UofS/fact.py b/UofS/fact.py
index f480307..69804be 100644
--- a/UofS/fact.py
+++ b/UofS/fact.py
@@ -7,7 +7,7 @@ def factorial(n):
     Return:
         a non-negative integer
     '''
-    if n == 0:
-        return 1
-    else:
-        return n * factorial(n-1)
+    prod = 1
+    for i in range (1, n):
+        prod = prod * i
+    return prod
gnikolov@Georgis-MacBook-Pro UofS (master) $ git add fact.py
gnikolov@Georgis-MacBook-Pro UofS (master) $ git commit -m "Fixed calculation error in factorial() loop version"
[master fafe19f] Fixed calculation error in factorial() loop version
 1 file changed, 3 insertions(+), 2 deletions(-)
gnikolov@Georgis-MacBook-Pro UofS (master) $ git diff HEAD~1 HEAD -- fact.py
diff --git a/UofS/fact.py b/UofS/fact.py
index 69804be..15a9e18 100644
--- a/UofS/fact.py
+++ b/UofS/fact.py
@@ -8,6 +8,7 @@ def factorial(n):
         a non-negative integer
     '''
     prod = 1
-    for i in range (1, n):
-        prod = prod * i
+    while n >= 1:
+        prod = prod * n
+        n = n - 1
     return prod
gnikolov@Georgis-MacBook-Pro UofS (master) $
