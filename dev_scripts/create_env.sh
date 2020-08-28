
#%%writefile make_conda_env.sh
#!/usr/bin/env bash
# author: github.com/ruxi
# reproducibly create conda env

read -p "Create new conda env (y/n)?" CONT

if [ "$CONT" == "n" ]; then
  echo "exit";
else
# user chooses to create conda env
# prompt user for conda env name
  env_name='wrike'
  echo "Creating new conda environment, named $env_name"

  # Create environment.yml or not
  read -p "Create 'enviroment.yml', will overwrite if exist (y/n)?"
    if [ "$CONT" == "y" ]; then
      # yes: create enviroment.yml
      echo "# BASH: conda env create
# source activate wrike
name: $env_name
channels:
  - conda-forge
dependencies:
  # python
  - pytest
  - pytest-cov
  - python >= 3.7
  - tqdm
  - beautifulsoup4
  # pydata
  - matplotlib
  - numpy
  - pandas >= 1.0.0
  - pandas-datareader = 0.8.0
  - scikit-learn
  - scipy
  - seaborn
  - statsmodels
  # jupyter
  - ipykernel
  - jupyter
  - jupyter_contrib_nbextensions
  - jupyter_nbextensions_configurator
  - jupytext
  - nb_conda
  - nb_conda_kernels
  # NLP
  - nltk
  - SpaCy
  # Misc
  - pylint
  - git">environment.yml    
    
  #list name of packages
  conda env create
    else
        echo "installing base packages"
        conda create --name $env_name\
        python=3.7 jupyter notebook numpy rpy2\
        pandas scipy numpy scikit-learn seaborn 
    fi
  echo "to exit: source deactivate"
fi

