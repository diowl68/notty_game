# NottyGame
A simple card game called Notty using Pygame package

# Development Setup

1. You need git (install it if you don't have it already)

2. Clone this repository
```bash
git clone https://github.com/Winipedia/notty_game.git
```

3. You need python 3.12 (install it if you don't have it already, later python versions are not 100% supported yet by Pygame)

3. You need poetry (install it if you don't have it already)

4. you need VSCode or another IDE like PyCharm (install it if you don't have it already)

5. Open the project in your IDE

6. Install dependencies via terminal in the project directory (Can and should be done via the Terminal in the IDE as well)
```bash
poetry install
```

7. First Contribution:
    - open pyproject.toml
    - add yourself as an author in the project section
    - add your name and email to the end of the authors list

8. Commit your changes
```bash
git add pyproject.toml
git commit -m "Add myself as an author"
```
If you get a pre commit error run with --no-verify flag
```bash
git commit -m "Add myself as an author" --no-verify
```

9. Create a pull request(PR)
Branch protection is active. You cannot just push to main. You need to create a PR and get it approved by a maintainer.
```bash
# make a new branch
git checkout -b add-myself-as-author
# push the branch
git push origin add-myself-as-author
```

10. Git will output a URL. Open it in your browser to create a PR.



