# import the necessary libraries
import boto
import pandas as pd

# set our access key and secret key
access_key = r'INSERT_ACCESS_KEY'
secret_key = r'INSERT_SECRET_KEY'

# connect and get all our instances
ec2_conn = boto.connect_ec2(access_key, secret_key)
all_reservations = ec2_conn.get_all_instances()

# create lists to hold various pieces of info
vpc_ids, instance_ips, instance_ids, instance_names = [], [], [], []

# interate through the reservations, through the instances, to get the information we're interested in
for reservation in all_reservations:
    for instance in reservation.instances:
        vpc_ids.append(instance.vpc_id)
        instance_ips.append(instance.private_ip_address)
        instance_ids.append(instance.id)
        instance_names.append(instance.tags['Name'])

# create a dataframe with the info we pulled out
output = pd.DataFrame({
        'vpc_id': vpc_ids,
        'instance_ips': instance_ips,
        'instance_ids': instance_ids,
        'instance_names': instance_names
    })

# write it to a csv
output.to_csv('aws_inventory.csv',index=False)

