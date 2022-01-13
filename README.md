# Bridging the Gap: CSE6242_Team054_Project

![Bridging the Gap Logo](./CODE/app/static/Images/github_readme_lead.png)

---

Local Installation Video Demonstration: https://www.youtube.com/watch?v=cOb_mOdR_Qk

## Description

Welcome to Team 54's repository for the Fall 2021's CSE6242 Data & Visual Analytics final project. This project focuses on the modeling and visualization of United States bridge infrastructure data. 

The project is built as a web application, which is accessible via the following link: [http://bit.ly/BridgingTheGapTeam54](http://bit.ly/BridgingTheGapTeam54). **The code contained within this repository is therefore not necessary to access our visualizations or modeling output.** However, it is available in this repository for eager contributors or anyone interested in looking behind the scenes.  

## Installation of Local Web Application (Optional)

The fully-functional web application (including visualizations and modeling results) is available, without local installation, at the following link: [http://bit.ly/BridgingTheGapTeam54](http://bit.ly/BridgingTheGapTeam54)

If you chose to install run the application locally however, we you will first need to install the Python package manager [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

Once Conda is installed, open an Anaconda/terminal prompt session and create a new enviornment using the requirements.txt file contained in the repository root:

```bash
conda create -n bridging-the-gap --file requirements.txt
```

Next, activiate this new Conda environment with the following command:

```bash
conda activate bridging-the-gap # activate our environment
```

You can now navigate to the Flask application's root directory (`/CODE/app/`) and start the application:

```bash
cd CODE/app/ # navigate to the Flask app's directory
python main.py # start the Flask application
```

Flask will now launch a local web server on your computer. By default this will be accessible via any major web browswer by navigating to the following url: https://localhost:5000

Note: If port 5000 is already in use for another process, the application will simply launch on another port; this alternative port will be printed in the terminal window after running the `main.py` script. 
 
Once you are finished viewing the application, you can use the `CTRL-C` keystroke to terminate the local webserver and terminal session. 
 
For additional information on Flask, Conda, and Python see our tutorials section below.

## Execution

Whether you navigate to the public website or run the application locally, you will first be presented with the Bridging the Gap homepage in your browswer. 

![Bridging the Gap Homepage](../main/CODE/app/static/Images/bridging_gap_homepage.png)

Use the navigation bar or the links on the homepage to view our interactive visualizations, modeling information, or information about our project/team.

## Modeling & Supporting Code Usage (Optional)  

The code used to generate our project's neural network models utilizes PyTorch and TensorFlow, which require very specific versions, dependencies, and drivers; these are highly platform-specific and, in the case of this project, is only guaranteed to run on Nvidia GTX & RTX GPUs with 64-bit Windows 10/11 under the modeling conda environment given below. **All modeling output is available via the web application (detailed above) and therefore it is not necessary to run this modeling code directly.** Your experience running this modeling code will depend on your platform and specific hardware. If you have hardware that is not compatible with the modeling conda environment, conda will let you know that the installation was not successful. In such a situation, if you still wish to run the modeling code locally, we recommend consulting outside resources for instructions on how to download, install, and compile the latest version of TensorFlow. If your local hardware does not include a reasonably modern and robust GPU or CPU, it is not recommended for you to run the code locally. Given the scripts dependence on multiprocessing it could take an extremely large amount of time to run these files without the proper hardware capacity.

If do you plan to run some of the modeling locally, you will need to download the zipped pickles of the random forest models and raw data files from this Dropbox [link](https://www.dropbox.com/sh/253esns4km760qq/AABz9fWzaoK2AzJsVrcsAMvRa?dl=0). Due to their size, they are not hosted directly within the repository even in compressed form.

To run this code, first navigate to the `CODE/Modeling/` directory and create a new Conda environment using the `requirements.txt` in this directory:

```bash
cd CODE/Modeling/
conda create -n bridging-the-gap-modeling --file requirements.txt
```

Next, activate this new Conda environment with the following command:

```bash
conda activate bridging-the-gap-modeling # activate our environment
```

It is easiest to use a JupyterLab session to optionally explore, run, and view all of the code contained within the repository. To activate JupyterLab, use the following command: 

```bash
jupyter lab
```

For additional information on JupyterLab/Jupyter Notebooks see our tutorials section below.

## Tutorials

If you aren't familiar with some of the technologies or languages used within our project, that's perfectly fine. Below we have listed a few links to popular resources to better understand, utilize, and operate all aspects of our repository.

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html)
- [Python](https://docs.python.org/3/tutorial/)
- [JupyterLab/Jupyter Notebooks](https://jupyterlab.readthedocs.io/en/stable/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/tutorial/index.html)
- [Sklearn](https://scikit-learn.org/stable/tutorial/index.html)
- [SQL/SQLAlchemy](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)
- [Pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/tutorials.html)
- [Numpy](https://numpy.org/doc/stable/user/quickstart.html)
- [Tensorflow](https://www.tensorflow.org/tutorials)
- [D3](https://d3js.org/)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

We use a standard [MIT](https://choosealicense.com/licenses/mit/) license please see the link for further details.
