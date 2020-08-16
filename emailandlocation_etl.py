import pandas as pd 
from pandas import DataFrame
import csv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#Extract

#data from a CSV on my desktop (located via pathname)
emails_df = pd.read_csv('/Users/Desktop/SampleData.csv', sep = ";", usecols=["Email"])
location_df = pd.read_csv('/Users/Desktop/SampleData.csv', sep = ";", usecols=["Latitude",
                                                                                    "Longitude"])
#print(emails_df)

#Transform

#Split email into username and domain 
split_email = emails_df.Email.str.split("@", expand = True)
emails_df = emails_df.assign(
    username=split_email[0],
    domain=split_email[1],
    )
#print(emails_df)


#Load

#data to a CSV (saved to desktop via pathname)
emails_df.to_csv('/Users/user/Desktop/emails.csv')
location_df.to_csv('/Users/user/Desktop/location.csv')

#Analysis

#Frequency
#loop through columnar DataFrame to find count of domains 

frequency = emails_df['domain'].value_counts()
print(frequency)
                                       
#K-Means Cluster
#finding locations of local business nodes in the Cape Town area
df = DataFrame(location_df, columns = ['Latitude', 'Longitude'])
  
kmeans = KMeans(n_clusters=4).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(df['Latitude'], df['Longitude'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.show()                                    
                                       
                                       
