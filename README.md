# Project Overview

This project aims to explore and understand the reasons behind candidates not attending their scheduled appointments with companies after applying for job positions. Despite receiving appointment offers, a significant portion of candidates fail to show up. The project seeks to answer the critical question: Why do candidates not attend their appointments, and what can be done to improve attendance rates?

## Structure of the Workspace

The workspace is organized into several key components essential for conducting a thorough analysis:


- **analysis_script.py**: A Python script that contains a clean and executable version of the analysis performed in the Jupyter Notebook. It includes data preprocessing, visualization, and analysis steps.
- **notebooks/**: Contains a Jupyter Notebook (`analysis.ipynb`) that details the analysis process step-by-step, including visualizations and explanations.
- **requirements.txt**: Lists all the Python libraries required to run the project. This file facilitates easy installation of dependencies for anyone looking to run the project.

## Project Goals

The primary objective of this project is to identify the factors contributing to the high no-show rate among candidates who receive appointment offers from companies. By analyzing the data and identifying patterns, the project aims to provide insights into:

1. The reasons behind candidates not attending their appointments.
2. Potential strategies that companies can implement to encourage candidates to attend their appointments.

## How to Run the Project

To run this project, follow these steps:

1. Ensure that Python and pip are installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory and install the required Python libraries using the command:

pip install -r requirements.txt

4. Activate the virtual environment suitable for your operating system found in the `yirmidort/Scripts/` directory.
5. Set up the environment variables by ensuring the `.env` file contains the correct path to the dataset.
6. Run the `analysis_script.py` Python script to perform the analysis:

python analysis_script.py

7. Alternatively, you can explore the analysis step-by-step by opening the `notebooks/analysis.ipynb` Jupyter Notebook.

## Contributing

Contributions to this project are welcome. Please feel free to fork the repository, make changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is open-source and available under the [MIT License](LICENSE.md).