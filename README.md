# RoyalTS Dynamic folder script for Google Cloud Platform

Script for loading Google Cloud Platform VM instances. Supports multiple accounts and Secure Gateways.

## Requirements
* gcloud cli authenticated
* Custom property ```Project``` (Text field) which defines used project

## Optional settings
* Custom property ```Account``` (Text field) allows to define account used for requesting data
* Custom property ```Gateway``` (Text field) defines Secure Gateway to be used when connecting. Requires RoyalTs objectId.