from setuptools import setup

with open("README.md", "r",encoding="utf-8") as f:
    long_description=f.read()
    
REPO_NAME="Books_Recommender_System"
AUTHOR_NAME="RohanKhodade"
SRC_REPO="src"
LIST_OF_REQUIREMENTS=["streamlit","numpy","scipy","scikit-learn"]

setup(
    name=SRC_REPO,
    version="0.0.1",
    authpr=AUTHOR_NAME,
    description="This is a books recommender system",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    author_email="rohankhodade883@gmail.com",
    packages=[SRC_REPO],
    python_requires="<=3.10",
    install_requires=LIST_OF_REQUIREMENTS,
)