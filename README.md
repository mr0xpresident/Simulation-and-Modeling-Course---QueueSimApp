# Simulation-and-Modeling-Course---QueueSimApp
A Python-based simulation app for queueing systems with visualization, built using Tkinter, Matplotlib, and Seaborn, dedicated to improve the real process of queueing based on useful results extracted from the given data.
#**QueueSimApp**
#My 2 cents Mohamed Sayed
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



**5. Understanding the Output**


_After running the simulation, the application provides two types of outputs: plots and the results TextBox._

**- Plots:**
  
    The application generates visualizations to help analyze the queue system:

    .Inter-arrival Time Distribution:
    
        This plot shows the time intervals between consecutive arrivals in the system, It follows an exponential distribution if arrivals are Poisson-distributed.
    
    .Service Time Distribution:
    
        Displays the time taken to serve each customer, The shape of this plot depends on the service rate (μ) and the distribution used.
    
    .Queue Length Over Time:
    
        This time-series plot shows how the number of customers in the queue evolves during the simulation, Peaks indicate periods of high congestion.
    
    .Customer Wait Time Distribution:
    
        A histogram of the waiting times for all customers, Helps to identify patterns or outliers in wait times.
    
    .Server Utilization:
    
        Visualizes how busy the servers were during the simulation, High utilization indicates efficiency but might suggest the need for more servers to prevent overloading.


**- Results TextBox:**
    
The application provides a detailed summary of key statistics at the end of each simulation. These metrics are displayed as text output and help evaluate the performance of the queueing system.

******Statistics Summary******

    .Average Waiting Time:
    
         The average time a customer spends waiting in the queue before being served.
    
    .Probability of Customer Waiting:
    
        The proportion of customers who had to wait in the queue.
    
    .Average Service Time:
    
        The average time a server spends serving a customer.
    
    .Probability of Idle Server:
    
        The likelihood that a server was idle during the simulation.
    
    .Average Time Between Arrivals:
    
        The mean time interval between consecutive customer arrivals.
    
    . Average Waiting Time for Those Who Wait:
    
        The average wait time for customers who experienced a delay in the queue.
    
    .Average Time Customer Spends in the System:
    
        The total average time a customer spends in the system, including waiting and service time.
    
    .Expected Metrics
        The results also include additional expected performance metrics for the queueing system:
    
    
    .Time Between Arrivals:
    
        The observed mean time between customer arrivals.
    
    .Service Time (1/µ):
    
        The mean service time, based on the server's service rate.
    
    .Server Utilization (c):
    
    
        The proportion of server capacity that was actively utilized.
    
    .Expected Waiting Time in Line (Wq):
    
    
        The average waiting time customers spent in the queue.
    
    .Expected Time Spent in the System (Ws):
    
    
         The total average time a customer spends in the system.
    
    .Expected Number of Customers in Line (Lq):
    
    
        The average number of customers waiting in the queue.
    
    .Expected Number of Customers in the System (Ls):
    
    
        The average number of customers present in the system at any time.
    
    . Expected Number of Occupied Servers:
    
    
        The average number of servers actively serving customers.

__**You can include these metrics to analyze the performance of the system under various conditions and identify bottlenecks or opportunities for optimization.**__
