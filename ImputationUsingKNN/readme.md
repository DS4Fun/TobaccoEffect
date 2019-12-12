{\rtf1\ansi\ansicpg1252\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Many datasets we use for our data science tasks contain missing values. \
As each entity in our dataset can potentially represent important information, we can\'92t simply remove entities with missing values. There are different ways to deal with this missing values and replace them with some other numeric values, which are called data imputation strategies. One of the most effective way is imputation using KNN (K nearest neighbors) \
KNN constructs a KDTree and then looks for the k nearest neighbor of each node with a missing value. The weighted average of mentioned neighbors will be assigned to that node, as its value.}