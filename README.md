# orch
Service registry with IaC config generation


# Clean Way to Install
* install pyenv and pyenv-virtualenv
    * `brew install pyenv`
    * `brew isntall pyenv-virtualenv`
* create a python env
    * `pyenv install 3.7.0` 
    * `pyenv virtualenv 3.7.0 orchcli-3.7.0`
* add pyenv detection to your shell
    * `echo 'eval "$(pyenv init -)"' >> ~/.bashrc`
    * `echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash`
* prep the app
    * checkout the project
    * `cd orch`
    * `pip install -r requirements.txt`
* install postgres database locally ( must be postgres | not needed for just the cli)
* run the db upgrade
    * `export FLASK_APP=app.py`
    * `export FLASK_DEBUG=1 #if you want the code to autoreload after you make changes`
    * set the appropriate environment variables needed in `base.py`
    * `flask db upgrade`
* run the application
    * `flask run`
* use the app
    * [GUI](http://localhost:5000/admin)
    * [REST](http://localhost:5000/api)
    

# CLI
* install argcomplete in your shell
  ```
  activate-global-python-argcomplete --dest=- > $HOME/.argcomplete
  echo "source \$HOME/.argcomplete" >> $HOME/.bashrc
  ```
* Enjoy tab completion