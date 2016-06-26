# -*- coding: utf-8 -*-

import pymongo

mongourl = "127.0.0.1"
mongoport = 27017
database = "jobdescription"
table = "jobdescription"

connection = pymongo.MongoClient(mongourl, mongoport)
db = connection[database][table]
dbtarget = connection[database]["jobtarget"]

with open("jdtitle.txt", 'r') as jdfile:
    for jdline in jdfile:
        jdlist = jdline.split(" ")
        jobdesc_count = db.count({"job": jdlist[1]})
        jobdescs = db.find({"job": jdlist[1]})
        jobdescriptions = []
        if jobdesc_count != 0:
            for jobdesc in jobdescs:
                jobdescriptions.append(jobdesc['decription'])
        dbtarget.insert(
            {"id": jdlist[0],
             "job": jdlist[1],
             "description": jobdescriptions,
             "description_count": jobdesc_count}
        )





