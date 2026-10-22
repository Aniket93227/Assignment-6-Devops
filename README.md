# Assignment 7: Continuous Integration Using Jenkins and GitHub

A small, dependency-free Python application used to demonstrate source checkout, build validation, tests, and Pipeline as Code.

## Requirements
- Jenkins running locally (the previous assignment used `http://localhost:8080`)
- Git installed and available on PATH
- Python 3 installed on the Jenkins machine and available as `python`
- Jenkins plugins: Pipeline and Git (install from Manage Jenkins → Plugins if missing)
- GitHub repository with this project committed to the `main` branch

## Project files
- `app.py`: tiny application function
- `test_app.py`: automated tests using Python's standard-library `unittest`
- `Jenkinsfile`: declarative pipeline with Checkout, Build, and Test stages

## Run the tests locally
From this folder:
```powershell
python -m unittest -v
```

## Configure Jenkins
1. Ensure Git is installed on the computer where Jenkins runs. For the Windows Jenkins service, restart the Jenkins service after installing Git or Python so the service refreshes its PATH.
2. In Jenkins, go to Manage Jenkins → Plugins and make sure the **Git** and **Pipeline** plugins are installed.
3. On the Jenkins dashboard, click **New Item**.
4. Enter `Assignment-7-CI-GitHub`, select **Pipeline**, and click **OK**.
5. Under **Pipeline**, set **Definition** to **Pipeline script from SCM**.
6. Set **SCM** to **Git** and Repository URL to your repo URL, e.g. `https://github.com/USERNAME/REPOSITORY.git`.
7. Set Branch Specifier to `*/main` (change it if your repository uses another default branch).
8. Set Script Path to `Jenkinsfile`, then click **Save**.
9. Click **Build Now** and inspect **Console Output**. The checkout stage should retrieve the repository; build and test stages should succeed.

## Demonstrate change detection
1. Change the success message in `app.py` or add an additional assertion in `test_app.py`.
2. Commit and push the change to the GitHub default branch.
3. Click **Build Now** in Jenkins and verify the new commit is checked out and tests run against it. This manual build demonstrates re-checkout; automatic triggering requires a GitHub webhook or Jenkins polling configuration.

## Test a deliberate failure (then restore)
Temporarily change the expected value in `test_app.py` so it no longer matches the application result. Push the change and run Jenkins. The Test stage should fail and Console Output should show a failed assertion. Restore the correct expected value, commit and push, then run the pipeline again; it should return to SUCCESS.

## Notes and troubleshooting
- This example uses Python's standard library, so it needs no pip dependencies.
- The Jenkins Windows service must be able to find `git` and `python`. Check the versions in a terminal and restart the Jenkins service after PATH changes.
- A public repository can usually be checked out without credentials. For private repositories, create credentials in Jenkins Credentials and reference them in the job; never store tokens in this repository.
- The sample does not configure a webhook automatically. Manual builds are enough to demonstrate updated checkout; use GitHub webhook or polling only if automatic triggering is specifically required.
