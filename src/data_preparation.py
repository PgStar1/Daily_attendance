from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.io as pio
from PIL import Image
import numpy as np

def create_dataframe(csv_file):
    df = pd.read_csv(csv_file)
    df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)
    return df

def print_dataframe_info(df):
    # Print the number of rows and columns in the DataFrame using `.shape()`
    print("\nNumber of rows and columns:\n")
    print(df.shape)

    # Print the first 7 rows of data using `.head()` and the last 6 rows using `.tail()`
    print("\nFirst 7 rows:\n")
    print(df.head(7))
    print("\nLast 6 rows:\n")
    print(df.tail(6)) 

    #  Print the column labels using `.info()` or `.columns`.
    print("\nColumn labels:\n")
    print(df.info())

    # Print the column data types using `.info()` or `.dtypes`
    print("\nColumn data types:\n")
    print(df.dtypes)  # Add your code inside the brackets
    # Print general statistics using `.describe()`
    # Why are some columns not shown in the output?
    print("\nStatistics:\n")
    print(df.describe)  # Add your code inside the brackets
    print(df[df.isna().any(axis=1)])
    print(df.isna().sum())

def processing(df):
    absent = df['Absent_Percentage'] = (df['Absent'] / df['Enrolled']) * 100
    present = df['Present_Percentage'] = (df['Present'] / df['Enrolled']) * 100
    #df.set_index('Date', inplace=True)
    
    """fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df['Date'][:7],
        y=absent[:7],
        name='cycle_spaces'
    ))
    fig.add_trace(go.Bar(
        x=df['Date'][:7],
        y=present[:7],
        name='car_spaces',
        #marker=dict(color=['teal','cyan'])
    ))
    print (present[:7])
    fig.update_layout(title='How does car parking spaces compare to cycle spaces for different Higher Education Providers?',
        #template="simple_white",
        barmode= 'group',height = 800,paper_bgcolor='#FFFFFF')
    fig.update_traces(marker_line_width=0.01)
    fig.update_xaxes(ticklen=0,tickfont=dict(size=16,color='teal'))
    #fig.show()
    #pio.show(fig, render='png')
    img_bytes = pio.to_image(fig, format='png')

# Convert bytes to an image object
    image = Image.open(pio.BytesIO(img_bytes))

# Display the image
    image.show()
    return fig"""
    dates = df['Date'][:7]
    
    #bar_width = 1.35  # Adjust width for better separation

# Create x-axis positions for each bar group
    #x = np.arange(len(dates))
    
    plt.figure(figsize=(14, 7))
    plt.bar(dates, present[:7], label='Enrolled', alpha=0.7)
    plt.bar(dates, absent[:7], label='Absent', alpha=0.7)
    plt.show()

    """df[['Absent_Percentage', 'Present_Percentage']].plot(figsize=(14, 7))
    plt.title('Percentage of Absentees and Present Students')
    plt.ylabel('Percentage')
    plt.show()
    
    df.set_index('Date', inplace=True)
    df[['Enrolled']].plot(figsize=(14, 7))
    plt.title('Daily Attendance Trends')
    plt.ylabel('Number of Students')
    plt.show()
    """

    
if __name__ == '__main__':
    # Use Pathlib.Path to read a file using the location relative to this file
    raw_dataset_file = Path(__file__).parent.parent.joinpath('data','2018-2019_Daily_Attendance_20240429.csv')
    df_raw = create_dataframe(raw_dataset_file)
    processing(df_raw)
    #print(print_dataframe_info(df_raw))