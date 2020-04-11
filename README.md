# webscrapers

A collection of example script for create crawlers which crawling data for practice or make a dataset collection and ...etc

## Quickstart

Start Docker compose for a simple demo

```
docker-compose up
```

Results

```
gh-crawler_1      | Crawling a github profile...
gh-crawler_1      | ============================
gh-crawler_1      | {
gh-crawler_1      |     "github": "https://github.com/quan-vu",
gh-crawler_1      |     "fullname": "Quan Vu",
gh-crawler_1      |     "bio": "Backend Engineer working on Microservices system with Python/Flask/Django & Kubernetes. Learning AI Specialist.",
gh-crawler_1      |     "avatar": ""
gh-crawler_1      | }
gh-crawler_1      | ============================
gh-crawler_1      | Stop web driver
webscrapers_gh-crawler_1 exited with code 0
py3.6-selenium_1  | Find and click top-right button ... ok
py3.6-selenium_1  | test_case_2 (__main__.TestTemplate)
py3.6-selenium_1  | Find and click Learn more button ... ok
py3.6-selenium_1  | 
py3.6-selenium_1  | ----------------------------------------------------------------------
py3.6-selenium_1  | Ran 2 tests in 17.822s
py3.6-selenium_1  | 
py3.6-selenium_1  | OK
```

Result of **test_github_script.py**

![](py3.6-selenium/test_github_profile_repositories.png)
