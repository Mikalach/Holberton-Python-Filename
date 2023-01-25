# Holberton-Python-File-Creator

## File description
- AliasCreator.sh:
  - Shell Script that create an alias to easily launch the programm
  - Alias: "template"
  - ❗each use of the script will create a template variable: may flood the ~/.bashrc after many uses

- main.py:
  - Create each Holberton School file from the HTML source of the intranet website
  - Create a README.md with most .py file (need to be double checked and completed if desired)
  - Fill most Holberton School file with "#!/usr/bin/python3" and the corresponding prototype
  - chmod u+x every file

- SourceCod:
  - test file filled with the HTML source code of the intranet page on you current project


## How to use

Only the first time:
- Clone the repo into your environement : 
  ```bash
  git clone https://github.com/AlexandreGRN/Holberton-Python-Filename.git
  ```
- Launch AliasCreator.sh (./AliasCreator.sh)

Before each use:
- Create the holberton directory of the corresponding project
- In the new holberton directory use `template` command, it will open a text file
- Open 1 project in intranet page (exemple: https://intranet.hbtn.io/projects/####)
- Open the source page (`CTRL + U` or right click 'Source Page')
- Copy everything on the Source Page (`CTRL + A` and `CTRL + C` (select all + copy all command))
- Paste it into the opened text-file (`CTRL + V`)
- Save and quit
