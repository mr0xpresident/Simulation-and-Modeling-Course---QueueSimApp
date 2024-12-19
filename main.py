# Credits: Ammar Yasser , Mohamed Sayed Saad - Under supervision of Prof/ Mina S. Younnan

import sys
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')
np.random.seed(0)


class QueueSimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Queue Simulation")
        # Increase window height to accommodate results
        self.root.geometry("1000x800")

        # Input fields
        self.create_input_fields()

        # Plot frame
        self.plot_frame = ttk.Frame(self.root)
        self.plot_frame.grid(row=0, column=2, rowspan=6,
                             padx=14, pady=14, sticky="nsew")

        # Navigation buttons in a horizontal row (next to each other)
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.grid(row=6, column=2, pady=10, sticky="w")

        self.prev_button = ttk.Button(
            self.button_frame, text="Previous Plot", command=self.show_previous_plot)
        self.prev_button.grid(row=0, column=0, padx=5)
        self.prev_button.grid_remove()  # Hide until simulation is run
        # left arrow
        self.root.bind("<Left>", lambda event: self.show_previous_plot())

        self.next_button = ttk.Button(
            self.button_frame, text="Next Plot", command=self.show_next_plot)
        self.next_button.grid(row=0, column=1, padx=5)
        self.next_button.grid_remove()  # Hide until simulation is run
        # right arrow
        self.root.bind("<Right>", lambda event: self.show_next_plot())

        # Placeholder for plots
        self.figures = []
        self.current_plot_index = 0

        # Results Text Box with a scrollbar
        self.results_frame = ttk.Frame(self.root)
        self.results_frame.grid(row=8, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Adjusted text box height to make sure it fits all content and moves it up a bit
        self.results_text = tk.Text(self.results_frame, height=18, width=110)
        self.results_text.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(self.results_frame, orient="vertical", command=self.results_text.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        
        self.results_text.config(yscrollcommand=self.scrollbar.set)
    
    def create_input_fields(self):
        ttk.Label(self.root, text="Average number of arrivals (λ):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_l = ttk.Entry(self.root)
        self.entry_l.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.root, text="Average number served per minute (µ):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_mu = ttk.Entry(self.root)
        self.entry_mu.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.root, text="Number of customers:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_number_of_customers = ttk.Entry(self.root)
        self.entry_number_of_customers.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.root, text="Number of servers:").grid(
            row=3, column=0, padx=5, pady=5, sticky="w")
        self.entry_n_servers = ttk.Entry(self.root)
        self.entry_n_servers.grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(self.root, text="Run Simulation", command=self.run_simulation).grid(
            row=4, column=0, columnspan=2, pady=10)
        self.root.bind(
            "<Return>", lambda event: self.run_simulation())  # Enter key
        self.root.bind("r", lambda event: self.run_simulation()) # 'r' key

        ttk.Button(self.root, text="Done", command=self.terminate_program).grid(
            row=5, column=0, columnspan=2, pady=10)
        self.root.bind("<Escape>", lambda event: self.terminate_program())  # esc key
        self.root.bind("d", lambda event: self.terminate_program())          # d key

    def plot_utilization(self, utilization):
        # Create a figure for utilization
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.pointplot(x=utilization.index, y=utilization.values, ax=ax)
        ax.set_title('Number of Servers vs Utilization')
        ax.set_xlabel('Number of Servers')
        ax.set_ylabel('Utilization Rate of the System')
        return fig

    def run_simulation(self):
        try:
            l = float(self.entry_l.get())
            µ = float(self.entry_mu.get())
            number_of_customers = int(self.entry_number_of_customers.get())
            n_servers = int(self.entry_n_servers.get())

            self.figures, results = self.simulate_simulation(
                l, µ, number_of_customers, n_servers)
            self.current_plot_index = 0
            self.next_button.grid()  # Show the "Next Plot" button
            self.prev_button.grid()  # Show the "Previous Plot" button
            self.show_next_plot()
            self.display_results(results)
        except ValueError:
            messagebox.showerror(
                "Input Error", "Please enter valid numeric values.")

    # get the statistics for current data, nothing is generated
    def calculate_(self, inter_arrival_times, arrival_times, customers_time_service_ends, service_times, customers_time_spent_in_system, customers_wainting_time_in_queue, number_of_customers):

        time_service_begin = list(np.zeros(number_of_customers))
        system_idle = list(np.zeros(number_of_customers))
        time_service_begin[0] = arrival_times[0]
        for i in range(1, number_of_customers):
            # Time Service Begin
            time_service_begin[i] = max(
                arrival_times[i], customers_time_service_ends[i - 1])
            # Time when system remains idle
            if (arrival_times[i] > customers_time_service_ends[i - 1]):
                system_idle[i] = arrival_times[i] - \
                    customers_time_service_ends[i - 1]
            else:
                system_idle[i] = 0

        # Average waiting time
        average_waiting_time = sum(
            customers_wainting_time_in_queue) / number_of_customers

        # Probability of customer to wait
        no_customer_who_are_waiting = len(
            list(filter(lambda x: x > 0, customers_wainting_time_in_queue)))

        prob_customer_waiting = no_customer_who_are_waiting / number_of_customers

        # Average service time
        average_service_time = sum(service_times) / number_of_customers

        # Probability of idle server
        prob_ideal_server = sum(system_idle) / \
            customers_time_service_ends[number_of_customers - 1]

        # Average time between arrival
        average_time_between_arrivals = arrival_times[number_of_customers - 1] / (
            len(arrival_times) - 1)

        # Average waiting time those who wait
        average_waiting_time_those_who_wait = sum(
            customers_wainting_time_in_queue) / no_customer_who_are_waiting

        # Average time customer spent in the system
        average_time_customer_spends_in_system = sum(
            customers_time_spent_in_system) / number_of_customers

        results = ""
        results += "Average waiting time : {:.2f}".format(
            average_waiting_time) + '\n'

        results += "Probability of customer were waiting : {:.2f}".format(
            prob_customer_waiting) + '\n'

        results += "Average service time : {:.2f}".format(
            average_service_time) + '\n'

        results += "Probability of idle server :{:.2f} ".format(
            prob_ideal_server)+'\n'

        results += "Average Time Between Arrival : {:.2f}".format(
            average_time_between_arrivals) + '\n'

        results += "Average waiting time those who wait : {:.2f}".format(
            average_waiting_time_those_who_wait) + '\n'

        results += "Average time customer spent in the system : {:.2f}".format(
            average_time_customer_spends_in_system) + '\n'

        return results

    def simulate_simulation(self, l, µ, number_of_customers, number_of_servers):
        figures = []
        results_summary = "***Statistics for The Specified Inputs***\n\n"

        utilization = {}
        service_times = []
        c = 1  # counter for number of servers

        # inter_arrival_times and service_times are Only generated once, as they do not depend on the number of servers.
        # the mean of the exponential distribution is the reciprocal of the service rate µ (average number of people served per minute
        # generating inter arrival times using exponential distribution

        inter_arrival_times = list(
            np.random.exponential(scale=1 / l, size=number_of_customers))

        # Generate random service times for each customer
        service_times = list(
            np.random.exponential(scale=1 / µ, size=number_of_customers))

        while c <= number_of_servers:

            arrival_times = []  # list of arrival times of a person joining the queue
            finish_times = []  # list of finish times after waiting and being served

            arrival_times = list(np.zeros(number_of_customers))
            finish_times = list(np.zeros(number_of_customers))

            # arrival of first customer
            arrival_times[0] = round(inter_arrival_times[0], 4)

            # Generate arrival times
            for i in range(1, number_of_customers):
                arrival_times[i] = round(
                    (arrival_times[i - 1] + inter_arrival_times[i]), 4)

            # Generate finish times
            finish_times[0] = round((arrival_times[0] + service_times[0]), 4)
            for i in range(1, number_of_customers):
                previous_finish = finish_times[:i]
                previous_finish.sort(reverse=True)
                # save (slice) last c  in server
                previous_finish = previous_finish[:c]
                if i < c:
                    finish_times[i] = round(
                        arrival_times[i] + service_times[i], 4)
                else:
                    finish_times[i] = round(
                        (max(arrival_times[i], min(previous_finish)) + service_times[i]), 4)

            customers_time_spent_in_system = [
                abs(round((finish_times[i] - arrival_times[i]), 4)) for i in range(number_of_customers)]

            customers_wainting_time_in_queue = [abs(round((customers_time_spent_in_system[i] - service_times[i]), 4))
                                                for i in range(number_of_customers)]
            results_summary += 'For ' + str(c) + ' Server(s): \n\n' + self.calculate_(
                inter_arrival_times, arrival_times, finish_times, service_times, customers_time_spent_in_system, customers_wainting_time_in_queue, number_of_customers)

            # creating a dataframe with all the data of the model
            data = pd.DataFrame(
                list(zip(arrival_times, finish_times, service_times,
                     customers_time_spent_in_system, customers_wainting_time_in_queue, inter_arrival_times)),
                columns=['arrival_times', 'finish_times', 'service_times', 'customers_time_spent_in_system', 'customers_wainting_time_in_queue',
                         'inter_arrival_times'])

            # generating the timeline , and their description (arrivals, departures)
            tbe = list([0])
            timeline = ['simulation starts']
            for i in range(0, number_of_customers):
                tbe.append(data['arrival_times'][i])
                tbe.append(data['finish_times'][i])
                timeline.append('customer ' + str(i + 1) + ' arrived')
                timeline.append('customer ' + str(i + 1) + ' left')

            # generating a dataframe with the timeline and description of events
            """
            timeline: A DataFrame that tracks events in the system (e.g., arrivals, departures)
            and the number of customers (n) at each moment.
            """

            timeline = pd.DataFrame(list(zip(tbe, timeline)),
                                    columns=['time', 'Timeline']).sort_values(by='time').reset_index()
            timeline = timeline.drop(columns='index')

            # generating the number of customers inside the system at any given time of the simulation and recording idle and working times

            timeline['n'] = 0
            x = 0
            for i in range(1, (2 * number_of_customers) - 1):
                if len(((timeline.Timeline[i]).split())) > 2:
                    z = str(timeline['Timeline'][i]).split()[2]
                else:
                    continue
                if z == 'arrived':
                    x = x + 1
                    timeline['n'][i] = x
                else:
                    x = x - 1
                    if x == -1:
                        x = 0
                    timeline['n'][i] = x

            # computing time between events
            t = list()
            for i in timeline.index:
                if i == (2 * number_of_customers) - 2:
                    continue
                if i < 2 * number_of_customers:
                    x = timeline.time[i + 1]
                else:
                    x = timeline.time[i]
                y = timeline.time[i]
                t.append(round((x - y), 4))

            t.append(0)
            timeline['tbe'] = t

            # computing the probability of 'n' customers being in the system
            Pn = timeline.groupby('n').tbe.agg(sum) / sum(t)
            Tn = timeline.groupby('n').tbe.agg('count')

            # computing expected number of customers in the system
            Ls = (sum(Pn * Pn.index))

            # computing expected customers waiting in line
            Lq = sum((Pn.index[c + 1:] - 1) * (Pn[c + 1:]))

            # plots

            fig1 = plt.figure(figsize=(6, 4))
            sns.lineplot(x=data.index, y=customers_wainting_time_in_queue,
                         color='black').set(xticklabels=[])
            plt.xlabel('Customer number')
            plt.ylabel('minutes')
            plt.title('Wait time of customers with ' + str(c) + ' servers')
            figures.append(fig1)

            if c == 1:
                fig2 = plt.figure(figsize=(6, 4))
                sns.distplot(inter_arrival_times, kde=False, color='r')
                plt.title('Time between Arrivals')
                plt.xlabel('Minutes')
                plt.ylabel('Frequency')
                figures.append(fig2)

                fig3 = plt.figure(figsize=(6, 4))
                sns.distplot(service_times, kde=False)
                plt.title('Service Times')
                plt.xlabel('Minutes')
                plt.ylabel('Frequency')
                figures.append(fig3)

            fig4 = plt.figure(figsize=(6, 4))
            sns.barplot(x=Pn.index, y=Pn, color='g')
            plt.title(
                'Probability of n Customers in the System with ' + str(c) + ' Server(s)')
            plt.xlabel('number of customers')
            plt.ylabel('Probability')
            figures.append(fig4)

            # Utilization for the current number of
            """
            Utilization measures how effectively the servers are being used.
            It's the fraction of time the servers are busy serving customers as opposed to being idle.
            Utilization = Total Available Time of All Servers / Total Time Servers areBusy

            (Ls - Lq) / c:
            This calculates the fraction of servers that are actively serving customers (on average).
            In other words, it's the utilization rate for the system when c servers are used.

            The function setdefault() is used to add a key-value pair
            to the dictionary utilization only if the key does not already exist. looks like try_emplace() :) C++
            """
            utilization.setdefault(c, (Ls - Lq) / c)

            results_summary += 'Time Between Arrivals : ' + \
                str(data.inter_arrival_times.mean()) + '\n'
            results_summary += 'Service Time: (1/µ)' + \
                str(data.service_times.mean()) + '\n'
            results_summary+' Utilization (c): ' + str((Ls - Lq) / c) + '\n',
            results_summary += 'Expected wait time in line (Wq):' + str(
                data['customers_wainting_time_in_queue'].mean()) + '\n'
            results_summary += 'Expected time spent on the system (Ws):' + str(
                data.customers_time_spent_in_system.mean()) + '\n'
            results_summary += 'Expected number of customers in line (Lq):' + str(
                Lq) + '\n'
            results_summary += 'Expected number of clients in the system (Ls):' + str(
                Ls) + '\n'
            results_summary += 'Expected number of occupied servers :' + \
                str(Ls - Lq) + '\n\n'

            c += 1

        utilization = pd.Series(utilization)
        figures.append(self.plot_utilization(utilization))
        return figures, results_summary

    def terminate_program(self):
        messagebox.showinfo("Info", "Thanks For Using Our Queuing System :)")
        sys.exit()  # Exit the program

    def display_results(self, results):
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, results)

    def show_next_plot(self):
        if self.current_plot_index < len(self.figures):
            self.display_plot(self.current_plot_index)
            self.current_plot_index += 1
        else:
            messagebox.showinfo("Info", "All plots have been displayed.")

    def show_previous_plot(self):
        if self.current_plot_index > 1:
            self.current_plot_index -= 1
            self.display_plot(self.current_plot_index - 1)
        else:
            messagebox.showinfo("Info", "No previous plot available.")

    def display_plot(self, index):
        for widget in self.plot_frame.winfo_children():
            widget.destroy()  # Clear previous content in the plot frame

        fig = self.figures[index]
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)  # Proper packing


# Main Tkinter Window
root = tk.Tk()
app = QueueSimulationApp(root)
root.mainloop()
