# Simulation-and-Modeling-Course---QueueSimApp
A Python-based simulation app for queueing systems with visualization, built using Tkinter, Matplotlib, and Seaborn, dedicated to improve the real process of queueing based on useful results extracted from the given data.
#**QueueSimApp**

## How to Use the Application

Follow these steps to set up and run the application on your system:


**Follow these steps to set up and run the application on your system:**

**1. Install Python**

- On Windows

. Download Python from the [the official Python website](https://www.python.org/downloads/) and run the installer.

. Ensure you download Python version 3.6 or above.

. During installation, check the option to add Python to your PATH.

. Verify the installation by opening Command Prompt and running:

```

python --version

```

- On Linux

. Use your package manager to install Python. For example:

```
    sudo apt update
    sudo apt install python3 python3-pip
```

. Verify the installation:

```

python3 --version

```
- On macOS

. Install Python using Homebrew or download it from the official Python website.

```

   brew install python

```

. Verify the installation:

```

python3 --version

```





**2. Install Required Packages**

The application relies on several Python libraries. Install them using the following steps:

Open your terminal or command prompt.

Use the following command to install the required packages:


```

   pip install matplotlib seaborn pandas numpy tkinter

```


Alternatively, create a requirements.txt file with the following content and use it for installation:

```

  tkinter
  matplotlib
  seaborn
  pandas
  numpy

```

Install all packages at once with:

```   

  pip install -r requirements.txt

```


**3. Run the Application**

 . Save the provided Python code in a file named queue_simulation_app.py.
 
 . Execute the file in your terminal:
 
```

python queue_simulation_app.py

```


***The application window will appear, allowing you to input simulation parameters and view results.***







**4. Application Controls**

Input Parameters:
 
  . Average number of arrivals (λ): Specify the arrival rate.
  
  . Average number served per minute (μ): Specify the service rate.
  
  . Number of customers: Define the number of customers in the simulation.
  
  . Number of servers: Specify the number of available servers.
  
  . Run Simulation: Click the Run Simulation button or press Enter to execute the simulation.
  
  . Navigation: Use the Next Plot and Previous Plot buttons or the Right and Left arrow keys to navigate through plots.
  
  . Exit Application: Click Done or press Esc to close the application.


***Now you're ready to use QueueSimApp to simulate queue systems and analyze the results!***

